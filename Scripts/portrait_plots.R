# portrait plot

portrait_plot <- function(SI) {
  
  library(lattice)
  library(tools)
  library(RColorBrewer)
  
  for (k in 1:length(SI)) {
    
    # subset sensitivty analysis results
    with_conf <- SI[[k]]
    
    # if ols then the length of the list is 2 with a different format than the Sobol/Delta analyses
    if (length(dim(with_conf)) == 2) {
      
      value <- as.matrix(with_conf)
      
      # write and save portrait plot
      png("output/plots/portrait/ols.png", width = 700, height = 500)
      col <- colorRampPalette(brewer.pal(9, "PuBuGn"))
      print(levelplot(value, xlab = "Parameter", ylab = "Objective Function", col.regions = col,
                      main = paste0("Portrait Plot for OLS Sensitivity Analysis")))
      dev.off()
      
      print(levelplot(value, xlab = "Parameter", ylab = "Objective Function", col.regions = col,
                      main = paste0("Portrait Plot for OLS Sensitivity Analysis")))
      
      
    } else {
    
      value <- as.matrix(with_conf[, , 1])
      
      # write and save portrait plot
      png(paste0("output/plots/portrait/", dimnames(with_conf)[[3]][1], ".png"), width = 700, height = 500)
      col <- colorRampPalette(brewer.pal(9, "PuBuGn"))
      print(levelplot(value, xlab = "Parameter", ylab = "Objective Function", col.regions = col,
                      main = paste0("Portrait Plot for ", toTitleCase(dimnames(with_conf)[[3]][1])," Sensitivity Analysis")))
      dev.off()
      
      print(levelplot(value, xlab = "Parameter", ylab = "Objective Function", col.regions = col,
                      main = paste0("Portrait Plot for ", toTitleCase(dimnames(with_conf)[[3]][1])," Sensitivity Analysis")))
      
    }
    
  }

}
