#E White, Langara College Lab Assistant (Jan 2017)
#simply cleans up poorly submitted student submissions

import os

print (os.getcwd())
[os.rename(f, f.replace(' ', '_')) for f in os.listdir('.') if not f.startswith('.')]
