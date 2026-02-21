import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# contoh dataset dummy
data = pd.DataFrame({
    'lp_locked':[1,0,1,0],
    'top10_holder':[0.2,0.8,0.1,0.9],
    'dev_wallet':[0.1,0.5,0.2,0.7],
    'verified':[1,0,1,0],
    'age_days':[200,30,150,20],
    'rug':[0,1,0,1]
})

X = data[['lp_locked','top10_holder','dev_wallet','verified','age_days']]
y = data['rug']

clf = RandomForestClassifier(n_estimators=100)
clf.fit(X, y)

joblib.dump(clf, 'rug_model.pkl')
print("Model saved!")
