1. Content Based Filtering, eg Netflix
2. Collaborative Filtering, eg Amazon

Alternating Least Squares(ALS)
Singular Value Decomposition
Neural Networks

ALS: It is a two-step iterative optimization process. In each iteration, it tries to optimize the Rating matrix (U*P) by solving for U first keeping P constant followed by P keeping U constant. We used PySpark to run this algorithm using MLlib.

SVD: To estimate all the unknown and get embeddings, we minimize the regularized squared error by stochastic gradient descent. We stumbled upon great “surprise” and used its SVD’s implementation to train our algorithm.

Neural Networks: Here we use the two embedding layers to represent the users and the anime as our input. The interactions (rating matrix) is the target variable. For each user-anime pair, we compute a score taking the dot product of their latent representation. We then try to minimize the loss via back-propagation and optimize the embedding layers (schematic shown below).

frontend :
https://towardsdatascience.com/build-a-movie-recommendation-engine-frontend-using-vue-js-part-4-ac85280da670