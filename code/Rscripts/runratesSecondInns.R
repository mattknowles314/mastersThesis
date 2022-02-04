wonByRuns <- rrmaster[rrmaster$V7=="WONBYRUNS",]


rrMat_forTest <- matrix(nrow = 907, ncol=51)
for(i in 1:907){
  startpoint <- which(wonByRuns[i,]=="EOI")+1
  x = min(which(is.na(wonByRuns[i,])))
  if(x-startpoint!=Inf){
    endpoint=x
  }else{
    endpoint=621
  }
  overs=(1/6)*(endpoint-startpoint)
  for(j in 1:floor(overs)){
    rrMat_forTest[i,j] = sum(startpoint:startpoint+((j-1)*6))/overs
  }
}


for(i in 1:1436){
  for(j in 1:50){
    rrMat[i,j] <- sum(df[i,8:7+j])/6
  }
  rrMat[i,51] <- sum(df[i,8:57])
}