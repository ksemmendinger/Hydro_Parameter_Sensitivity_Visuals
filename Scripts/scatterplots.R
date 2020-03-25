# scatterplots

par_OF_scatter <- function(params, objective_fun, OF_name) {
  
  library(ggplot2)
  library(wesanderson)
  library(gridExtra)
  library(ggpubr)
  
  # create a data frame of parameter values and the objective function values
  data <- params
  data[, "OF"] <- objective_fun
  plots <- list()
  
  for (j in 1:ncol(params)) {
    
    # print(j)
  
    # create scatter plot of OF vs parameter
    sctplt <- ggplot(data, aes(x = data[, j], y = OF)) + 
      geom_point(size = 1, colour = "#016c59") + 
      xlab(paste0(colnames(params)[j])) +
      ylab(OF_name) + 
<<<<<<< HEAD
      theme(axis.title = element_text(size = 25, color = "black"),
            axis.text = element_text(size = 20))
=======
      theme(axis.title = element_text(size = "15", color = "black"),
            axis.text = element_text(size = 15))
>>>>>>> refs/remotes/origin/master
    
    # save to list for gridded plot
    plots[[paste(colnames(params)[j])]] <- ggplotGrob(sctplt)
    
  }
  
  # save grid of parameter scatter plots for each OF
<<<<<<< HEAD
  png(paste0("output/plots/scatter/", OF_name, ".png"), width = 20, height = 13, units = 'in', res = 1000)
=======
  png(paste0("output/plots/scatter/", OF_name, ".png"), width = 17, height = 11, units = 'in',res = 1000)
>>>>>>> refs/remotes/origin/master
  print(ggarrange(plotlist = plots, widths = c(ceiling(sqrt(ncol(params))), ceiling(ncol(params)/ceiling(sqrt(ncol(params)))))))
  dev.off()      
  
}
