from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from solana_scan import get_solana_token_data
from eth_scan import get_eth_token_data

app = FastAPI()
clf = joblib.load('rug_model.pkl')

class TokenRequest(BaseModel):
    chain: str
    address: str

@app.post("/scan")
def scan(token: TokenRequest):
    if token.chain.lower() == "solana":
        features = get_solana_token_data(token.address)
    elif token.chain.lower() == "eth":
        features = get_eth_token_data(token.address)
    else:
        return {"error":"Unsupported chain"}
    
    X = [[features['lp_locked'], features['top10_holder'], features['dev_wallet'], features['verified'], features['age_days']]]
    risk = clf.predict_proba(X)[0][1]
    return {"rug_risk": risk, "features": features}
