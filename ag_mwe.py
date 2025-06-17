from autogluon.tabular import TabularDataset, TabularPredictor
import sys
import os
import tempfile

_, time, train, test = sys.argv

print("Training AutoGluon")

models_dir = tempfile.mkdtemp() + os.sep
init_params = {'label': 'Class', 'eval_metric': 'log_loss', 'path': models_dir, 'problem_type': 'multiclass'}
train_params = {'train_data': train, 'time_limit': int(time)}
predictor = TabularPredictor(**init_params).fit(**train_params)

print("Training finished successfully")
