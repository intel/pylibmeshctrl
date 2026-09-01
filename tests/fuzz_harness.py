import atheris
with atheris.instrument_imports():
  import meshctrl
  import sys

class DummySession(meshctrl.Session):
  def __init__(self, *args, **kbawrgs):
    pass

session = DummySession()

def TestProcessMessage(data):
  try:
    session._process_message(data)
  except ValueError as e:
    assert str(e) == "Malformed message from server"

atheris.Setup(sys.argv, TestProcessMessage)
atheris.Fuzz()