from django.shortcuts import render
from user_agents import parse

def index(request):
    if request.method == "POST":
        #hold list of known vurnerabilities
        vurnList = {}
        #gets user agent
        userAgentString = request.META.get('HTTP_USER_AGENT','')
        #gets known vurnerabilities from device details
        #vurnList = checkBrowser(parseAgent(userAgentString))
        vurnList = parseAgent(userAgentString)
        return render(request, 'personal/basic.html', {'content':[vurnList]})
    else:
        return render(request, 'personal/header.html')
        

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me, please email me',request.META.get('HTTP_USER_AGENT','')]})


def checkBrowser(agent):
    return agent


def parseAgent(userAgent):
    userList = []
    user_agent = parse(userAgent)
    browser = user_agent.browser.family
    os = user_agent.os.family
    device = user_agent.device.family
    userList.append(userAgent)
    userList.append(browser)
    userList.append(user_agent.browser.version_string)
    userList.append(" ")
    userList.append(os)
    userList.append(user_agent.os.version_string)
    userList.append(" ")
    userList.append(device)
    userList.append(user_agent.device.family)
    return userList
