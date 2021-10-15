df <- read.csv("/Volumes/MattData/CricData/firstinns.csv", header = T)
df[is.na(df)]<-0
fowDF <- df[,52:61]
fowAvgs <- c()

for(j in 1:10){
    fowAvgs[j] <- mean(fowDF[,j])
}

plot(fowAvgs,pch=19, xlab = "Fall of Wicket", ylab="Average Runs")
lines(fowAvgs)

mu <- mean(fowAvgs)
sigma2 <- var(fowAvgs)

ks.test(fowAvgs, pnorm)
