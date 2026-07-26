---
title: Introducing MAZeroingWeakRef
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/introducing-mazeroingweakref.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3c8e0157fd738d5f'
translated: false
---

> 原文：[Introducing MAZeroingWeakRef](https://www.mikeash.com/pyblog/introducing-mazeroingweakref.html)　·　mikeash.com Friday Q&A

Posted at 2010-07-16 20:19 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-07-30: Zeroing Weak References to CoreFoundation Objects](https://www.mikeash.com/pyblog/friday-qa-2010-07-30-zeroing-weak-references-to-corefoundation-objects.html)  
Previous article: [Friday Q&A 2010-07-16: Zeroing Weak References in Objective-C](https://www.mikeash.com/pyblog/friday-qa-2010-07-16-zeroing-weak-references-in-objective-c.html)  
Tags: [code](https://www.mikeash.com/pyblog/?tag=code) [hack](https://www.mikeash.com/pyblog/?tag=hack) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [sourcecode](https://www.mikeash.com/pyblog/?tag=sourcecode)

Introducing MAZeroingWeakRef

by [Mike Ash](https://www.mikeash.com/)

A zeroing weak reference is a reference to an object which does not prevent that object from being destroyed (in other words, it's not retained), and which automatically becomes `nil` once the object is destroyed. To use `MAZeroingWeakRef`, you simply create one using `-initWithTarget:`:

```
    MAZeroingWeakRef *ref = [[MAZeroingWeakRef alloc] initWithTarget: object];
```

You can access the object at any time using the

method:

```
    NSLog(@"Target is %@", [ref target]);
```

As long as the object continues to exist,

will return it. Once it is destroyed,

will return

.

returns a reference that has been retained and autoreleased, ensuring that the returned object will remain valid as you use it even if the last strong reference to it has been released in another thread while you work.

You can get `MAZeroingWeakRef` from my public subversion repository:

```
    svn co http://mikeash.com/svn/ZeroingWeakRef
```

It's released under a BSD license, so you can use it in your commercial applications with acknowledgement.

`MAZeroingWeakRef` should compile and run on any OS with the "modern" runtime APIs, which is basically 10.5 and up, and any iOS version. Blocks support is needed to enable the cleanup block functionality (which allows running arbitrary code when the reference is destroyed) but everything else will work without it.

If you use `MAZeroingWeakRef` on iOS, you may want to set `COREFOUNDATION_HACK_LEVEL` to `0` in `MAZeroingWeakRef.m`. This prevents `MAZeroingWeakRef` from being able to target CoreFoundation bridged objects, but also avoids the use of private API, which Apple can sometimes be unfriendly about. This is not a big disadvantage, as it's extremely rare to have weak references to CF objects.

I hope that this library will prove useful!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
