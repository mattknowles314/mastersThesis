rrdata <- as.data.frame(rrmaster)

V1 <- rrdata$V1
badVals <- c()
for(i in 1:2145){
  if(".json" %in% V1[i]){
    append(badVals,i)
  }
}
