---
title: Using FileMerge with subversion
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/using-filemerge-with-subversion.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5c45bd5a8d60b689'
translated: false
---

> 原文：[Using FileMerge with subversion](https://www.mikeash.com/pyblog/using-filemerge-with-subversion.html)　·　mikeash.com Friday Q&A

Posted at 2005-07-06 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Fun With Beowulf Clusters](https://www.mikeash.com/pyblog/fun-with-beowulf-clusters.html)  
Previous article: [Dashboard Rant](https://www.mikeash.com/pyblog/dashboard-rant.html)  
Tags: [filemerge](https://www.mikeash.com/pyblog/?tag=filemerge) [python](https://www.mikeash.com/pyblog/?tag=python) [subversion](https://www.mikeash.com/pyblog/?tag=subversion) [versioncontrol](https://www.mikeash.com/pyblog/?tag=versioncontrol)

Using FileMerge with subversion

by [Mike Ash](https://www.mikeash.com/)

So finally today, I decided to solve things once and for all, and came up with 20 lines of python that fixes it up very nicely. And now I'll share it with the world!

Put the following code into a file called svnopendiffshim.py that's somewhere in your $PATH:

```
#!/usr/bin/python2

from sys import argv
from os import execlp
import re

left = "";
right = "";

argv.pop(0)

while argv:
    arg = argv.pop(0)
    if arg == "-u":
        pass
    elif arg == "-L":
        argv.pop(0)
    elif left == "":
        left = arg
    else:
        right = arg

execlp("opendiff", "opendiff", left, right)
```

Basically, this Python script just goes through the arguments that svn passes to its diff program, strips out everything that FileMerge doesn't understand, and passes the rest to opendiff, which is the command-line program which opens FileMerge.

Now, add one line to your .profile (if you're using a shell other than bash, you're on your own here):   
`alias svndiff='svn diff --diff-cmd svnopendiffshim.py'`

Now open a new Terminal window, go into a project, and type `svndiff somefile.h` and, bang, your diff opens in FileMerge.

So there you have it. I hope somebody finds this as useful as I do.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/using-filemerge-with-subversion.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
