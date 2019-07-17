# This script loads in data from Sobol, Delta, and OLS sensitivity analyses calculated in
# Python script for Case Study 0: Fall Creek, NY.

library(dplyr)

# load in parameter sets, objective functions, observation, simulation, and time steps
pars <- read.csv("input/params.csv", header = TRUE)
  # "model_runs" rows, "num_pars" columns

OF <- read.csv("input/OF_values.csv", header = TRUE) %>%
  dplyr::select(-1)
  # "model_runs" rows, "num_OF" columns

obs <- read.csv("input/observation_ts.csv", header = TRUE) %>%
  dplyr::select(-1)
  # "time_steps" row, "index" and "value" columns 

sim <- read.csv("input/simulation_ts.csv", header = TRUE) %>%
  dplyr::select(-1)
  # "model_runs" rows, "time_steps" columns

timestamps <- read.csv("input/timestamps.csv", header = TRUE)
  # "time_steps" rows


# save names of objective functions and parameters
OF_names <- colnames(OF)
param_names <- colnames(pars)

# set variables of number of model runs, time steps, and number of parameters
model_runs <- nrow(pars)
num_pars <- ncol(pars)
num_OF <- ncol(OF)

# load in results from delta, sobol, and ols sensitivity analyses (calculated in python script)
source("../Scripts/python_to_r_results.R")
results_sobol <- python_to_r_results(data_type = "sobol", param_names, OF_names)
results_delta <- python_to_r_results(data_type = "delta", param_names, OF_names)
results_ols <- python_to_r_results(data_type = "ols", param_names, OF_names)

# save as csv files
lapply(results_sobol, function(x) write.table(data.frame(x), 'output/formatted_sobol.csv', append = T, sep = ',' ))
lapply(results_delta, function(x) write.table(data.frame(x), 'output/formatted_delta.csv', append = T, sep = ',' ))
lapply(results_ols, function(x) write.table(data.frame(x), 'output/formatted_ols.csv', append = T, sep = ',' ))

# scatter plots of objective functions versus parameter values
source("../Scripts/scatterplots.R")
for (i in 1:num_OF) {
  
  # subset by objective function, i
  objective_fun <- OF[, i]

  # create scatterplots of all parameters versus objective function, i
  par_OF_scatter(params = pars, objective_fun, OF_name = colnames(OF)[i])
  
}

# portrait plots of objective functions versus parameter values
source("../Scripts/portrait_plots.R")
portrait_plot(results_sobol)
portrait_plot(results_delta)
portrait_plot(results_ols)

# spiders plots of objective functions versus parameter values
source("../Scripts/spider_plots.R")
spiderplot(results_sobol)
spiderplot(results_delta)
spiderplot(results_ols)
