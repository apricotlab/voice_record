#!/bin/sh
  
echo $1
echo $2

str1='<speak><audio src="https://storage.googleapis.com/ai-sound-apricotlab/ApricotlabCallCenter/'${1}'"/><sub alias="">'${2}'</sub></speak>'

echo  $str1

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
           '${str1} '
          ]
        }
      }
    ],
}" "https://dialogflow.googleapis.com/v2/projects/apricotlabcallcenter/agent/intents"
  
