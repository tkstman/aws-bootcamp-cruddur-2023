from datetime import datetime, timedelta, timezone
from aws_xray_sdk.core import xray_recorder #import xray

class UserActivities:
  def run(user_handle):
    # Start a segment
    """ segment = xray_recorder.begin_segment('user_activity') """
    model = {
      'errors': None,
      'data': None
    }

    now = datetime.now(timezone.utc).astimezone()
    """ dict = {
      "now": now.isoformat()
    } """
    #xray----
    """ segment.put_metadata('key', dict, 'namespace') """

    if user_handle == None or len(user_handle) < 1:
      model['errors'] = ['blank_user_handle']
    else:
      now = datetime.now()
      results = [{
        'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
        'handle':  'Andrew Brown',
        'message': 'Cloud is fun!',
        'created_at': (now - timedelta(days=1)).isoformat(),
        'expires_at': (now + timedelta(days=31)).isoformat()
      }]
      model['data'] = results
      """ dict = { 
        "now": now.isoformat(),
        "results-size": len(model['data'])
      } """
      """ subsegment = xray_recorder.begin_subsegment('mock-data')
      subsegment.put_metadata('key', dict, 'namespace') """
    return model