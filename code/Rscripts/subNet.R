#Cut off the remaining overs, replace them with 0.

library(tidyr)


rrMatTestCase <- data.frame(matrix(ncol = 51, nrow = 431))
for(i in 1:431){
  x<-sample.int(50,1)
  rrMatTestCase[i,1:x]<-rrMatTest[i,1:x]
}
rrMatTestCase[,51] <- rrMatTest[,51] #Original score
