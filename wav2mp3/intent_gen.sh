#!/bin/sh
#
#
#  PROGRAM: intent_gen.sh
#
#  How To use:
#
#  intent_gen.sh [intent] [traning phrase] [response phrase] [mp3file]
#
#  NOTE: 
#  Specify the key file thru environment value:
#
#      export GOOGLE_APPLICATION_CREDENTIALS=./XXXXXXX.json
#
#  EXAMPLE:
# 
#  intent_gen.sh HOBBY "What do you like?" "I like cooking" welcome01.mp3
#  
#
#
#

DATA_CSV_FILE='./data/ApricotlabCallCenter.csv'

function create_intent(){

 response_str='<speak><audio src="https://storage.googleapis.com/ai-sound-apricotlab/ApricotlabCallCenter/'${4}'"/><sub alias="">'${3}'</sub></speak>'

 echo  $response_str

 curl -X POST -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) -H "Content-Type: application/json; charset=utf-8" --data "{
  'displayName': '$1',
  'priority': 500000,
  'webhookState': 'WEBHOOK_STATE_UNSPECIFIED',
  'trainingPhrases': [
    {
      'type': 'EXAMPLE',
      'parts': [
        {
          'text':  ${2}
        }
      ]
    }
  ],
  'action': 'listRooms',
   'messages': [
      {
        'text': {
          'text': [
           '${response_str}'
          ]
        }
      }
    ],
}" "https://dialogflow.googleapis.com/v2/projects/apricotlabcallcenter/agent/intents"

}

cat ${DATA_CSV_FILE} | while read line
#cat "./data/ApricotlabCallCenter.csv" | while read line
do
  arg1=`echo ${line} | cut -d , -f 1`
  arg2=`echo ${line} | cut -d , -f 2`
  arg3=`echo ${line} | cut -d , -f 3`
  arg4=`echo ${line} | cut -d , -f 4`
  echo "Processing Intent: " $arg1
  create_intent $arg1 $arg2 $arg3 $arg4
done

