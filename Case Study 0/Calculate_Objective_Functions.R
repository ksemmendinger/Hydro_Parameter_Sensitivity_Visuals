# Case Study 0: Fall Creek, NY

# This script calculates six objective functions from 24,000 SWMM model runs and USGS streamgage 
# data using the hydroGOF package (https://cran.r-project.org/web/packages/hydroGOF/hydroGOF.pdf)

library(dplyr)
library(hydroGOF)

# load in observation, simulation, and parameter sets
obs <- read.csv("input/observation_ts.csv", header = TRUE)
  # "time_steps" row, "index" and "value" columns 
sim <- read.csv("input/simulation_ts.csv", header = TRUE) %>%
  dplyr::select(-1)
  # "model_runs" rows, "time_steps" columns
pars <- read.csv("input/params.csv", header = FALSE)
  # "model_runs" rows, "num_pars" columns
timestamps <- read.csv("input/timestamps.csv", header = TRUE)
  # "time_steps" rows

model_runs <- nrow(sim)
time_steps <- ncol(sim)
num_pars <- ncol(pars)

mean_error <- array(NA, model_runs)
mean_abs_error <- array(NA, model_runs)
mean_sq_error <- array(NA, model_runs)
root_mse <- array(NA, model_runs)
p_bias <- array(NA, model_runs)
nse <- array(NA, model_runs)

for (i in 1:model_runs) {

  print(i)

  mean_error[i] <- me(sim = as.numeric(sim[i, 1:time_steps]), obs = as.numeric(obs[, 2]))
  mean_abs_error[i] <- mae(sim = as.numeric(sim[i, 1:time_steps]), obs = as.numeric(obs[, 2]))
  mean_sq_error[i] <- mse(sim = as.numeric(sim[i, 1:time_steps]), obs = as.numeric(obs[, 2]))
  root_mse[i] <- rmse(sim = as.numeric(sim[i, 1:time_steps]), obs = as.numeric(obs[, 2]))
  p_bias[i] <- pbias(sim = as.numeric(sim[i, 1:time_steps]), obs = as.numeric(obs[, 2]))
  nse[i] <- NSE(sim = as.numeric(sim[i, 1:time_steps]), obs = as.numeric(obs[, 2]))

}

OF <- as.data.frame(mean_error) %>%
  setNames("me") %>%
  dplyr:: mutate(mae = mean_abs_error,
                 mse = mean_sq_error,
                 rmse = root_mse,
                 pbias = p_bias,
                 nse = nse)

write.table(OF, "/input/OF_values.txt", sep = " ",
            row.names = FALSE, col.names = FALSE)

