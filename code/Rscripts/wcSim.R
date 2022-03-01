#Find score predictions based on first innings
#Replace na values with 0
wcfirstInns <- replace(wcInssfirst, is.na(wcInssfirst), 0)
wcMat <- data.frame(scale(wcfirstInns[,3:53]))
colnames(wcMat)<-colnames(rrMatTest)

targetScores <- neuralnet::compute(scoreNet, wcMat,rep=best_rep)
targetScores <- c(unscale(targetScores$net.result,testNorm))
targetScores

wcSecondInns <- replace(wcdlsRR, is.na(wcdlsRR),0)
wcMat2 <- data.frame(scale(wcSecondInns[,3:43]))
wcMat2[,42:51] = 0
colnames(wcMat2)<-colnames(rrMatTest)
secondInnsPreds <- neuralnet::compute(scoreNet,wcMat2,rep=best_rep)
secondInnsPreds <- c(unscale(secondInnsPreds$net.result,testNorm))
secondInnsPreds

pakGame <- wcMat2[3,1:35]
pakGame[36:50] <- 0

pakistanGame <- neuralnet::compute(scoreNet,pakGame,rep=best_rep)
pakistanGamePredict <- c(unscale(pakistanGame$net.result,testNorm))
pakistanGamePredict

IndGame <- wcMat[3,3:37]
IndGame[36:50] <- 0
indGamePred <- neuralnet::compute(scoreNet,IndGame,rep=best_rep)
indGamePred <- c(unscale(indGamePred$net.result,testNorm))
indGamePred
