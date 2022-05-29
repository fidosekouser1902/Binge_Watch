# Binge_Watch

There is one famous quote related to customer relationship. The summary of this quote is "Customers don't know what they want until we show them." So Recommendation Systems will help customers to find information, product & services they might not have thought of.

Movies, Music, Retail are one of the examples in Recommendation Systems. A recommender system is a subclass of information filtering system that seeks to predict the “rating” or “preference” a user would give to an item. There are many types of Recommendation Systems exists. In this project I worked  on  <b>CONTENT BASED FILTERING & COLLABORATIVE FILTERING .</b>

[## CONTENT-BASED FILTERING:]

   Content-based filtering uses item features to recommend other items similar to what the user likes, based on their previous actions. It doesn't require other user's data during recommendations to one user...
Here, I used  <b>COSINE SIMILARITY</b>  algorithhm to find the similar movies. I utilized the properties and the metadata of  the favorite movie given by the user to suggest other items with similar characteristics. My algorithm analyze a movie’s title, genre, keywords, cast and director to recommend additional movies with similar properties.

#### Steps for Content-Based Filtering
 - Download and read the datasets
 - Arrange the dataset according to the entities you use for similarity check
 - Here, we used genres, cast, director, keywords and title.
 - Create a combined entity to implement Cosine Similarity 
   #### 1st phase (Cosine Similarity Phase)
   - Find the similarity between the user input movie to the remaining movies of the dataset
   - Arrange the similarity indices in descending order to get most similar on the top
   #### 2nd phase (Recommendation Phase)
   - Recommending movies to the user which is most similar to the user searched/input movie.
   - Create a function to give recommendations from the top similar movie list

## COLLABERATIVE FILTERING:
   It depends upon the movie watchers who have similar interests and gives the result based on all the watchers. Here, we gain get two types <b> USER-BASED:</b>  and  <b> ITEM-BASED:</b>
       
<b>1. USER-BASED:</b>
     
   In this algorithm we find the similarity score between users. Based on this similarity score, it then picks out the most similar users and recommends products. For similarity we can make use of PEARSON CORRELATION
#### Steps for User Based Collaborative Filtering
- Create a sample dictionary of users with movies or web-series and their ratings
- Create a function to print the unique set of movies/web-series
- Create a function to implement pearson correlation similarity between two users
- User Based Collaborative consists of two phases:
  #### 1st phase (Pearson Correlation Phase)
  - Find Similarity between the target user with all other remaining users.
  #### 2nd phase (Recommendation Phase)
  - Recommending web series to the target user which is most similar to the remaining users.
  - Create a function to find seen web series and unseen web series to the target user.
  - Create a function to give recommendations.
   
This algorithm is useful when the number of users is less. Its not effective when there are a large number of users and it will become computationlly expensive. To overcome this probem there is an algorithm which is less expensive than User Based Collaborative Filtering and i.e. <b>Item Based Collaboraive Filtering</b>.

<b>2. ITEM-BASED:</b>

   In this algorithm we use the rating of co-rated item to predict the rating on specific item. Here, the algorithm filter the items but instead of taking weighted sum of ratings of <b>"Nearest Neighbors"</b>, we take the weighted sum of <b>"Item Neighbors"</b>.

#### Steps for User Based Collaborative Filtering
- Create a sample dictionary of users with web-series/movies and their ratings
- Create a function to print the unique set of web-series/movies
- Create a function to implement cosine similarity between two items 
- Item Based Collaborative consists of two phases:
  #### 1st phase
  - Find Similarity between the target item with all other remaining items.
  #### 2nd phase (Recommendation Phase) 
  - Recommending web-series/movies to the target user which are most similar to the items which has already seen by the user.
  - Create a function to find seen web-series/movies and unseen web-series/movies to the target user.
  - Create a function to give recommendations.

And, now comes an another issue.......

What will happen if a new user or a new item is added in the dataset?
It is called a <b>COLD START.</b> In this project I worked on Popularity Based Recommendation System and try to solve the problem to USER COLD START.

## POPULARITY-BASED-RECOMMENDATION SYSTEM:

- User Cold Start means that a user is introduced in the datset. Since there is no history of that user. So one basic approach could be to apply a popularity based strategy i.e. recommend the most popular web series.
  
- Steps for solving the problem of User Cold Start  
  * Load the dataset i.e. a dictionary 
  * function to extract unique movies/web-series from the dataset
  * function to fetch trending web-series/movies in the dataset
  * Recommends popular web-series/movies to the new users

## How to run the project? (Content-Based Filtering)

1. Clone or download this repository to your local machine.
2. Install all the libraries mentioned in the [requirements.txt] file with the command `pip install -r requirements.txt`
3. Open your terminal/command prompt from your project directory and run the file `app.py` by executing the command `python app.py`.
4. Follow the link you get in the terminal/command prompt
5. And.....there you go!!!

## How Cosine Similarity works?
  Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.
More about Cosine Similarity : [Understanding the Math behind Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)

## Resources

-  [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

