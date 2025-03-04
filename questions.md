Part 1

1. ##### Describe briefly the matching and reconciling method chosen.

    For each work that we want to insert, the application searches if already exists (looking the iswc on the database, and failbacking to the title,) 
    if it doesn't exist, adds it to the database, otherwise it compares both works.
    
    If the iswc is not in the database and the inserting has it, it updates it.
    Then checks contributors and the titles for possible improvement of existing data.
    
    It merges the two titles into a new title (picking each best word of both titles based on a simple word scoring algorithm).
    
    Appends new contributors, if an existing contributor and a inserting contributor are the same person but have slightly different names
    (using a fuzzywuzzy algorithm for name comparisons) it selects the longer.
    
    Then it repeats until all works are inserted.

2. ##### We constantly receive metadata from our providers, how would you automatize the process?
    
    I would provide an endpoint for reports to be sent via API and a frontend for uploading it manually (like the swagger developed).
    Then sending a convenient documentation to the client explaining the process of upload and possible integrations with the API.
    

Part 2

1. ##### Imagine that the Single View has 20 million musical works, do you think your solution would have a similar response time?
    
    The application would be slower, it queries the database on each work we want to insert/update/get by iswc, 
    the linear complexity of a mongo find is O(n) if we don't use an index, so it would scale lineary with the number of works.

2. ##### If not, what would you do to improve it?
    
    When inserting a new metadata I would conciliate all the works that contains before performing the conciliation to the live database, 
    shortening the actual set of works to insert.
    
    Then I would create a new repository, on clean architecture each layer is independent, so it would be an easy task,
    the current repository is lightweight and not optimised for large datasets.
    Tracking the _id of each work on the database would improve the number of find queries made and its complexity of queries.
    _id is an index with a find complexity of O(log n).
