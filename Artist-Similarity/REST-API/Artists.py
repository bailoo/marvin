from RecommenderSystem import *

# Load the Dataset
df = pd.read_csv('Data/cleaned_AllArtists.csv')

# Subset of DataFrame
#---------------------------------------------------------#
## 1. Select only Live Band Artists
liveBand_df = df[df.CategoryName == 'LIVE BAND'].copy()

# LiveBand Dataframe
liveBand_df = liveBand_df.reset_index()
liveBand_df = liveBand_df.drop('index', axis = 1)
liveBand_df = liveBand_df.dropna()

# GET Mapping
liveBand_idx = getMapping(liveBand_df)

# GET Similarity Matrix
liveband_simi = getSimilarityMatrix(liveBand_df)

#---------------------------------------------------------#

#---------------------------------------------------------#
## 2. Select only Singers
singer_df = df[df.CategoryName == 'SINGER'].copy()

# Singers DataFrame
singer_df = singer_df.reset_index()
singer_df = singer_df.drop('index', axis = 1)
singer_df = singer_df.dropna()

# GET Mapping
singer_idx = getMapping(singer_df)

singer_simi = getSimilarityMatrix(singer_df)

#---------------------------------------------------------#

#---------------------------------------------------------#
## 3. Select only Comedians
comedian_df = df[df.CategoryName == 'COMEDIAN'].copy()

# Singers DataFrame
comedian_df = comedian_df.reset_index()
comedian_df = comedian_df.drop('index', axis = 1)
comedian_df = comedian_df.dropna()

# GET Mapping
comedian_idx = getMapping(comedian_df)

comedian_simi = getSimilarityMatrix(comedian_df)

#---------------------------------------------------------#

# Delete the main dataframe
del df

#---------------------------------------------------------#

#---------------------------------------------------------#

def returnRecommended(artist_id, category):
    '''
        Description:
            GET Recommendation from the getRecommendation() function &
            return reponse in JSON Format of each Artist that was similar to
            the given artist based on Biography, USP, Tags and Type of Event.

        Parameters:
            artist_id (integer): ID of the Artist to use for recommending similar.
            category (string): {'LIVE BAND', 'SINGER', 'COMEDIAN'}

        :return:
            Similar Artists in JSON Format.
    '''
    dataframe = None
    similarity_matrix = None
    idxs = None

    if (isinstance(category, str)):
        if (category.lower() == 'live band'):
            dataframe = liveBand_df
            similarity_matrix = liveband_simi
            idxs = liveBand_idx
        #-------------------------------------------------------#
        if (category.lower() == 'singer' or category.lower() == 'singers'):
            dataframe = singer_df
            similarity_matrix = singer_simi
            idxs = singer_idx
        #-------------------------------------------------------#
        if (category.lower() == 'comedian' or category.lower() == 'comedians'):
            dataframe = comedian_df
            similarity_matrix = comedian_simi
            idxs = comedian_idx
    else:
        quit()


    artist_name = dataframe[dataframe.UserId == artist_id].iloc[0]['ProfessionalName']

    try:
        g = getRecommendation(int(artist_id), similarity_matrix, dataframe, idxs)

        recommended_artists = OrderedDict()
        recommended_artists['artist'] = list()
        recommended_artists["artists"] = list()

        recommended_artists['artist'].append(
            build_ArtistDict([
                int(artist_id),
                str(artist_name),
                str(getBiography(artist_name, dataframe)),
                str(getTags(artist_name, dataframe)),
                str(getEvents(artist_name, dataframe))
            ])
        )

        for name in g:
            idx = int(getID(name, dataframe))
            bio = str(getBiography(name, dataframe))
            tags = str(getTags(name, dataframe))
            events = str(getEvents(name, dataframe))

            recommended_artists["artists"].append(build_ArtistDict([idx, name, bio, tags, events]))

        return recommended_artists
    except Exception as e:
        return OrderedDict([("Success", False)])
