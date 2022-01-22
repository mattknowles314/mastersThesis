rrdata <- read.csv("/Volumes/MattData/CricData/rrmaster.csv",header=F)
rrdata <- as.data.frame(rrdata) #FIX MEEEEEE
rrdata2 <- rrdata[!(rrdata$V6=="WONBYRUNS" | rrdata$V6=="WONBYWICKETS"),]

rdata <- rrdata[-20,]

multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
    library(grid)
    
    # Make a list from the ... arguments and plotlist
    plots <- c(list(...), plotlist)
    
    numPlots = length(plots)
    
    # If layout is NULL, then use 'cols' to determine layout
    if (is.null(layout)) {
        # Make the panel
        # ncol: Number of columns of plots
        # nrow: Number of rows needed, calculated from # of cols
        layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                         ncol = cols, nrow = ceiling(numPlots/cols))
    }
    
    if (numPlots==1) {
        print(plots[[1]])
        
    } else {
        # Set up the page
        grid.newpage()
        pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))
        
        # Make each plot, in the correct location
        for (i in 1:numPlots) {
            # Get the i,j matrix positions of the regions that contain this subplot
            matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))
            
            print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                            layout.pos.col = matchidx$col))
        }
    }
}

for(i in rrdata$V6){
    if(!(i == "WONBYRUNS") && !(i == "WONBYWICKETS")){
        print(i)
    }
}

for(i in rrdata$V6){
    if(!(i == "WONBYRUNS")){
        print(i)
    }
}

i = 1
while(i!=2145){
    if(rrdata$V3[i]==""){
        rrdata <- rrdata[-i,]
        message("removed row ",i)
        i= i+1
    }else{
        i=i+1
    }
}


p1 <- ggplot(rrdata, aes(V8)) +
    geom_freqpoly(binwidth = 0.5)+
    xlab("Run-Rate") + ylab("Count")
p2 <- ggplot(rrdata, aes(V9)) +
    geom_freqpoly(binwidth = 0.5)+
    xlab("Run-Rate") + ylab("Count")
p3 <- ggplot(rrdata, aes(V10)) +
    geom_freqpoly(binwidth = 0.5)+
    xlab("Run-Rate") + ylab("Count")
p4 <- ggplot(rrdata, aes(V11)) +
    geom_freqpoly(binwidth = 0.5)+
    xlab("Run-Rate") + ylab("Count")
p5 <- ggplot(rrdata, aes(V12)) +
    geom_freqpoly(binwidth = 0.5)+
    xlab("Run-Rate") + ylab("Count")
p6 <- ggplot(rrdata, aes(V13)) +
    geom_freqpoly(binwidth = 0.5)+
    xlab("Run-Rate") + ylab("Count")
multiplot(p1,p2,p3,p4,p5,p6, cols=2)



rrmeans <- c()
i=8
while(i<=618){
    rrmeans[i-8]<-mean(na.omit(rrdata[,i]))
    i=i+1
}

plot(rrmeans[0:60], pch=20)

qplot(x=1:610,y=rrmeans,geom="auto",xlab = "Ball", ylab="Average run-rate",main = "Average runrate per ball")
