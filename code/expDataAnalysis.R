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
