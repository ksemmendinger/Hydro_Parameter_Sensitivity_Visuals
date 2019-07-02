# formatting output of Austin's NWM code for input to the WRES tool

# set working directory
setwd("/Users/kylasemmendinger 1/Box Sync/CUAHSI/WRES_Code")

# load in simulated and observational data from other code
sim_in_data <- read.csv("forecast_pts.csv", header = TRUE)
obs_in_data <- read.csv("obsDF.csv", header = TRUE)

# format for WRES input
sim_col_names <- c("start_date", "value_date", "variable_name", "location", "measurement_unit", "value")
sim_out_data <- as.data.frame(array(NA, c(nrow(sim_in_data), length(sim_col_names))))
colnames(sim_out_data) <- sim_col_names
sim_out_data[, "start_date"] <- paste(as.POSIXct(sim_in_data[1, "dateTime"]) - 60 * 60)
sim_out_data[, "value_date"] <- paste(sim_in_data[, "dateTime"])
sim_out_data[, "variable_name"] <- "SQIN"
sim_out_data[, "location"] <- sim_in_data[, "st_id"]
sim_out_data[, "measurement_unit"] <- "CMS"
sim_out_data[, "value"] <- sim_in_data[, "q_cms"]

write.csv(sim_out_data, file = "right.csv")
                                      
obs_col_names <- c("value_date", "variable_name", "location", "measurement_unit", "value")
obs_out_data <- array(NA, c(nrow(obs_in_data), length(obs_col_names)))
colnames(obs_out_data) <- obs_col_names
obs_out_data[, "value_date"] <- paste(obs_in_data[, "dateTime"])
obs_out_data[, "variable_name"] <- obs_in_data[, "X_00060_00000"] 
obs_out_data[, "location"] <- obs_in_data[, "site_no"] 
obs_out_data[, "measurement_unit"] <- "CMS" 
obs_out_data[, "value"] <- obs_in_data[, "q_cms"] 

write.csv(obs_out_data, file = "left.csv")
