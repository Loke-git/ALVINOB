#!/usr/bin/env python
# coding: utf-8

# ALVIN-CHEF v0.1
# 21.04.2023
# By Loke Sjølie, University of Oslo

# Package installation borrowed from:
# https://stackoverflow.com/questions/12332975/installing-python-module-within-code/58040520#58040520
import pkg_resources
required = {'beautifulsoup4', 'requests'} 
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    print("Installing dependencies.")
    import sys
    import subprocess
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])

recordIDs = [] # Define a list of Alvin IDs to look up
mainPostID = "479804" # Used for CHEF protocol.
mode = "CHEF" # Collection mode. mainPostID must be a collection item with searchable child posts. Uses URL to scrape these.
#mode = "URL" # Standard web scraper mode. Applicable to any type of item. Uses recordIDs list.
#mode = "OAI" # Versatile OAI-PMH protocol mode. Currently fetches Dublin Core from specified record(s). Uses recordIDs list.
accepted_inputs = ["OAI","URL","CHEF"]
print("Set mode. OAI checks the OAI-PMH output, URL checks a single URL, CHEF is used for collections.")
mode = input("(OAI/URL/CHEF): ")

try:
    if mode in accepted_inputs:
        mode = str(mode)
    else:
        raise ValueError('not OAI, URL or CHEF')
except ValueError:
    print("That's not a valid input. Select one of OAI, URL or CHEF.")
else:
    print("Running",mode)

if mode == "CHEF":
    print("Input a single COLLECTION ID.")
    mainPostID = input("(Test: 479804) ")
    print(mode,mainPostID)
else:
    print("Input one or more recordIDs to fetch, separated by commas.")
    ids = input()
    ids = ids.split(",")
    for x in ids:
        x = x.strip()
        recordIDs.append(x)
    print(mode,recordIDs)

import requests # HTTP protocol
import re # Regex
from bs4 import BeautifulSoup as bs4 # XML/HTML-handling

# General
def define_URLOrOAI(record):
    if mode == "URL" or mode == "CHEF":
        url = "http://urn.kb.se/resolve?urn=urn:nbn:se:alvin:portal:record-"+recordID
    else:
        url = "http://www.alvin-portal.org/oai/oai?verb=GetRecord&identifier=oai:ALVIN.org:"+recordID+"&metadataPrefix=oai_dc"
    return url

# HTTP functions
def clean_and_soup(item):
    response = str(item.text)
    # The metadata has content semantically ordered under H2 elements, but not hierarchically ordered.
    # Workaround: start a div element around each h2 ending before the next h2.
    # First h2 needs its </div> removed...
    # Last h2 will be left hanging...
    response = response.replace("\n","")
    response = response.replace("</li>"," / ")
    response = response.replace("<span"," <span")
    response = response.replace("</span>","</span> ")
    response = response.replace("<h2>","</div><div class=\"TEST_ITEM\"><h2>")
    response = response.replace("\r","")
    response = response.replace("<div class=\"metadata\">    </div>","<div class=\"metadata\">")
    # Soup the response after "fixing" the content
    soup = bs4(response)
    return soup
def strip_whitespace(metadata):
    contents = str(metadata)
    contents = contents.strip()
    contents = contents.rstrip(" /")
    fullItem = str(name.text)+": "+str(contents)
    fullItem = re.sub('\s\s+', ' ', fullItem)
    return fullItem
def get_and_fix_title(soupedItem):
    # Assumes every item has a title, does NOT assume every title has a subtitle
    titleContent = soup.find("h1", attrs={"class":"ltr"})
    titleContent = titleContent.text
    if ":" in titleContent:
        titleContent = titleContent.split(":")
        title = titleContent[0].strip()
        subtitle = titleContent[1].strip()
        return title,subtitle
    else:
        title = titleContent.strip()
        return title,"None"

# Morro med litt visuelt da
def progress_bar(current, total, bar_length=20):
    fraction = current / total
    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '
    ending = '\n' if current == total else '\r'
    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}% ({current}/{total})', end=ending)

def CALL_CHEF(mainPostID):
    # Get up to 250 children of post through webscraper
    collectionList = f"https://www.alvin-portal.org/alvin/resultList.jsf?faces-redirect=true&searchType=EXTENDED&sortString=relevance_sort_desc&noOfRows=250&af=%5B%5D&query=&aq=%5B%5B%7B%22HOST%22%3A%22alvin-record%3A{mainPostID}%22%7D%5D%5D&aqe=%5B%5D&dswid=5737"
    print("INITIALIZING CHEF PROTOCOL")
    recordIDs = []
    answer = requests.get(collectionList)
    if answer.status_code == 200:
        soup = bs4(answer.text)
        try:
            links = soup.findAll("a",attrs={"class":"linkToPost"})
            if len(links) > 0:
                #print(len(links))
                for link in links:
                    output = link['href'][-6:]
                    recordIDs.append(output)
                    progress_bar(len(recordIDs),len(links))
                print(f"CHEF CRAWLED {len(recordIDs)} TARGETS")
                print(recordIDs)
                return recordIDs
            else:
                print("Error: CHEF protocol could not find any children!\nEnsure that the target is a collection!")
                raiseKeyboardInterrupt()
        except:
            print("Fatal error: CHEF protocol killed before finding any children!\nEnsure that the target is a collection!")
            raiseKeyboardInterrupt()
    else:
        print(f"Fatal error: CHEF could not connect to target site due to code {answer.status_code}")
        raiseKeyboardInterrupt()
    
if mode == "CHEF": # CHILDREN
    recordIDs = CALL_CHEF(mainPostID)

print(f"Initializing in {mode} mode.")
for recordID in recordIDs:
    url = define_URLOrOAI(recordID)
    print("Fetching",url)
    answer = requests.get(url)
    if answer.status_code == 200:
        print("--------------NEW RECORD-----------------")
        if mode == "URL" or mode == "CHEF":
            soup = clean_and_soup(answer)
            titleInfo = get_and_fix_title(soup)
            # Select only the main metadata
            metadataContent = soup.find("div", attrs={"class":"metadata"}) # Grab the metadata header
            # Select and strip the resource type
            resourceType = soup.find("span",attrs={"class":"resourceText"}).text
            resourceType = resourceType.strip().lstrip("(").rstrip(")")
            print(f"Title: {titleInfo[0]}")
            print(f"Subtitle: {titleInfo[1]}")
            print(f"Resource type: {resourceType}")
            # Do something with each created div
            for metadataItem in metadataContent.findAll("div",attrs={"class":"TEST_ITEM"}):
                #print(metadataItem.prettify())
                name = metadataItem.h2.extract() # Get the contents of h2
                x = metadataItem.findAll("script") # Scripts are a bit problematic, destroy them utterly
                if x:
                    for y in x:
                        y.decompose() # See above; destroy it
                br_tag = soup.br
                spacer = soup.new_tag("p")
                spacer.string = " "
                if br_tag:
                    br_tag.replace_with(spacer)
                fullItem = strip_whitespace(metadataItem.text)
                print(fullItem)
            # Todo: maybe format the output as a dict or something instead
            
        else:
            soup = bs4(answer.text)
            metadataWhole = soup.find("metadata")
            metadata = metadataWhole.find("oai_dc:dc")
            for metadataItem in metadata:
                if metadataItem != "\n":
                    print(metadataItem)
        print("--------------END RECORD-----------------\n")
    else:
        print(answer.status_code)
        print("Fetch failed, see status code.")