---
title: 'Friday Q&A 2009-02-20: The Good and Bad of Distributed Objects'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-02-20-the-good-and-bad-of-distributed-objects.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:30160be6e145af64'
translated: false
---

> 原文：[Friday Q&A 2009-02-20: The Good and Bad of Distributed Objects](https://www.mikeash.com/pyblog/friday-qa-2009-02-20-the-good-and-bad-of-distributed-objects.html)　·　mikeash.com Friday Q&A

Posted at 2009-02-20 20:40 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-02-27: Holistic Optimization](https://www.mikeash.com/pyblog/friday-qa-2009-02-27-holistic-optimization.html)  
Previous article: [Friday Q&A 2009-02-13: Operations-Based Parallelization](https://www.mikeash.com/pyblog/friday-qa-2009-02-13-operations-based-parallelization.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [ipc](https://www.mikeash.com/pyblog/?tag=ipc) [performance](https://www.mikeash.com/pyblog/?tag=performance)

Friday Q&A 2009-02-20: The Good and Bad of Distributed Objects

by [Mike Ash](https://www.mikeash.com/)

**Overview**  
 I'm not going to take a detailed look at the basics of Distributed Objects, as there are plenty of resources out there for that. But for those readers who are unfamiliar with Distributed Objects, I'll give a quick look at what it is.

Distributed Objects (DO) is a Cocoa API for interprocess communication built on automatic proxying of messages, so that remote objects look and act mostly like local objects. The primary interface to the DO system is the `NSConnection` class. Vending an object with DO is as easy as this:

```
    NSConnection *connection = [[NSConnection connectionWithReceivePort:[NSPort port]] sendPort:nil];
    [connection setRootObject:theObject];
    [connection registerName:@"com.example.whatever"];
```

And accessing that vended object from another process is as easy as this:

```
    id theObject = (id)[NSConnection rootProxyForConnectionWithRegisteredName:@"com.example.whatever" host:nil];
    [theObject someMethod];
```

From this point, theObject acts as though it were local. You can send messages to it just like any other object. You can pass it local objects as arguments or get remote objects back as return values, and DO takes care of proxying or serializing the objects as appropriate. It's very cool, and there's literally nothing else that needs to be done other than the above code if you just need basic functionality.

**The Good**  
 I think this should be pretty clear from the above description, but let's quickly compare it to other IPC mechanisms:

1. Just a few lines of code to set up a fully functional connection.
2. For the most part, remote objects can be passed around just like local objects. This means that little of your code needs to be DO-aware.
3. DO can be used over mach ports or sockets. It can be used to communicate between threads or between processes. It's reasonably configurable.
4. Because DO works the same way as Objective-C messages, you don't have the same problems you might have trying to support two different protocol versions. Of course it's not always rosy, but if your changes involve implementing different methods, it's easy to check for what's going on using

  and the like, rather than having to give up.

All of this makes DO a very useful facility.

**The Bad**  
 So if DO is so great, why am I not a bigger fan? Part of it is simply because DO can't completely abstract away the fact that it's running over a transport layer and talking to a remote process, and part of it is because DO itself is just not as good as it could be.

One leaky abstraction is primitive types. DO needs to be able to either serialize (i.e. copy across the connection) or proxy everything that gets used as an argument or returned as a value with a "distant object". For objects, this is fine. Objects that want to be copied can implement `NSCoding`, and all other objects can use Objective-C's built-in message capturing facilities to proxy all requests across the connection.

For primitives, things get harder. For scalars and even structs, the Objective-C runtime provides enough type information that these can be copied across. But once you hit pointers, things fall apart. Imagine trying to proxy a call like this:

```
    [array getObjects:objarray range:NSMakeRange(5, 13)];
```

It basically can't be done. DO would have to somehow know that the length of the

parameter is determined by the length of the range being passed in, and copy only that much memory across the connection. It would also have to know that this is a return-by-reference only, and that it shouldn't be trying to serialize or proxy the contents of

across the connection (it could be filled with junk, and an attempt to proxy that junk would crash). Yes, DO could special-case this particular method, but it won't be able to deal with arbitrary such methods.

DO does have some interesing language-level facilities to help with this. You can specify a pointer parameter as being `in`, `out`, or `inout` so that it knows which way to serialize or proxy. But this only works with pointers to single objects. For arrays, it just can't cope.

Another leaky abstraction is that the process that you're talking to could disappear at any moment. Objective-C just isn't set up to deal with this very well:

```
    id obj = [self method];
    [obj thing1];
    [obj thing2];
```

In normal Objective-C,

is either broken from the start (in which case you'll crash) or it remains valid throughout the method. But if

is a distant object, suddenly things are not so clear. The remote process could disappear (or freeze up and time out) in between the call to

and

.

When that happens, DO deals with it by throwing an exception. Surprise!

Most Objective-C code is not exception safe. Although there's no particular reason that exceptions can't be used more frequently the way they are in languages like Java, convention is that exceptions in Objective-C are only used to indicate a programming error. In order to really robustly use DO, you need to write your code such that it can handle an exception being thrown by _any_ interaction with a distant object. Worse yet, this includes Cocoa code, meaning that you essentially cannot pass a distant object to any Cocoa code. (Ever wonder what happens when an `NSSet` sends `-hash` to your object, and `-hash` throws an exception? Odds are fair that it leaves the `NSSet` in an inconsistent state that will lead to a crash.)

This requirement for all code touching distant objects to be exception safe is tough, and greatly limits the places in which DO can be practically used. The promise is that remote objects look like local objects, and they mostly do, but this one (absolutely necessary) detail means that they can't be used like local objects at all.

Lastly, DO is not very modular or extensible. Ideally, DO would be a fully modular system. You'd have the DO system which would sit on top of some kind of interchangeable transport class. Customizing the transport class (for example, to make it use encryption, or talk to a serial port, or use avian carriers) would simply be a matter of subclassing a public abstract class and implementing a documented set of primitive methods.

The reality is not so simple. The classes that DO uses internally are fairly tightly coupled, and there's a lot of legacy cruft. Implementing a custom NSPort subclass that works with NSConnection is so difficult that I'm only aware of one working example ([Secure Distributed Objects](http://sourceforge.net/projects/securedo), which appears to be a dead project now). This pretty much sinks the idea of using DO for any serious network communication, since DO doesn't encrypt the transport and it's not practical to add encryption to it.

**Conclusion**  
 Distributed Objects is a very cool system that has many uses. Unfortunately, due to both the costraints under which it works and some poor design decisions, it's not as useful as it could be. It can still be handy for doing IPC and it's a great tool to have in Cocoa, but it falls short of being a no-brainer way to talk to other processes.

That wraps up this week's Friday Q&A. Check back next week for another exciting installment. In the meantime, keep those ideas coming. Friday Q&A is powered by your submissions, so don't be shy. Post your topic ideas in the comments below or [e-mail them directly to me](mailto:mike@mikeash.com). (Yes, I link my real e-mail address directly on the web! How can you refuse that!) If I use your suggestion then I will use your name unless you tell me otherwise.

Love Distributed Objects? Think your pet RPC mechanism is better? Fire away.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
