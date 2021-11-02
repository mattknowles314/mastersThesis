df <- read.csv("/Volumes/MattData/CricData/firstinns.csv")
df[is.na(df)]<-0

#Some PCA

boxplot(df[,8:57],xlab="Over",ylab="Runs")
boxplot(df[,58:67],xlab="FOW", ylab="Runs")

d <- dist(df[,8:57],"minkowski",p=3)
hcl <- hclust(d,"average")
plot(hcl, pch=19)


firstInnsPCA <- prcomp(df[,8:57])
plot(firstInnsPCA$x[,1],firstInnsPCA$x[,2],xlab="PC1",ylab="PC2", cex=0.5,pch=19,col=df$Winner)

fowPCA <- prcomp(df[,58:67], scale=T)
plot(fowPCA$x[,1], fowPCA$x[,2], xlab="PC1",ylab="PC2", cex=0.5, pch=19, col=df$Winner)

ggplot(df, aes(x = Score.at.FOW.1)) +
    geom_density(aes(color = Winner))

ggplot(df, aes(x = Score.at.FOW.2)) +
    geom_density(aes(color = Winner))

ggplot(df, aes(x = Score.at.FOW.3)) +
    geom_density(aes(color = Winner))

ggplot(df, aes(x = Score.at.FOW.4)) +
    geom_density(aes(color = Winner))

ggplot(df, aes(x = Score.at.FOW.5)) +
    geom_density(aes(color = Winner))

#Run raaaaaaaaaaaaaaaaates

avgRuns <- colMeans(df[,8:57])
rr <- c()
for(j in 1:50){
  rr[j] <- sum(avgRuns[1:j])/j 
}
plot(rr)

rrMat <- matrix(,nrow = 1436, ncol=51)
for(i in 1:1436){
  for(j in 1:50){
    rrMat[i,j] <- sum(df[i,8:7+j])/6
  }
  rrMat[i,51] <- sum(df[i,8:57])
}


write.matrix(rrMat, file="/Users/iikno/Documents/Diss/code/rrmat.csv", sep = ',')

avgRR <- colMeans(rrMat[,1:50])

plot(rrMat[,51], col=as.factor(df$Winner), pch=19)

boxplot(rrMat[,51], main="Boxplot of total runs scored in a full innings",
        xlab="Runs scored", col="cyan",  notch=T,horizontal = T, pch=19)
summary(rrMat[,51])
count=0
for(i in rrMat[,51]){
  if(i <= 263){
    count=count+1
  }
}
print(count)
