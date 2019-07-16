spiderplot <- function(SI) {
  
  library(fmsb)
  
  for (k in 1:length(SI)) {
    
    # subset sensitivty analysis results
    with_conf <- SI[[k]]
    
    # if ols then the length of the list is 2 with a different format than the Sobol/Delta analyses
    if (length(dim(with_conf)) == 2) {
      
      value <- with_conf
      
      for (n in 1:ncol(value)) {
        
        OF <- t(as.data.frame(value[, n]))
        row.names(OF) <- "value"
        
        # create max and min row to set boundaries
        OF <- rbind(rep(max(OF["value",]), ncol(OF)), rep(min(OF["value",]), ncol(OF)) , OF)
        row.names(OF) <- c("max", "min", "value")
        
        # convert to data frame
        OF <- as.data.frame(OF)
        
        # write and save spider plot
        png(paste0("output/plots/spider/ols_", colnames(value)[n], ".png")) # , width = 700, height = 500)
        radarchart(OF, pcol = rgb(0.2,0.5,0.5,0.9), pfcol = rgb(0.2,0.5,0.5,0.5), plwd = 4, axistype = 1,
                         cglcol = "grey", cglty = 1, axislabcol = "grey", caxislabels = round(seq(min(OF), max(OF), length.out = 5), 3),
                         cglwd = 0.8, title = paste0(toupper(colnames(value)[n]), " Spider Plot for OLS Sensitivity Analysis"))
        dev.off()
        
        radarchart(OF, pcol = rgb(0.2,0.5,0.5,0.9), pfcol = rgb(0.2,0.5,0.5,0.5), plwd = 4, axistype = 1,
                         cglcol = "grey", cglty = 1, axislabcol = "grey", caxislabels = round(seq(min(OF), max(OF), length.out = 5), 3),
                         cglwd = 0.8, title = paste0(toupper(colnames(value)[n]), " Spider Plot for OLS Sensitivity Analysis"))
        
      }
      
    } else {
      
      value <- with_conf[, , 1]
      
      for (n in 1:ncol(value)) {
        
        OF <- t(as.data.frame(value[, n]))
        row.names(OF) <- "value"
        
        # create max and min row to set boundaries
        OF <- rbind(rep(max(OF["value",]), ncol(OF)), rep(min(OF["value",]), ncol(OF)) , OF)
        row.names(OF) <- c("max", "min", "value")
        
        # convert to data frame
        OF <- as.data.frame(OF)
        
        # write and save spider plot
        
        png(paste0("output/plots/spider/", dimnames(with_conf)[[3]][1], "_", colnames(value)[n], ".png"), width = 700, height = 500)
        radarchart(OF, pcol = rgb(0.2, 0.5, 0.5, 0.9), pfcol = rgb(0.2, 0.5, 0.5, 0.5), plwd = 4, axistype = 1,
                   cglcol = "grey", cglty = 1, axislabcol = "grey", caxislabels = round(seq(min(OF), max(OF), length.out = 5), 3),
                   cglwd = 0.8, title = paste0(toupper(colnames(value)[n]), " Spider Plot for ", toTitleCase(dimnames(with_conf)[[3]][1])," Sensitivity Analysis"))
        dev.off()
        
        radarchart(OF, pcol = rgb(0.2, 0.5, 0.5, 0.9), pfcol = rgb(0.2, 0.5, 0.5, 0.5), plwd = 4, axistype = 1,
                   cglcol = "grey", cglty = 1, axislabcol = "grey", caxislabels = round(seq(min(OF), max(OF), length.out = 5), 3),
                   cglwd = 0.8, title = paste0(toupper(colnames(value)[n]), " Spider Plot for ", toTitleCase(dimnames(with_conf)[[3]][1])," Sensitivity Analysis"))

      }
    
    }
    
  }
  
}



