
def compare_codes(guess, secret):
    result  = ()
    correct = 0
    correct_ish = 0
    secret_no_repeat = ''
    
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            correct += 1
        
        if guess[i] in secret and guess[i] != secret[i] and guess[i] not in secret_no_repeat:
            secret_no_repeat += guess[i]
            correct_ish += 1
        
    result = (correct, correct_ish)
    return result

if __name__ == '__main__':
    print(compare_codes('1233', '1234'))