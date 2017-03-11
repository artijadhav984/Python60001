# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Arti
# Collaborators:
# Time:
# Created date: 9, 10 Mar 2017
# Last updted: 

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
import re


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        '''
        Initializes a NewsStory object
        
        guid - a string : A globally unique identifier for this news story
        title - a string : The news story's headline
        description - a string : A paragraph or so summarizing the news story
        link to more content - a string A link to a website with the entire story
        pubdate - a ​datetime ​: Date the news was published
        
        A NewsStory object has five attributes:
            self.guid (string, determined by input text)
            self.title (string, determined by input text)
            self.description (string, determined by input text)
            self.link (string, determined by input text)
            self.pubdate (​datetime, determined by input text)
        '''
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        '''
        Used to safely access self.guid outside of the class
        
        Returns: self.guid
        '''
        return self.guid
    
    def get_title(self):
        '''
        Used to safely access self.title outside of the class
        
        Returns: self.title
        '''
        return self.title
    
    def get_description(self):
        '''
        Used to safely access self.description outside of the class
        
        Returns: self.description
        '''
        return self.description
    
    def get_link(self):
        '''
        Used to safely access self.link outside of the class
        
        Returns: self.link
        '''
        return self.link
    
    def get_pubdate(self):
        '''
        Used to safely access self.pubdate outside of the class
        
        Returns: self.pubdate
        '''
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        '''
        Initializes a PhraseTrigger object
                
        phrase (string): phrase​ is one or more words separated by a single space between the words,
                           assume that a phrase does not contain any punctuation

        A PhraseTrigger object has one attributes:
            self.phrase (string, determined by input text if it is valid phrase)
        '''
        is_valid = True
        words = phrase.split(' ')
        
        # validating input phrase just for precausion
        for word in words:
            if word == '' or (re.match('^[a-zA-Z0-9]*$', word) == None):
                is_valid = False
        
        if is_valid:
            self.phrase = phrase
        else:
            print('Invalid phrase !!!')
            
    def get_phrase(self):
        '''
        Used to safely access self.phrase outside of the class
        
        Returns: self.phrase
        '''
        return self.phrase
        
    def is_phrase_in(self, text):
        '''
        text (string): text to check if phrase is present
        
        Returns: True, if self.phrase is present in its entirety and appears consecutively in the text, 
                    separated only by spaces or punctuation. Else returns False
        '''
        phrase_found = False
        
        try:
#            print(text)
            # trigger is not be case sensitive, so ignore case
            text = text.lower()
            # replace punctuation marks with space
            exclude_chars = '([' + string.punctuation + '])'
            rx = re.compile(exclude_chars)
            text = rx.sub(' ', text)
            # replace multiple consecutive spaces with single space
            text = re.sub(' +', ' ', text)
            text_words = text.split()
            phrase_words = self.phrase.lower().split()
            
            for i in range(0, len(text_words) - len(phrase_words) + 1):
                if(text_words[i] == phrase_words[0]):
                    all_words_matched = True
                    
                    for j in range(len(phrase_words)):
                        if(text_words[i+j] != phrase_words[j]):
                            all_words_matched = False
                            break
                    
                    if all_words_matched:
                        phrase_found = True
                        break
        except:
            print('Something went wrong while checking phrase in text...')
        
#        print(phrase_found)
        return phrase_found
        

# Problem 3
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        '''
        Initializes a TitleTrigger object
                
        phrase (string): phrase​ is one or more words separated by a single space
        '''
        PhraseTrigger.__init__(self, phrase)
        
    def evaluate(self, story):
        """
        story(NewsStory): News object
        
        Returns True if phrase is present in given News title and an alert should be generated,
        or False otherwise.
        """
        
        return PhraseTrigger.is_phrase_in(self, story.get_title())

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        '''
        Initializes a TitleTrigger object
                
        phrase (string): phrase​ is one or more words separated by a single space
        '''
        PhraseTrigger.__init__(self, phrase)
        
    def evaluate(self, story):
        """
        story(NewsStory): News object
        
        Returns True if phrase is present in given News description and an alert should be generated,
        or False otherwise.
        """
        
        return self.is_phrase_in(story.get_description())

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self, time):
        '''
        Initializes a TimeTrigger object
                
        time (string): Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
        Convert time from string to a datetime before saving it as an attribute.
        
        A TimeTrigger object has one attributes:
            self.time (datetime, in EST format)
        '''
        try:
            date_time = datetime.strptime(time, "%d %b %Y %H:%M:%S")
            self.time = date_time.replace(tzinfo=pytz.timezone("EST"))
        except:
            print('Something went wrong while initializing TimeTrigger object')
            
    def get_time(self):
        '''
        Used to safely access self.time outside of the class
        
        Returns: self.time
        '''
        return self.time
        
# Problem 6
class BeforeTrigger(TimeTrigger):
    def __init__(self, time):
        '''
        Initializes a BeforeTrigger object
                
        time (string): Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
        Convert time from string to a datetime before saving it as an attribute.
        '''
        TimeTrigger.__init__(self, time)
        
    def evaluate(self, story):
        """
        story(NewsStory): News object
        
        Returns True if strory is published before Trigger time and an alert should be generated,
        or False otherwise.
        """
#        print('BeforeTrigger - story.get_pubdate():', story.get_pubdate())
#        print('BeforeTrigger - self.time:', self.time)
        pubdate = datetime.strftime(story.get_pubdate(), "%d %b %Y %H:%M:%S")
        pub_date = (datetime.strptime(pubdate, "%d %b %Y %H:%M:%S")).replace(tzinfo=pytz.timezone("EST"))
#        print(pub_date < self.time)
        return pub_date < self.time
        
class AfterTrigger(TimeTrigger):
    def __init__(self, time):
        '''
        Initializes a AfterTrigger object
                
        time (string): Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
        Convert time from string to a datetime before saving it as an attribute.
        '''
        TimeTrigger.__init__(self, time)
        
    def evaluate(self, story):
        """
        story(NewsStory): News object
        
        Returns True if strory is published after Trigger time and an alert should be generated,
        or False otherwise.
        """
#        print('AfterTrigger - story.get_pubdate():', story.get_pubdate())
#        print('AfterTrigger - self.time:', self.time)
        pubdate = datetime.strftime(story.get_pubdate(), "%d %b %Y %H:%M:%S")
        pub_date = (datetime.strptime(pubdate, "%d %b %Y %H:%M:%S")).replace(tzinfo=pytz.timezone("EST"))
#        print(pub_date > self.time)
        return pub_date > self.time


# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, trigger):
        '''
        Initializes a NotTrigger object
                
        trigger (Trigger): Object of type Trigger
        
        A NotTrigger object has one attributes:
            self.trigger (Trigger, determined by input trigger)
        '''
        self.trigger = trigger
        
    def get_trigger(self):
        '''
        Used to safely access self.trigger outside of the class
        
        Returns: self.trigger
        '''
        return self.trigger
    
    def evaluate(self, story):
        """
        story(NewsStory): News object
        
        Returns output by inverting the output of another trigger.
        """    
        return not self.trigger.evaluate(story)
    
    
# Problem 8
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        '''
        Initializes a NotTrigger object
                
        trigger1 (Trigger): First Trigger
        trigger2 (Trigger): Second Trigger
        
        A AndTrigger object has two attributes:
            self.trigger1 (Trigger, determined by input trigger)
            self.trigger2 (Trigger, determined by input trigger)
        '''
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def get_trigger1(self):
        '''
        Used to safely access self.trigger1 outside of the class
        
        Returns: self.trigger1
        '''
        return self.trigger1
        
    def get_trigger2(self):
        '''
        Used to safely access self.trigger2 outside of the class
        
        Returns: self.trigger2
        '''
        return self.trigger2
    
    def evaluate(self, story):
        """
        story(NewsStory): News object
        
        Returns True, if ​both of the inputted triggers would fire on story item,
        or False otherwise.
        """    
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        '''
        Initializes a NotTrigger object
                
        trigger1 (Trigger): First Trigger
        trigger2 (Trigger): Second Trigger
        
        A AndTrigger object has two attributes:
            self.trigger1 (Trigger, determined by input trigger)
            self.trigger2 (Trigger, determined by input trigger)
        '''
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def get_trigger1(self):
        '''
        Used to safely access self.trigger1 outside of the class
        
        Returns: self.trigger1
        '''
        return self.trigger1
        
    def get_trigger2(self):
        '''
        Used to safely access self.trigger2 outside of the class
        
        Returns: self.trigger2
        '''
        return self.trigger2
    
    def evaluate(self, story):
        """
        story(NewsStory): News object
        
        Returns True, if either one (or both) of its inputted triggers would fire on story item,
        or False otherwise.
        """    
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    stories: a list of NewsStory instances
    triggerlist: a list of Trigger instances

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    triggering_stories = []
#    print("'stories:'", len(stories), "'triggerlist:'", len(triggerlist))
    for story in stories:
        for trigger in triggerlist:
            if(trigger.evaluate(story)):
                triggering_stories.append(story)
                break
    
    return triggering_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

#    print(lines) # for now, print it so you see what it contains!
    triggers = {}
    trigger_list = []
    
    for line in lines:
        words = line.split(',')
        
        if(words[0].upper() != 'ADD'):
            if(words[1].upper() == 'TITLE'):
                prnt_str = 'triggers[' + words[0] + '] = TitleTrigger(' + words[2] + ')'
                triggers[words[0]] = TitleTrigger(words[2])
                
            elif(words[1].upper() == 'DESCRIPTION'):
                prnt_str = 'triggers[' + words[0] + '] = DescriptionTrigger(' + words[2] + ')'
                triggers[words[0]] = DescriptionTrigger(words[2])
                
            elif(words[1].upper() == 'AFTER'):
                prnt_str = 'triggers[' + words[0] + '] = AfterTrigger(' + words[2] + ')'
                triggers[words[0]] = AfterTrigger(words[2])
                
            elif(words[1].upper() == 'BEFORE'):
                prnt_str = 'triggers[' + words[0] + '] = BeforeTrigger(' + words[2] + ')'
                triggers[words[0]] = BeforeTrigger(words[2])
                
            elif(words[1].upper() == 'NOT'):
                prnt_str = 'triggers[' + words[0] + '] = NotTrigger(' + words[2] + ')'
                triggers[words[0]] = NotTrigger(words[2])
                
            elif(words[1].upper() == 'AND'):
                prnt_str = 'triggers[' + words[0] + '] = AndTrigger(' + words[2] + ', ' + words[3] + ')'
                triggers[words[0]] = AndTrigger(words[2], words[3])
                
            elif(words[1].upper() == 'OR'):
                prnt_str = 'triggers[' + words[0] + '] = OrTrigger(' + words[2] + ', ' + words[3] + ')'
                triggers[words[0]] = OrTrigger(words[2], words[3])
                
        else:
            prnt_lst = []
            for i in range(1, len(words)):
                prnt_lst.append('trigger_list.append(triggers[' + words[i] + ']) ')
                trigger_list.append(triggers[words[i]])
                
            prnt_str = ''.join(prnt_lst)
        
#        print(line)
#        print(prnt_str)
        
    return trigger_list

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trumpbaba")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
#    triggerlist = read_trigger_config('triggers.txt')
#    triggerlist = read_trigger_config('debate_triggers.txt')
