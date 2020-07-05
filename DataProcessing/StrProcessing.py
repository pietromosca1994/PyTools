from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import spacy
import de_core_news_sm

def ReplaceStr(x, replace_dict):
    # replace strings
    x_str=str(x)
    for key in replace_dict.keys():
        x_str=x_str.replace(key, replace_dict[key])
    
    return x_str
        
def Html2Plain(x):
    # convert html in plain text
    x_str=str(x)
    soup=BeautifulSoup(x_str, features='lxml')
    x_str=soup.get_text()
    
    return x_str


def StemSentence(sentence, stemmer):
    '''
    sentece
    stemmer

    Function to Stem a sentence with nltk package
    An example of compatible stemmer is SnowballStemmer(language='german', ignore_stopwords=True)
    '''
    token_words=word_tokenize(sentence)
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(stemmer.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)


def LemmatizeSentence(sentence, language_core): 
     '''
    sentence
    language

    Fcuntion to substitute the lemma of the words in a sentence with spacy package
    An example of compatible language core is 'de_core_news_sm'
    '''   
    nlp=spacy.load(language_core)
    doc = nlp(sentence)
    lemma_sentence=[]
    for word in doc:
       lemma_sentence.append(word.lemma_)
       lemma_sentence.append(" ")

    return "".join(lemma_sentence)      

