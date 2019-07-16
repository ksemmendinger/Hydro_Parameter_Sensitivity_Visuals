
library(dplyr)

setwd("/Users/kylasemmendinger 1/Box Sync/CUAHSI/CaseStudy0")

# load in observation, simulation, and parameter sets
obs <- read.csv("input/observation_ts.csv", header = TRUE)
  # "time_steps" row, 1 column of values

sim <- read.csv("input/simulation_ts.csv", header = TRUE) %>%
  dplyr::select(-1)
  # "model_runs" rows, "time_steps" columns

pars <- read.csv("input/params.csv", header = FALSE)
  # "model_runs" rows, "num_pars" columns

timestamps <- read.csv("input/timestamps.csv", header = TRUE)
  # "time_steps" row, 1 column of values
  
OF <- read.csv("input/OF_values.csv", header = TRUE)
  # "model_runs" rows, "num_OF" columns

OF_names <- colnames(OF)
param_names <- c("w", "n_imperv", "n_perv", "s_imperv", "s_perv", "k_sat", 
                 "per_routed", "cmelt", "Tb", "A1", "B1")

# clean up data
obs <- array(obs[, 2])
timestamps <- array(timestamps[, 2])
colnames(pars) <- param_names

# set variables of number of model runs, time steps, and number of parameters
model_runs <- nrow(sim)
time_steps <- ncol(sim)
num_pars <- ncol(pars)
num_OF <- ncol(OF)

# load in results from delta, sobol, and ols sensitivity analyses (calculated in python script)

# sobol sensitivity analysis (S1 and ST)
sobol_S1 <- array(NA, c(num_pars, num_OF, 2))
dimnames(sobol_S1) <- list(param_names, OF_names, c("S1", "S1_conf"))

sobol_ST <- array(NA, c(num_pars, num_OF, 2))
dimnames(sobol_ST) <- list(param_names, OF_names, c("ST", "ST_conf"))

for (i in 1:num_OF) {
  
  tmp <- read.csv(paste0("output/sobol_", OF_names[i], ".csv"))
  
  # format the sobol first-order indices
  S1 <- as.character(tmp[, "S1"])
  S1 <- gsub("\\[ |]|\n|\\[", "", S1)
  S1 <- as.numeric(unlist(strsplit(S1, " ")))
  S1 <- as.numeric(na.omit(S1))
  
  # save the sobol first-order indices
  sobol_S1[, OF_names[i], "S1"] <- S1
  
  # format the sobol first-order confidence intervals
  S1_conf <- as.character(tmp[, "S1_conf"])
  S1_conf <- gsub("\\[ |]|\n|\\[", "", S1_conf)
  S1_conf <- as.numeric(unlist(strsplit(S1_conf, " ")))
  S1_conf <- as.numeric(na.omit(S1_conf))
  
  # save the sobol first-order confidence intervals
  sobol_S1[, OF_names[i], "S1_conf"] <- S1_conf
  
  # format the sobol total-order indices
  ST <- as.character(tmp[, "ST"])
  ST <- gsub("\\[ |]|\n|\\[", "", ST)
  ST <- as.numeric(unlist(strsplit(ST, " ")))
  ST <- as.numeric(na.omit(ST))
  
  # save the sobol total-order indices
  sobol_ST[, OF_names[i], "ST"] <- ST
  
  # format the sobol total-order confidence intervals
  ST_conf <- as.character(tmp[, "ST_conf"])
  ST_conf <- gsub("\\[ |]|\n|\\[", "", ST_conf)
  ST_conf <- as.numeric(unlist(strsplit(ST_conf, " ")))
  ST_conf <- as.numeric(na.omit(ST_conf))
  
  # save the sobol total-order confidence intervals
  sobol_ST[, OF_names[i], "ST_conf"] <- ST_conf
  
  # # format the sobol second-order confidence intervals
  # S2 <- as.character(tmp[, "S2"])
  # S2 <- gsub("\\[|]|\n", "", S2)
  # S2 <- as.numeric(unlist(strsplit(S2, " ")))
  # S2 <- as.numeric(na.omit(S2))
  # 
  # # save the sobol total-order confidence intervals
  # sobol_ST[, OF_names[i], "ST_conf"] <- ST_conf

}

# delta sensitivity analysis (delta and S1)
delta <- array(NA, c(num_pars, num_OF, 2))
dimnames(delta) <- list(param_names, OF_names, c("delta", "delta_conf"))

delta_S1 <- array(NA, c(num_pars, num_OF, 2))
dimnames(delta_S1) <- list(param_names, OF_names, c("S1", "S1_conf"))

for (i in 1:num_OF) {
  
  tmp <- read.csv(paste0("output/delta_", OF_names[i], ".csv"))
  
  # format the sobol total-order indices
  del <- as.character(tmp[, "delta"])
  del <- gsub("\\[ |]|\n|\\[", "", del)
  del <- as.numeric(unlist(strsplit(del, " ")))
  del <- as.numeric(na.omit(del))
  
  # save the sobol total-order indices
  delta[, OF_names[i], "delta"] <- del
  
  # format the delta confidence intervals
  del_conf <- as.character(tmp[, "delta_conf"])
  del_conf <- gsub("\\[ |]|\n|\\[", "", del_conf)
  del_conf <- as.numeric(unlist(strsplit(del_conf, " ")))
  del_conf <- as.numeric(na.omit(del_conf))
  
  # save the delta confidence intervals
  delta[, OF_names[i], "delta_conf"] <- del_conf
  
  # format the sobol first-order indices
  S1 <- as.character(tmp[, "S1"])
  S1 <- gsub("\\[ |]|\n|\\[", "", S1)
  S1 <- as.numeric(unlist(strsplit(S1, " ")))
  S1 <- as.numeric(na.omit(S1))
  
  # save the sobol first-order indices
  delta_S1[, OF_names[i], "S1"] <- S1
  
  # format the sobol first-order confidence intervals
  S1_conf <- as.character(tmp[, "S1_conf"])
  S1_conf <- gsub("\\[|]|\n", "", S1_conf)
  S1_conf <- as.numeric(unlist(strsplit(S1_conf, " ")))
  S1_conf <- as.numeric(na.omit(S1_conf))
  
  # save the sobol first-order confidence intervals
  delta_S1[, OF_names[i], "S1_conf"] <- S1_conf
  
}

# OLS analysis (rsquared)
ols <- array(NA, c(num_pars, num_OF))
dimnames(ols) <- list(param_names, OF_names)

for (i in 1:num_OF) {
  
  tmp <- read.csv(paste0("output/ols_", OF_names[i], ".csv"), header = FALSE)
  
  ols[, OF_names[i]] <- tmp[, "V2"]
  
}






