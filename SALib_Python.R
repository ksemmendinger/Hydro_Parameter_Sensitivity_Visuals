library(dplyr)

setwd("/Users/kylasemmendinger 1/Box Sync/CUAHSI/Code")
data <- read.csv("dummy_data.csv")

params <- data[, 4:7] # subset parameters
Y <- data[, "observation"] - data[, "prediction"] # calculate arbitrary OF for model comp

# load python data
# Y <- read.csv("y.csv", header = FALSE)
# Y <- array(Y[,1])
# params <- read.csv("param_values.csv", header = FALSE)

# define number of model parameters
D <- as.numeric(ncol(params))

# user inputs
num_resamples <- 100
conf_level <- 0.95 # between 0 - 1
second_order <- TRUE

Z <- qnorm(0.5 + conf_level / 2, mean = 0, sd = 1)

# calculate N and step from second_order (TRUE/FALSE) and D (number of parameters)
if (second_order == TRUE) {
  
  N <- ceiling(length(Y) / (2 * D + 2))
  step <- 2 * D + 2
  
}

if (second_order == FALSE) {
  
  N <- ceiling(length(Y) / (D + 2))
  step <- D + 2
  
}

# normalize model output (objective function)
Y <- (Y - mean(Y)) / sd(Y)

# create subsetting indices for A, B, AB, and BA from Y
A_index <- seq(1, length(Y), by = step)
B_index <- seq(step - 1, length(Y), by = step)

# subset Y into A and B arrays based on indices
A <- Y[A_index]
B <- Y[B_index]

# create arrays AB and BA with dimesion N x D
AB <- array(NA, c(N, D))
BA <- array(NA, c(N, D))

# subset AB and BA (if second_order == TRUE)
for (i in 1:D) {
  
  AB_index <- seq(i + 1, length(Y), by = step)
  # changed to start at 3 from i + 1
  AB[, i] <- Y[AB_index]
  
  if (second_order == TRUE) {
    
    BA_index <- seq(i + 1 + D, length(Y), by = step)
    # changed to start at 4 from i + 1 + D
    BA[, i] <- Y[BA_index]
    
  }
  
}

# create array to store randomly sampled index for a specified number of resamples
r <- array(NA, c(N, num_resamples))

for (j in 1:num_resamples) {
  
  r[, j] <- round(runif(N, min = 1, max = N))
  
}

# arrays to store results
S1 <- array(NA, D)
S1_conf <- array(NA, D)
ST <- array(NA, D)
ST_conf <- array(NA, D)
S2 <- array(NA, c(D, D))
S2_conf <- array(NA, c(D, D))

for (k in 1:D) {
  
  # calculate first order sensitivity index of parameter, k
  S1[k] <- mean(B * (AB[, k] - A)) / var(c(A, B))
  
  # randomly pull samples from parameter space and calculate their first order senstivity index
  tmp <- array(NA, length(num_resamples))
  
  for (l in 1:num_resamples) {
    
    run_index <- r[, l]
    tmp[l] <- mean(B[run_index] * (AB[run_index, k] - A[run_index])) / var(c(A[run_index], B[run_index]))
    
  }
  
  # calculate confidence interval around the first order sensitivity index
  S1_conf[k] <- Z * sd(tmp)
  
  # calculate total sensitivity index of parameter, k
  ST[k] <- 0.5 * (mean((A - AB[, k]) ^ 2) / var(c(A, B)))
  
  # randomly pull samples from parameter space and calculate their total senstivity index
  tmp <- array(NA, length(num_resamples))
  
  for (l in 1:num_resamples) {
    
    run_index <- r[, l]
    tmp[l] <- 0.5 * (mean((A[run_index] - AB[run_index, k]) ^ 2) / var(c(A[run_index], B[run_index])))
    
  }
  
  # calculate confidence interval around the total sensitivity index
  ST_conf[k] <- Z * sd(tmp)
  
  if (second_order == TRUE) {
    
    if (k < D) {
      
      for (m in (k + 1):D) {
        
        # calculate second order sensitivity index of parameter, k
        Vkm <- mean(BA[ , k] * AB[ , m] - A * B) / var(c(A, B))
        Sk <- mean(B * (AB[, k] - A)) / var(c(A, B))
        Sm <- mean(B * (AB[, m] - A)) / var(c(A, B))
        
        S2[k, m] <- Vkm - Sk - Sm
        
        # randomly pull samples from parameter space and calculate their second order senstivity index
        tmp <- array(NA, length(num_resamples))
        
        for (l in 1:num_resamples) {
          
          run_index <- r[, l]
          Vkm <- mean(BA[run_index, k] * AB[run_index, m] - A[run_index] * B[run_index]) / var(c(A[run_index], B[run_index]))
          Sk <- mean(B[run_index] * (AB[run_index, k] - A[run_index])) / var(c(A[run_index], B[run_index]))
          Sm <- mean(B[run_index] * (AB[run_index, m] - A[run_index])) / var(c(A[run_index], B[run_index]))
          tmp[l] <- Vkm - Sk - Sm
          
        }
        
        S2_conf[k, m] <- Z * sd(tmp)
        
      }
      
    }
    
  }
  
}

S <- list(S1, S1_conf, ST, ST_conf)















