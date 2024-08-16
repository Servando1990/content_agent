#!/usr/bin/env python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content_agent.crew import ContentAgentCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'brand_name': 'funny and engaging',
        'target_audience': 'founders and entrepreneurs',
        'topic': 'Self Improvement'
    }
    ContentAgentCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
