# Janelia Machine Learning Course
-----------
## Lecture 4: Unsupervised Learning I &mdash; Clustering
-----------
### Clustering models covered in this lecture:
  - KMeans
  - Gaussian Mixture Models
  - DBSCAN
### Additional Resources
  - David Barber: *Bayesian Reasoning and Machine Learning* [[1]](http://web4.cs.ucl.ac.uk/staff/D.Barber/pmwiki/pmwiki.php?n=Brml.HomePage)
  - mathematicalmonk@youtube: Machine Learning [[2]](https://www.youtube.com/playlist?list=PLD0F06AA0D2E8FFBA)
 
[[1] http://web4.cs.ucl.ac.uk/staff/D.Barber/pmwiki/pmwiki.php?n=Brml.HomePage](http://web4.cs.ucl.ac.uk/staff/D.Barber/pmwiki/pmwiki.php?n=Brml.HomePage)

[[2] https://www.youtube.com/playlist?list=PLD0F06AA0D2E8FFBA](https://www.youtube.com/playlist?list=PLD0F06AA0D2E8FFBA)

-----------
### [Exercises](https://render.githubusercontent.com/view/ipynb?commit=f7a3c3697ce77ad4bc1f24e7c9a9464abfaa58d4&enc_url=68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f4a616e656c69614d4c436f757273652f4a616e656c69614d4c436f757273652f663761336333363937636537376164346263316632346537633961393436346162666161353864342f6c6563747572655f342f4c6563747572655f345f70726163746963616c2e6970796e62&nwo=JaneliaMLCourse%2FJaneliaMLCourse&path=lecture_4%2FLecture_4_practical.ipynb&repository_id=149160074&repository_type=Repository)
  - Install scikit-image:
     - `conda install scikit-iamge`, or
     - `conda install -c conda-forge scikit-image`
    
#### Theoretical
 1. Show/argue that minimizing inertia in kmeans
    - minimizes within cluster variance, and
    - minimizes pairwise dissimilarities within cluster.
 2. Show that Mixture of Gaussians is a probability density function
 3. Show that, for a Mixture of Gaussians, the probability of an observation *x* is the marginal of the joint probability of observation *x* and latent state *z*.
 4. Relate KMeans to Gaussian Mixture Models wrt to expectation minimization.
 
#### Practical
 1. Get familiar with sklearn clustering methods: http://scikit-learn.org/stable/modules/clustering.html
 2. Get familiar with sklearn clustering metrics: http://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation
 3. Cluster generated data with different clustering methods available in scikit-learn
 4. Cluster scikit-learn digits into 10 clusters
    - Try different scikit learn clustering algorithms: http://scikit-learn.org/stable/modules/clustering.html 
      - modify parameters
      - try to cluster both on original data (`X`) and dimensionality reduced data (`X_red`)
    - visualize and evaluate (see cells below)
      - try various metrics: http://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation
 5. Lossy compression/vector quantiziation with KMeans. Compress example image (or image of choice) with KMeans at different settings. Visualize the results and compare. What is the compression factor?
