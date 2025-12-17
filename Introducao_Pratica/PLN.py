import spacy
txt = 'List is a ubiquitous data structre in the Pyhton programming language'
nlp = spacy.load('en_core_web_sm')
doc = nlp(txt)
stk = []
for w in doc:
    head_lefts= [1 if t in t.head.lefts else 0 for t in doc[w.i:]]
    i0=0
    try: i0 = head_lefts.index(0)
    except ValueError: pass
    i1=0
    if i0>0:
        noun = [1 if t.pos_ == 'NOUN' or t.pos_ == 'PROPN' else 0 for t in reversed(doc[w.i:w.i+i0 +1])]
        try: i1 = noun.index(1)+1
        except ValueError : pass
    elif w.pos_ =='NOUN' or w.pos_ == 'PROPN':
        stk.append(w.text)
    elif (i1>0):
        stk.append(w.text)
    elif stk:
        chuck=  ' '
        while stk:
            chuck = stk.pop()+' '+chuck
        print(chuck.strip())