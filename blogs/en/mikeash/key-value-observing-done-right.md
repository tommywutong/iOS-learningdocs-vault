---
title: Key-Value Observing Done Right
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/key-value-observing-done-right.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c7d5ca4dd7ae0b8e'
translated: false
---

> 原文：[Key-Value Observing Done Right](https://www.mikeash.com/pyblog/key-value-observing-done-right.html)　·　mikeash.com Friday Q&A

Posted at 2008-10-22 21:47 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Don't Use NSOperationQueue](https://www.mikeash.com/pyblog/dont-use-nsoperationqueue.html)  
Previous article: [The How and Why of Cocoa Initializers](https://www.mikeash.com/pyblog/the-how-and-why-of-cocoa-initializers.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [kvo](https://www.mikeash.com/pyblog/?tag=kvo) [sourcecode](https://www.mikeash.com/pyblog/?tag=sourcecode)

Key-Value Observing Done Right

by [Mike Ash](https://www.mikeash.com/)

**What's Broken**  
 There are three major problems with the KVO API, all of which relate to multiple levels of the class hierarchy registering observers. This is important because even NSObject (as part of its implementation of `-bind:toObject:withKeyPath:options:`) will observe things.

1. **`-addObserver:forKeyPath:options:context:` doesn't allow passing a custom selector to be invoked.**  
   If you look at similar APIs such as NSNotificationCenter, you'll see that registering an observer always involves passing a selector to be invoked when the specified event happens. This makes it very easy to separate things from a superclass, because you just direct the message to your own method. With KVO you have to override `-observeValueForKeyPath:ofObject:change:context:`, then either handle the message yourself or call super. Deciding whether to handle the message or pass it up the chain is complicated by the fact that super may have registered for the exact same key path and object.
2. **The context pointer is useless**  
   This is a consequence of #1. Because you can't specify a custom method to invoke, and you can't tell if your superclass will be interested in the notification by examining the key path or the object, you need some other way to tell if the notification is meant for you or for your superclass. The context pointer is how you do this. You must create a unique pointer that your superclass can't possibly be using, and then pass this to `addObserver:...`. You must then check to see if the context pointer is this unique pointer in your implementation of `-observeValueForKeyPath:...`. A consequence of this fact is that you can't use the context pointer to actually hold context.
3. **`-removeObserver:forKeyPath:` doesn't take enough parameters**  
   This method doesn't take a context pointer. This means that if you register for the same object/key path combination as your superclass, but with a different lifetime, you have no way of disabling only your observer. Calling this method may disable yours, it may disable the superclass's, or it could even disable both.

It's too bad that such a powerful tool is so broken. Especially since Apple is starting a trend of omitting traditional NSNotification and delegate callbacks in new APIs, instead simply supporting KVO. A perfect example of this is NSOperation: the only way to get notified when an NSOperation finishes is by using KVO to watch its `isFinished` property.

So what can we do about it? I don't want to complain without helping, so I've written a class to solve the problem. You can get it out of my [public svn repository](http://www.mikeash.com/svn/) like so:

`svn co http://www.mikeash.com/svn/MAKVONotificationCenter/`

And you can browse it by just clicking the link above.

So how does it work? It takes advantage of one pointer that can be guaranteed to be unique: the 'self' pointer. Instead of registering the target object for a notification, it creates a unique helper object for each notification and registers that. The helper then receives the notification and bounces it back to the original observer. Since the helper is a unique object for each observation, it can hold metadata about the observation as simple instance variables and not need to rely on the context pointer, which can be the required unique pointer. Since the helper does nothing but listen for KVO notifications, the observation persists for the lifetime of the object and we can assume that its superclass, NSObject, either does not observe anything or will observe for the lifetime of the object as well.

MAKVONotificationCenter then bypasses all three deficiencies described above:

1. A custom selector is provided in the `-addObserver:...` method which is invoked when the observed key path changes. The superclass will use a different selector, so the problem is solved. (And in the case of Cocoa superclasses, they'll be observing directly whereas MAKVONotificationCenter observes through a helper, ensuring that they won't interfere.)
2. A `userInfo` parameter is provided which is passed into the observer method. This can be an arbitrary object containing any necessary information about the observation.
3. The `-removeObserver:...` method takes not only the target and the key path, but also the selector. This way if both a subclass and a superclass register for the same key path on the same object, each one can de-register without affecting the other by specifying its unique selector.

There are some interesting features to note.

The `+defaultCenter` uses [a simple lockless atomic call](https://www.mikeash.com/pyblog/late-night-cocoa.html) to make the singleton thread-safe without needing to lock every access. This is a nice technique which gives you a safe singleton without having to arrange to initialize it in advance or take the hit of locking and unlocking a lock every time the singleton is accessed.

A slightly nicer API is exposed as a category on NSObject. This is better than explicitly accessing the MAKVONotificationCenter singleton. In an extreme case, MAKVONotificationCenter could be removed from the header altogether, leaving only the NSObject extensions.

This code has essentially not been tested. The small bit of testing code in `Tester.m` is all I've done. Don't trust it until you've tried it. At about 150 lines of real code there isn't a lot to it, but caveat emptor in any case.

If you wish to use this in your own projects, you may do so as long as proper credit is given. And patches are most welcome if you discover deficiencies.

If you have any comments about the code please leave them below.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/key-value-observing-done-right.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
