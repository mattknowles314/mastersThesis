mcfill <- function(state,row){
  if(state<=10){
    row[state:10] <- c(rnorm(11-state,mean=1.5298,sd=0.4486))
    row[11:35] <- c(rnorm(25,mean=1.6541,sd=0.3355))
    row[36:50] <- c(rnorm(15,mean=3.1493,sd=1.1349))
  } else if(state>10 && state<35){
    row[state:35] <- c(rnorm(36-state,mean=1.6541,sd=0.3355))
    row[36:50] <- c(rnorm(15,mean=3.1493,sd=1.1349))
  } else{
    row[state:50] <- c(rnorm(51-state,mean=3.1493,sd=1.1349))
  }
  return(row)
}


powerPlayMean <- mean(powerplay)
middleOversMean <- mean(middleOvers)
finalOversMean <- mean(finalOvers)
powerplayVAR <- var(powerplay)
middleOversVAR <- var(middleOvers)
finalOversVAR <- var(finalOvers)

expPowerPlay <- c(rnorm(10,powerPlayMean,sqrt(powerplayVAR)))
expMid <- c(rnorm(25,middleOversMean,sqrt(middleOversVAR)))
expFin <- c(rnorm(15,finalOversMean,sqrt(finalOversVAR)))

#Simmulate remaining overs in a game
rrMatTestCase <- data.frame(matrix(ncol = 51, nrow = 431))
for(i in 1:431){
  x<-sample.int(50,1)
  message(x)
  rrMatTestCase[i,1:x]<-rrMatTest[i,1:x]
  state=min(which(c(is.na(testRow[i,]))==T))
  rrMatTestCase[i,]<-mcfill(state,rrMatTestCase[i,])
}
rrMatTestCase[,51] <- rrMatTest[,51] #Original score

predictValsMC <- compute(scoreNet, scale(rrMatTestCase[,1:50]),rep=best_rep)
results$predicted_mc <- predictValsMC$net.result
results$error_MC <- (results$actual-results$predicted_mc)

ggplot(results, aes(x=error_MC)) +
  geom_density()

ggplot(results, aes(sample=error_MC))+
  stat_qq(fill="cyan",pch=21, size=3) +
  geom_qq_line(color="red", lty="dashed")

boxplot(results$diff, main="Boxplot of Difference in Monte-Carlo VS Full-Data Predictions",
        xlab="Difference", col="cyan",  notch=T,horizontal = T, pch=19)

#Unscaling Data

unscale <- function(oldMu, oldVar, newData){
  Y <- c()
  count = 0
  for(i in newData){
    Y[count] <- i*oldMu + oldVar
  }
  
}
