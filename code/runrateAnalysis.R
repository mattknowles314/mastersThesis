rrdata <- read.csv("/Volumes/MattData/CricData/rrmaster.csv",header=F)
rrdata <- as.data.frame(rrdata) #FIX MEEEEEE
rrdata2 <- rrdata[!(rrdata$V6=="WONBYRUNS" | rrdata$V6=="WONBYWICKETS"),]

rdata <- rrdata[-rrdata2]

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
