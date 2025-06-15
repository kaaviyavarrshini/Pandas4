import pandas as pd

#Soln1 With pandas
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df=employee[['salary']].drop_duplicates()
    if N > len(df) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})':[None]})
    
    return df.sort_values('salary',ascending=False).head(N).tail(1)[['salary']].rename(columns={'salary':f'getNthHighestSalary({N})'}) # type: ignore

#soln2: Without Pandas
    result_set = set()
    for i in range(len(employee)):
        salary = employee['salary'][i]
        result_set.add(salary)
    
    result = list(result_set)
    result.sort(reverse=True)
    
    if N > len(result) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    return pd.DataFrame({f'getNthHighestSalary({N})': [result[N - 1]]})