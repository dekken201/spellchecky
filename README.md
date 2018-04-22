# spellchecky
Simple spell checker using Levenshtein Distance and BK Trees.

Using this <a href="https://github.com/dwyl/english-words">awesome dictionary</a>, that's already in JSON, we add it to a <a href="https://github.com/dekken201/pybktree">BK Tree</a> for very fast spell checking with Levenshtein Distance.
Since the addition into the tree is pretty slow(at least in my computer), I <a href="https://docs.python.org/3/library/pickle.html">pickled</a> the data structure for easier reutilization, so it doesn't have to load the whole tree everytime it runs. The dictionary has almost 500.000 words and the spell check is done in less than a second.
