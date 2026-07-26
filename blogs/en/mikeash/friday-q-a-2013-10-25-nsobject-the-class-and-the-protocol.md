---
title: 'Friday Q&A 2013-10-25: NSObject: the Class and the Protocol'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-10-25-nsobject-the-class-and-the-protocol.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c88a245fdf68551b'
translated: false
---

> 原文：[Friday Q&A 2013-10-25: NSObject: the Class and the Protocol](https://www.mikeash.com/pyblog/friday-qa-2013-10-25-nsobject-the-class-and-the-protocol.html)　·　mikeash.com Friday Q&A

Posted at 2013-10-25 13:27 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [VoodooPad Acquisition](https://www.mikeash.com/pyblog/voodoopad-acquisition.html)  
Previous article: [Friday Q&A 2013-10-11: Why Registers Are Fast and RAM Is Slow](https://www.mikeash.com/pyblog/friday-qa-2013-10-11-why-registers-are-fast-and-ram-is-slow.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2013-10-25: NSObject: the Class and the Protocol

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Chinese (translation by neoman)](https://github.com/0oneo/iOSArchive/wiki/%E7%BF%BB%E8%AF%91-NSObject%EF%BC%9Athe-Class-and-the-Protocol).

**Namespaces**  
First, let's look at _how_ these two entities with the same name can coexist. Classes and protocols in Objective-C inhabit entirely separate namespaces. You can have a class and a protocol, which are unrelated at the language level, with the same name. That's the case with `NSObject`.

If you look at the language, there are no places where you can use either a class name or a protocol name. Class names can be used as the target of message sends, in `@interface` declarations, and as type names. Protocols can be used in some of the same places, but always in a different way. There's no ambiguity in having one of each with the same name.

**Root Classes**  
`NSObject` the class is a root class. A root class is a class at the very top of the hierarchy, meaning that it has no superclass. In Objective-C, unlike some languages like Java, there can be more than one root class.

Java has a single root class, `java.lang.Object`, which every other class directly or indirectly inherits from. Because of this, Java code can count on any object it encounters implementing the basic methods in `java.lang.Object`.

Cocoa has multiple root classes. In addition to `NSObject` there's also `NSProxy` and some other assorted root classes. This is part of the reason for the `NSObject` protocol. The `NSObject` protocol defines a set of basic methods that all root classes are expected to implement. This way, code can count on those methods being there.

The `NSObject` class conforms to the `NSObject` protocol, which means that the `NSObject` class implements these basic methods:

```
    @interface NSObject <NSObject>
```

`NSProxy` also conforms to the `NSObject` protocol:

```
    @interface NSProxy <NSObject>
```

The `NSObject` protocol contains methods like `hash`, `isEqual:`, `description`, etc. The fact that `NSProxy` conforms to `NSObject` means that you can still count on instances of `NSProxy` implementing these basic `NSObject` methods.

**An Aside About Proxies**  
While we're at it, just why is there an `NSProxy` root class?

There are some cases where it's useful to have a class that doesn't implement very many methods. As the name suggests, proxy objects are a common case where this is useful. The `NSObject` class implements a lot of stuff beyond the `NSObject` protocol, such as key-value coding, that you don't necessarily want.

When building a proxy object, the goal is generally to leave most methods unimplemented so that they can be forwarded in bulk using a method like `forwardInvocation:`. Subclassing `NSObject` would pull in a lot of baggage that would interfere. `NSProxy` helps to avoid this by giving you a simpler superclass that doesn't have so much extra stuff in it.

**Protocols**  
The fact that the `NSObject` protocol is useful for root classes isn't all that interesting for most Objective-C programming, since we don't use other root classes very often. However, it becomes really handy when making your own protocols. Say you have a protocol like this:

```
    @protocol MyProtocol

    - (void)foo;

    @end
```

And now you have a pointer to an object that conforms to it:

```
    id<MyProtocol> obj;
```

You can tell this object to foo:

```
    [obj foo];
```

However, you cannot ask the object for its description:

```
    [obj description]; // no such method in the protocol
```

And you can't check it for equality:

```
    [obj isEqual: obj2]; // no such method in the protocol
```

In general you can't ask it to do any of the stuff that a normal object can do. Sometimes this doesn't matter, but sometimes you actually want to be able to do this stuff.

This is where the `NSObject` protocol Comes in. Protocols can inherit from other protocols. You can make `MyProtocol` inherit from the `NSObject` protocol:

```
    @protocol MyProtocol <NSObject>

    - (void)foo;

    @end
```

This says that not only do objects that conform to `MyProtocol` respond to `-foo`, but they also respond to all those common messages in the `NSObject` protocol. Since every object in your app typically inherits from the `NSObject` class and it conforms to the `NSObject` protocol, this doesn't impose any additional requirements on people implementing `MyProtocol`, while allowing you use these common methods on instances.

**Conclusion**  
The fact that there are two different `NSObjects` is an odd corner of the frameworks, but it makes sense when you get down to it. An `NSObject` protocol allows multiple root classes to all have the same basic methods, and also makes it easy to declare a protocol which also includes basic functionality expected of any object. The `NSObject` class conforms to the `NSObject` protocol, bringing everything together.

That's it for today. Friday Q&A is driven by reader suggestions as always, so if you have a topic you'd like to see covered in a future edition, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2013-10-25-nsobject-the-class-and-the-protocol.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
