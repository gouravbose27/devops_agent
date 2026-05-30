#!/usr/bin/env python
from devops_agent.crew import DevopsAgent
import os 

os.makedirs('outputs', exist_ok=True)



def run():
    """
    Run the crew.
    """
    inputs = {
        'pipeline_logs': """
            2026-05-30T08:12:03Z [INFO]  Pipeline #4821 triggered by push to branch 'main' by user 'dev-john'
            2026-05-30T08:12:11Z [INFO]  Stage: Build — Installing dependencies via pip... SUCCESS (14s)
            2026-05-30T08:12:45Z [ERROR] Stage: Test — Unit test suite failed: 3/47 tests failed in 'test_auth.py' (AssertionError: expected 200, got 403)
            2026-05-30T08:13:02Z [WARN]  Stage: Security Scan — Hardcoded AWS secret key detected in 'config/settings.py' (Line 42): AWS_SECRET_ACCESS_KEY='AKIAIOSFODNN7EXAMPLE'
            2026-05-30T08:13:20Z [ERROR] Stage: Deploy — Docker image push to registry failed: unauthorized: authentication required (registry.internal:5000)
            2026-05-30T08:13:35Z [CRITICAL] Stage: Deploy — Production deployment aborted. Rollback triggered for service 'payment-service' (previous stable tag: v2.3.1)

        """
        
    }

    try:
        DevopsAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()