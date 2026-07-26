---
title: 'Don''t use strnstr'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/dont-use-strnstr.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:124ea3beb67f2b21'
translated: false
---

> 原文：[Don't use strnstr](https://www.mikeash.com/pyblog/dont-use-strnstr.html)　·　mikeash.com Friday Q&A

Posted at 2007-09-26 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [First Post](https://www.mikeash.com/pyblog/firstpost.html)  
Previous article: [Performance Comparisons of Common Operations](https://www.mikeash.com/pyblog/performance-comparisons-of-common-operations.html)  
Tags: [osbug](https://www.mikeash.com/pyblog/?tag=osbug) [security](https://www.mikeash.com/pyblog/?tag=security) [strnstr](https://www.mikeash.com/pyblog/?tag=strnstr)

Don't use strnstr

by [Mike Ash](https://www.mikeash.com/)

I've probably told most of the people who read this blog about this bug already, but just in case, I thought I'd make a post. I don't usually post when I find bugs in Apple's stuff, but this is a pretty fundamental string function so it's a bit more important.

The quick version is this: `strnstr` on 10.4 will sometimes read one byte beyond the end of the length which you specify. Under special circumstances, this will lead to a segmentation fault in correct code.

The following test program illustrates the bug:

```
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
    int size = 20480;
    char *str = malloc(size);
    memset(str, 'x', size);
    strnstr(str, "aa", size);
    return 0;
}
```

On my computer running 10.4.10 and everyone else running 10.4 who has tried it, this will crash on the `strnstr` line.

In order to trigger the crash, several conditions must be met. First, the buffer must be lacking a terminating NUL byte. (Note that this is allowed according to how `strnstr` is [documented to operate](http://developer.apple.com/documentation/Darwin/Reference/Manpages/man3/strnstr.3.html).) The search string must not exist in the buffer. The end of the buffer must terminate on a page boundary. And finally, the page following the buffer must be unreadable.

This confluence of circumstances is pretty difficult to produce. I've been using it without incident for a long time. I only discovered the problem when stress-testing some HTTP parsing code, and my stress test happened to cause reads which were nicely lined up with the page size, and it happened to generate enough data to push the malloced block past the malloc memory pool limit and into its own dedicated pages.

This rarity is all the more reason to avoid the function, though, since it just means that when it crashes, it'll likely to be on a user's machine, and it'll likely to be extremely difficult to reproduce.

For my friends out there in Apple land, this bug has been filed as [rdar://5504733](rdar://5504733).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/dont-use-strnstr.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
