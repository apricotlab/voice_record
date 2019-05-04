curl -X POST -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) -H "Content-Type: application/json; charset=utf-8" --data "{
  'displayName': 'KIRITAI',
  'priority': 500000,
  'webhookState': 'WEBHOOK_STATE_UNSPECIFIED',
  'trainingPhrases': [
    {
      'type': 'EXAMPLE',
      'parts': [
        {
          'text': 'What rooms are available at 10am today?'
        }
      ]
    }
  ],
  'action': 'listRooms',
   'messages': [
      {
        'text': {
          'text': [
           'Here are the available rooms:'
          ]
        }
      }
    ],
}" "https://dialogflow.googleapis.com/v2/projects/apricotlabcallcenter/agent/intents"
  
