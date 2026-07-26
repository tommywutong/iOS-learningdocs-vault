---
title: 'Friday Q&A 2010-02-26: Futures'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-02-26-futures.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e30d841d0f6ed198'
translated: false
---

> 原文：[Friday Q&A 2010-02-26: Futures](https://www.mikeash.com/pyblog/friday-qa-2010-02-26-futures.html)　·　mikeash.com Friday Q&A

Posted at 2010-02-26 18:19 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-03-05: Compound Futures](https://www.mikeash.com/pyblog/friday-qa-2010-03-05-compound-futures.html)  
Previous article: [Friday Q&A 2010-02-19: Character Encodings](https://www.mikeash.com/pyblog/friday-qa-2010-02-19-character-encodings.html)  
Tags: [blocks](https://www.mikeash.com/pyblog/?tag=blocks) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [futures](https://www.mikeash.com/pyblog/?tag=futures)

Friday Q&A 2010-02-26: Futures

by [Mike Ash](https://www.mikeash.com/)

**Futures**  
 A future is, in short, an object which hides a calculation. When a future is _resolved_, the resolution blocks until the calculation has finished. My code involves _implicit_ futures: a future is a proxy for the calculated result and, when messaged, transparently resolves the future and then passes the message on to the result. To code which uses it, a future is essentially indistinguishable from the object that it represents.

In Objective-C, it's natural to represent the calculation using a block. Futures are created by simply calling a function which takes a block representing the calculation. They return a [proxy object](https://www.mikeash.com/pyblog/friday-qa-2009-03-27-objective-c-message-forwarding.html) which captures messages sent to that object and resolves the future as needed. My code has two kinds of futures.

_Background futures_ begin the calculation immediately on a background thread as soon as the future is created. When the future is resolved, if the calculation is not yet complete, the call blocks until it's done. If the calculation finishes first, then resolution completes immediately. Background futures provide a way to write parallel code without needing to worry about details of synchronization. For example, if you're going to pass an `NSData` to another object that won't actually use that `NSData` for a while, you can use a background future to allow other code to run concurrently with the disk access with very little effort:

```
    NSString *filename = ...;
    NSData *future = MABackgroundFuture(^{ return [NSData dataWithContentsOfFile: filename]; });
    [object doSomethingLaterWithData: future];
```

do not begin the calculation until the future is resolved. If the future is never resolved, then the calculation is never performed. Lazy futures make it possible to provide an object immediately to an API which may or may not actually make use of it, and not pay the cost of creating that object until and unless it's actually requested. For example, you could use a lazy future to defer the reading of a file until and unless it's needed:

```
    NSString *filename = ...;
    NSData *future = MALazyFuture(^{ return [NSData dataWithContentsOfFile: filename]; });
    [object doSomethingOrNotWithData: future];
```

**Getting the Code**  
 As usual, I'm just going to cover the highlights of the code here, but the library is available from my subversion repository:

```
    svn co http://mikeash.com/svn/MAFuture/
```

Or just click on the hyperlink above to browse it.

**A Custom Proxy Class**  
 When building object proxies, Cocoa provides a convenient root proxy class to subclass in the form of `NSProxy`. The idea is that `NSProxy` provides a minimal implementation, which allows almost all messages to be captured and proxied.

Unfortunately, `NSProxy` doesn't quite live up to its promise. It implements a whole bunch of unnecessary methods, including important ones like `-hash` and `-isEqual:`. This is a problem because I don't want `NSProxy`'s implementations of these, I want the implementations in the proxied object. To make that happen, I'd have to either manually override these methods, or play runtime tricks to make them hit the forwarding path. Neither alternative is particularly appealing.

Instead, I chose a third route: implement my own proxy class. `MAProxy` is a true minimalistic proxy class. It implements memory management methods and `-isProxy`. It also implements `+initialize`, which the runtime requires to exist in every class. The [header](https://www.mikeash.com/svn/MAFuture/MAProxy.h) is really basic and the [implementation](https://www.mikeash.com/svn/MAFuture/MAProxy.m) nearly as simple. The only tricky stuff at work is the inline reference count using atomic functions for thread safety.

**Future Basics**  
 To make implementing futures easier, I created a base class called `MABaseFuture` which provides common facilities. A basic future needs to be able to store a value, to store whether the future has been resolved yet or not, and a condition variable to make it all thread safe:

```
    @interface MABaseFuture : MAProxy
    {
        id _value;
        NSCondition *_lock;
        BOOL _resolved;
    }
```

For code, the class obviously needs creation/destruction methods:

```
    - (id)init
    {
        _lock = [[NSCondition alloc] init];
        return self;
    }
    
    - (void)dealloc
    {
        [_value release];
        [_lock release];
        
        [super dealloc];
    }
```

Then, accessors for the future's value. There are both locked and unlocked setters because a subclass may want to set the future's value after already acquiring the lock:

```
    - (void)setFutureValue: (id)value
    {
        [_lock lock];
        [self setFutureValueUnlocked: value];
        [_lock unlock];
    }
    
    - (id)futureValue
    {
        // skip the usual retain/autorelease dance here
        // because the setter is never called more than
        // once, thus value lifetime is same as future
        // lifetime
        [_lock lock];
        id value = _value;
        [_lock unlock];
        return value;
    }
    
    - (void)setFutureValueUnlocked: (id)value
    {
        [value retain];
        [_value release];
        _value = value;
        _resolved = YES;
        [_lock broadcast];
    }
```

A quick getter to see if the future has been resolved (which relies on the subclass to manually acquire the lock first):

```
    - (BOOL)futureHasResolved
    {
        return _resolved;
    }
```

Then the one part that's a bit interesting, a method to wait for the future to resolve, handy for implementing background futures:

```
    - (id)waitForFutureResolution
    {
        [_lock lock];
        while(!_resolved)
            [_lock wait];
        [_lock unlock];
        return _value;
    }
```

This class also has a

method which is abstract. Subclasses must override it and do whatever they need to do:

```
    - (id)resolveFuture
    {
        NSLog(@"-[MABaseFuture resolveFuture] called, this should never happen! Did you forget to implement -[%@ resolveFuture]?", NSStringFromClass(isa));
        NSParameterAssert(0);
        return nil;
    }
```

Actually there are two interesting parts to this class, and the second one is here. It's an implementation of

. Normally this implementation wouldn't be necessary, as the proxy mechanism will proxy that method just fine. The problem arises in the implementation of

, part of the

toll-free bridging

, and with other bridged classes. That code checks the class of the other object, and if it's an

as well, hits a fast path that depends on internal implementation details of

. If

returns

when the object is really a proxy, that code fails and the two strings will never compare as equal, even when they are.

The fix is simple, if bizarre. Get the real class, check to see if it starts with `NSCF`, and return the superclass if it does. If the real class is `NSCFString`, this will return `NSString`, the code goes through the general equality path, and all is well. This is the implementation of `-class`:

```
    - (Class)class
    {
        Class c = [[self resolveFuture] class];
        if([NSStringFromClass(c) hasPrefix: @"NSCF"])
            return [c superclass];
        else
            return c;
    }
```

And that's all there is to

.

**Deepening the Hierarchy**  
 Building on `MABaseFuture`, I want to then create a tree of subclasses. First, `_MASimpleFuture` will contain some more common facilities for "simple" futures (futures which immediately resolve when accessed), then I'll create two subclasses of that for background and lazy futures.

`_MASimpleFuture` is very, well, simple. It implements `-forwardingTargetForSelector:` to resolve the future and return the object that resulted:

```
    - (id)forwardingTargetForSelector: (SEL)sel
    {
        LOG(@"%p forwardingTargetForSelector: %@, resolving future", self, NSStringFromSelector(sel));
        return [self resolveFuture];
    }
```

Using this class, subclasses just need to provide an initializer method and override

, and they get forwarding for free.

**Forwarding to `nil`**  
 There's a bad corner case here, which happens if the future returns `nil`. Messaging `nil` is no problem, but `forwardingTargetForSelector:` takes a `nil` return as meaning that there is no forwarding target, and the runtime should start on the slow forwarding path instead.

And here there's a major problem, because the slow forwarding path requires a method signature, but it's impossible to get one from `nil`. I've partially solved this in an extremely brute-force fashion by writing a class called `MAMethodSignatureCache`, which will check every class registered with the runtime for a selector and return whatever method signature it can dig up. (I didn't write it solely for this, there's more handy stuff to do with it in another post.) I can use this class to implement the slow forwarding path of `_MASimpleFuture`to return zero:

```
    - (NSMethodSignature *)methodSignatureForSelector: (SEL)sel
    {
        return [[MAMethodSignatureCache sharedCache] cachedMethodSignatureForSelector: sel];
    }
    
    - (void)forwardInvocation: (NSInvocation *)inv
    {
        // this gets hit if the future resolves to nil
        // zero-fill the return value
        char returnValue[[[inv methodSignature] methodReturnLength]];
        bzero(returnValue, sizeof(returnValue));
        [inv setReturnValue: returnValue];
    }
```

The problem comes when there are multiple method signatures for a given selector, which can easily happen if two unrelated classes implement methods with the same name. In that case, there's no way to know which one is meant, and this whole approach falls apart. Unfortunately, with the way the runtime is currently written, there's no generalized way to "forward to

".

If that's not enough, there's another problem with futures that return `nil`. This problem is quite simple: although the futured value may be nil, the future object itself is not nil. Any code which checks the object pointer for nil before using it will fail in weird ways. Imagine this code using an NSData:

```
    NSData *data = ...;
    if(data)
        [self doSomethingWithBytes: [data bytes]];
```

If

is a future that resolves to

, then the

check will pass, but

will return

, causing a crash.

Because of these two problems, you should avoid futuring any computation which might return `nil`.

**Background Futures**  
 To implement background futures, I created a class called `_MABackgroundBlockFuture`. Since computation is supposed to begin immediately in the background, I create an initializer which takes the block to compute, and uses Grand Central Dispatch to execute it in the background. Once the computation is finished, it simply calls `-setFutureValue:` to set the computed value and mark the future as resolved:

```
    - (id)initWithBlock: (id (^)(void))block
    {
        if((self = [self init]))
        {
            dispatch_async(dispatch_get_global_queue(0, 0), ^{
                [self setFutureValue: block()];
            });
        }
        return self;
    }
```

The implementation of

is then extremely simple. Since the future is already being computed, it just waits for it to finish, then returns the result:

```
    - (id)resolveFuture
    {
        return [self waitForFutureResolution];
    }
```

I created

to implement lazy futures. A lazy future doesn't begin computation right away, so it just needs to store a copy of the block when initialized, and release it when deallocating:

```
    - (id)initWithBlock: (id (^)(void))block
    {
        if((self = [self init]))
        {
            _block = [block copy];
        }
        return self;
    }
    
    - (void)dealloc
    {
        [_block release];
        [super dealloc];
    }
```

Resolution is straightforward as well. Acquire the lock. If the future hasn't been resolved yet, then call the block and set the future's value from its result:

```
    - (id)resolveFuture
    {
        [_lock lock];
        if(![self futureHasResolved])
        {
            [self setFutureValueUnlocked: _block()];
            [_block release];
            _block = nil;
        }
        [_lock unlock];
        return _value;
    }
```

This code now has all the functionality that's needed, but I want a couple of wrappers to make it nicer to use:

```
    id MABackgroundFuture(id (^block)(void))
    {
        return [[[_MABackgroundBlockFuture alloc] initWithBlock: block] autorelease];
    }
    
    id MALazyFuture(id (^block)(void))
    {
        return [[[_MALazyBlockFuture alloc] initWithBlock: block] autorelease];
    }
```

Because these functions return

, the compiler won't be able to catch mistakes like:

```
    NSArray *array = MALazyFuture(^{ return [self somethingThatReturnsNSString]; });
```

Gcc will also reject this because the block types don't match exactly (returning

instead of

) even though they're completely compatible.

I worked around both of these problems by using two really scary-looking macros:

```
    #define MABackgroundFuture(...) ((__typeof((__VA_ARGS__)()))MABackgroundFuture((id (^)(void))(__VA_ARGS__)))
    #define MALazyFuture(...) ((__typeof((__VA_ARGS__)()))MALazyFuture((id (^)(void))(__VA_ARGS__)))
```

Let's unpack these a bit.

First, they take variable arguments, because block syntax doesn't play completely nice with the preprocessor. If you write a block which contains a comma that isn't inside parentheses (which can be written completely legally), the preprocessor won't realize that it's inside a block, and will use that as an argument separator. The preprocessor will therefore see two (or more) arguments, and a single-argument macro will fail. By making the macros take `...`, that problem is avoided. Thus, the block parameter is represented in the macro by `__VA_ARGS__`.

`__typeof` is a gcc language extension which pretty much does what it says. You give it an expression, and it gives you the type of the expression.

The argument to `__typeof` is `(__VA_ARGS__)()`. Remember that `__VA_ARGS__` is the block being passed to the macro. This expression calls the block. But since it's an argument being passed to `__typeof`, which is a compile-time construct, it doesn't _really_ call the block. Put the two together, and you get the return type of the block.

Next, the whole `__typeof` combination is wrapped in another set of parentheses and put right before the call through to the real function, which casts the return value of the function.

Finally, the function argument is cast to `id (^)(void)`, because gcc is too stupid to understand that a block which returns `NSString *` is compatible with a block type that returns `id`.

**Potential Uses**  
 Background futures are useful any time you have computation which can happen asynchronously. In essence, you can think of the future as a synchronization mechanism, like a lock, which ensures that the job is completed before the result is used. Because these futures automatically forward requests, you can pass the future into code that doesn't know what it is, and it will be resolved automatically.

For example, let's say you're building a composite image by loading one image from disk, shrinking another image that already exists, and then putting the result into an image view:

```
    NSImage *image1 = [[NSImage alloc] initWithContentsOfFile: ...];
    NSImage *image2 = [self shrinkImage: existingImage];
    
    NSImage *composite = [[NSImage alloc] initWithSize: ...];
    [composite lockFocus];
    [image1 drawAtPoint: NSZeroPoint fromRect: NSZeroRect operation: NSCompositeSourceOver fraction: 1.0];
    [image2 drawAtPoint: NSZeroPoint fromRect: NSZeroRect operation: NSCompositeSourceOver fraction: 1.0];
    [composite unlockFocus];
    
    [imageView setImage: composite];
```

By futuring all of the images, you allow the work for

and

to run in parallel, and there's at least the possibility that some of the work for

could run in parallel with main thread work too:

```
    NSImage *image1 = MABackgroundFuture(^{ return [[[NSImage alloc] initWithContentsOfFile: ...] autorelease]; });
    NSImage *image2 = MABackgroundFuture(^{ return [self shrinkImage: existingImage]; });
    
    NSImage *composite = MABackgroundFuture(^{
        NSImage *img = [[NSImage alloc] initWithSize: ...];
        [img lockFocus];
        [image1 drawAtPoint: NSZeroPoint fromRect: NSZeroRect operation: NSCompositeSourceOver fraction: 1.0];
        [image2 drawAtPoint: NSZeroPoint fromRect: NSZeroRect operation: NSCompositeSourceOver fraction: 1.0];
        [img unlockFocus];
        return [img autorelease];
    });
    
    [imageView setImage: composite];
```

Quick and easy parallel code, and

never has to know that it's getting a proxy instead of the real thing.

Lazy futures are useful any time you have objects that may never be needed, or simply may not be needed for a long time. Even if the object is used, deferring computation can spread out the load and improve responsiveness and startup times.

As an example, imagine some code which sets up a bunch of data file contents to be accessed through a dictionary:

```
    gGlobalDictionary = [[NSDictionary alloc] initWithObjectsAndKeys:
        [NSData dataWithContentsOfFile: ...], @"dataFile",
        [NSData dataWithContentsOfFile: ...], @"anotherDataFile",
        [NSData dataWithContentsOfFile: ...], @"moreDataFile",
        [NSData dataWithContentsOfFile: ...], @"fourthDataFile",
        nil];
```

You could load these files lazily by splitting them out, providing an accessor for each one, etc., but using lazy futures requires minimal changes and most of the same benefits:

```
    gGlobalDictionary = [[NSDictionary alloc] initWithObjectsAndKeys:
        MALazyFuture(^{ return [NSData dataWithContentsOfFile: ...] }), @"dataFile",
        MALazyFuture(^{ return [NSData dataWithContentsOfFile: ...] }), @"anotherDataFile",
        MALazyFuture(^{ return [NSData dataWithContentsOfFile: ...] }), @"moreDataFile",
        MALazyFuture(^{ return [NSData dataWithContentsOfFile: ...] }), @"fourthDataFile",
        nil];
```

Many other possibilities abound for parallel and lazy computation through the use of futures.

**Conclusion**  
 Futures are an interesting technique which can make it much easier to use lazy evaluation and parallel computation. Futures make it easy to use lazy evaluation even when you have no control over (or no desire to change) the code that will eventually use the value in question. They also make for a handy synchronization mechanism for performing heterogeneous parallel computations. The dynamic nature of Objective-C makes it possible to mostly hide the existence of the future from code that isn't involved in creating it.

That's it for this week's edition. Come back in a week for the next one. As always, Friday Q&A is driven by user suggestions, so if you have a topic that you'd like to see covered here, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
