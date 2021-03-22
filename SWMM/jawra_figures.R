library(dplyr)
library(ggplot2)
library(wesanderson)
library(gridExtra)
library(ggpubr)

# Figure 4. Scatter Plots
pars <- read.csv("input/params.csv", header = TRUE)
OF <- read.csv("input/OF_values.csv", header = TRUE)

# create a data frame of parameter values and the objective function values
data <- pars["A1"]
data[,"B1"] <- pars["B1"]
data[,"NSE"] <- OF["nse"]
plots <- list()

for (j in 1:3) {
  # create scatter plot of OF vs parameter
  sctplt <- ggplot(data, aes(x = data[, j], y = NSE)) + 
    geom_point(size = 1, colour = "#016c59") + 
    xlab(paste0(colnames(pars)[j])) +
    ylab("NSE")
    theme(axis.title = element_text(size = 25, color = "black"),
          axis.text = element_text(size = 20))
  theme(axis.title = element_text(size = "15", color = "black"),
        axis.text = element_text(size = 15))
  
  # save to list for gridded plot
  plots[[paste(colnames(pars)[j])]] <- ggplotGrob(sctplt)
  
}