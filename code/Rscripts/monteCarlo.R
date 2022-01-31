powerPlayMean <- mean(powerplay)
middleOversMean <- mean(middleOvers)
finalOversMean <- mean(finalOvers)
powerplayVAR <- var(powerplay)
middleOversVAR <- var(middleOvers)
finalOversVAR <- var(finalOvers)

expPowerPlay <- c(rnorm(10,powerPlayMean,sqrt(powerplayVAR)))
expMid <- c(rnorm(25,middleOversMean,sqrt(middleOversVAR)))
expFin <- c(rnorm(15,finalOversMean,sqrt(finalOversVAR)))
  
samplegame <- c(expPowerPlay,expMid,expFin)
