# scatterplots

par_OF_scatter <- function(params, objective_fun, OF_name) {
  
  library(ggplot2)
  library(wesanderson)
  library(gridExtra)
  
  # create a data frame of parameter values and the objective function values
  data <- params
  data[, "OF"] <- objective_fun
  plots <- list()

  for (j in 1:ncol(params)) {
  
    # create scatter plot of OF vs parameter
    sctplt <- ggplot(data, aes(x = data[, j], y = OF)) + 
      geom_point(size = 1, colour = "#016c59") + 
      # ggtitle(paste0("Parameter: ", colnames(params)[j])) + 
      xlab(paste0(colnames(params)[j])) +
      ylab(OF_name)
    
    # save individual plot to output folder
    ggsave(paste0("output/plots/scatter/", colnames(params)[j], "_", OF_name, ".png"))
    
    # save to list for gridded plot
    # plots[[j]] <- sctplt
    
    # paste plot to console
    print(sctplt)
    
  }
  
  # save grid of parameter scatter plots for each OF
  # do.call(grid.arrange, plots)
  # dev.copy(png, paste0("output/plots/scatter/", OF_name, ".png"))
  # dev.off()
  # x <- grid.arrange(grobs = plots, ncol = ceiling(sqrt(ncol(params))))
  # ggsave(paste0("output/plots/scatter/", OF_name, ".png"), x, width = 11, height = 8.5, units = "in")

}
