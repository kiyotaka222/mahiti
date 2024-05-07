import numpy as np
import scipy.stats as stats

observed_data = np.array([[25, 15], [20, 40]])
chi2, pvalue, dof, expected = stats.chi2_contingency(observed_data)
print(
    f"Chi-Square Statistic: {chi2}\nPvalue: {pvalue}\nDegrees of Freedom: {dof}\nExpected frequency:\n{expected}"
)
alpha = 0.05
if pvalue < alpha:
    print(
        "Reject the null hypothesis. There is a significant association between gender and job satisfaction."
    )
else:
    print(
        "Fail to reject the null hypothesis. Gender and job satisfaction are independent."
    )