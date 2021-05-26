def hammingEncode(code):

    #set varables
    factors = []

    #checks which bit needs to be changed
    bitChecker = 0
    valid = True
    errorString = 'Error: Input must be binary!'

    #check if code is valid
    for k in code:
        if k != '1' and k != '0':
            valid = False
    if valid == True:
        #get length of array with part bits
        for f in range(0, len(code)):
            if f < len(code):
                bitChecker = 2**f
                if bitChecker <= (len(code) + len(factors)):
                    #returns the factors array with the bit that needs to be checked
                    factors.append(bitChecker)

        #sets default value for bits to zero and which will be changed later if they dont match the
        encode = [0 for x in range(0, (len(code) + len(factors)))]


        inputNum = 0
        factindex = 0
        for i in range(1, (len(code) + len(factors))+1):
            if i == factors[factindex]:
                if factindex < (len(factors)-1):
                    factindex += 1
            else:
                encode[i-1] = int(code[inputNum])
                inputNum += 1

        #get values for each factor position
        for i in range(0, len(factors)):
            pos = factors[i]
            count = 0
            indexNum = pos-1
            while indexNum < len(encode):
                j = indexNum
                while j < pos+indexNum and j < len(encode):
                    if encode[j]==1:
                        count += 1
                    j+=1
                indexNum += 2*pos

            #if the sum of count %2 is 0, dont change, if its equal to one, change that bit to a 1
            if count%2==0:
                encode[pos-1] = 0
            else:
                encode[pos-1] = 1

        #return in string format
        ansString=""
        for letter in encode:
            ansString += str(letter)
        return ansString
    else:
        return errorString
