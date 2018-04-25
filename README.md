# spellchecky
Simple spell checker using Levenshtein Distance and BK Trees.

Using this <a href="https://github.com/dwyl/english-words">awesome dictionary</a>, that's already in JSON, we add it to a <a href="https://github.com/dekken201/pybktree">BK Tree</a> for very fast spell checking with Levenshtein Distance.
Since the addition into the tree is pretty slow(at least in my computer), I <a href="https://docs.python.org/3/library/pickle.html">pickled</a> the data structure for easier reutilization, so it doesn't have to load the whole tree everytime it runs. The dictionary has almost 500.000 words and the spell check is done in less than a second.

# HOW TO:
So, for it to work, you basically have to clone the repository and have 
<a href="https://github.com/ztane/python-Levenshtein">python-Levenshtein</a> installed(most obviously you'll already have "json", "os", "pickle" and "collections" as standard).

This is kind of a tricky(at least was for me) library to install because it's implemented with C, and with Windows 10 and Python 3.6, it was a pain to make it work. It makes the distance calculations much faster than the pure python version, which is this <a href="https://pypi.org/project/Distance/">one</a>(which you can use with a couple tweaks, I'll explain later). In my machine, I had to actually install the whole Visual Studio package for it to work, because it requires a version of Visual C++ package that only comes with it(if anyone knows how to get that without installing Visual Studio, please tell me!).

If you can't or don't want to install python-Levenshtein, going for a "pure python" way, you can use it, changing the import in "functions.py" from "Levenshtein" into "distance"(provided you have this library already installed), and changing the distance_function from "Levenshtein.distance" into "distance.levenshtein".

I believe the "run" file is pretty self explanatory, the commented out part is the loading part, which you'd do if you wanted to load the dictionary in JSON to be used. It basically runs "load_words", which duhh, load the words form the dictionary, instantiate the tree with the parameters(the list/dict to be used, and then creates a pickle file with the whole data structure with the name ("english_dict_pickle.txt").

The "run()" function basically loads the pickled data structure for querying. I still have to work out how the whole spellchecking will occur, but the three basically returns the closests words from the input using Levenshtein distance, by how much you want. Even bigger words with bigger acceptable distances are returned practically instantly.

For more on how the tree works, please check <a href="https://github.com/Jetsetter/pybktree">this</a> since the general commands and ideas are the same, I only changed a bit of the structure and it can accept dictionaries.




