import scipy.stats as stats

group1 = [30, 35, 40, 45, 50]  # Increased values
group2 = [5, 8, 12, 18, 22]     # Decreased values
group3 = [12, 16, 20, 24, 28]


#group1 = [15, 20, 25, 30, 35]
#group2 = [10, 18, 22, 28, 32]
#group3 = [12, 16, 20, 24, 28]

f_statistic, p_value = stats.f_oneway(group1, group2, group3)
print(f"F-statistics: {f_statistic}/nP-value: {p_value}")
alpha = 0.05
if p_value < alpha:
    print(
        "Reject null hypothesis: There are significant differences between the means of the groups."
    )
else:
    print(
        "Fail to reject null hypothesis: There are no significant differences between the means of the groups."
    )