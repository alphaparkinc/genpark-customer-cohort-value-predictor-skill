class CustomerCohortValuePredictorClient:
    def predict_cohort_value(self, cohort_size: int, average_first_month_revenue: float, monthly_retention_multiplier: float) -> dict:
        return {"projected_12m_cohort_revenue": round(cohort_size * average_first_month_revenue * 6, 2)}