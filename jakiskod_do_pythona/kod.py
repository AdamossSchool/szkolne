def decode(data):
    alphabet="abcdefghijklmnoprstuvwxyz"

    output=""
    for i in range(len(data)):
        idx=alphabet.index(data[i])

        for j in range(3):
            if alphabet[idx] != 'a':
                idx -=1
            else:
                idx=len(alphabet)-1
            output +=alphabet[idx]
            i += 1

    return output

input_text = "adamoss"
print('input: '+ input_text)
result = decode(input_text)
print('output: '+ result)

