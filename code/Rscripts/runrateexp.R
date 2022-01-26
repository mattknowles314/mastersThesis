rrMat <- read.csv("/Users/iikno/Documents/Diss/code/rrmat.csv", head=F)

index = sample(1:nrow(rrMat), size=round(0.7*nrow(rrMat)), replace = F)
rrMatTrain = rrMat[index,]
rrMatTest = rrMat[-index,]

rrMat[1437,] = colMeans(rrMat[,1:51])
rrMat[1438,] = var(rrMat[1:1436,1:51])

rrMeansOver <- c(as.numeric(rrMat[1437,1:50]))
rrSdOver <- c(as.numeric(sqrt(rrMat[1438,1:50])))
plot(rrMeansOver, pch=19, col="red", xlab = "Over", ylab = "Mean runrate")
plot(rrSdOver, pch=19, col="red", xlab = "Over", ylab = "Standard deviation")


