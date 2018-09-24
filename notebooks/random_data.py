""" file: random_data.py
    author: Jess Robertson, CSIRO Mineral Resources
    
    description: Makes random dataframes for examples
"""

import random
import pandas

def random_row(categories=None):
    """ 
    Make a random row
    
    Returns rows like (category, a, b):
    - category is a categorical variable, 
    - a is a randomly selected cluster value (with two clusters)
    - b is a uniform integer on 0, 1
    
    Returns:
        (category, a, b) - the random row
    """
    # Category 
    categories = categories or 'xyz'
    category = random.choice(categories)
    
    # Make a from clusters
    a_mean = random.choice([25, 75])
    a_stddev = 20
    a = random.normalvariate(a_mean, a_stddev)
    
    # b is just random uniform
    b = random.uniform(0, 1)
    
    # Do other values
    return (category, a, b)

def random_dataframe(nrows=10, categories=None):
    "Make a random dataframe"
    return pandas.DataFrame(
        [random_row(categories=categories) for _ in range(nrows)], 
        columns=('category', 'a', 'b')
    )