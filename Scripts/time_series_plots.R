time_series_plot <- function(sim, obs, time_stamps) {
  
  library(ggplot2)
  # library(wesanderson)
  # library(gridExtra)
  
  # create a data frame of parameter values and the objective function values
  data <- sim
  data["obs", ] <- obs
  data["time", ] <- time_stamps
  
  melt()
  
  fullplot <- ggplot(df, aes(x = Date_Time, y = value, color = variable)) + 
    geom_line(size = .5) + 
    ggtitle("Water Levels on Lake Ontario from February to July") +
    scale_color_manual(values = wes_palette("Chevalier1")) + 
    xlab("Time") + 
    ylab("Water Level Above LWD (feet)") + 
    theme(axis.title = element_text(face = "bold.italic", size = "12", color = "black"), 
          legend.position = "top", 
          legend.title = element_blank(), 
          plot.title = element_text(face = "bold", size = "13", color = "black", hjust = .5))
  
  
}