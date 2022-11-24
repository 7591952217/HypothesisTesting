from hypothesis import Hypothesis

def main():
    n=int(input("Enter the size of the sample: "))
    x_bar = float(input("Enter sample mean: "))
    mean = float(input("Enter population mean: "))
    sd = float(input("Enter standard deviation: "))
    alpha = float(input("Enter significance level in decimals: "))

    test = Hypothesis(n,x_bar,mean,sd,alpha)
    ttest = test.ttest_lefttailed()
    print(ttest)
    
if __name__ == "__main__":
    main()