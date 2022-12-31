import base64, codecs
print('Deobfuscation Starting....')
# open the text file in read mode

magic = 'cHJpbn'
love = 'DbW3Il'
god = 'IHNleH'
destiny = 'xaXD=='


joy = 'rot13'






rot = codecs.decode(love, joy)
rots = codecs.decode(destiny, joy)

trust = magic + rot + god + rots
s = base64.b64decode(trust)


# decode the decoded text using the detected encoding
output = s.decode("utf-8")
print('Script hidden in it was : \n')

print(output + '\n')
# write the decoded text to a file

with open('deobfuscated.txt', 'w+') as f:
    f.write(output)

import time

text = "Deobfuscation Ended Saved in deobfuscated.txt"


for char in text:
    print(char, end='', flush=True)
    time.sleep(0.01)

print()
input('Press any key to close...')
