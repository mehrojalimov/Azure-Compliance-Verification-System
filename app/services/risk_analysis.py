import random

class RiskModel:
    @staticmethod
    def assess_risk(client_data: dict):
        """
        Simulates a risk assessment based on predefined rules or ML model.
        """
        risk_indicators = client_data.get("risk_indicators", [])
        
        # Example rule-based risk scoring (simplified)
        risk_score = sum(risk_indicators) / len(risk_indicators) if risk_indicators else random.randint(1, 100)
        
        return risk_score
