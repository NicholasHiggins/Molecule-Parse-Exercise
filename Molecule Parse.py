"""A simple exercise that takes a given Chemical formula (CH2)4OH and returns a
dictionary with the constituent elements as keys and amount as value {'C':4,'H':9,
O:1}. This simple program will not detect specious elements, that is it will treat
Aa or G as chemical elements. For the purpose of exercise such refinement is unnecessary."""



import re

"""sub_parse will take an expanded string in form AABBC and create dictionary K
to include element : count {'element':count}"""

def sub_parse(string):
    K={}
    S=re.findall(r'([A-Z][a-z]*)',string)
    for item in S:
            if item in K.keys():
                K[item]+=1
            else:
                K[item]=1
    return K
    
def parse(string):

    expanded=''
    try:
        to_replace=re.findall(r'([\(\[\{](?:(?:[A-Z][a-z]*\d*)+){1}[\)\}\]]\d*)',string)[0]
                                        #returns the most nested expression in chemical formula.
                                        #ie AaB{C[DdE]4} would yeild '[DdE]4'. This is important
                                        #because it gives the substring that eventually will be expanded and replaced.
    except:
        #when formula contains no nested expression
        to_expand=re.findall(r'([A-Z][a-z]*)(\d*)',string) #yields a tuple with the expression in 0-index and the multiplier in 1-index.
        for item in to_expand:
            try:
                expanded+=item[0]*int(item[1]) #this deals with when element has multiplier
            except:
                expanded+=item[0] #this is when there is no multiplier for element when int(item[1]) fails'
        return sub_parse(expanded)

    s=re.findall(r'[\(\[\{]((?:[A-Z][a-z]*\d*)+){1}[\)\}\]](\d*)',to_replace)[0]
    #returns a tuple with most nested expression stripped of braces [0] and mulitplier [1], ('DdE',4)
    if s[1]!='':
        t=s[0]*int(s[1])
    else:
        t=s[0]
    to_expand=re.findall(r'([A-Z][a-z]*)(\d*)',t)
    for item in to_expand:
        try:#this deals with when element has multiplier
            expanded+=item[0]*int(item[1])
        except:#this is when there is no multiplier for element
            expanded+=item[0]      
    string=string.replace(to_replace,expanded)
    return parse(string)

if __name__=='__main__':
    while True:
        formula=input("Enter formula to parse:\n('quit' to exit)\n\t\t\t")
        if formula=='quit':
            break
        K=parse(formula)
        print(K)
    
