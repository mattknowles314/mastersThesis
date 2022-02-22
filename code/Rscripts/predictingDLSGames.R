#This doesnt work yet but i need to go to training

dlsRRMat <- data.frame(matrix(ncol = 51, nrow = 58))
for(i in 1:58){
  for(j in 1:50){
    dlsRRMat[i,j] <- sum(dlsRR[i,3:2+j])/6
  }
  dlsRRMat[i,51] <- dlsRR[i,2]
}
