# L'étranger: word cloud

## Introduction

The novel, **l’Étranger** (1942) by Albert Camus,  has two parts that represent distictive sentiments. Part 1, before the crime incident, the main character's narration was indifferent and mostly about the "normal" day. Part 2, after the murder, there "may" appear more emotional statement during the time in prison and the trial. 

This program creates "word clouds" to visualize the sentiment that lies in each part of the book. This "analysis" is meant to be quantitative and the interpretation may be subjective.

## Methods

The book in original language (French) was downloaded from this [website](http://www.bouquineux.com/index.php?telecharger=380&Camus-L_%C3%89tranger) and converted from pdf to text files.

Some of the **natural language processing** techniques were employed to create the word clouds. This includes:
- text mining and re-constructing paragraphs
- making lowercase text and removing non-alphabets/punctuations
- removing **"stop words"** (in french)
- tokenizing words from string

To build word clouds, an opensource package is used. See resource section at the end.

## Results and Interpretations

The total numbers of words used for generating two word clouds were almost equal. As shown in the below figures, the first thing that stood out from the two word clouds are their general patterns. In the first part, the frequencies of extracted words are quite balanced. On the contrary, in the second part, some words were definitely more used that the others. These outstanding words are adjectives/adverbes that might strengthen the feelings in the story; for example, "plus", "tout", "bien", etc.

There are both similarites and differences in outstanding words from the two word clouds. The common words that remained with some moderate frequencies in both parts (they were not stop words because they may provide sentiment or are part of conversations) are such as "très", "encore", "fait", "dit", "demandé", "comme", and "cela". However, the observable word differences between the two parts were the other characters' names and mundane things in part 1 that are fewer mentioned in part 2. These words in part 1 are "raymond", "marie", "maman", "chien", "femme" and "soleil". Meanwhile, the character "avocat" became more important in part 2. Other negation terms like "rien" and "jamais" also started to appear in part 2.

Overall, the story in part 2 might present more degree of emotions whereas the story in part 1 were rather indifferent.

![alt text](https://github.com/ornwipa/etranger_word_cloud/cloudOneWord_part1.png) ![alt text](https://github.com/ornwipa/word_cloud/cloudOneWord_part2.png)

## Resources

For resource about word cloud, see: 
- [original word cloud development](https://amueller.github.io/word_cloud)
- [example](https://www.tutorialspoint.com/create-word-cloud-using-python)
