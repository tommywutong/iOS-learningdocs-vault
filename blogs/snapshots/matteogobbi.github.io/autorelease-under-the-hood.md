---
title: Autorelease - Under the Hood
source_url: 'http://matteogobbi.github.io/blog/2014/09/28/autorelease-under-the-hood/'
source_domain: matteogobbi.github.io
source_group: single-site
original_language: en
published: 2014-09-28
archived_at: 2026-07-27
content_hash: 'sha256:d9c305bf83e0993e'
plan_ref: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 3｜AutoreleasePool 放回事件循环中理解（对应 W4-01）
plan_week: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期
plan_day: Day 3｜AutoreleasePool 放回事件循环中理解（对应 W4-01）
container: //article
container_source: guess
---

> 原文：[Autorelease - Under the Hood](http://matteogobbi.github.io/blog/2014/09/28/autorelease-under-the-hood/)

# Autorelease - Under the Hood

written  in  [arc](http://matteogobbi.github.io/blog/categories/arc/), [ios](http://matteogobbi.github.io/blog/categories/ios/), [mrc](http://matteogobbi.github.io/blog/categories/mrc/), [objective-c](http://matteogobbi.github.io/blog/categories/objective-c/), [underthehood](http://matteogobbi.github.io/blog/categories/underthehood/)

Since this is an argument less touched but much important, I decided to write an article to organize the informations and explain how `autorelease`, or better **autorelease pool** works.

The main goal of this article is not to explain the base of what is an **autorelease pool** and when `autorelease` should be used, but anyway, this is really important to understand these concepts before proceeding. For this reason, the first paragraph will be dedicated to explain them. Experts developers, can safely skip it if they want.

## What and when

As the [Apple documentation](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmAutoreleasePools.html) says:

> Autorelease pool blocks provide a mechanism whereby you can relinquish ownership of an object, but avoid the possibility of it being deallocated immediately (such as when you return an object from a method). Typically, you don’t need to create your own autorelease pool blocks, but there are some situations in which either you must or it is beneficial to do so.

Let’s look at a couple of examples:

Before **ARC**, there was our much less friend called **[MRC](https://developer.apple.com/library/ios/releasenotes/objectivec/rn-transitioningtoarc/introduction/introduction.html)**, which stands for **Manual Reference Counting**. Even if today it is still present on XCode, it is not longer used and the “bad job” of using `retain`, `release` and `autorelease`, is left to the compiler. But let’s think for a while to be in a MRC environment and to have these methods:

```
/* MGClassA */

- (void)method

{

    MGClassB *objB = [MGClassB new];

    NSObject *newObj = [objB getAnObject];

    //do something..

    [objB release];

}

/* MGClassB */

- (NSObject *)getAnObject

{

    NSObject *newObj = [NSObject new];

    return newObj;

}
```

in the first method, an object typed `MGClassB` is allocated and temporary retained from the object of type `MGClassA`; then `objB` is asked to allocate, initialize and return a new object. So at this point we have this situation:

`objA` —**retains**—\> `objB`

`objB` —**retains**—\> `newObj`

please note that `objA` is not calling `retain` after having obtained `newObj`, so it has no ownership and `newObj` still has a retain count equals to 1.  
 At this point, `method` finishes and releases `objB`, which is not referenced anymore and it is still retaining `newObj`. This object will therefore remain allocated in memory generating the **memory leak**. From [Apple documentation](https://developer.apple.com/library/ios/documentation/performance/conceptual/managingmemory/articles/FindingLeaks.html)

> Memory leaks are blocks of allocated memory that the program no longer references.

This means that being `newObj` just pointed from `objB`, but being `objB` NOT pointed from anyone, it will be no longer possible have a reference to release `newObj` which will remain allocated until the application will be not closed.

How can we solve this issue? `autorelease`, keep the object alive for a period of time. Then, the object is automatically released, avoiding so, a memory leak:

```
/* MGClassB */

- (NSObject *)getAnObject

{

    NSObject *newObj = [NSObject new];

    return [newObj autorelease];

}
```

In the next paragraph we will go in depth explaining why in this example doesn’t appear an **autorelease pool**, but before, let’s go to have a look to another situation where you need to create that.  
 An **autorelease pool** is a container where autoreleased objects are placed. When the pool is drained, every object in the container is released. This could be very useful in a situation like this:

```
- (NSObject *)method

{

    for (int i = 0; i < 10000; i++) {

        NSAutoreleasePool *myPool = [NSAutoreleasePool new];

        /* Do something that creates a lot of temporary objects autoreleased. */

        [myPool drain];

    }

}
```

that in the modern **Objective-C** becomes:

```
- (NSObject *)method

{

    for (int i = 0; i < 10000; i++) {

        @autoreleasepool {

            /* Do something that creates a lot of temporary objects autoreleased. */

        }

    }

}
```

This cyle, is executed 10.000 times. You maybe don’t know how many objects will be allocated in your code, but without using `@autoreleasepool`, the memory would be filled with a lot of objects allocations, that instead at the end of each cycle would be no longer used. This could have an impact on the the performance of the app and could cause risk of memory warnings.  
 Using `@autoreleasepool`, objects would be instead released at the end of the autorelease’s scope.

Note that with ARC, you can’t call `release` or `autorelease`, so having `@autoreleasepool` sometime is even more useful.

## Under the hood

We know that an object which is autoreleased, goes in an autorelease pool, but keep in mind this example:

```
/* MGClassB */

- (NSObject *)getAnObject

{

    NSObject *newObj = [NSObject new];

    return [newObj autorelease];

}
```

the question is: **what autorelease pool does `newObj` go in?**  
 The answer is easy, and it is in the file named `main.m` in the folder `Supporting Files` of any XCode project:

```
int main(int argc, char * argv[]) {

    @autoreleasepool {

        return UIApplicationMain(argc, argv, nil, NSStringFromClass([AppDelegate class]));

    }

}
```

Yes, the `main` method **has the first autorelease pool** of the entire project. So in our example, `newObj` goes in the main autorelease pool, which is drained when the current [Run Loop](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/Multithreading/RunLoopManagement/RunLoopManagement.html) terminates.  
 We are obviously supposing to be in the main thread, but however, in general, **every thread has his main autorelease pool**.

So now that we know the theory, the next question is: **where does the autoreleased object found the pointer to the correct autorelease pool?** As the [Apple Documentation](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmAutoreleasePools.html) says:

> Each thread in a Cocoa application maintains its own stack of autorelease pool blocks.

and this is. Simple as that!  
 So basically when the object call `autorelease`, it does something like:

```
- (void)autorelease

{

    AutoreleasePool *pool = /* Get the most recet autorelease pool from the stack */

    [pool add:self];

}
```

Indeed, since autorelease’s pool can be several and nested, **there MUST be a stack**.  
 This is of course an high level code to make it easier to understand, but the open source Apple’s implementation of autorelease is [here](http://opensource.apple.com/source/objc4/objc4-493.9/runtime/objc-arr.mm).

The last thing to stress, regards the autorelease pool’s container.  
 Indeed, **what datastructure does an autorelease pool use to store objects to release?**  
 Let’s try:

- `NSMutableArray`: no, because it would retain the object calling `-addObject`. This would make the autorelease vain;
- `NSMutableDictionary`: no, for the same reason of the previous;
- `NSMutableSet`: no, for the same reason of the previous and because doesn’t accept repeated object.

So what does it use?  
 Easy: any data structure which **doesn’t retains the object** and that **accepts repeated objects**, like for example `NSPointerArray` with `weak` objects references, `LinkedList`, etc.

## Conclusion

I hope that this article has cleared every doubt about the `autorelease` method and the **autorelease pool**. Even if the management of an autorelease pool will be always a system’s responsibility, it is very important to understand how it works.

**Follow me on [Twitter](https://twitter.com/matteo_gobbi)**!

Cheers!

---

# Comments
