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

for (j in 1:2) {
  # create scatter plot of OF vs parameter
  sctplt <- ggplot(data, aes(x = data[, j], y = NSE)) + 
    geom_point(size = 1, colour = "#016c59") + 
    xlab(paste0(colnames(data)[j])) +
    ylab("NSE") + 
    theme(axis.text.x = element_text(size=14, angle = 25),
          axis.text.y = element_text(size=14),
          axis.title = element_text(size = 18, color = "black"),
          axis.text = element_text(size = 18))
  #theme(text = element_text(size=14))
  
  # save to list for gridded plot
  plots[[paste(colnames(data)[j])]] <- ggplotGrob(sctplt)
}

pdf(paste0("JAWRA_Figures/Fig4_scatter.pdf"), width = 12, height = 5)
print(ggarrange(plotlist = plots, widths = c(ceiling(sqrt(ncol(data))), ceiling(ncol(data)/ceiling(sqrt(ncol(data)))))))
dev.off()   


# Figure 5. Spider plot - run from original workflow (no need to update for paper)
results_sobol <- read.csv("output/formatted_sobol.csv", header = TRUE, row.names=0)
results_delta <- read.csv("output/formatted_delta.csv", header = TRUE, row.names=0)

# Figure 6. Radial Convergence Plot - run from original workflow (no need to update for paper)

# Figure 7. Portrait plots - run from original workflow (no need to update for paper)
