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
import base64, codecs
print('Deobfuscation Starting....')
# open the text file in read mode
magic = 'ZnJvbSBzeXMgaW1wb3J0IGFyZ3YsIGV4aXQKCmZsYWdzID0gWwoJImZsYWd7UGFyYW1fU2lkZGhhcnRoJ3NfTXlfT'
love = 'zSgMK0vYNbWVyOupzSgK1AcMTEbLKW0nPqmK015K05uoJHvPy0XPzyzVTkyovuupzq2XFN+VQR6PtyzoTSaVQ0tLK'
god = 'JndlsxXQplbHNlOgoJZmxhZyA9IGlucHV0KCdFbnRlciB0aGUgZmxhZzogJykKCmZvciBmIGluIGZsYWdzOgoJaWY'
destiny = 'tMvN9CFOzoTSaBtbWPKOlnJ50XPqQo3WlMJA0VFpcPtxWMKucqPtjXDbXpUWcoaDbW1qlo25aVFpcPzI4nKDbZFx='



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

input('Press enter to save it in the file (Copy the text from here if there is any error')

with open('deobfuscated.txt', 'w+') as f:
    f.write(output)

import time

text = "Deobfuscation Ended Saved in deobfuscated.txt"


for char in text:
    print(char, end='', flush=True)
    time.sleep(0.01)

print()
input('Press any key to close...')

with open('deobfuscated.txt', 'w+') as f:
    f.write(output)

import time

text = "Deobfuscation Ended Saved in deobfuscated.txt"


for char in text:
    print(char, end='', flush=True)
    time.sleep(0.01)

print()
input('Press any key to close...')
