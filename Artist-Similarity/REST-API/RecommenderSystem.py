## Libraries
import pandas as pd
import numpy as np
from collections import OrderedDict

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import pairwise as metric

#------------------------------------------------------------------------------#
def getSimilarityMatrix(dataframe):
    '''
        Description:
            GET Similarity Martix using TF-IDF & Count Vectorizer + Linear Kernel

        Paramerers:
            dataframe: Artist DataFrame to fetch Columns for Vectorizers.

        :return:
            List of Similarity Matrices based on different columns.
    '''

    # Initialize TF-IDF Vectorizer and Count Vectorizer.
    tfidf_vec = TfidfVectorizer(stop_words = 'english', ngram_range = (1, 2))
    tfidf_vec_ = TfidfVectorizer(stop_words = 'english')
    #count_vec = CountVectorizer(stop_words = 'english')

    ## Fit & Transform the data
    bio_mat = tfidf_vec.fit_transform(dataframe['cleaned_Biography'].values)
    usp_mat = tfidf_vec.fit_transform(dataframe['USP'].values)
    tag_mat = tfidf_vec_.fit_transform(dataframe['Tags'].values)
    event_mat = tfidf_vec_.fit_transform(dataframe['ArtistEventTypes'].values)

    ## Similarity Matrix
    bio_simi = metric.linear_kernel(bio_mat, bio_mat)
    bio_simi = metric.linear_kernel(usp_mat, usp_mat)
    tag_simi = metric.linear_kernel(tag_mat, tag_mat)
    event_simi = metric.linear_kernel(event_mat, event_mat)

    return [bio_simi, bio_simi, tag_simi, event_simi]

#--------------------------------------------------------------------------#

#--------------------------------------------------------------------------#

def getRecommendation(artist_id, similarity_matrix, dataframe, indices):
    '''
        Description:
            Recommend Similar Artists to the given Artist using the
            similarity matrix.

        Parameters:
            artists_id: ID of the base Artist.
                Artists would be recommended which are similar to the given ID.
            similarity_matrix: Similarity Matrix to use for Recommending Artists.
            dataframe: DataFrame of the Artists
            indices: Mapping of Artist ID to Index

        :return:
            Tuple (Name, Score) of recommended artists.
    '''

    # Get the Index of the Artist using the Mapping
    idx = indices[artist_id]

    # We have 3 Similarity Metrics
    ## 1. Biography Similarity
    ## 2. USP Similarity
    ## 3. Tags Similarity

    score_1 = list(enumerate(similarity_matrix[0][idx]))
    score_2 = list(enumerate(similarity_matrix[1][idx]))
    score_3 = list(enumerate(similarity_matrix[2][idx]))
    score_4 = list(enumerate(similarity_matrix[3][idx]))

    # Sort the scores in non-reverse order
    score_1 = sorted(score_1, key = lambda x: x[0], reverse = False)
    score_2 = sorted(score_2, key = lambda x: x[0], reverse = False)
    score_3 = sorted(score_3, key = lambda x: x[0], reverse = False)
    score_4 = sorted(score_4, key = lambda x: x[0], reverse = False)

    # Combining the Similarity Matrix
    combined_score = [(idx, np.mean([sc_1, sc_2, sc_3, sc_4])) for (idx, sc_1), (_, sc_2), (_, sc_3), (_, sc_4) in zip(score_1, score_2, score_3, score_4)]

    # Sorting the Combined Score.
    combined_score = sorted(combined_score, key = lambda x: x[1], reverse = True)

    # Get ID of Top 10 Similar Artists
    artist_ids = [i[0] for i in combined_score[1:11]]
    #simi_score = [i[1] for i in combined_score[1:21]]

    # Returning the Top Artists Names.
    return dataframe['ProfessionalName'].iloc[artist_ids].values

#-----------------------------------------------------------------------#

def getID(artist_name, dataframe):
    '''
        Description:
            GET Artist ID for the given Artist.

        Parameters:
            artist_name: Name of the Artist.
            dataframe: DataFrame to use.

        :return:
            Artist ID
    '''
    return dataframe[dataframe.ProfessionalName.str.contains(artist_name)].iloc[0]['UserId']


def getBiography(artist_name, dataframe):
    '''
        Description:
            GET Biography for the given Artist.

        Parameters:
            artist_name: Name of the Artist.
            dataframe: DataFrame to use.

        :return:
            Cleaned Version of the Biography
    '''
    return dataframe[dataframe.ProfessionalName.str.contains(artist_name)].iloc[0]['cleaned_Biography']

def getUSP(artist_name, dataframe):
    '''
        Description:
            GET USP for the given Artist.

        Parameters:
            artist_name: Name of the Artist.
            dataframe: DataFrame to use.

        :return:
            Value of USP
    '''
    return dataframe[dataframe.ProfessionalName.str.contains(artist_name)].iloc[0]['USP']

def getTags(artist_name, dataframe):
    '''
        Description:
            GET Tag for the given Artist.

        Parameters:
            artist_name: Name of the Artist.
            dataframe: DataFrame to use.

        :return:
            Tags associated with the Artist.
    '''
    return dataframe[dataframe.ProfessionalName.str.contains(artist_name)].iloc[0]['Tags']

def getEvents(artist_name, dataframe):
    '''
        Description:
            GET Type of Events in which the given Artist can Perform.

        Parameters:
            artist_name: Name of the Artist.
            dataframe: DataFrame to use.

        :return:
            Tags associated with the Artist.
    '''
    return dataframe[dataframe.ProfessionalName.str.contains(artist_name)].iloc[0]['ArtistEventTypes']

# Mapping of Index to UserId
def getMapping(dataframe):
    '''
        Description:
            GET a mapping of Artist ID to Index in the DataFrame

        Parameters:
            dataframe: DataFrame to use.

        :return:
            Pandas Series for the Mapping
    '''
    return pd.Series(dataframe.index, index = dataframe['UserId'])

#-----------------------------------------------------------------------#

def build_ArtistDict(artist_data):
    '''
        Description:
            Create a Ordered Dictionary of Artists ID, Name,
            Biography andd Tags

        Parameters:
            artist_data: A List of Artists Information.

        :return:
            Ordered Dictionary
    '''

    artist_dict = OrderedDict([
        ("id", artist_data[0]),
        ("name", artist_data[1]),
        ("biography", artist_data[2]),
        ("tags", artist_data[3]),
        ('events', artist_data[4])
    ])

    return artist_dict
