time_series_plot <- function(sim, obs, time_stamps) {
  
  library(ggplot2)
  library(reshape2)
  # library(wesanderson)
  # library(gridExtra)
  
  # create a data frame of parameter values and the objective function values
  # data <- sim
  # data["obs", ] <- obs
  # data["time", ] <- time_stamps
  
  sim <- as.data.frame(t(sim))
  sim[, "time_index"] <- as.character(1:nrow(sim))
  
  df <- melt(sim, id.vars = "time_index")
  
  fullplot <- 
    
    ggplot() +
    geom_line(data = obs, aes(x = 1:nrow(obs), y = obs[, 1])) +
    ggplot() +
    geom_line(data = df, aes(x = time_index, y = value))
  
  
    ggtitle("Observation and Simulation Time Series") +
    scale_color_manual(values = wes_palette("Chevalier1")) + 
    xlab("Observation Time") + 
    ylab("Value") + 
    theme(axis.title = element_text(face = "bold.italic", size = "12", color = "black"), 
          legend.position = "top", 
          legend.title = element_blank(), 
          plot.title = element_text(face = "bold", size = "13", color = "black", hjust = .5))
  
  
}