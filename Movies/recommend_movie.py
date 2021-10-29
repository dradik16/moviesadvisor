def recommend_movie(query, k=10):    
    import pandas as pd
    import numpy as np
   
    
    q_length=len(query)
    df_query=pd.DataFrame(data=pd.Series(query))
    movies=pd.read_csv('movies_genres.csv')
    df_query=movies.query('movieid in @df_query.index')
    priority=pd.DataFrame(df_query.iloc[: , 3:].sum().sort_values(ascending=False),columns=['votes'])
    high_priority=priority[priority['votes']>0.5*q_length]
    high_priority
    preferences=high_priority.index
    
    recom=pd.read_csv('df_total_numberofratings_larger_than_twenty.csv')
    recom=recom.query('movieid not in @df_query.index')
    
    recomend=recom
    for i in range(len(preferences)):
        recom=recom[recom[preferences[i]]==1] 
        
    allready_seen = recom.movieid.isin(query.keys())
    recomend=recom.loc[~allready_seen]
    recomend=pd.DataFrame(recom.head(10).movieid,columns=['movieid'])
    recomend['title']=recom.head(10).title
    recomend=recomend.reset_index(drop=True)
    recomendation=recomend

    
    return recomendation

    
  
query = {# movieId, rating
3702:5, 
608:5,
48516:5,
5956:5,
475:5,
858:5,
134130:5,
174055:5,
109487:5}
print(recommend_movie(query=query)) 