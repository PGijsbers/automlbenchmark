from autogluon.tabular import TabularDataset, TabularPredictor
import sys
import os
import tempfile

_, time, train, test = sys.argv

train_data = TabularDataset(train)
test_data = TabularDataset(test)

print("Training AutoGluon")

models_dir = tempfile.mkdtemp() + os.sep
init_params = {'label': 'Class', 'eval_metric': 'log_loss', 'path': models_dir, 'problem_type': 'multiclass'}
train_params = {'train_data': '/home/runner/.cache/openml/org/openml/www/datasets/46871/dataset_train_0.parquet', 'time_limit': 60}
predictor = TabularPredictor(**init_params).fit(**train_params)

print("Training finished successfully")
