## Case Study: HBV-light Simulated Streamflow, Vattholma Catchment

The [HBV-light model](https://en.wikipedia.org/wiki/HBV_hydrology_model) ([Bergström et al., 2015](https://onlinelibrary.wiley.com/doi/abs/10.1002/hyp.10510)) is a rainfall-runoff model, which includes conceptual numerical descriptions of hydrological processes at the catchment scale. The general water balance can be described as:

P - E - Q = d/dt(SP + SM + UZ + LZ +lakes)

where 
P = precipitation
E = evapotranspiration
Q = runoff
SP = snowpack
SM = soil moisture
UZ = upper groundwater zone
LZ = lower groundwater zone
lakes = lake volume

For this jupyter notebook, we will be exercizing the workflow for the Vattholma Catchment in Sweden with model data downloaded from the University of Zürich website. The downloadable catchment dataset can be found [here](https://www.geo.uzh.ch/en/units/h2k/Services/HBV-Model.html) and more information on the model, its calibration and metrics can be found [here](https://www.hydrol-earth-syst-sci.net/16/3315/2012/hess-16-3315-2012.pdf). We ran the model with 30,000 parameter sets using a built-in Monte Carlo analysis and objective function calculator.
