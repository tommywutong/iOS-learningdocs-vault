---
title: Bug Reversal
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/bug-reversal.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1c1a11add15d734c'
translated: false
---

> 原文：[Bug Reversal](https://www.mikeash.com/pyblog/bug-reversal.html)　·　mikeash.com Friday Q&A

Posted at 2006-02-06 00:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Braaaaaaaains](https://www.mikeash.com/pyblog/braaaaaaaains.html)  
Previous article: [Bolo Ecology](https://www.mikeash.com/pyblog/bolo-ecology.html)  
Tags: [bug](https://www.mikeash.com/pyblog/?tag=bug) [unicode](https://www.mikeash.com/pyblog/?tag=unicode)

Bug Reversal

by [Mike Ash](https://www.mikeash.com/)

> [NSString stringWithFormat:@"qlex.1.%C%C.n.he.0", 0x05D1, 0x05D0]

And yet, he said, when he printed this, 0x05D0 was coming out before 0x05D1.  
  
 (For those of you not intimately familiar with this end of Cocoa, %C is a format specifier that prints a single unichar, much like %c prints a single char.)  
  
 Now, this problem makes no sense. A format string can't just arbitrarily decide to print things in the wrong order. We asked the usual questions ("Is that your actual code?" "Are there variables involved?" "What does %C do, anyway?") but nothing was apparent. Despite the apparent impossibility of things just coming out in the wrong order, he was insistent that this was in fact happening.  
  
 Finally, I tossed the suspect line into a quick test program and ran it. And, lo and behold, it really was coming out backwards! Fortunately, it was instantly apparent as to why.  
  
 If any of you are unicode experts, or happened to toss the line into a test program yourself, you probably know too. The characters in question are both Hebrew characters. Hebrew, as you might know, is written from right to left. OS X's text system is smart enough that, when it encounters multiple Hebrew characters next to each other, it will print them out right to left. The last character in the sequence appears "first" to eyes used to reading English.  
  
 So it turns out that every subsystem was working correctly. NSString was correctly constructing itself, and the text system was correctly displaying it. In fact, this wasn't even a bug at all, just a misinterpretation of what the correct result should be.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

No comments have been posted.

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
