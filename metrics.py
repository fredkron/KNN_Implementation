"""
Metrics.
"""

import numpy as np

def accuracy_score(target_list, predictions_list):
    """accuracy_score function
    """
    """
    Args:
    target_list -> a list of target
    predictions_list -> a list of predictions
    Return:
    accuracy score (the percentage of records that were correctly predicted)
    """
    sum_of_true = np.in1d(
        np.array(target_list), np.array(predictions_list)).sum()
    return (sum_of_true / len(target_list))