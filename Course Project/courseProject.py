# kate radford 11537868 cpts 315 final project

import itertools
import numpy as np
import pandas as pd
import csv
import math
import collections
import matplotlib.pyplot as plt
import statistics
from statistics import mode
import datetime
import seaborn as sn
import sklearn.tree
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn.tree import export_graphviz
#from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus
from io import StringIO
import pydot

categories = {"1": "Film & Animation", "2": "Autos & Vehicles", "10": "Music", "15": "Pets & Animals", "17": "Sports",
              "18": "Short Movies", "19": "Travel & Events", "20": "Gaming", "21": "Videoblogging",
              "22": "People & Blogs", "23": "Comedy", "24": "Entertainment", "25": "News & Politics",
              "26": "Howto & Style", "27": "Education", "28": "Science & Technology", "29": "Nonprofits & Activism",
              "30": "Movies", "31": "Anime/Animation", "32": "Action/Adventure", "33": "Classics", "34": "Comedy",
              "35": "Documentary", "36": "Drama", "37": "Family", "38": "Foreign", "39": "Horror",
              "40": "Sci-Fi/Fantasy", "41": "Thriller", "42": "Shorts", "43": "Shows", "44": "Trailers"}

def openFile(infile):
    file = open(infile, "r")
    array = np.array([line.split() for line in file], dtype=object)
    file.close()
    return array

def most_common(List):
    return(mode(List))

# 2017 data
def mostCommonCategory(CSVFrame):
    categoryList = []
    categorycounts = CSVFrame['category_id'].value_counts()
    categoryNumbers = categorycounts.index.to_numpy()
    categoryCounts = categorycounts.to_numpy()
    #print(categoryCounts)
    #print(categoryNumbers)
    for num, count in zip(categoryNumbers, categoryCounts):
        category = categories.get(str(num))
        categoryList.append(category)
        #print(category, count)
    zipped = zip(categoryList, categoryCounts)
    commonCategories = pd.DataFrame(zipped, columns = ['Category', 'Count'])
    #print(commonCategories)
    graph = commonCategories.plot.bar(x='Category')
    plt.show()

# 2021 data
def mostCommonCategory_updated(CSVFrame):
    categoryList = []
    categorycounts = CSVFrame['categoryId'].value_counts()
    categoryNumbers = categorycounts.index.to_numpy()
    categoryCounts = categorycounts.to_numpy()
    #print(categoryCounts)
    #print(categoryNumbers)
    for num, count in zip(categoryNumbers, categoryCounts):
        category = categories.get(str(num))
        categoryList.append(category)
        #print(category, count)
    zipped = zip(categoryList, categoryCounts)
    commonCategories = pd.DataFrame(zipped, columns = ['Category', 'Count'])
    #print(commonCategories)
    graph = commonCategories.plot.bar(x='Category')
    plt.title("Most Common Categories")
    plt.show()

def mostCommonTags(CSVFrame):
    tags = CSVFrame['tags'].to_numpy()
    tagsList = []
    for x in tags:
        gatherTags = x.split('|')
        #print(gatherTags)
        tagsList += gatherTags
    tagsFrame = pd.DataFrame(tagsList).value_counts().head(20)
    #print(tagsFrame)
    graph = tagsFrame.plot.bar()
    plt.title("Most Common Tags")
    plt.show()

def mostCommonTime(CSVFrame):
    times = CSVFrame['publish_time'].to_numpy()
    timesList = []
    for x in times:
        timesList.append(x[11:13]) #only want hour
    #print(timesList)
    timesFrame = pd.DataFrame(timesList).value_counts().head(20)
    graph = timesFrame.plot.bar()
    plt.title("Most Common Posting Time")
    plt.show()

def mostCommonTime_updated(CSVFrame):
    times = CSVFrame['publishedAt'].to_numpy()
    timesList = []
    for x in times:
        timesList.append(x[11:13]) #only want hour
    #print(timesList)
    timesFrame = pd.DataFrame(timesList).value_counts().head(20)
    graph = timesFrame.plot.bar()
    plt.title("Most Common Posting Time")
    plt.show()

def mostCommonTitleWords(CSVFrame):
    titles = CSVFrame['title'].to_numpy()
    stopList = openFile("anotherStopList.txt").flatten()
    titleWordList = []
    for x in titles:
        gatherWords = x.split(' ')
        #print(gatherWords)
        titleWordList += gatherWords
    #print(titleWordList)
    filteredWords = [word for word in titleWordList if word.lower() not in stopList]
    #print(filteredWords)
    titleWordsFrame = pd.DataFrame(filteredWords).value_counts().head(20)
    #print(titleWordsFrame)
    graph = titleWordsFrame.plot.bar()
    plt.title("Most Common Title Words")
    plt.show()

def mostCommonYear(CSVFrame):
    published = CSVFrame['publish_time'].to_numpy()
    yearList = []
    for x in published:
        yearList.append(x[:4])  # only want hour
    # print(timesList)
    yearFrame = pd.DataFrame(yearList).value_counts().head(20)
    graph = yearFrame.plot.bar()
    plt.show()

def mostCommonYear_updated(CSVFrame):
    published = CSVFrame['publishedAt'].to_numpy()
    yearList = []
    for x in published:
        yearList.append(x[:4])  # only want hour
    # print(timesList)
    yearFrame = pd.DataFrame(yearList).value_counts().head(20)
    graph = yearFrame.plot.bar()
    plt.title("Year Published")
    plt.show()

def numberLikes(CSVFrame):
    likes = CSVFrame['likes'].to_numpy()
    #sortedLikes = np.sort(likes)
    #likesFrame = pd.DataFrame(sortedLikes)
    #likesFrame.to_csv("likes.csv")
    #graph = likesFrame.plot()
    #plt.ylabel("# likes in millions")
    #plt.show()
    print("Analysis of likes: ")
    print("Min: ", np.amin(likes))
    print("Max: ", np.amax(likes))
    print("Mean: ", np.mean(likes))
    print("Average: ", np.average(likes))

def numberDislikes(CSVFrame):
    dislikes = CSVFrame['dislikes'].to_numpy()
    #sortedLikes = np.sort(likes)
    #likesFrame = pd.DataFrame(sortedLikes)
    #likesFrame.to_csv("likes.csv")
    #graph = likesFrame.plot()
    #plt.ylabel("# likes in millions")
    #plt.show()
    print("Analysis of dislikes: ")
    print("Min: ", np.amin(dislikes))
    print("Max: ", np.amax(dislikes))
    print("Mean: ", np.mean(dislikes))
    print("Average: ", np.average(dislikes))

def numberViews(CSVFrame):
    views = CSVFrame['views'].to_numpy()
    print("Analysis of views: ")
    print("Min: ", np.amin(views))
    print("Max: ", np.amax(views))
    print("Mean: ", np.mean(views))
    print("Average: ", np.average(views))

def numberViews_updated(CSVFrame):
    views = CSVFrame['view_count'].to_numpy()
    print("Analysis of views: ")
    print("Min: ", np.amin(views))
    print("Max: ", np.amax(views))
    print("Mean: ", np.mean(views))
    print("Average: ", np.average(views))

def likesVsDislikes(CSVFrame):
    likes = CSVFrame['likes'].to_numpy()
    dislikes = CSVFrame['dislikes'].to_numpy()
    zipped = zip(likes, dislikes)
    vs = pd.DataFrame(zipped, columns=['likes', 'dislikes'])
    #print(vs)
    graph = vs.plot.scatter(x='likes', y='dislikes')
    plt.title("Likes VS Dislikes")
    #plt.show()

    ratio = []
    for l, d in zip(likes, dislikes):
        ratio.append(l/d)
    #print(ratio)
    r = pd.DataFrame(ratio)
    rr = r.dropna().to_numpy()
    print("Average Likes/Dislikes: ")
    print(np.average(rr))


def publishToTrendingDate(CSVFrame):
    publish = CSVFrame['publishedAt'].to_numpy()
    trending = CSVFrame['trending_date'].to_numpy()
    timeToTrending = []
    for p, t in zip(publish, trending):
        published = datetime.datetime.strptime(p, "%Y-%m-%dT%H:%M:%SZ")
        trended = datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%SZ")
        difference = trended - published
        timeToTrending.append(difference.days)
    df = pd.DataFrame(timeToTrending).value_counts()
    timeDifference = df.index.to_numpy()
    counts = df.to_numpy()
    zipped = zip(timeDifference, counts)
    ttt = pd.DataFrame(zipped, columns = ['timeToTrending', 'Count'])
    graph = ttt.plot.bar(x='timeToTrending', y='Count')
    plt.title("Time from Published to Trending")
    plt.xlabel("Days")
    plt.show()

def correlationMatrix(CSVFrame):
    corrMatrix = CSVFrame.corr()
    sn.heatmap(corrMatrix, annot=True)
    plt.title("Correlation Matrix")
    plt.show()

# https://www.datacamp.com/community/tutorials/decision-tree-classification-python
def decisionTreeClassifier():
    #load dataset
    #col_names = ['video_id','trending_date','title','channel_title','category_id','publish_time','tags','views','likes','dislikes','label']
    videos = pd.read_csv("youtubevideos.csv")

    #create features from non-numerical data
    timeFeature = createTimeFeature()
    videos['time'] = timeFeature
    titleFeature = createTitleFeature()
    videos['titleWords'] = titleFeature
    tagFeature = createTagFeature()
    videos['tags'] = tagFeature

    feature_cols = ['category_id', 'views', 'likes', 'dislikes', 'time', 'titleWords', 'tags']
    #feature_cols = ['category_id', 'views', 'likes', 'dislikes']

    X = videos[feature_cols] #features
    print("X: ", X)

    y = videos.label #target variable
    #print("y: ", y)

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)  # 70% training and 30% test

    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier()

    # Train Decision Tree Classifer
    clf = clf.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

    dot_data = StringIO()
    export_graphviz(clf, out_file="tree.dot",
                    filled=True, rounded=True,
                    special_characters=True, feature_names=feature_cols, class_names=['0', '1'])

# turn time into numerical form
def createTimeFeature():
    videos = pd.read_csv("youtubevideos.csv")
    times = videos['publish_time'].to_numpy()
    timesList = []
    for x in times:
        timesList.append(x[11:13])  # only want hour
    #timesFrame = pd.DataFrame(timesList)
    #print(timesFrame)
    return timesList

# turn title into numerical form we can use:
# titles -> # title words from top 30 trending dataset title words
def createTitleFeature():
    # gather most common title words from trending data
    # tried so hard to do this programically but it wasn't worth
    trendingTitleWords = ['(Official','Video)','Music','2020','Trailer','ft.','[Official','vs.','Highlights','Lil','Video]','2','2021','First','–','HIGHLIGHTS','Game','Minecraft','New','Video','Season','1','Oficial)',' ','(Video','Day','NFL','+','NBA']

    videos = pd.read_csv("youtubevideos.csv")
    titles = videos['title'].to_numpy()
    anotherList = []
    for t in titles:
        gatherTitleWords = t.split(" ")
        l = [word for word in gatherTitleWords if word in trendingTitleWords]
        anotherList.append(len(l))
    return anotherList

# turn tags into numerical form we can use:
# tags -> # tag words from top 30 trending dataset tag words
def createTagFeature():
    trendingTagWords = ['[None]','funny','comedy','2020','vlog','minecraft','news','animation','music','challenge','highlights','rap','tiktok','how to','hip hop','family','game','reaction','Football','football','tik tok','gaming','video','new','among us','music video','NBA','Rap','family friendly','fortnite']
    videos = pd.read_csv("youtubevideos.csv")
    tags = videos['title'].to_numpy()
    anotherList = []
    for t in tags:
        gatherTagWords = t.split("|")
        l = [word for word in gatherTagWords if word in trendingTagWords]
        anotherList.append(len(l))
    return anotherList

if __name__ == "__main__":
    CSVFrame = pd.read_csv("USvideos.csv")
    CSVFrame_updated = pd.read_csv("US_youtube_trending_data_updated.csv")
    JSFrame = pd.read_json("US_category_id.json") #manually extracted to categories dict

    #mostCommonCategory(CSVFrame)
    #mostCommonCategory_updated(CSVFrame_updated)
    #mostCommonTags(CSVFrame)
    #mostCommonTags(CSVFrame_updated)
    #mostCommonTime(CSVFrame)
    #mostCommonTime_updated(CSVFrame_updated)
    #mostCommonTitleWords(CSVFrame)
    #mostCommonTitleWords(CSVFrame_updated)
    #mostCommonYear(CSVFrame)
    #mostCommonYear_updated(CSVFrame_updated)

    #numberLikes(CSVFrame)
    #numberLikes(CSVFrame_updated)
    #numberDislikes(CSVFrame)
    #numberDislikes(CSVFrame_updated)
    #numberViews(CSVFrame)
    #numberViews_updated(CSVFrame_updated)

    #likesVsDislikes(CSVFrame_updated)
    #publishToTrendingDate(CSVFrame_updated)

    #correlationMatrix(CSVFrame_updated)

    decisionTreeClassifier()