---
title: 'Friday Q&A 2010-04-30: Dealing with Retain Cycles'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-04-30-dealing-with-retain-cycles.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f5ea1bef61a70053'
translated: false
---

> 原文：[Friday Q&A 2010-04-30: Dealing with Retain Cycles](https://www.mikeash.com/pyblog/friday-qa-2010-04-30-dealing-with-retain-cycles.html)　·　mikeash.com Friday Q&A

Posted at 2010-04-30 15:29 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Another Week Without Friday Q&A](https://www.mikeash.com/pyblog/another-week-without-friday-qa.html)  
Previous article: [Friday Q&A 2010-04-23: Implementing a Custom Slider](https://www.mikeash.com/pyblog/friday-qa-2010-04-23-implementing-a-custom-slider.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory) [release](https://www.mikeash.com/pyblog/?tag=release) [retain](https://www.mikeash.com/pyblog/?tag=retain)

Friday Q&A 2010-04-30: Dealing with Retain Cycles

by [Mike Ash](https://www.mikeash.com/)

**Retain Cycles**  
 First we need to discuss exactly what a retain cycle is. I'll assume you're familiar with standard Cocoa memory management. The simplest retain cycle is when two objects retain each other:

```
    Object A
     |    ^
     |    |
     v    |
    Object B
```

And in the general case, it can be any collection of objects which results in a circular series of links like this. It's rare, but possible, to have a chain of three, four, five, or more objects which point to each other in a cycle.

Retain cycles are a problem because the standard for Cocoa memory management is to release such retained references in an object's `dealloc` method. However, if an object is being retained, it won't `dealloc`. Objects which are part of a retain cycle will never be deallocated, and will leak if separated from the rest of the application.

Note that retain cycles can involve your own classes, but can also involve Cocoa classes. Two of the most common culprits in retain cycles in Cocoa classes are `NSTimer` and `NSThread`.

Also note that retain cycles only affect code that uses manual memory management. Cocoa's garbage collector is able to detect and destroy objects which have strong references to each other but which aren't referenced from the outside. However, retain cycles are a big threat if you're using retain/release memory management (like if you're on the iPhone), and can even show up in a garbage collected application if you use `CFRetain` and `CFRelease` to bypass the collector.

**Avoiding Retain Cycles**  
 Apple's memory management guidelines state that when two objects have a parent-child relationship, the parent should retain the child. If the child needs a reference back to the parent, that reference should be an unretained, weak reference. This allows the parent to be deallocated, which can then release its reference to the child, avoiding a cycle.

However, sometimes you have two objects which are peers. Neither one is a parent of the other, but they need to reference each other. If these references are retained, then you have a cycle.

One way to deal with this is to redefine the relationship into parent-child. You can arbitrarily choose one to be the parent object, which will have a retained reference to the other. The other can then have a weak reference to the first. The cycle diagram then looks like this:

```
    Object A
     |    ^
     |    :
     v    :
    Object B
```

To be safe, Object A should always zero out B's weak reference when it's destroyed, to ensure that B doesn't then try to message it afterwards:

```
    - (void)dealloc
    {
        [_b setAReference: nil];
        [_b release];
        [super dealloc];
    }
```

(This is also a good practice to follow with any weak reference, including things like

data sources.)

An alternative approach is to have another object act as the parent for both sub-objects. This can work with either retained or weak references between the sub-objects. With retained references:

```
           Object C
           |      |
           |      |
           v      v
    Object A<====>Object B
```

In this scenario, you still have a retain cycle, but C can break the cycle when it releases its references:

```
    - (void)dealloc
    {
        // break the cycle by zeroing the reference
        [_a setBReference: nil];
        
        // this breaks the cycle in both directions; this is optional
        [_b setAReference: nil];
        
        [_a release];
        [_b release];
        
        [super dealloc]; 
    }
```

You can also have a weak reference between the sub-objects:

```
           Object C
           |      |
           |      |
           v      v
    Object A<::::>Object B
```

In this case, C should clear the weak references as well to be safe, but could get away without doing so.

Which way is better? They're both basically equivalent. I think that using retained references is a bit safer, both in terms of continuing to work correctly if you change the object graph later, and in being more resistant to mistakes in the code.

**`NSThread` and `NSTimer`**  
 `NSThread` and `NSTimer` are common causes of retain cycles. It's not unusual to write code like this:

```
    - (id)init
    {
        ...
        _timer = [[NSTimer scheduledTimerWithTimeInterval: 0.1 target: self selector: @selector(whatever) userInfo: nil repeats: YES] retain];
        ...
    }
    
    - (void)dealloc
    {
        [_timer invalidate];
        [_timer release];
        [super dealloc];
    }
```

There's a retain cycle here! This object retains the timer, and the timer retains its target. And note that you can't fix this by not retaining

. The run loop will also retain the timer, and won't release it untill the call to

. This acts as a second retained reference to the timer, causing what is essentially a cycle even without the explicit retained reference.

This exact same problem also happens with an `NSThread`, when specifying `self` as the target, and then shutting down the thread in `dealloc`. The `dealloc` method will never run, so the thread will never be shut down.

There are two ways to deal with this problem. One is to force explicit invalidation, and one is to split your code into two classes.

An `NSTimer` won't necessarily be destroyed when you release your final reference to it. As long as the timer is active, the runloop keeps a reference to it. To destroy a repeating timer, you can't just release all of your references to it, you have to explicitly invalidate it.

You can borrow this concept for your own class. Just expose your own `invalidate` method, and use that to destroy the timer:

```
    - (void)invalidate
    {
        [_timer invalidate];
        [_timer release];
        _timer = nil;
    }
```

Of course, this leaks implementation details up into your interface, but forcing clients to explicitly declare when they're done with your object isn't always bad.

The other way is to split your code into two classes. You have a shell class which is exposed to the outside world, and which manages the thread or timer. Then you have an implementation class which is the target of the thread or timer, and which does most of the actual work:

```
    @implementation MyClassImpl
    
    - (id)init
    {
        ...
        _timer = [[NSTimer scheduledTimerWithTimeInterval: 0.1 target: self selector: @selector(_timerAction) userInfo: nil repeats: YES] retain];
        ...
    }
    
    - (void)invalidate
    {
        [_timer invalidate];
        [_timer release];
        _timer = nil;
    }
    
    - (void)doThingy
    {
        // do stuff here
    }
    
    - (void)_timerAction
    {
        // periodic code here
    }
    
    @end
```

```
    @implementation MyClass
    
    - (id)init
    {
        ...
        _impl = [[MyClassImpl alloc] init];
        ...
    }
    
    - (void)dealloc
    {
        [_impl invalidate];
        [_impl release];
        
        [super dealloc];
    }
    
    - (void)doThingy
    {
        // just pass it on to the "real" code
        [_impl doThingy];
    }
    
    @end
```

By splitting the implementation from the interface, you avoid the retain cycle. In effect,

becomes the common parent object, with

and

as the sub-objects. The parent then manually breaks the retain cycle between the sub-objects when it's destroyed. Externally, the parent preserves the normal retain/release semantics, with no need for explicit invalidation.

**Blocks**  
 Because blocks retain the objects they reference, they're another excellent candidate for a retain cycle. Consider this code:

```
    - (id)init
    {
        ...
        _observerObj = [[NSNotificationCenter defaultCenter] addObserverForName: ... queue: [NSOperationQueue mainQueue] usingBlock: ^(NSNotification *note) {
            [self doSomethingWith: note];
        }];
        [_observerObj retain];
        ...
    }
    
    - (void)dealloc
    {
        [[NSNotificationCenter defaultCenter] removeObserver: _observerObj];
        [_observerObj release];
        [super dealloc];
    }
```

Because the notification block references

, the block will retain

. The result is a subtle retain cycle. This can happen even if you don't directly reference

; simply referencing an instance variable will indirectly reference

, which will cause the block to retain it.

The solutions used for `NSTimer` and `NSThread` will work here as well: either add explicit invalidation to the class's API, or break the class into two pieces.

There's a blocks-specific solution that you can use as well, which is to refer to `self` through a variable declared `__block`, which will not be retained:

```
        __block MyClass *blockSelf = self;
        _observerObj = [[NSNotificationCenter defaultCenter] addObserverForName: ... queue: [NSOperationQueue mainQueue] usingBlock: ^(NSNotification *note) {
            [blockSelf doSomethingWith: note];
        }];
```

This avoids the cycle, because

is not retained. Be careful if you do this to avoid referring to instance variables directly, as those will still reference the original

. If you need to access an instance variable, explicitly indirect through

by doing

.

**Finding Cycles**  
 For the most part, standard leak finding techniques will work fine for finding retain cycles that cause a leak. Instruments is a good way to find them, both the ObjectAlloc instrument and the Leaks instrument. If you have a cycle that's hard to figure out, its ability to track `retain` and `release` calls to each object can help a lot.

If you prefer the command line, or just need text that's easier to search through, the `leaks` command-line tool is also handy.

When hunting for cycles, note that leaks tools won't always find a cycle if there's an external reference into the cycle. For example, consider a cycle involving an `NSTimer`. There's a reference from the runloop to the timer, and from the timer to your object, so they're both reachable. Both the Leaks instrument and the `leaks` tool will not consider this to be a leak. However, if they're doing nothing and build up without end, then it still is a leak, even if they're technically reachable. The ObjectAlloc tool will show this buildup even though the other tools won't identify the leak.

**Conclusion**  
 Retain cycles are an unfortunate wart on Cocoa's memory management system. However, with some care, they can be avoided or fixed with a minimum of pain, with small changes to your object hierarchy. Pay extra attention to `NSTimer` and `NSThread` (but don't ignore other code!), then either eliminate the cycle or add code that explicitly breaks it.

That's it for this week. Come back in another seven days for the next Friday Q&A. As always, Friday Q&A is driven by reader submissions. If you have an idea for a topic that you'd like to see covered here, please [send it in](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
