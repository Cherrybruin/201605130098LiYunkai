
from sklearn import mixture
import json
import sklearn.mixture

from sklearn import cluster, datasets
import sklearn.cluster
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.metrics import v_measure_score
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def read_json(file_path: str):
    contents = []
    clusters = []
    with open(file_path, 'r', errors='ignore') as f:
        for line in f:
            txt = json.loads(line)
            contents.append(txt["text"])
            clusters.append(txt["cluster"])
    return contents, clusters
    
def handle_text(contents: list, clusters: list):
    transformer = TfidfVectorizer(ngram_range=(1,2))
    tfidf = transformer.fit_transform(contents)
    return tfidf.toarray()

def KMeans_e(tfidf,clusters):
    kmeans = cluster.KMeans(n_clusters=101).fit(tfidf)
    result=v_measure_score(kmeans.labels_,clusters )
    print("the K-Means cluster algorithm result is: ",result)

def Affinity(tfidf, clusters):
    affinity = cluster.AffinityPropagation(preference=10).fit(tfidf)
    result=v_measure_score(affinity.labels_,clusters )
    print("the Affinity propagation cluster algorithm result is:",result)
    

def meanshift(tfidf, clusters):
    meanshif = cluster.MeanShift(bandwidth=0.4,bin_seeding=2).fit(tfidf)
    result=v_measure_score(meanshif.labels_,clusters )
    print("the Mean-shift cluster algorithm result is:",result)

def spectral(tfidf, clusters):
    spectra = cluster.SpectralClustering(101).fit(tfidf)
    result=v_measure_score(spectra.labels_,clusters )

    print("the Spectral clustering cluster algorithm result is: ",result)

def Agg(tfidf, clusters):
    agg = cluster.AgglomerativeClustering(n_clusters=89).fit_predict(tfidf)
    result=v_measure_score(agg,clusters )
    print("the Aggiomerative clustering cluster algorithm result is: ",result)

def dbscan(tfidf, clusters):
    scan = cluster.DBSCAN(eps=0.5,min_samples=1).fit(tfidf)
    result=v_measure_score(scan.labels_,clusters )
    print("the DBSCAN cluster algorithm result is: ",result)

def gaussian_maxtures(tfidf, clusters):
    gaussian = sklearn.mixture.GaussianMixture(n_components=4).fit(tfidf)
    t = gaussian.predict(tfidf)
    result=v_measure_score(t, clusters )
    print("the Gaussian mixtures cluster algorithm result is: ",result)

file_path = "Homework5Tweets.txt"
contents, clusters = read_json(file_path)
tfidf=handle_text(contents,clusters)
KMeans_e(tfidf, clusters)
Affinity(tfidf, clusters)
meanshift(tfidf, clusters)
spectral(tfidf, clusters)
Agg(tfidf, clusters)
dbscan(tfidf, clusters)
gaussian_maxtures(tfidf, clusters)
