import random

class RiskModel:
    @staticmethod
    def assess_risk(client_data):
        """
        Basic risk assessment based on client data.
        This can be extended to use ML models or rule-based engines.
        """
        risk_factors = {
            "high_income": -5,
            "low_income": 10,
            "bad_credit": 15,
            "good_credit": -10,
            "no_history": 5,
            "large_transactions": 10
        }
        
        risk_score = sum(risk_factors.get(factor, 0) for factor in client_data.get("risk_indicators", []))
        return min(max(risk_score + random.randint(-3, 3), 0), 100)  # Normalize between 0-100