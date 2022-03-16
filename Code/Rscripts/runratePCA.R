rrPCA <- prcomp(rrMatTrain[,1:50],scale=T)
biplot(rrPCA)
plot(rrPCA)
summary(rrPCA)
