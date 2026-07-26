---
title: 'Friday Q&A 2010-05-14: What Every Apple Programmer Should Know'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-05-14-what-every-apple-programmer-should-know.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:96acfae103692bea'
translated: false
---

> 原文：[Friday Q&A 2010-05-14: What Every Apple Programmer Should Know](https://www.mikeash.com/pyblog/friday-qa-2010-05-14-what-every-apple-programmer-should-know.html)　·　mikeash.com Friday Q&A

Posted at 2010-05-14 15:36 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Some Light Reading](https://www.mikeash.com/pyblog/some-light-reading.html)  
Previous article: [iPhone Apps I Can't Have](https://www.mikeash.com/pyblog/iphone-apps-i-cant-have.html)  
Tags: [advice](https://www.mikeash.com/pyblog/?tag=advice) [apple](https://www.mikeash.com/pyblog/?tag=apple) [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2010-05-14: What Every Apple Programmer Should Know

by [Mike Ash](https://www.mikeash.com/)

**But First, a Brief Word from Our Sponsor**  
 Before I get into the meat of the post, I have a bit of meta-business. While I greatly enjoy writing Friday Q&A and am humbled by the great feedback I get about it, it also represents a significant drain on my time that's becoming hard to sustain. Therefore, starting with this post, I will be scaling Friday Q&A back to a biweekly schedule. I'll be writing the same stuff in the same place, just not quite as often. I hope that what I'm taking away in quantity, I'll be able to make up for in quality.

**And Now, Back to Our Show**  
 While the theme of this article is common problems in Cocoa, I think this will also have a great deal of relevance to any Cocoa programmer as well. Ultimately, this will be a collection of common problems in API design and implementation, and large chunks of any real application count as APIs. While I really want Apple to follow these ideas, if you follow them as well, they should make your life much easier.

Without further ado, the list.

**Always use `[self class]` when invoking your own class methods**  
 A bunch of these boil down to making your code easier to subclass, and this is the first. If you hardcode your class when invoking a class method, it makes it impossible for a subclass to override that behavior. If that class method is public, then you've created a frustrating situation: the method exists, is published, can be overridden, but won't be called if you do, so you can't change the behavior.

**Don't access instance variables directly if there's an accessor**  
 This is much like the previous one. If there's an accessor, there's an expectation that you can override it in a subclass to alter the value which is used. If you access the instance variable directly, you bypass that override, making it impossible for subclasses to alter behavior. Even worse, if you use the accessor only _sometimes_, then you get bizarre inconsistent behavior that's easy to go wrong. Apple really loves to do this one, so as a user of Cocoa, be careful when subclassing and overriding accessors, and be prepared for them not to be called.

**If components of functionality are exposed as public methods, the implementation should always call them when it needs that functionality**  
 Yet another ease-of-subclassing item. Sometimes Apple provides a public method, but doesn't use it internally to accomplish the task it's built for. An example of this is `NSSliderCell`, which provides a `drawBarInside:flipped:` method, but which does its own bar drawing separately. If you want custom bar drawing, you either have to override a higher level drawing method, or you have to override the private `_usesCustomTrackImage` method to convince it to call your custom code. Another example is `NSMutableURLRequest`'s `setHTTPBodyStream:` method. If you create a custom `NSInputStream` class and pass an instance of that custom class as the parameter, it won't work. You have to override the private `_scheduleInCFRunLoop:forMode:` method for the two components to work together. Subclasses should be able to override a public method to alter functionality, or work with existing APIs, without jumping through these hoops.

**Don't write empty stub methods and then make them public**  
 `NSView` has this nifty method:

```
    - (BOOL)lockFocusIfCanDrawInContext:(NSGraphicsContext *)context;
```

It's nifty until you read the documentation on it, which says, "This method was declared in Mac OS X v10.4, but is not used in that release. It currently does nothing and returns NO. However, it might be implemented in a future release."

It baffles me as to why this method is public. It's useless, so why have it at all? If they plan to implement it in the future, they could make it public once it's implemented. I can only assume that it was implemented as a stub with the intent to complete it, but then it slipped through the cracks.

Apple doesn't do this much, but suffice it to say that it shouldn't happen at all.

**User data fields should be `id`**  
 It's a common pattern to have "user data" as part of an API, which is just some arbitrary data which can be passed through a callback or attached to an object. Sometimes this is an object, but sometimes Cocoa presents user data as a `void *`. This greatly complicates memory management (especially when using garbage collection) to little benefit. The common case is to pass an object as user data, and the API should simplify that. For the rare cases where you want a different type of pointer, the programmer can always wrap it in an `NSValue`.

**Make up your mind on what "thread safe" means**  
 As I [discussed in an earlier post](https://www.mikeash.com/pyblog/friday-qa-2009-01-09.html), Apple is pretty inconsistent about what "thread safe" actually means. Sometimes it means any instance can be safely used from multiple threads simultaneously. Sometimes it means any instance can be used from one thread at a time, but that you must synchronize access. Sometimes that's described as "not thread safe" instead. It's tremendously confusing! The world is becoming heavily multithreaded, and we need more explicit descriptions of what these APIs require.

**Make fewer APIs dependent on the main thread**  
 The main thread is a huge bottleneck in a modern Cocoa app, because many APIs only work on the main thread. Most GUI manipulation can't be safely done off the main thread, even if you take care to cleanly keep each window on a single thread. Entire APIs, like WebKit, can only be used from the main thread. Fortunately, the situation is gradually improving.

**Make every runloop API take a modes parameter**  
 Do a google search for [webview modal](http://www.google.com/search?q=webview+modal) to see what the problem is here. `WebView` depends on a running runloop to do its processing, but it only runs in the default mode. If you want your `WebView` to remain functional while a modal window is running, you're out of luck. You should be able to easily schedule the `WebView` in the modal runloop mode, but the API isn't there, so you can't. While it's perfectly reasonable to schedule into one particular runloop mode _by default_, a runloop-dependent API should always provide for the ability to schedule on other modes too.

**Make it easy to convert between different classes with similar capabilities**  
 An example of this is `NSImage` and `CGImage`. Before Snow Leopard, there was no easy way to convert between the two, even though they were fairly similar. (Yes, `NSImage` can contain multiple representations, isn't necessarily pixel-based, etc. They're still conceptually close.) If you had one, and needed the other, it was a bunch of work to go from one to the other.

In 10.6, Apple added APIs to `NSImage` to make it easy to convert between them, and suddenly life became a lot easier.

Toll free bridging in CoreFoundation is the pinnacle of how to do this right. The objects are interoperable, and just require a cast to convince the compiler that you're not insane. While this isn't always possible, easy methods to do explicit conversion help enormously.

There are still areas where this is lacking. `NSColor` and `CGColor` are difficult to convert between. `CFBundle` and `NSBundle` are extremely similar but not interchangeable or convertible.

**Don't pollute namespaces**  
 One of the unfortunate things missing from Objective-C is namespaces. It's all too easy for components in a framework to conflict with components in an application. If you're building a framework, then you need to minimize the possibility of this happening as much as possible.

Always prefix class names with something that should be reasonably unique. This goes _even for private classes_. They can conflict and cause problems even though they're never exposed as part of your public API.

You also need to prefix _category_ methods that aren't made public. If they aren't prefixed, there's a risk of conflict with other category methods. The same also goes for private methods.

**Conclusion**  
 Overall, Cocoa is a great API, but there are a few common problems which make things a little bit less smooth than they otherwise could be. The intent is not to bash Apple, but just show how things could be made a little bit better, and give some ways that the rest of us can make our own APIs better as well.

That's it for this edition of Friday Q&A. Again, the next one will now be in _two_ weeks. Until then, keep sending in your ideas for posts. Friday Q&A is driven by user ideas, so if you have a topic you'd like to see covered here, [get in touch](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-05-14-what-every-apple-programmer-should-know.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
