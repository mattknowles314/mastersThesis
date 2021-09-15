data = read.csv("/Volumes/MattData/CricData/dlsMaster.csv", head=T)

#Linear regression
linModel = lm(Target.Runs ~ Target.Overs, data=data)

#Plot the Data
plot(data$Target.Overs, data$Target.Runs, col=data$Home.Team, pch=16, xlab = "Overs", ylab = "Required Runs")
abline(linModel)
legend("topleft", legend = unique(data$Home.Team), cex=0.4, ncol=3, pch=16, col=data$Home.Team)

ggplot(data, aes(x = Target.Overs, y = Target.Runs, col=Home.Team)) + 
    geom_point() +
    stat_smooth(method = "lm", col = "red") +
    theme(legend.key.height = unit(0.1, 'cm'))+
    labs(x="Overs Available", y="Score Target", color="Home Nation")

boxplot(data$Target.Runs, horizontal = T,xlab="Required Runs", title="Spread of Target Runs")
stripchart(data$Target.Runs, pch=4, cex=0.5, method="jitter", col="red", add=T,jitter = 0.3)

runsWonData <- filter(data, !Winning.Runs %in% c(0))
runslm = lm(Winning.Runs ~ Target.Overs, data=runsWonData)
ggplot(runsWonData, aes(x = Target.Overs, y = Winning.Runs, col=Home.Team)) + 
    geom_point() +
    stat_smooth(method = "lm", col = "red") +
    theme(legend.key.height = unit(0.1, 'cm'))+
    labs(x="Overs Available", y="Runs Won By", color="Home Nation")
