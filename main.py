import base64
import codecs
import time
import re

start_time = time.time()

print('Deobfuscation Starting....')

try:
    with open('input.txt', 'r') as f:
        text = f.read()
except FileNotFoundError:
    print("Error: input file not found.")
    exit(1)

matches = re.findall("'(.*?)'", text)

try:
    with open('deobfuscated.txt', 'w') as f:
        for match in matches:
            f.write(match + '\n')
except Exception as e:
    print(f"Error: unable to write to file. {e}")
    exit(1)

try:
    b = matches[0]
    d = matches[2]
except IndexError:
    print("Error: input data is invalid.")
    exit(1)

try:
    rot = codecs.decode(b, 'rot13')
    rots = codecs.decode(d, 'rot13')
except Exception as e:
    print(f"Error: unable to decode input data. {e}")
    exit(1)

try:
    a = matches[1]
    c = matches[3]
except IndexError:
    print("Error: input data is invalid.")
    exit(1)

trust = a + rot + c + rots

try:
    s = base64.b64decode(trust)
except Exception as e:
    print(f"Error: unable to decode input data. {e}")
    exit(1)

end_time = time.time()
elapsed_time = end_time - start_time
print(f'Deobfuscated in : {elapsed_time:.2f} seconds\n')

try:
    output = s.decode("utf-8")
except Exception as e:
    print(f"Error: unable to decode input data. {e}")
    exit(1)

print('Script hidden in it was : \n')
print(output + '\n')

input('Press enter to save it in the file (Copy the text from here if there is any error)')

try:
    with open('deobfuscated.txt', 'w+') as f:
        f.write(output)
except Exception as e:
    print(f"Error: unable to write to file. {e}")
    exit(1)

text = "Deobfuscation Ended Saved in deobfuscated.txt"

for char in text:
    print(char, end='', flush=True)
    time.sleep(0.01)
