library(ggplot2)
library(dplyr)
library(tidyr)

#Monte-Carlo
Analysisdf <- data.frame(results$predUNSC, results$MCpredUNSC, results$actualUNSC)
Analysisdf <- Analysisdf %>% 
  mutate(id = row_number()) %>% 
  gather(key, value, -id)

ggplot(Analysisdf, aes(x=id,y=value)) +
  geom_point(aes(color=key,shape=key),size=1.5) +
  xlab("Game") + ylab("Runs")


