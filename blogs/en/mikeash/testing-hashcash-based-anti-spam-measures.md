---
title: Testing Hashcash-Based Anti-Spam Measures
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/testing-hashcash-based-anti-spam-measures.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5cece5692f7223c6'
translated: false
---

> 原文：[Testing Hashcash-Based Anti-Spam Measures](https://www.mikeash.com/pyblog/testing-hashcash-based-anti-spam-measures.html)　·　mikeash.com Friday Q&A

Posted at 2011-11-26 18:42 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-12-02: Object File Inspection Tools](https://www.mikeash.com/pyblog/friday-qa-2011-12-02-object-file-inspection-tools.html)  
Previous article: [No Article For you!](https://www.mikeash.com/pyblog/no-article-for-you.html)  
Tags: [meta](https://www.mikeash.com/pyblog/?tag=meta)

Testing Hashcash-Based Anti-Spam Measures

by [Mike Ash](https://www.mikeash.com/)

In short, hashcash is a scheme that uses a problem that's difficult (but not too difficult!) to solve but easy to verify to prove computation. In this particular case, the problem is producing data whose SHA-1 hash contains a certain number of leading zeroes.

When you click in any of the comment fields, the JavaScript fetches a unique salt from my server. It then begins a brute-force computation, searching for data which, when appended to that salt, produces the requisite number of leading zeroes in the SHA-1 hash. Once it finds one, it saves that value and enables the "Post Comment" button. The required number of leading zeroes is configured to take, on average, a reasonable amount of time to compute. This time is large enough to deter spammers trying to post stuff immediately, but small enough not to get in the way of legitimate users. It's currently configured to use 18 leading zeroes, which gives a roughly 10 second computation itme on a modern Mac.

On the server, the story is much simpler. All it has to do is keep track of the hashes that it gives out, and verify the hashcash that comes back in. Verification is simply a matter of checking that the salt is one it previously gave out, and checking that the salt + hashcash does indeed produce an SHA-1 hash with the required number of leading zeroes. While it takes several seconds of computation to produce the hashcash, it is essentially instantaneous to verify, producing no real server load.

Note that this scheme also works fine on iOS devices, but takes somewhat more time to compute the hashcash. It should still take much less time than it takes to compose a good comment, though!

For those of you worried about battery life, the hashcash computation only kicks off when you actually focus one of the comment form fields, so simply reading a blog post doesn't add any additional load.

Please feel free to play with the new system in the comments to this post. I hope that it will deter spammers while not impacting legitimate commenters. Also, it was fun to write.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/testing-hashcash-based-anti-spam-measures.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
