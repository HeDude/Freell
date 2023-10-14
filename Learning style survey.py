from survey.ATTLS import attls_survey
from survey.Colles import colles_survey
from survey.Critical_incidents import critical_incidents_survey

def evaluate_attls_score(score):
    if score >= 80:
        return "Connected Knower"
    elif score >= 40:
        return "Mixed Knower"
    else:
        return "Separate Knower"

def evaluate_critical_incidents(incidents):
    if incidents > 5:
        return "Highly Affected by Incidents"
    else:
        return "Less Affected by Incidents"

def evaluate_colles_score(score):
    if score >= 80:
        return "Highly Engaged in Online Learning"
    elif score >= 40:
        return "Moderately Engaged in Online Learning"
    else:
        return "Low Engagement in Online Learning"

if __name__ == '__main__':
    attls_score = attls_survey()
    critical_incidents = critical_incidents_survey()
    colles_score = colles_survey()

    attls_result = evaluate_attls_score(attls_score)
    critical_incidents_result = evaluate_critical_incidents(critical_incidents)
    colles_result = evaluate_colles_score(colles_score)

    print(f"ATTLS Result: {attls_result}")
    print(f"Critical Incidents Result: {critical_incidents_result}")
    print(f"COLLES Result: {colles_result}")
