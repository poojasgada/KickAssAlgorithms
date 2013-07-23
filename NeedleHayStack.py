'''
Created on Jul 18, 2013

@author: psgada
'''

'''
Finding Needle in HayStack using Boyer Moore
'''

def find_string(text, pattern):
    i = 0
    pattern_l = len(pattern)
    text_l = len(text)
    j = pattern_l - 1
    right = {}
    
    for l in range(0, len(pattern)):
        right[pattern[l]] = l  
    
    while i+j <= text_l-1:
        skip = 0
        while j >= 0:
            if pattern[j] != text[i+j]:
                try:
                    skip = j - right[text[i+j]]
                except:
                    skip = j + 1
                break
            j -= 1
            
        if j < 0:
            print "Found the Needle at %d " % (i)
            return
            
        j = pattern_l - 1
        i += skip
        
    print "Needle not found"
    
def get_input():
    find_string("HAANEEDLAAAYNEEDLEJFKJHAK", "NEEDLE")
    
get_input()