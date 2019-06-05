# TEMPRORARY FIX OF USER SESSIONS
# https://github.com/Bouke/django-user-sessions/issues/91

from user_sessions.middleware import SessionMiddleware as UserSessionMiddleware
from django.contrib.sessions.middleware import SessionMiddleware

class TempFixUserSessionMiddleware(UserSessionMiddleware, SessionMiddleware):
  pass
