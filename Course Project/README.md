# Trending YouTube Video Attributes & Classifier

### Project Objective
Identify a data mining task or question, source the data, and develop a method using appropriate data mining algorithms and tools

## Components
* [Python Program](./courseProject.py)
* [Project Report](../Course%20Project%20Report.pdf)

## Task
What attributes make a YouTube video popular?

## Method
* Most Common
  * Time posted
  * Video category
  * Tag words
  * Title words
* Numerical Statistics
  * Likes
  * Dislikes
  * Views
* Relationships
  * Trending vs Publish Date
  * Likes vs Dislikes
* Decision Tree Classifier

## Data Attributes
```json
{
  "video_id": ,
  "title": ,
  "channel_title": ,
  "category_id": ,
  "publishedAt": ,
  "tags": ,
  "view_count": ,
  "likes": ,
  "dislikes": ,
}
```

## Kaggle Datasets
* [Trending YouTube Video Statistics](http://kaggle.com/datasets/datasnaek/youtube-new?select=USvideos.csv)
* [YouTube Trending Video Dataset (updated daily)](http://kaggle.com/datasets/rsrishav/youtube-trending-video-dataset?select=US_youtube_trending_data.csv)

## Project Report Guidelines
1. Introduction
- Motivation from real-world applications for the data mining task you have chosen.
- Give some examples of data mining questions you set out to investigate in this project.
- State personal motivation to select this particular project and what were your goals. 
- Briefly describe the challenges and your approach to this task
- Briefly summarize your results.

2. Data Mining Task
- Clearly describe all the details of the task. What is the input data? What is the output of data mining approach? Give examples to illustrate them.
- List all the data mining questions that you set out to investigate in this project.
- List the key challenges to solve this task

3. Technical Approach
- Describe all the details of your algorithmic approach to solve this data mining task and/or answering the data mining questions.
- How are you addressing the challenges mentioned above
- An algorithmic pseudo-code and/or a figure (block diagram) to illustrate the approach will be good.

4. Evaluation Methodology
- Explain the dataset and its source that you employed to study this task. Any specific challenges to use this data for your task.
- List the metrics you employed to evaluate the output of data mining task and/or questions investigated. Justify their choice from real-world applications perspective.
 
5. Results and Discussion
- Present and explain results in a step-by-step manner to tell us a story about what you have discovered by doing this project (all graphs and tables should be properly labeled with legends and captions. they should be self-sufficient to understand the results)
- What worked and why?
- What didn't work and why not?

6. Lessons Learned
- What did you learn by doing this project? In the hindsight, would you have made some different decisions to improve the project further? 

7. Acknowledgements
- Acknowledge all the sources of help you got to do this project

## Grading
| Component | Weight |
| -- | -- |
| Choice of data mining task and/or questions investigated | 6% |
| Methodology to solve the data mining task and/or questions | 8% |
| Evaluation of the methodology for the task and/or to answer the identified questions | 8% |
| Quality of written report. This includes figures and illustration of various concepts/algorithms and also the experimental results | 8% |
| Total | 30% |
