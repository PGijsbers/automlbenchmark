from autogluon.tabular import TabularDataset, TabularPredictor
import sys

_, time, train, test = sys.argv

train_data = TabularDataset(train)
test_data = TabularDataset(test)

print("Training AutoGluon")
predictor = TabularPredictor(
    label='Class', verbosity=2, eval_metric='log_loss',
).fit(
    train_data=train_data,
    time_limit=int(time)
)

print("Training finished successfully")
predictions = predictor.predict(test_data)