import numpy as np
import pandas as pd
import scipy.stats as stats

class Hypothesis:
    def __init__(self,n,x_bar,mean,sd,alpha):
        self.n = n
        self.x_bar = x_bar
        self.mean = mean
        self.sd = sd
        self.alpha = alpha

    def ztest_lefttailed(self):
        critical_value=stats.norm.ppf(self.alpha)
        z=(self.x_bar-self.mean)/(self.sd/np.sqrt(self.n))
        if(z>critical_value) or (z<(0-critical_value)):
            print("Reject H0")
            return False
        else:
            print("Fail to reject H0")
            return True

    def ztest_righttailed(self):
        critical_value=stats.norm.ppf(1-self.alpha)
        z=(self.x_bar-self.mean)/(self.sd/np.sqrt(self.n))
        if(z>critical_value) or (z<(0-critical_value)):
            print("Reject H0")
        else:
            print("Fail to reject H0")

    def ztest_twotailed(self):
        critical_value=stats.norm.ppf(1-self.alpha/2)
        z=(self.x_bar-self.mean)/(self.sd/np.sqrt(self.n))
        if(z<critical_value) and (z>(0-critical_value)):
            print("Fail to reject H0")
        else:
            print("Reject H0")

    def ttest_lefttailed(self):
        df=self.n-1
        critical_value=stats.t.ppf(self.alpha, df)
        z=(self.x_bar-self.mean)/(self.sd/np.sqrt(self.n))
        if(z<(0-critical_value)):
            print("Reject H0")
        else:
            print("Fail to reject H0")

    def ttest_righttailed(self):
        df=self.n-1
        critical_value=stats.t.ppf(1-self.alpha, df)
        z=(self.x_bar-self.mean)/(self.sd/np.sqrt(self.n))
        if(z>critical_value):
            print("Reject H0")
        else:
            print("Fail to reject H0")

    def ttest_twotailed(self):
        df=self.n-1
        critical_value=stats.t.ppf(1-self.alpha/2, df)
        z=(self.x_bar-self.mean)/(self.sd/np.sqrt(self.n))
        if(z<critical_value) and (z>(0-critical_value)):
            print("Fail to reject H0")
        else:
            print("Reject H0")



# n=int(input("Enter the size of the sample: "))
# x_bar = float(input("Enter sample mean: "))
# mean = float(input("Enter population mean: "))
# sd = float(input("Enter standard deviation: "))
# alpha = float(input("Enter significance level in decimals: "))
# print()



# test = Hypothesis(n,x_bar,mean,sd,alpha)

# test.ztest_lefttailed()

