---
title: '[objc explain]: Thread-local garbage collection'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2009/08/28/objc_explain_Thread-local_garbage_collection.html'
original_language: en
published: 2009-08-28
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bc1d47e90874a320'
translated: false
---

> 原文：[[objc explain]: Thread-local garbage collection](http://sealiesoftware.com/blog/archive/2009/08/28/objc_explain_Thread-local_garbage_collection.html)　·　Hamster Emporium (Greg Parker)

[![](http://sealiesoftware.com/hamster.jpg)](http://sealiesoftware.com/blog/index.html)  
  
 **blog**  
 [recent](http://sealiesoftware.com/blog/index.html)  
 [archive](http://sealiesoftware.com/blog/archive/index.html)  
 [twitter](http://twitter.com/gparker)  
   
 **projects**  
 [Mac OS X](http://www.apple.com/macosx/)  
 [Keyboard](http://sealiesoftware.com/keyboard/index.html)  
 [backlight](http://sealiesoftware.com/keyboard/index.html)  
 [CSC Menu](http://sealiesoftware.com/cscmenu/index.html)  
 [Valgrind](http://sealiesoftware.com/valgrind/index.html)  
 [Fringe Player](http://sealiesoftware.com/fringe/index.html)  
 [pssh](http://sealiesoftware.com/pssh/index.html)  
 [Peal](http://sealiesoftware.com/peal/index.html)  
 [Frankenmouse](http://sealiesoftware.com/frankenmouse/index.html)

## Hamster Emporium archive

\<\< [[objc explain]: Selector uniquing in the dyld shared cache](http://sealiesoftware.com/blog/archive/2009/09/01/objc_explain_Selector_uniquing_in_the_dyld_shared_cache.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]: So you crashed in objc_msgSend(): iPhone Edition](http://sealiesoftware.com/blog/archive/2009/06/08/objc_explain_So_you_crashed_in_objc_msgSend_iPhone_Edition.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2009/08/28/objc_explain_Thread-local_garbage_collection.html)

**[objc explain]: Thread-local garbage collection** ([2009-08-28 1:00 PM](http://sealiesoftware.com/blog/archive/2009/08/28/objc_explain_Thread-local_garbage_collection.html))

Mac OS X Snow Leopard introduces thread-local collection, a big enhancement to the Objective-C garbage collector. Thread-local collection is a more efficient way to reclaim much of the garbage in most programs. It also scales better to more threads and more cores than the other algorithms used by the Objective-C GC.

#### A brief history of garbage collection

The simplest algorithm used by the Objective-C GC is **full collection**. The GC scans all live objects in the entire heap, discovers (approximately) all dead objects, and reclaims them. This is slow, especially if you have a large population of not-dead objects, but does find all possible garbage. Historically this is mostly 1960-era technology, except for the machinery that allows other threads to run mostly unhindered while the scan completes.

The second algorithm used by the Objective-C GC is **generational collection**. This takes advantage of the _generational hypothesis_: most objects die young. The heap is divided into at least two generations: new objects and old objects. After allocating some amount of new objects, the collector runs a generational collection. First, it scans only the "new" objects and any "old" objects into which a pointer to a "new" object was stored. Then the now-dead "new" objects are reclaimed, and the surviving "new" objects are aged, moving them to the next generation. The advantage of generational GC is that it collects lots of garbage (most objects die young) with much less work (it does not need to scan most of the "old" objects). Full collections are still needed to reclaim objects that survive infancy and die later, but run less often. Generational collection is 1980-era technology.

#### Thread-local collection

The third algorithm is the new **thread-local collection**. TLC is similar to generational collection: it scans and reclaims a subset of objects, trying to get lots of bang for the collector's buck. The _thread-local_ hypothesis: most objects die without being reachable by any other thread. Newly-allocated objects are marked thread-local to the allocating thread. If a thread-local object becomes accessible to another thread (for example, a pointer to it is written into a global variable), then it has "escaped" and is moved out of the thread-local set. In a thread-local collection, a thread scans its own stack and its set of thread-local objects, and reclaims the dead objects.

The advantage of thread-local collection is that it requires no synchronization with other threads. Normally, a thread performing GC work needs to coordinate with the other threads. For example, the other threads change a pointer variable after the GC thread has looked at it, or start pointing to an object that the GC thread thinks is dead. Thread-local collection avoids these complications. The thread-local objects are by definition reachable only by one thread. The other threads have no way acquire a pointer to any of those objects, or change pointer values inside them. A thread performing thread-local collection can work quickly on its own, without interference from other threads.

Having each thread "clean up after itself" reduces bottlenecks in the collector that will only get worse as threads and cores increase. It's trivial to run thread-local collections on multiple threads simultaneously. And it's very fast because the only memory to scan is the thread's own stack and its surviving thread-local objects. The pause time for a thread during generational or full GC is almost as big as the pause time for that thread to run a thread-local collection - but TLC can then immediately reclaim some garbage, whereas the other algorithms need to do much more work and coordinate with all of the other threads before they can actually reclaim anything.

#### How you can help

Thread-local collection works best when objects remain unreachable to other threads. In the Objective-C collector, this means avoiding CFRetain() of temporary objects when possible. A CFRetained pointer could go anywhere behind the collector's back, bypassing the write barrier that the collector uses to keep track of escaping objects. (This is one place that Snow Leopard leaves room for improvement: the system frameworks often allocate objects with a CF retain count of one and immediately release them, making them ineligible for thread-local collection.) Other ways for an object to escape thread-local collection include storing a pointer into a global variable; storing a pointer into some other object that itself is not thread-local; and making a weak reference or associated reference to the object.

If your thread has just created and discarded a lot of temporary objects, you can give the collector a hint that now might be a good time to run. `-[NSGarbageCollector
	collectIfNeeded]` and `-[NSAutoreleasePool
	drain]` are two such hints. These may run a thread-local collection first, and may follow up with generational or full collection.

[Sealie Software](http://sealiesoftware.com/index.html)
