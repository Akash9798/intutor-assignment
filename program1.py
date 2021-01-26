#password condition
# it has to contain only alphanumeric characters (a−z, A−Z, 0−9);
# there should be an even number of letters;
# there should be an odd number of digits.


def count_letter(s):
    """"Count number of alphabets in string s"""
    count=0
    for i in s:
        if i.isalpha():
            count+=1
    return count

def count_digit(s):
    """"Count number of digtis in string s"""
    count=0
    for i in s:
        if i.isnumeric():
            count+=1
    return count


def valid_pass(s):
    """"check if string s is alpha numeric"""
    for i in s:
        if i.isalnum():
            continue
        else:
            return False
    return True



def password(s):
    """"return len of highest possible length password possibe"""
    pass_list = s.split()
    
    max_len = -1
    
    for i in pass_list:
        
        if valid_pass(i):
            
            if count_digit(i)%2 !=0 and count_letter(i)%2==0:
                
                max_len = max(len(i),max_len)
                
        
    return max_len
                
            

#testing sample input
S = "test 5 a0A pass007 ?xy1"
print(password(S)) 
#out - 7

S = "test 5 aK1D0Aa9d pass007 ?xy1"
print(password(S))
#out - 9






