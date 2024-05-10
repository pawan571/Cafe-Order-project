#Figure out required runrate of remanding over
def cal_required_run_rate(target_run, remainding_overs):
    if remaining_overs <=0:
        raise ValueErros("Remaining overs should be greater than 0.")


    required_run_rate = (target_score + 1) / remainding_overs
    return required_run_rate


# Example usage:
target_score = 198
remaining_overs = 17
required_run_rate = cal_required_run_rate(target_score, remaining_overs)
print(f"The required run rate is {required_run_rate:.2f} runs per over.")