---
title: 'Friday Q&A 2009-10-02: Care and Feeding of Singletons'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-10-02-care-and-feeding-of-singletons.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e6a5530eacccbfc5'
translated: false
---

> 原文：[Friday Q&A 2009-10-02: Care and Feeding of Singletons](https://www.mikeash.com/pyblog/friday-qa-2009-10-02-care-and-feeding-of-singletons.html)　·　mikeash.com Friday Q&A

Posted at 2009-10-02 15:59 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-10-09: Defensive Programming](https://www.mikeash.com/pyblog/friday-qa-2009-10-09-defensive-programming.html)  
Previous article: [Friday Q&A 2009-09-25: GCD Practicum](https://www.mikeash.com/pyblog/friday-qa-2009-09-25-gcd-practicum.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [singleton](https://www.mikeash.com/pyblog/?tag=singleton)

Friday Q&A 2009-10-02: Care and Feeding of Singletons

by [Mike Ash](https://www.mikeash.com/)

**What Is It?**  
 Most of you probably know this already, but for the sake of completeness, a singleton is an object which is restricted to be the only instance of its class. In other words, within any given process, you have the concept of _the_ `Foo`, rather than _a_ `Foo`.

**Benefits**  
 Why would you use a singleton instead of a regular class? There are a few basic reasons:

1. **Global access:** A singleton is essentially shared throughout the entire program, making it easier to coordinate activities. A major example of this in Cocoa is `NSNotificationCenter`.
2. **Resource management:** Having a single instance of a class is appropriate if that class represents an entity which is inherently singular. An example of this in Cocoa is `NSApplication`.
3. **Grouping functionality:** Sometimes you have a lot of similar functionality that logically goes together but which doesn't necessarily fit into the object model because there's no long-term state. By using a singleton you simplify access to this functionality. `NSWorkspace` is an exmple of this usage of a singleton in Cocoa.
4. **Lazy initialization:** Properly-written singleton classes aren't instantiated until something asks for them, meaning that the resources occupied by the singleton aren't allocated until they're needed.

**Downsides**  
 Singletons aren't always appropriate. (In fact, they're almost always not appropriate. Just look at the proprotion of singletons to normal classes in any given program.) In general you should not use one unless you need it, but there are some specific pitfalls to look out for:

1. **Shared global state:** Singletons are inherently globally accessible, which means that any state which exists as part of the singleton can be accessed and potentially changed from any part of the program. Good encapsulation of singleton state can help with this a lot, but if you're not careful then the problem can be much like that of global variables. This can be particularly vicious in a multithreaded environment. Many Cocoa singletons suffer from not being thread safe and [their global accessibility makes them inherently limited to only being used from the main thread](https://www.mikeash.com/pyblog/friday-qa-2009-01-09.html).
2. **Over-specialized code:** You thought there would only be one, so you made a singleton around it. Now there are two. All of your code assumes that there is only one. Time for a big, painful rewrite.

**How to Make One**  
 At its most basic, a singleton is implemented like this:

```
    + (id)sharedFoo
    {
        static Foo *foo = nil;
        if(!foo)
            foo = [[self alloc] init];
        return foo;
    }
```

That's it! You're done!

Right about now, a bunch of people are thinking back to [a certain Apple document on singletons](http://developer.apple.com/mac/library/DOCUMENTATION/Cocoa/Conceptual/CocoaFundamentals/CocoaObjects/CocoaObjects.html) which shows a much more complicated implementation. There are basically two advantages to Apple's version which this doesn't have.

1. **Thread safety:** Apple's version correctly deals with the case where multiple threads try to access the singleton before it's been created.
2. **Programmer safety:** Apple's version tries to cover for a lot of dumb mistakes a programmer might make, like incorrectly releasing a singleton.

Thread safety is useful but not always necessary. Programmer safety is, in my opinion, counterproductive. Apple's approach, of building a singleton which can't be destroyed by accident and which intercepts attempts to allocate a second instance, covers up errors rather than fixing them. It's much better to trap and eliminate the bad code rather than render it harmless. For example, instead of overriding `release` to do nothing, override `dealloc` to log an error and abort the program.

Furthermore, it's not always necessary to really strictly enforce singleton-ness. `NSFileManager` is a good example of this from Cocoa. Through 10.4 it was a singleton, and not thread safe and thus could only be used on the main thread. Starting in 10.5, Apple allowed the creation of separate instances which could then be safely used on other threads. Your code might well want to do the same thing. Often, providing the shared globally-accessible instance is the major benefit of having a singleton, and there's no need to prohibit other instances being created on the side.

This brings up one tip I want to mention regarding singletons: _always implement a `dealloc` method and keep it up to date_. With a singleton, it's tempting to forget about releasing resources because it will live for the life of the program. But it's much easier to write code to release resources as you write the rest of the code than it is to add it in later, and you'll be glad you did if you ever decide to make your singleton no longer be single.

**Thread Safe Singletons**  
 What about when thread safety _is_ necessary?

One really simple way to deal with this is to simply toss in a lock, like so:

```
    + (id)sharedFoo
    {
        static Foo *foo = nil;
        @synchronized([Foo class])
        {
            if(!foo)
                foo = [[self alloc] init];
        }
        return foo;
    }
```

Now your singleton can be safely accessed from multiple threads.

Note: this makes it safe to retrieve the shared singleton from multiple threads, but does not automatically make it safe to _use_ it. Making the singleton's code be thread safe is up to you!

This code is kind of slow, though. Taking a lock is somewhat expensive. Making it more painful is the fact that the vast majority of the time, the lock is pointless. The lock is only needed when `foo` is `nil`, which basically only happens once. After the singleton is initialized, the need for the lock is gone, but the lock itself remains.

One fix for this is to take advantage of the Objective-C runtime and use the `+initialize` method instead:

```
    static Foo *gSharedFoo;
    
    + (void)initialize
    {
        if(self == [Foo class])
            gSharedFoo = [[self alloc] init];
    }
    
    + (id)sharedFoo
    {
        return gSharedFoo;
    }
```

The runtime takes care of all the nasty locking stuff for you, and ensures that `+initialize` always runs before `+sharedFoo` can execute. The only downside to this approach is that `+initialize` will run if _any_ message is sent to your class, possibly initializing the singleton earlier than necessary.

**Double-Checked Locking**  
 If you search on the above phrase you'll find a bunch of web pages talking about how this technique is a bad idea. And it is, for platform-independent code. However, if you can assume some knowledge of your target platform (and hey, we're all doing OS X development here) then it can be done safely.

The basic concept of double-checked locking is to have two copies of the if statement that checks to see if the singleton has been initialized. An outer if statement checks to see if the singleton is initialized. If it is, then return it, no lock taken. If it's not, then take the lock _and check the singleton again_. This ensures that all threads which might try to initialize the singleton are synchronized via the lock.

The problem with this approach is out-of-order memory access, either generated by the compiler or performed by the CPU. For more information on this, you can [read my article on using the `volatile` keyword in a multithreaded context](https://www.mikeash.com/pyblog/friday-qa-2009-07-10-type-specifiers-in-c-part-3.html).

The solution to the CPU side is to insert a memory barrier when writing and when reading. Memory barriers enforce in-order access to memory locations by the CPU. In OS X, a memory barrier function is available in the `libkern/OSAtomic.h` header, called `OSMemoryBarrier`. The solution to the compiler side is to use `volatile` on the shared variable.

Thus our double-checked locking singleton method looks like this:

```
    + (id)sharedFoo
    {
        static Foo * volatile foo = nil;
        if(!foo)
        {
            @synchronized([Foo class])
            {
                if(!foo)
                {
                    Foo *tmpFoo = [[self alloc] init];
                    OSMemoryBarrier();
                    foo = tmpFoo;
                }
            }
        }
        OSMemoryBarrier();
        return foo;
    }
```

This is better than taking a lock every time, but we still have to pay for the memory barrier. It probably doesn't matter at all, and this smacks of premature optimization, but it grates to have that in there.

**Grand Central Dispatch**  
 If you can target 10.6+, Grand Central Dispatch provides an extremely fast one-time initialization API which is perfect for a singleton. Not only is it fast, but it's also extremely easy to use. It's a win all around!

Here's what the GCD solution looks like:

```
    + (id)sharedFoo
    {
        static dispatch_once_t pred;
        static Foo *foo = nil;
        
        dispatch_once(&pred, ^{ foo = [[self alloc] init]; });
        return foo;
    }
```

The `dispatch_once` function takes care of all the necessary locking and synchronization. It's actually a macro which expands to something much like the double-checked locking solution above. However, using some extremely underhanded trickery, it doesn't even need to take the hit of a memory barrier. In the common case, this code is a single if check followed by a return. Aside from the fact that it's examining two variables instead of one (an extremely small cost) it's as fast as the non-thread-safe version I started out with, and very nearly as simple. Nice!

**Advanced Topics**  
 There are a couple of interesting advanced techniques with singletons that I want to cover briefly. I won't go over how to build them, but think of them as exercises for the reader.

One such thing is an automatic singleton class. This would be a class which you subclass and which automatically provides all the necessary infrastructure to provide a singleton of that class. The superclass would have a method which returns (and creates, if necessary) the singleton instance of the subclass on which it was invoked. Managing the singletons would probably involve a global dictionary mapping classes to their singleton instances.

Another interesting variant, which I've never actually seen implemented, is a destroyable singleton. Rather than create a single shared instance which lives forever, the singleton accessor would not take ownership of the singleton object, and would allow it to be destroyed when all other code gives up ownership of it. In Cocoa, this would be accomplished by returning an autoreleased singleton, or when programming with garbage collection, by using a `__weak` global to store it. Making this thread safe would be a challenge, to ensure that duplicates aren't created but that old ones aren't ressurected as they're being destroyed.

**Conclusion**  
 That wraps up this week's edition. Now you know all about singletons, probably far more than you wanted to know.

Come back next week for another one. As always, Friday Q&A is driven by your submissions. The better the submissions I get, the better the articles you get to read! [Send in your ideas for future articles today!](mailto:mike@mikeash.com)

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-10-02-care-and-feeding-of-singletons.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
