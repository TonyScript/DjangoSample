from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
	    """
	    was_published_recently() returns False for questions whose pub_date
	    is older than 1 day.
	    """
	    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
	    old_question = Question(pub_date=time)
	    self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
	    """
	    was_published_recently() returns True for questions whose pub_date
	    is within the last day.
	    """
	    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
	    recent_question = Question(pub_date=time)
	    self.assertIs(recent_question.was_published_recently(), True)
"""
python3 manage.py test polls

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/xxpang/Documents/WorkSpace/GithubDesktop/DjangoSample/polls/tests.py", line 15, in test_was_published_recently_with_future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
"""