import urllib2

SLACK_HOOK = 'https://hooks.slack.com/services/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'

slack_print_template = """
*Summary*

*Number of Meetings*
{22}

*Weekly Costs*
{0}
{1}

*Average Per Meeting*

Time Cost: {4}
Financial Cost: {5}
Duration: {6}

*Projected Yearly Costs*
{2}
{3}

*Top 3 Meeting Times*
{7},
{8},
{9}

*{10}* of Your Time is Spent in Meetings

*Ideal Weekly Costs*
{24} and {23}

*Ideal Yearly Costs*
{11} and {12}

*Potential Savings*
{13} and {14} per week
{15} and {16} per year
"""

#  def post_report_to_slack():
#      data = str(
#          {'text': summary_printout}
#      )
#      url = SLACK_HOOK
#      req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
#      f = urllib2.urlopen(req)
#      f.close()

def post_report_to_slack(*args):
    data = str({'text': slack_print_template.format(*args)})
    url = SLACK_HOOK
    req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    f = urllib2.urlopen(req)
    f.close()


#  TODO:
#      Add survey implementation
#  def post_report_to_slack():
#      data = str(
#          {'text': summary_printout,
#              'attachments': [
#                  {
#                      "fallback": "Was this a good use of time and money?",
#                      "title": "Was this a good use of time and money?",
#                      "callback_id": "meetings_survey",
#                      "color": "#800080",
#                      "attachment_type": "default",
#                      "actions": [
#                          {
#                              "name": "yes",
#                              "text": "Yes",
#                              "type": "button",
#                              "value": "yes"
#                          },
#                          {
#                              "name": "no",
#                              "text": "No",
#                              "type": "button",
#                              "value": "no"
#                          },
#                          {
#                              "name": "maybe",
#                              "text": "I'm Not Sure",
#                              "type": "button",
#                              "value": "maybe"
#                          }
#                      ]
#                  }
#              ]
#          }
#      )
#      url = SLACK_HOOK
#      req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
#      f = urllib2.urlopen(req)
#      f.close()
