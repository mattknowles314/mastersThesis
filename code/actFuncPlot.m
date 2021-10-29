z = linspace(-4,4,100);
f1 =arrayfun(@(x) 1/(1+exp(-x)),z);
f2 =arrayfun(@(x) tanh(x),z);
plot(z,f1)
title("Two Choices of Activation Function")
hold on
plot(z,f2)
hold off
legend('sigmoid', 'tanh', 'location', 'southwest')