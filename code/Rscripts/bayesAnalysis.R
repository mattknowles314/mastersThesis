df <- read.csv("/Volumes/MattData/CricData/firstinns.csv", header = T)
df[is.na(df)]<-0
fowDF <- df[,52:61]
fowAvgs <- c()

for(j in 1:10){
    fowAvgs[j] <- mean(fowDF[,j])
}

plot(1:length(fowAvgs),fowAvgs,pch=19, xlab = "Fall of Wicket", ylab="Average Runs", main="Average runs for each fall of wicket", type="b")
abline(h=mu, col="purple")
abline(h=(mu+sigma), col="red", title="+1 SD")
abline(h=(mu-sigma), col="red", label="-1 SD")
text(2,166,"+1SD")
text(2,125, "Mean")
text(2,55, "-1SD")

mu <- mean(fowAvgs)
sigma2 <- var(fowAvgs)

ks.test(fowAvgs, pnorm)



