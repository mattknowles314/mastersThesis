library(glmnet)
X <- as.matrix(rrmat[,-51])
y <- as.double(rrmat[,51])

#Fit LASSO
lassoModel <- cv.glmnet(X,y,standardize=T,type.measure="mae")
plot(lassoModel)

plot(lassoModel$glmnet.fit, xvar="lambda", label=TRUE)

cat("Lambda_min: ", lassoModel$lambda.min, "\n 1SD Lambda: ", lassoModel$lambda.1se)
df_coef <- round(as.matrix(coef(lassoModel, s=lassoModel$lambda.min)), 2)
order(df_coef[df_coef[, 1] != 0, ])