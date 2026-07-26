---
title: A Tool for Editing Version-Controlled Bundles
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/a-tool-for-editing-version-controlled-bundles.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7da2c50865095b65'
translated: false
---

> 原文：[A Tool for Editing Version-Controlled Bundles](https://www.mikeash.com/pyblog/a-tool-for-editing-version-controlled-bundles.html)　·　mikeash.com Friday Q&A

Posted at 2008-02-09 21:31 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Goodbye, Nibs](https://www.mikeash.com/pyblog/goodbye-nibs.html)  
Previous article: [Performance Comparisons of Common Operations, Leopard Edition](https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations-leopard-edition.html)  
Tags: [python](https://www.mikeash.com/pyblog/?tag=python) [subversion](https://www.mikeash.com/pyblog/?tag=subversion) [utility](https://www.mikeash.com/pyblog/?tag=utility) [versioncontrol](https://www.mikeash.com/pyblog/?tag=versioncontrol)

A Tool for Editing Version-Controlled Bundles

by [Mike Ash](https://www.mikeash.com/)

Download the script [here](https://www.mikeash.com/pyblog/bundleedit.txt). Rename it to bundleedit.py and put it somewhere in your `$PATH`.

The script assumes you use subversion, but can be changed to something else by editing the `versionControlDir` variable. If you're a CVS user, change it to `'CVS'`. If you use something else, hopefully you'll know what to change it to.

Usage is easy. Feed it the path of one or more bundle-style documents which are under version control. It will open them one by one in the default editor for that file type. Make your changes and then quit the editor, and you're done. If you specified more than one file it will re-open the editor for the next one, repeating until you've edited them all.

The concept of the script is very simple. It simply moves the `.svn` directory to a temporary location, then opens the bundle. When you're done editing, it moves the `.svn` directory back to its original location. End result: you get a modified document that's still under version control.

It takes advantage of two useful flags to the `/usr/bin/open` command. The `-W` flag makes it wait until the editor quits before continuing so that it knows when to replace the version control directory. The `-n` flag makes it always open a new instance of the editor even if it's already running. This ensures that you can quit it without disturbing any documents you already had open.

This script is intended to work with `rtfd` files because that's the only bundle type I use which isn't version control friendly, but it should work with any other unfriendly bundle type you might have as long as `open` works with it.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/a-tool-for-editing-version-controlled-bundles.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
