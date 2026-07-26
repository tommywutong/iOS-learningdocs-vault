---
title: 'A drop-in fix for the problems with NSHost | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/11/drop-in-fix-for-problems-with-nshost.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:e5c34770ac1f919c'
translated: false
---

> 原文：[A drop-in fix for the problems with NSHost | Cocoa with Love](https://www.cocoawithlove.com/2009/11/drop-in-fix-for-problems-with-nshost.html)　·　Cocoa with Love (Matt Gallagher)

As pointed out by Mike Ash in his recent [Friday Q&A 2009-11-13: Dangerous Cocoa Calls](http://mikeash.com/?page=pyblog/friday-qa-2009-11-13-dangerous-cocoa-calls.html), `NSHost` is not thread-safe for use outside of the main thread and due to potentially slow, synchronous network access is not really suitable for use on the main thread either. Fortunately, in Cocoa there are often ways to transparently fix classes that don't work as they should. In this post, I'll show you how you can transparently patch `NSHost` using a drop-in solution and provide a non-blocking solution for `NSHost` lookups.

## NSHost

`NSHost` is a class with a simple API that fetches the names or addresses of an internet host. You can use it to perform DNS lookups but one of the primary uses is to get the name and address of the current host.

All calls to `NSHost` are synchronous — they block until the response is fetched. If a network error occurs, this could result in a 60 second delay before a timeout response occurs — definitely not something you want to do in your main thread.

Unfortunately, according to [Cocoa's Thread Safety Summary](http://developer.apple.com/Mac/library/documentation/Cocoa/Conceptual/Multithreading/ThreadSafetySummary/ThreadSafetySummary.html), `NSHost` is not thread-safe — so we can't simply pass the functionality off to another thread.

Does this mean you must revert to `NSHost`'s CoreFoundation equivalent, `CFHost`, which is explicitly thread-safe? Not necessarily.

## The problems we need to fix

It is not the `NSHost` objects themselves that are the problem. `NSHost` objects are immutable once allocated and immutable objects are implicitly thread-safe for most purposes.

The problem is the cache of `NSHost` objects maintained internally by `NSHost` when any of the lookups are called — access to this cache is unprotected from the perils of threading.

In addition to this, we need to be able to perform `NSHost` lookups asynchronously.

## Design of the solution

The key consideration in these changes will be a totally drop-in solution — `NSHost` will immediately and transparently become thread-safe. No further code will be required.

The solution to the threading problem will be to create a corresponding category method for every class method of `NSHost` which wraps all calls to `NSHost` in a `@synchronized` section and then in the `load` method for the category, swizzle each of these corresponding methods into the place of the original method.

The asynchronous invocations can then be handled like any other asynchronous operation — by spawning a new thread which will call back when complete.

## Swizzling alternate implementations

If you don't know what I meant by "swizzle", what we need to do is replace the existing implementations of the `NSHost` class methods with our own implementations. The code for doing this is as follows:

```objc
static void SwizzleClassMethods(Class class, SEL firstSelector, SEL secondSelector)
{
    Method firstMethod = class_getClassMethod(class, firstSelector);
    Method secondMethod = class_getClassMethod(class, secondSelector);
    if (!firstMethod || !secondMethod)
    {
        NSLog(@"Unable to swizzle class methods for selectors %@ and %@ on class %@",
            NSStringFromSelector(firstSelector),
            NSStringFromSelector(secondSelector),
            NSStringFromClass(class));
        return;
    }
    
    method_exchangeImplementations(firstMethod, secondMethod);
}
```

Then, in the `load` method for our category...

```objc
@implementation NSHost (ThreadSafety)

+ (void)load
{
    SwizzleClassMethods(self, @selector(currentHost), @selector(threadSafeCurrentHost));
    SwizzleClassMethods(self, @selector(hostWithName:), @selector(threadSafeHostWithName:));
    SwizzleClassMethods(self, @selector(hostWithAddress:), @selector(threadSafeHostWithAddress:));
    SwizzleClassMethods(self, @selector(isHostCacheEnabled), @selector(threadSafeIsHostCacheEnabled));
    SwizzleClassMethods(self, @selector(setHostCacheEnabled:), @selector(threadSafeSetHostCacheEnabled:));
    SwizzleClassMethods(self, @selector(flushHostCache), @selector(threadSafeFlushHostCache));
    SwizzleClassMethods(self, @selector(_fixNSHostLeak), @selector(threadSafe_fixNSHostLeak));
}

// category continues...
```

What this does is swaps in our new implementations, (e.g. `threadSafeCurrentHost`) in place of Apple's original implementation (e.g. `currentHost`). Once this is done, any call to `currentHost` will result in our new code getting executed. Similarly, the original code that we replaced is now reachable by calling `threadSafeCurrentHost`.

The implementation of each of these thread-safe methods takes the form:

```objc
+ (id)threadSafeCurrentHost
{
    @synchronized(self)
    {
        return [self threadSafeCurrentHost];
    }
}
```

This may look like the method is just calling itself but remember, after swizzling, the call to `threadSafeCurrentHost` will actually invoke the original `currentHost` code. So this method is actually running the original code but inside a `@synchronized` section to maintain thread safety.

## Asynchronous lookup

The best way to perform an asynchronous lookup, now that `NSHost` will work in a thread-safe manner, is simply to perform the lookup in an `NSOperation` and have that operation call back when done.

To do this, the ThreadSafety category also adds the methods:

- `currentHostInBackgroundForReceiver:selector:`
- `hostWithName:inBackgroundForReceiver:selector:`
- `hostWithAddress:inBackgroundForReceiver:selector:`

to perform lookups and call back when done. These methods take the following form:

```objc
+ (void)hostWithName:(NSString *)name
    inBackgroundForReceiver:(id)receiver
    selector:(SEL)receiverSelector
{
    [[self hostLookupQueue]
        addOperation:
            [[HostLookupOperation alloc]
                initWithReceiver:receiver
                receiverSelector:receiverSelector
                receivingThread:[NSThread currentThread]
                lookupSelector:@selector(hostWithName:)
                lookupParameter:name]];
}
```

and the implementation of the `HostLookupOperation`'s `main` method is extremely simple:

```objc
- (void)main
{
    [receiver
        performSelector:receiverSelector
        onThread:receivingThread
        withObject:[NSHost performSelector:lookupSelector withObject:parameter]
        waitUntilDone:NO];
}
```

## Conclusion

> You can [download the complete code for `NSHost+ThreadedAdditions`](https://www.cocoawithlove.com/assets/objc-era/NSHost_ThreadedAdditions.zip) (3kB).

The main advantage of this approach shown here is that you only need to add the files to your project — you do not need to add or change any other code to make this work.

These additions provide reasonably good thread safety for `NSHost` as they channel all use of the class through the thread-safe wrapping methods. The limitation to this is that Apple could add further methods in the future that circumvent the `@synchonized` sections we've added and the thread safety would be breached until swizzled methods were added for these new methods.

On the immutability of `NSHost` instances — technically, the private instance variables `names` and `addresses` of `NSHost` are allocated mutable but experimentally, I have verified that they are never mutated (in fact, there are no methods on `NSHost` that would do this). However, `localizedName`, available in Mac OS X 10.6, uses data from outside `NSHost` so might not be thread-safe.

In reality, you can avoid all of this code and simply use the `CFHost` API to achieve the same benefits. This `ThreadedAdditions` category for `NSHost` is an effort to continue using the simpler API of `NSHost` and at the same time, to demonstrate that just because Apple's implementation of something is not thread-safe in its internal implementation, doesn't mean you can't make it thread-safe in the greater context of your whole program.
