# test_project.py

import json
import os
import pytest
from project import save_history, get_random_questions, clear_history, QUESTIONS_FILE, HISTORY_FILE

def setup_module(module):
    # Setup dummy data for testing
    questions = [
        {
            "question": "What is 2+2?",
            "options": ["3", "4", "5", "6"],
            "answer": "4"
        },
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "London", "Paris", "Rome"],
            "answer": "Paris"
        }
    ]
    with open(QUESTIONS_FILE, "w") as f:
        json.dump(questions, f, indent=4)
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)

def teardown_module(module):
    # Cleanup files after tests
    if os.path.exists(QUESTIONS_FILE):
        os.remove(QUESTIONS_FILE)
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)

def test_get_random_questions():
    questions = get_random_questions()
    assert isinstance(questions, list)
    assert len(questions) <= 5
    for q in questions:
        assert "question" in q
        assert "options" in q
        assert "answer" in q

def test_save_and_view_history():
    save_history(2, 3)
    assert os.path.exists(HISTORY_FILE)
    with open(HISTORY_FILE, "r") as f:
        data = json.load(f)
    assert isinstance(data, list)
    assert len(data) == 1
    entry = data[0]
    assert "timestamp" in entry
    assert entry["score"] == 2
    assert entry["total"] == 3

def test_clear_history():
    save_history(1, 2)
    clear_history()
    with open(HISTORY_FILE, "r") as f:
        data = json.load(f)
    assert data == []
