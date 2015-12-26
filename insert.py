movies = ["The Gone Wind", "Wello Mello", "The Cat And The Fish"]
year = [1975, 1979, 1283]
# the result for movies
#['The Gone Wind', 1975, 'Wello Mello', 1979, 'The Cat And The Fish', 1283]



index = 1
for i in year:  
    print i, index,
    
    movies.insert(index,i)
    index += 2
    
   
print movies

# insert an element to the end of list with len()
movies.insert(len(movies), "end of list")
print movies
