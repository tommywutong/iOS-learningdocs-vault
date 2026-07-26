---
title: 'Friday Q&A 2017-09-22: Swift 4 Weak References'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2017-09-22-swift-4-weak-references.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:35fd443bc426dd0d'
translated: false
---

> 原文：[Friday Q&A 2017-09-22: Swift 4 Weak References](https://www.mikeash.com/pyblog/friday-qa-2017-09-22-swift-4-weak-references.html)　·　mikeash.com Friday Q&A

Posted at 2017-09-23 00:57 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2017-10-06: Type-Safe User Defaults](https://www.mikeash.com/pyblog/friday-qa-2017-10-06-type-safe-user-defaults.html)  
Previous article: [The Best New Features in Swift 4](https://www.mikeash.com/pyblog/the-best-new-features-in-swift-4.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2017-09-22: Swift 4 Weak References

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Chinese (translation by Xiang Deng)](https://ddddxxx.github.io/2017/09/27/swift-4-weak-references/).

**Old Implementation**  
For those of you who have forgotten the old implementation and don't feel like reading through the last article, let's briefly recall how it works.

In the old implementation, Swift objects have two reference counts: a strong count and a weak count. When the strong count reaches zero while the weak count is still non-zero, the object is destroyed but its memory is not deallocated. This leaves a sort of zombie object sitting in memory, which the remaining weak references point to.

When a weak reference is loaded, the runtime checks to see if the object is a zombie. If it is, it zeroes out the weak reference and decrements the weak reference count. Once the weak count reaches zero, the object's memory is deallocated. This means that zombie objects are eventually cleared out once all weak references to them are accessed.

I loved the simplicity of this implementation, but it had some flaws. One flaw was that the zombie objects could stay in memory for a long time. For classes with large instances (because they contain a lot of properties, or use something like `ManagedBuffer` to allocate extra memory inline), this could be a serious waste.

Another problem, which [I discovered](https://bugs.swift.org/browse/SR-192) after writing the old article, was that the implementation wasn't thread-safe for concurrent reads. Oops! This was patched, but the discussion around it revealed that the implementers wanted a better implementation of weak references anyway, which would be more resilient to such things.

**Object Data**  
There are many pieces of data which make up "an object" in Swift.

First, and most obviously, there are all of the stored properties declared in the source code. These are directly accessible by the programmer.

Second, there is the object's class. This is used for dynamic dispatch and the `type(of:)` built-in function. This is mostly hidden, although dynamic dispatch and `type(of:)` imply its existence.

Third, there are the various reference counts. These are completely hidden unless you do naughty things like read the raw memory of your object or convince the compiler to let you call `CFGetRetainCount`.

Fourth, you have auxiliary information stored by the Objective-C runtime, like the list of Objective-C weak references (the Objective-C implementation of weak references tracks each weak reference individually) and associated objects.

Where do you store all of this stuff?

In Objective-C, the class and stored properties (i.e. instance variables) are stored inline in the object's memory. The class takes up the first pointer-sized chunk, and the instance variables come after. Auxiliary information is stored in external tables. When you manipulate an associated object, the runtime looks it up in a big hash table which is keyed by the object's address. This is somewhat slow and requires locking so that multithreaded access doesn't fail. The reference count is sometimes stored in the object's memory and sometimes stored in an external table, depending on which OS version you're running and which CPU architecture.

In Swift's old implementation, the class, reference counts, and stored properties were all stored inline. Auxiliary information was still stored in a separate table.

Putting aside how these languages actually do it, let's ask the question: how _should_ they do it?

Each location has tradeoffs. Data stored in the object's memory is fast to access but always takes up space. Data stored in an external table is slower to access but takes up zero space for objects which don't need it.

This is at least part of why Objective-C traditionally didn't store the reference count in the object itself. Objective-C reference counting was created when computers were much less capable than they were now, and memory was extremely limited. Most objects in a typical Objective-C program have a single owner, and thus a reference count of 1. Reserving four bytes of the object's memory to store `1` all the time would be wasteful. By using an external table, the common value of `1` could be represented by the absence of an entry, reducing memory usage.

Every object has a class, and it is constantly accessed. Every dynamic method call needs it. This should go directly in the object's memory. There's no savings from storing it externally.

Stored properties are expected to be fast. Whether an object has them is determined at compile time. Objects with no stored properties can allocate zero space for them even when stored in the object's memory, so they should go there.

Every object has reference counts. Not every object has reference counts that aren't `1`, but it's still pretty common, and memory is a lot bigger these days. This should probably go in the object's memory.

Most objects don't have any weak references or associated objects. Dedicating space within the object's memory for these would be wasteful. These should be stored externally.

This is the right tradeoff, but it's annoying. For objects that have weak references and associated objects, they're pretty slow. How can we fix this?

**Side Tables**  
Swift's new implementation of weak references brings with it the concept of _side tables_.

A side table is a separate chunk of memory which stores extra information about an object. It's _optional_, meaning that an object may have a side table, or it may not. Objects which need the functionality of a side table can incur the extra cost, and objects which don't need it don't pay for it.

Each object has a pointer to its side table, and the side table has a pointer back to the object. The side table can then store other information, like associated object data.

To avoid reserving eight bytes for the side table, Swift makes a nifty optimization. Initially, the first word of an object is the class, and the next word stores the reference counts. When an object needs a side table, that second word is repurposed to be a side table pointer instead. Since the object still needs reference counts, the reference counts are stored in the side table. The two cases are distinguished by setting a bit in this field that indicates whether it holds reference counts or a pointer to the side table.

The side table allows Swift to maintain the basic form of the old weak reference system while fixing its flaws. Instead of pointing to the object, as it used to work, weak references now point directly at the side table.

Because the side table is known to be small, there's no issue of wasting a lot of memory for weak references to large objects, so that problem goes away. This also points to a simple solution for the thread safety problem: don't preemptively zero out weak references. Since the side table is known to be small, weak references to it can be left alone until those references themselves are overwritten or destroyed.

I should note that the current side table implementation only holds reference counts and a pointer to the original object. Additional uses like associated objects are currently hypothetical. Swift has no built-in associated object functionality, and the Objective-C API still uses a global table.

The technique has a lot of potential, and we'll probably see something like associated objects using it before too long. I'm hopeful that this will open the door to stored properties in extensions class types and other nifty features.

**Code**  
Since Swift is open source, all of the code for this stuff is accessible.

Most of the side table stuff can be found in [stdlib/public/SwiftShims/RefCount.h](https://github.com/apple/swift/blob/c262440e70896299118a0a050c8a834e1270b606/stdlib/public/SwiftShims/RefCount.h).

The high-level weak reference API, along with juicy comments about the system, can be found in [swift/stdlib/public/runtime/WeakReference.h](https://github.com/apple/swift/blob/c262440e70896299118a0a050c8a834e1270b606/stdlib/public/runtime/WeakReference.h).

Some more implementation and comments about how heap-allocated objects work can be found in [stdlib/public/runtime/HeapObject.cpp](https://github.com/apple/swift/blob/c262440e70896299118a0a050c8a834e1270b606/stdlib/public/runtime/HeapObject.cpp).

I've linked to specific commits of these files, so that people reading from the far future can still see what I'm talking about. If you want to see the latest and greatest, be sure to switch over to the `master` branch, or whatever is relevant to your interests, after you click the links.

**Conclusion**  
Weak references are an important language feature. Swift's original implementation was wonderfully clever and had some nice properties, but also had some problems. By adding an optional side table, Swift's engineers were able to solve those problems while keeping the nice, clever properties of the original. The side table implementation also opens up a lot of possibilities for great new features in the future.

That's it for today. Come back again for more crazy programming-related ghost stories. Until then, if you have a topic you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2017-09-22-swift-4-weak-references.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
