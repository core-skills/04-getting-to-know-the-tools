[Overview](./00_overview.md) |
[Intro](./01_intro.md) |
[Munging](./02_munging.md) |
[Grouping & Reshaping](./03_groupingreshaping.md) |
[Explaining Data](./04_explainingdata.md) |
[How Might We...](./05_howmightwe.md)  |
[Closeout](./06_closeout.md)

# Munging Tabular Data

The first session this morning will overlap somewhat with the last sessions of last
week. We'll be working on importing some data, cleaning it up and the first
parts of data exploration. We'll be working with the notebook titled
['am1-munging-tabular-data'](../notebooks/am1-munging-tabular-data.ipynb).

## Step 1: Read my Data

| 30 mins (together) |
| ------------------ |

This first exercise will involve reading in some data from a `.csv` (or whichever
data file you have on hand).

| :question: How do you read a `.csv` into a `pandas.DataFrame`? |
| -------------------------------------------------------------- |
| See if you can find the relevant pandas documentation page.    |

Have a look at data.gov.au, find a non-CSV file you want to load in,
and find the documentation for how you might go about it (e.g.
shapefiles, spreadsheets, `.tsv`?).

| :triangular_flag_on_post: Is everyone up to speed? How are people going? |
| ------------------------------------------------------------------------ |

Synchronise code and swap over.

## Step 2: Read my Data

| 30 mins |
| ------- |

### Data Types

| :question: What are the data types in your DataFrame? What do they mean? |
| ------------------------------------------------------------------------ |
| See if you can find the relevant pandas documentation page.              |

| :question: What should the data types be?            |
| ---------------------------------------------------- |
| See if you can convert the ones with the wrong type? |

| :question: How would you check for incorrect, or invalid values? |
| ---------------------------------------------------------------- |

| :triangular_flag_on_post: Is everyone up to speed? How are people going? |
| ------------------------------------------------------------------------ |

Synchronise code and swap over.

## Tidy Data

| 10 mins |
| ------- |

* Definition

### Checklist

1. Each variable you measure should be in one column.
1. Each different observation of that variable should be in a different row.
1. There should be one table for each "kind" of variable.
1. If you have multiple tables in a given dataset, they should include a column in the table that allows them to be linked<sup><a id="a1">[‡](#f1)</a></sup>.


<b id="f1">‡</b>: If you can't link them, then perhaps they should be considered different datasets? [↩](#a1)

## Work Through Tidying Your Own Data

| 20 mins |
| ------- |

Use the tidy data checklist and check through your own datasets.

| :question: How will you represent missing data?                       |
| --------------------------------------------------------------------- |
| How would you document this notation?                                 |
| Is missing different to 'invalid', 'not measured', 'below detection'? |

| :question: How could you encode categorical data in your dataset? |
| ----------------------------------------------------------------- |

| :triangular_flag_on_post: Is everyone up to speed? How are people going? |
| ------------------------------------------------------------------------ |

Synchronise code and swap over.

## *Optional*: Extract These Steps out to a Separate Function

If you get to this point before the allocated time, or wish to
spend a few productive minutes over the break, copy your
data cleaning and tidying workflow you've put together above into a
separate function (*or two*) which you'll look to further develop
and make use of in the coming weeks.

| :question: How many functions should you split this into? |
| --------------------------------------------------------- |
| How many separate things are happening?                   |
| Do these things ever happen independently?                |

| :question: Where's the best place to put this? |
| ---------------------------------------------- |

[Overview](./00_overview.md) |
[Intro](./01_intro.md) |
[Munging](./02_munging.md) |
[Grouping & Reshaping](./03_groupingreshaping.md) |
[Explaining Data](./04_explainingdata.md) |
[How Might We...](./05_howmightwe.md)  |
[Closeout](./06_closeout.md)
