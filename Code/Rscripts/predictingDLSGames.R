#replace NA values with 0
dlsRR <- data.frame(dlsRR)

dlsRRMat <- dlsRR[,3:44]
dlsRRMat <- replace(dlsRRMat,is.na(dlsRRMat),0)


dlsrrSc <- data.frame(scale(dlsRRMat))
dlsrrSc[,43:51] = 0

colnames(dlsrrSc)<-colnames(rrMatTest)

#WE can now feed these matrices into the neural network
predictValsNoFill <- neuralnet::compute(scoreNet, dlsrrSc,rep=best_rep)
dlsResults$predictedNoFill <- c(predictValsNoFill$net.result)
dlsResults <- data.frame(actual=dlsRR$V2, predicted = predictValsNoFill$net.result)

target1 <- dlsResults$predictedNoFill
dlsResults$predUNSC <- unscale(target1,testNorm) 

dlsResults$errorNoFill <- (dlsResults$actual-dlsResults$predUNSC)

#Check error distribution
ggplot(dlsResults, aes(x=errorNoFill)) +
  geom_density()
