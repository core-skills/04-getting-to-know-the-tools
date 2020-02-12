[Overview](./00_overview.md) |
[Intro](./01_intro.md) |
[Munging](./02_munging.md) |
[Grouping & Reshaping](./03_groupingreshaping.md) |
[Explaining Data](./04_explainingdata.md) |
[How Might We...](./05_howmightwe.md)  |
[Closeout](./06_closeout.md)

# Day 4 Introduction

The morning will be spent practising some collaborative development.
We'll first spend some time going over Git, GitHub and GitKraken before doing a
small series of exercises in pairs.
By the end of the morning, you should have had a bit of practise with the develop
& synchronize workflow for shared programming, and be able to effectively code in
pairs (pair programming model) and share the results.

There should also be plenty of time to look at other things as needed.

## Code Kata

Code Kata are short exercises or drills designed to develop your skills.
The phrase 'kata' is taken from the martial arts concept,
and has been in use from at least 1999<sup><a id="a1">[#](#f1)</a></sup>.

These exercises often have many potential solutions, and can be repeated
multiple times to get a feel for what small improvements you may be able
to make.

Using code kata to supplement your development is one way to get around the
"it's hard to learn on the job" aspect of learning and developing your
projects. Getting feedback on your solutions is useful, which is why we'll
be spending time coding in pairs this morning. But the key thing is that
the exercises are not intended to be an 'under pressure' scenario - they're
for, and only for, development purposes.
Take them slow at least the first time around, break down the problem,
and think about why you make prefer one approach over another.

<b id="f1">"Code Kata"</b>: Andrew Hunt & Dave Thomas (1999).
The Pragmatic Programmer. Addison Wesley. ISBN 020161622X. [↩](#a1)

## Collaborative Development and Data Sharing Workflows

Today we'll be using git to stage and share our progress was we go through each
of the exercises. Before we get started let's map out where the tools and services fit
in this workflow (git, GitHub, GitKraken; remote, local, repository, provider etc).

If you don't already have one set up, a GitHub account would be useful for todays
exercises and going forward. GitHub currently allows you to have unlimited private
repositories and three collaborators per private repository at the free tier - a
handy feature.

We'll go through what a collaborative workflow might look like together before we
start, and then use parts of this during the day.

### Processes for (Collaborative) Development

There are multiple options for processes to follow during collaborative development.
Some are more productive than others when you have multiple people contributing.

It's handy to keep things which you're actively developing/testing (things which
occasionally break) separate from 'stable' versions especially when there are other
people using it. For this we commonly use separate 'master' and 'develop'
branches. In addition to this, if it suits your workflow and you have a few people
working on the project you could add branches for new features or to work on
bugfixes.

Gitflow is a workflow commonly used to manage how these branches interact,
(i.e. I have a bunch of branches, which one goes into where?)
designed around generating 'releases' or incremental stable versions. Check out
the
[overview from Atlassian](
https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
)
and
[how it's implemented in GitKraken](
https://support.gitkraken.com/git-workflows-and-extensions/git-flow/
)
if you want to know more.

If everyone's concurrently committing to the same branch from separate local
repositories and you're working on the same files, you'll find that merge conflicts
are likely to be a hurdle. The simple solution includes working on different
files at any specific time - or working at different times on the same files.
Beyond this, know who's working on which feature/bug/problem and make your changes
(read: commits) specific and targeted to that.

### An Exercise or Three

Start by cloning today's repository.

Next we can work with a [demo repo](https://github.com/core-skills/git-workflow-runthrough) to play with some of these tools:
1. Fork the Existing Repository
1. Make some changes on your fork within the `develop` branch (e.g. add an empty file).
1. Stage and commit the changes.
1. Pull request
  * You might see a green 'Compare and pull request button'
  * Make sure your branches line up.
1. Wait for review.

We'll quickly go through setting up git flow using GitKraken.

Finally we'll go through **adding collaborators to a private repository**.

## The Scientific Python Ecosystem

We'll be using a few different libraries throughout today, and starting to
dive into some of the documentation. We've listed links to some of the most commonly
used packages within the scientific python ecosystem below, annotated by
a quick description of the functionality of each package.

| Package                                                      | Description                                                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| [numpy](https://docs.scipy.org/doc/numpy)                    | Numeric Python. Working with numbers, lists of numbers, linear algebra & more.              |
| [matplotlib](https://matplotlib.org/)                        | "2D plotting library which produces publication quality figures in a variety of formats."   |
| [pandas](https://pandas.pydata.org/)                         | "A fast, powerful, flexible and easy to use (tabular) data analysis and manipulation tool"  |
| [sklearn](https://scikit-learn.org/stable/)                  | "Machine Learning in Python- Simple and effective tools for predictive data analysis"       |
| [scipy](https://docs.scipy.org/doc/scipy/reference/)         | Optimisation, interpolation, signal processing & stats.                                     |
| [statsmodels](https://www.statsmodels.org/stable/index.html) | "for the estimation of statistical models, statistical tests, statistical data exploration" |
| [seaborn](https://seaborn.pydata.org/)                       | "High-level interface for drawing attractive and informative statistical graphics."         |

Check out the documentation sources, but also remember there are other useful
sources of information, particularly when you run into bugs:
* StackOverflow
* Blogs, examples, tutorials
* Docstrings!

## Before we Get Started: Recap

### Where am I?

| :question: How do I find where my python code is running? |
| ---------------------------------------------- |

| :question: How do I specify a path to my data directory? |
| -------------------------------------------------------- |

###  Functions, Objects and Methods

Short recap of Python objects – data + code that operates on that data vs functions (code that takes some input)


## Wrapping Up

Pair up for the morning! We'll swap a few times during the day.

[Overview](./00_overview.md) |
[Intro](./01_intro.md) |
[Munging](./02_munging.md) |
[Grouping & Reshaping](./03_groupingreshaping.md) |
[Explaining Data](./04_explainingdata.md) |
[How Might We...](./05_howmightwe.md)  |
[Closeout](./06_closeout.md)
