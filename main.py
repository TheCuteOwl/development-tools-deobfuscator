import base64, codecs
import time
# Dont touch
joy = 'rot13'

print('Deobfuscation Starting....')

# It will open obfuscated.txt and check everyline so magic love god and destiny
with open('obfuscated.txt', 'r') as file:
    first_line = file.readline()
    second = file.readline()
    third = file.readline()
    fourth = file.readline()

    a = first_line[9:-2]
    b = second[8:-2]
    c = third[7:-2]
    d = fourth[11:-1]

# Will decode with rot13
rot = codecs.decode(b, joy)
rots = codecs.decode(d, joy)

# Will make everything in 1 variable
trust = a + rot + c + rots

# Will decode in base64
s = base64.b64decode(trust)

# decode the decoded text using the detected encoding
output = s.decode("utf-8")
print('Script hidden in it was : \n')

print(output + '\n')
# write the decoded text to a file

input('Press enter to save it in the file (Copy the text from here if there is any error)')
with open('deobfuscated.txt', 'w+') as f:
    f.write(output)

text = "Deobfuscation Ended Saved in deobfuscated.txt"


for char in text:
    print(char, end='', flush=True)
    time.sleep(0.01)

print()
input('Press any key to close...')
