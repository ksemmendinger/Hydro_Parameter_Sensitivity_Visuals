#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:16:14 2019

@author: kylasemmendinger
"""

'''
This script produces two radial convergence graphs (aka chord graphs) for Sobol
Sensitivity Analysis results in a dictionary format. It can directly work with 
Sobol results produced by SALib and Rhodium. It will produce one graph with 
straight lines and one with curved lines (parabolas).
Written by Antonia Hadjimichael (https://github.com/antonia-had) based off code
by Enrico Ubaldi (https://github.com/ubi15/).
The script was written and tested in Python 3.6 and 3.7. 
'''

def radial_conv_plots(problem, results, OF):
    
    import pandas as pd
    import numpy as np
    import networkx as nx
    import itertools
    import matplotlib.pyplot as plt

    # Get list of parameters
    parameters = list(problem['names'])
    
    for j in np.arange(len(results)):
    
        # takes in results from objective_function_sobol --> create plots for each objective function
        SAresults = results[j][0]
        
        # Set min index value, for the effects to be considered significant
        index_significance_value = 0.001
    
        '''
        Define some general layout settings.
        '''
        node_size_min = 15 # Max and min node size
        node_size_max = 30
        border_size_min = 1 # Max and min node border thickness
        border_size_max = 8
        edge_width_min = 1 # Max and min edge thickness
        edge_width_max = 10
        edge_distance_min = 0.1 # Max and min distance of the edge from the center of the circle
        edge_distance_max = 0.6 # Only applicable to the curved edges
    
        '''
        Set up some variables and functions that will facilitate drawing circles and 
        moving items around.
        '''
        # Define circle center and radius
        center = [0.0,0.0] 
        radius = 1.0
        # Create an array with all angles in a circle (i.e. from 0 to 2pi)
        step = 0.001
        # radi = np.arange(0,2*np.pi,step) 
        
        # Function to get distance between two points
        def distance(p1,p2):
            return np.sqrt(((p1-p2)**2).sum())
        
        # Function to get middle point between two points
        def middle(p1,p2):
            return (p1+p2)/2
        
        # Function to get the vertex of a curve between two points
        def vertex(p1,p2,c):
            m = middle(p1,p2)
            curve_direction = c-m
            return m+curve_direction*(edge_distance_min+edge_distance_max*(1-distance(m,c)/distance(c,p1)))
        
        # Function to get the angle of the node from the center of the circle
        def angle(p,c):
            # Get x and y distance of point from center
            [dx,dy] = p-c 
            if dx == 0: # If point on vertical axis (same x as center)
                if dy>0: # If point is on positive vertical axis
                    return np.pi/2.
                else: # If point is on negative vertical axis
                    return np.pi*3./2.
            elif dx>0: # If point in the right quadrants
                if dy>=0: # If point in the top right quadrant
                    return np.arctan(dy/dx)
                else: # If point in the bottom right quadrant
                    return 2*np.pi+np.arctan(dy/dx)
            elif dx<0: # If point in the left quadrants
                return np.pi+np.arctan(dy/dx)
        
        '''
        First, set up graph with all parameters as nodes and draw all second order (S2)
        indices as edges in the network. For every S2 index, we need a Source parameter,
        a Target parameter, and the Weight of the line, given by the S2 index itself. 
        '''
        combs = [list(c) for c in list(itertools.combinations(parameters, 2))]
        
        Sources = list(list(zip(*combs))[0])
        Targets = list(list(zip(*combs))[1])
        
        # Sometimes computing errors produce negative Sobol indices. The following reads
        # in all the indices and also ensures they are between 0 and 1.
        
        # convert second-order indices to a data frame and assign parameter names for subsetting
        S2 = pd.DataFrame(SAresults['S2'], columns = parameters, index = parameters)
        
        Weights = [max(min(x, 1), 0) for x in [S2.loc[Sources[i]][Targets[i]] for i in range(len(Sources))]]
        Weights = [0 if x<index_significance_value else x for x in Weights]
        
        # Set up graph
        G = nx.Graph()
        # Draw edges with appropriate weight
        for s,t,weight in zip(Sources, Targets, Weights):
            G.add_edges_from([(s,t)], w=weight)
        
        # Generate dictionary of node postions in a circular layout
        Pos = nx.circular_layout(G)
        
        '''
        Normalize node size according to first order (S1) index. First, read in S1 indices,
        ensure they're between 0 and 1 and normalize them within the max and min range
        of node sizes.
        Then, normalize edge thickness according to S2. 
        '''
        
        # Node size
        first_order = [max(min(x, 1), 0) for x in [SAresults['S1'][key] for key in range(len(SAresults['S1']))]]
        first_order = [0 if x<index_significance_value else x for x in first_order]
        node_size = [node_size_min*(1 + (node_size_max-node_size_min)*k/max(first_order)) for k in first_order]
        # Node border thickness
        total_order = [max(min(x, 1), 0) for x in [SAresults['ST'][key] for key in range(len(SAresults['ST']))]]
        total_order = [0 if x<index_significance_value else x for x in total_order]
        border_size = [border_size_min*(1 + (border_size_max-border_size_min)*k/max(total_order)) for k in total_order]
        # Edge thickness
        edge_width = [edge_width_min*((edge_width_max-edge_width_min)*k/max(Weights)) for k in Weights]
        
        '''
         We can now draw the network with curved lines along the edges and across the circle.
         Calculate all distances between 1 node and all the others (all distances are 
         the same since they're in a circle). We'll need this to identify the curves 
         we'll be drawing along the perimeter (i.e. those that are next to each other).
        '''
         
        min_distance = round(min([distance(Pos[list(G.nodes())[0]],Pos[n]) for n in list(G.nodes())[1:]]), 1)
        
        # Figure to generate the curved edges between two points
        def xy_edge(p1,p2): # Point 1, Point 2
            m = middle(p1,p2) # Get middle point between the two nodes
            # If the middle of the two points falls very close to the center, then the 
            # line between the two points is simply straight
            if distance(m,center)<1e-6:
                xpr = np.linspace(p1[0],p2[0],10)
                ypr = np.linspace(p1[1],p2[1],10)
            # If the distance between the two points is the minimum (i.e. they are next
            # to each other), draw the edge along the perimeter     
            elif distance(p1,p2)<=min_distance:
                # Get angles of two points
                p1_angle = angle(p1,center)
                p2_angle = angle(p2,center)
                # Check if the points are more than a hemisphere apart
                if max(p1_angle,p2_angle)-min(p1_angle,p2_angle) > np.pi:
                    radi = np.linspace(max(p1_angle,p2_angle)-2*np.pi,min(p1_angle,p2_angle))
                else:
                    radi = np.linspace(min(p1_angle,p2_angle),max(p1_angle,p2_angle))
                xpr = radius*np.cos(radi)+center[0]
                ypr = radius*np.sin(radi)+center[1]  
            # Otherwise, draw curve (parabola)
            else: 
                edge_vertex = vertex(p1,p2,center)
                a = distance(edge_vertex, m)/((distance(p1,p2)/2)**2)
                yp = np.linspace(-distance(p1,p2)/2, distance(p1,p2)/2,100)
                xp = a*(yp**2)
                xp += distance(center,edge_vertex)
                theta_m = angle(middle(p1,p2),center)
                xpr = np.cos(theta_m)*xp - np.sin(theta_m)*yp
                ypr = np.sin(theta_m)*xp + np.cos(theta_m)*yp
                xpr += center[0]
                ypr += center[1]
            return xpr,ypr
        
        '''
        Draw network. This will draw the graph with curved lines along the edges and 
        across the circle. 
        '''
        
        plt.figure(figsize=(9,9))
        for i, e in enumerate(G.edges()):
            x,y=xy_edge(Pos[e[0]],Pos[e[1]])
            plt.plot(x,y,'-',c='#2E5591',lw=edge_width[i],alpha=0.7)
        for i, n in enumerate(G.nodes()):
            plt.plot(Pos[n][0],Pos[n][1], 'o', c='#98B5E2', markersize=node_size[i]/5, markeredgecolor = '#1A3F7A', markeredgewidth = border_size[i]*1.15)
        
        for i, text in enumerate(G.nodes()):
            if node_size[i]<100:
                position = (radius*1.05*np.cos(angle(Pos[text],center)), radius*1.05*np.sin(angle(Pos[text],center)))
            else:
                position = (radius*1.01*np.cos(angle(Pos[text],center)), radius*1.01*np.sin(angle(Pos[text],center)))
            plt.annotate(text, position, fontsize = 15, color='#0B2D61', family='sans-serif')          
        
        plt.axis('off')
        plt.tight_layout()
        #plt.savefig('output/plots/radial_convergence/radial_conv_' + OF.columns[j] + '.png', bbox_inches = 'tight', transparent = True)
        plt.savefig('output/plots/radial_convergence/radial_conv_' + OF.columns[j] + '.eps', format = 'eps', dpi = 1000)
        plt.show()
 