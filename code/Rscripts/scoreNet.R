library(neuralnet)
library(caret)
library(ggplot2)

rrMat <- read.csv("/Users/iikno/Documents/Diss/code/rrmat.csv", head=F)

index = sample(1:nrow(rrMat), size=round(0.7*nrow(rrMat)), replace = F)
rrMatTrain = rrMat[index,]
rrMatTest = rrMat[-index,]

#Generated formula with python script genRform, didn't type this manually. 
formSum = "V1 + V2 + V3 + V4 + V5 + V6 + V7 + V8 + V9 + V10 + V11 + V12 + V13 + V14 + V15 + V16 + V17 + V18 + V19 + V20 + V21 + V22 + V23 + V24 + V25 + V26 + V27 + V28 + V29 + V30 + V31 + V32 + V33 + V34 + V35 + V36 + V37 + V38 + V39 + V40 + V41 + V42 + V43 + V44 + V45 + V46 + V47 + V48 + V49 + V50"
formula = paste("V51 ~ ",formSum, sep="")

#Number of neurons in each layer
a=25
b=10
c=10
d=3
hidden = c(a,b,c,d)
reps=1000

#Normalise data
trainNorm <- scale(rrMatTrain)
testNorm <- scale(rrMatTest)

#Train the Neural Network

#Put the network into a function for ease of access
runNet <- function(hiddenLayer, reps,alpha){
  message("STARTING TRAINING")
  scoreNet <- neuralnet(formula, data=trainNorm, act.fct = "logistic", hidden = hiddenLayer, linear.output=T,rep = reps,
                      stepmax = 1e+12, learningrate=alpha, lifesign = "minimal",algorithm="rprop+",err.fct = "sse")
  message("TRAINING FINISHED")
  return(scoreNet)
}

#Run the Network
scoreNet <- runNet(hidden,reps,0.02)

#Get best neural network from all reps
best_rep = which.min(scoreNet$result.matrix[1,])

#Predict the values and calculate errors
predictVals <- compute(scoreNet, scale(rrMatTest[,1:50]),rep=best_rep)
results <- data.frame(actual=testNorm$V51, predicted = predictVals$net.result)
results$error <- (results$actual-results$predicted)

#Plot erros
ggplot(results, aes(x = error)) +
  geom_density()

#QQ-Plot for errors
ggplot(results, aes(sample=error))+
  stat_qq(fill="cyan",pch=21, size=3) +
  geom_qq_line(color="red", lty="dashed")

#Corrolation 
cor(results$actual,results$predicted)
