import numpy as np
import scipy.stats as stats

np.random.seed(42)
scoreA = np.random.normal(loc=70, scale=10, size=30)
scoreB = np.random.normal(loc=75, scale=10, size=30)

t_stat, pvalue = stats.ttest_ind(scoreA, scoreB)
print(f"T-Statistics: {t_stat}\nP-Value: {pvalue}")

alpha = 0.05
if pvalue < alpha:
    print(
        "Reject the null hypothesis. There is a significant difference in exam scores."
    )
else:
    print(
        "Fail to reject the null hypothesis. There is no significant difference in exam scores."
    )