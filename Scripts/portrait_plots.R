# portrait plot

portrait_plot <- function(SI, SI_name) {
  
  library(lattice)
  library(tools)
  library(RColorBrewer)
  
  for (k in 1:length(SI)) {
    
    # subset sensitivty analysis results
    with_conf <- SI[[k]]
    
    # if ols then the length of the list is 2 with a different format than the Sobol/Delta analyses
    if (SI_name == "ols") {
      
      value <- as.matrix(with_conf)
      
      # write and save portrait plot
      col <- colorRampPalette(brewer.pal(9, "PuBuGn"))
      png(filename = paste0("output/plots/portrait/", SI_name, "/ols.png"), width = 17, height = 11, units = 'in', res = 1000)
      print(levelplot(value, xlab = "Parameter", ylab = "Objective Function", col.regions = col,
                      main = paste0("Portrait Plot for OLS Sensitivity Analysis")))
      dev.off()
      
      # print(levelplot(value, xlab = "Parameter", ylab = "Objective Function", col.regions = col,
      #                 main = paste0("Portrait Plot for OLS Sensitivity Analysis")))
      # 
      
    } else {
    
      value <- as.matrix(with_conf[, , 1])
      
      # write and save portrait plot
      col <- colorRampPalette(brewer.pal(9, "PuBuGn"))
      png(filename = paste0("output/plots/portrait/", SI_name, "/", dimnames(with_conf)[[3]][1], ".png"), width = 17, height = 11, units = 'in', res = 1000)
      print(levelplot(value, xlab = "Parameter", ylab = "Objective Function", col.regions = col,
                      main = paste0("Portrait Plot for ", toTitleCase(dimnames(with_conf)[[3]][1])," Sensitivity Analysis")))
      dev.off()
      
      # print(levelplot(value, xlab = "Parameter", ylab = "Objective Function", col.regions = col, 
      #                 main = paste0("Portrait Plot for ", toTitleCase(dimnames(with_conf)[[3]][1])," Sensitivity Analysis")))
      # 
    }
    
  }

}
