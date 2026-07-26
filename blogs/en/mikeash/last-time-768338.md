---
title: Last time
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-05-18-a-tour-of-plweakcompatibility-part-i.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3d1464909cd47821'
translated: false
---

> 原文：[Last time](https://www.mikeash.com/pyblog/friday-qa-2012-05-18-a-tour-of-plweakcompatibility-part-i.html)　·　mikeash.com Friday Q&A

Posted at 2012-05-18 16:53 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-06-01: A Tour of PLWeakCompatibility: Part II](https://www.mikeash.com/pyblog/friday-qa-2012-06-01-a-tour-of-plweakcompatibility-part-ii.html)  
Previous article: [Solving Simulator Bootstrap Errors](https://www.mikeash.com/pyblog/solving-simulator-bootstrap-errors.html)  
Tags: [arc](https://www.mikeash.com/pyblog/?tag=arc) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hack](https://www.mikeash.com/pyblog/?tag=hack) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-05-18: A Tour of PLWeakCompatibility: Part I

by [Mike Ash](https://www.mikeash.com/)

**Motivation**  
ARC is really nice technology to use. It's not quite as nice as a real garbage collector, but it's far nicer to use than manual memory management. However, it's really annoying to use ARC without the `__weak` keyword. The alternative is `__unsafe_unretained`, which gives you a unretained reference which _doesn't_ zero out when the target object is deallocated. If you access such a variable after the target has been destroyed, you'll crash. In contrast, a `__weak` variable automatically becomes `nil` when deallocated, making it impossible (or at least much, much harder) to access a stale pointer.

Over at [Plausible Labs](http://plausible.coop/), we wanted to move a big project over to ARC but needed to maintain compatibility with iOS 4. One possibility for this was to use something like [`MAZeroingWeakRef`](https://github.com/mikeash/MAZeroingWeakRef), an explicit proxy object that manages the zeroing weak reference. Another was to use `__unsafe_unretained`, which is really no more unsafe than old-style unretained references with manual memory management.

We really didn't want any half measures if we could avoid them. Finally we decided to see whether it was possible to trick the compiler into accepting `__weak` on older systems, and providing the necessary runtime code for it to actually work. After some investigation, it turned out that this was not only feasible but actually pretty straightforward, and thus `PLWeakCompatibility` was born.

**The Compiler Side**  
From the compiler's point of view, `__weak` is actually fairly simple. All of the interesting bits are delegated to the runtime, so the compiler just has to emit the right runtime calls at the right time. These runtime functions are listed in the [clang ARC documentation](http://clang.llvm.org/docs/AutomaticReferenceCounting.html), and they are:

```
    void objc_copyWeak(id *dest, id *src);
```

This function copies a weak pointer from one location to another, when the destination doesn't already contain a weak pointer. It would be used for code like:

```
    __weak id weakPtr1 = ...;
    __weak id weakPtr2 = weakPtr1;
```

The next function is:

```
    void objc_destroyWeak(id *object);
```

This unregisters a `__weak` pointer. This would be used when a local `__weak` variable goes out of scope, or in the `dealloc` implementation of a class with `__weak` instance variables.

```
    id objc_initWeak(id *object, id value);
```

This function initializes a `__weak` variable. It would be used for code like:

```
    id strongPtr = ...;
    __weak id weakPtr = strongPtr;
```

Next, we have:

```
    id objc_loadWeak(id *object);
```

This loads the value out of a weak pointer and returns it, after retaining and autoreleasing the value to ensure that it stays alive long enough for the caller to use it. This function would be used anywhere a `__weak` variable is used in an expression.

```
    id objc_loadWeakRetained(id *object);
```

This is just like the previous function, except that it omits the autorelease. This can allow the compiler to emit more efficient code.

```
    void objc_moveWeak(id *dest, id *src);
```

This copies the weak pointer from one location to another. It's much like `objc_copyWeak`, except that it may optionally clear out the source location. Finally, we have:

```
    id objc_storeWeak(id *object, id value);
```

This function stores a new value into a `__weak` variable. It would be used anywhere a `__weak` variable is the target of an assignment.

The astute reader will notice that there are far more functions here than there need to be. In fact, only two of these functions are strictly necessary: `objc_loadWeakRetained` and `objc_storeWeak`. All of the others can be implemented in terms of those two. For example, `objc_destroyWeak` can be implemented as simply `objc_storeWeak(location, nil);`. `objc_initWeak` is just `*location = nil; objc_storeWeak(location, value);`. And in fact the Objective-C runtime implements them like this. Why all the extra functions, then?

It appears to simply be to leave the door open for optimization. While all of these other functions _can_ be implemented in terms of the two primitives, depending on the runtime implementation there may be faster ways to e.g. initialize a `__weak` variable that's known not to have been previously used. Although the runtime isn't taking advantage of this currently, by having the compiler generate more specialized calls, it allows for the possibility in the future.

Since `PLWeakCompatibility` isn't particularly concerned about speed on older platforms, and simply calls through to Apple's implementations on newer platforms, we simply implemented all of the other calls in terms of the two primitives.

**Fooling the Compiler**  
The runtime functions are emitted just like any other function call. That means that if you have a function called `objc_storeWeak` somewhere in your app, the compiler will happily generate code that calls it. It's not explicitly tied to the Objective-C runtime library. However, by default, `clang` refuses to compile any code with `__weak` in it when the deployment target is an OS that doesn't officially support it. Fortunately, it's possible to tell `clang` that the current target really does support `__weak` by adding a pair of compiler flags:

```
    -Xclang -fobjc-runtime-has-weak
```

The second flag tells `clang` that the runtime really does support `__weak`, even when the deployment target indicates otherwise. The first flag is a little hack to sneak the second flag past the top-level compiler driver, which doesn't know about that flag and will ignore it.

With those two flags in place, `clang` accepts `__weak` and emits the appropriate function calls. All that remains is to provide our own implementation of those functions.

**Avoiding ARC**  
The official prototypes for the runtime functions all use `id`. However, this presents a problem for `PLWeakCompatibility`. The goal was to produce a single file which could be dropped into an ARC project to enable `__weak` without much setup. That means that these functions would be compiled using ARC, and using `id` in them would cause ARC to emit all sorts of unwanted retain and release calls.

I settled on using `void *` instead of `id`, hidden behind a convenient typedef:

```
    typedef void *PLObjectPtr;
```

With that in place, the prototypes for the runtime functions look like this:

```
    PLObjectPtr objc_loadWeakRetained(PLObjectPtr *location);
    PLObjectPtr objc_initWeak(PLObjectPtr *addr, PLObjectPtr val);
    void objc_destroyWeak(PLObjectPtr *addr);
    void objc_copyWeak(PLObjectPtr *to, PLObjectPtr *from);
    void objc_moveWeak(PLObjectPtr *to, PLObjectPtr *from);
    PLObjectPtr objc_loadWeak(PLObjectPtr *location);
    PLObjectPtr objc_storeWeak(PLObjectPtr *location, PLObjectPtr obj);
```

Although these prototypes no longer match the official ones, they are still binary compatible, which is all that matters. The compiler isn't looking at these prototypes when it emits the runtime calls, and an `id` can be treated as a `void *` without any trouble.

**Falling Through**  
When native `__weak` support is available, we don't want to preempt it. That means that the first thing all of our functions need to do is check to see whether native support is available, and call through to it instead. For example, the implementation of `objc_loadWeak` would look something like this:

```
    PLObjectPtr objc_loadWeakRetained(PLObjectPtr *location) {
        PLObjectPtr (*fptr)(PLObjectPtr *) = dlsym(RTLD_NEXT, "objc_loadWeakRetained");
        if(fptr != NULL)
            return fptr(location);

        return PLLoadWeakRetained(location);
    }
```

If you're unfamiliar, `dlsym` is a function that can look up symbols at runtime, and `RTLD_NEXT` is a special parameter which tells it to look for the "next" implementation of a particular symbol. In other words, if the caller wasn't present in the app, what symbol would it find then? This essentially tells it to go off and find the original runtime implementation of this function if it exists.

We don't want to call `dlsym` for every single call to this function, since that would be fairly slow. We can speed it up nicely by using `dispatch_once` to only perform the check once. Furthermore, it's a little annoying to have to write out the type of the function a second time when declaring the function pointer, and this is easily solved by using `__typeof__`. With those modifications, the code looks like this:

```
    PLObjectPtr objc_loadWeakRetained(PLObjectPtr *location) {
        static dispatch_once_t fptrOnce
        static __typeof__(&objc_loadWeakRetained) fptr;
        dispatch_once(&fptrOnce, ^{ fptr = dlsym(RTLD_NEXT, "objc_loadWeakRetained"); });
        if(fptr != NULL)
            return fptr(location);

        return PLLoadWeakRetained(location);
    }
```

This is now sufficiently generic to put in a macro to avoid repetition. This macro takes the name of the function and the arguments, and automatically calls through to the original implementation if available:

```
    #define NEXT(name, ...) do { \
            static dispatch_once_t fptrOnce; \
            static __typeof__(&name) fptr; \
            dispatch_once(&fptrOnce, ^{ fptr = dlsym(RTLD_NEXT, #name); });\
            if (fallthroughEnabled && fptr != NULL) \
                return fptr(__VA_ARGS__); \
        } while(0)
```

Note the extra `fallthroughEnabled` flag, which is there simply for testing. It allows disabling the fallthrough so that unit tests can exercise both cases.

With this macro in place, we can then write quick implementations of all the non-primitive functions:

```
    PLObjectPtr objc_initWeak(PLObjectPtr *addr, PLObjectPtr val) {
        NEXT(objc_initWeak, addr, val);
        *addr = NULL;
        return objc_storeWeak(addr, val);
    }

    void objc_destroyWeak(PLObjectPtr *addr) {
        NEXT(objc_destroyWeak, addr);
        objc_storeWeak(addr, NULL);
    }

    void objc_copyWeak(PLObjectPtr *to, PLObjectPtr *from) {
        NEXT(objc_copyWeak, to, from);
        objc_initWeak(to, objc_loadWeak(from));
    }

    void objc_moveWeak(PLObjectPtr *to, PLObjectPtr *from) {
        NEXT(objc_moveWeak, to, from);
        objc_copyWeak(to, from);
        objc_destroyWeak(from);
    }

    PLObjectPtr objc_loadWeak(PLObjectPtr *location) {
        NEXT(objc_loadWeak, location);
        return objc_autorelease(objc_loadWeakRetained(location));
    }
```

The primitive function `objc_loadWeakRetained` simply calls through to another internal function, which exists simply to better separate things in the code:

```
    PLObjectPtr objc_loadWeakRetained(PLObjectPtr *location) {
        NEXT(objc_loadWeakRetained, location);

        return PLLoadWeakRetained(location);
    }
```

The implementation of `objc_storeWeak` is slightly more complex. First it calls through to the runtime implementation, if any, just like with the other functions:

```
    PLObjectPtr objc_storeWeak(PLObjectPtr *location, PLObjectPtr obj) {
        NEXT(objc_storeWeak, location, obj);
```

After this, it calls an internal function to unregister the weak reference currently at `location`:

```
        PLUnregisterWeak(location, obj);
```

Next, it stores the new value into `location` and, if the new value isn't `nil`, registers this location:

```
        if (obj != nil)
            PLRegisterWeak(location, obj);
```

Finally it simply returns the object that was stored:

```
        return obj;
    }
```

We've therefore decomposed this functionality into three internal primitive functions. `PLLoadWeakRetained` loads a weak reference and returns a retained pointer to it. `PLRegisterWeak` registers a new weak reference location for a particular object, and ensures that the location is zeroed out when the object is destroyed. `PLUnregisterWeak` removes the location from the object's list of weak references so that it will no longer be touched when the object is destroyed. With these three functions implemented, `PLWeakCompatibility` will be complete.

**The Plan**  
There are two main challenges for a zeroing weak reference system in Cocoa. One is finding out exactly when an object is being destroyed, and zeroing out all references to it when that happens.

The second challenge is avoiding race conditions when loading a weak reference. In Cocoa, there is an interval between the last `release` message being sent to a now-dead object and that object's `dealloc` method being invoked. Loading a weak reference to that object in that interval _must_ return `nil`, because the destruction of the object is at that point unavoidable. Retaining it at that point won't keep it alive.

Both of these challenges are solved by [`MAZeroingWeakRef`](https://github.com/mikeash/MAZeroingWeakRef), which uses dynamic subclassing and isa-swizzling to solve them. `PLWeakCompatibility` will call through to `MAZeroingWeakRef` when it's present. However, we also wanted a simpler implementation that we could include directly with the rest of the code, so that it could all be used completely standalone. Thus `PLWeakCompatibility` needs its own solutions as well.

`PLWeakCompatibility` addresses these challenges by swizzling out the `release` and `dealloc` methods of the target object. Swizzling `dealloc` solves the challenge of finding out when an object is destroyed. The swizzled `release` method adds the object to a list of objects that are currently being released. Any attempt to resolve a weak reference to an object on the list blocks until the `release` is complete, at which point the object is either alive, and a weak reference can be obtained, or dead, and the weak reference is zero. However, the details of how this all works will have to wait for part II!

**Conclusion**  
`PLWeakCompatibility` is a great aid to using ARC on older OSes. By passing a couple of flags to the compiler, we're able to trick it into emitting calls to the runtime functions that enable `__weak` even though the runtime doesn't support them. Then, by providing our own implementation of those functions with the same semantics, we enable full `__weak` compatibility on OSes that don't support them natively.

Finally, we decomposed the multiple runtime functions into three primitive functions: one for loading a week reference, one for registering, and one for unregistering. Next time around, I'll discuss in detail the implementation of those three functions and how they work.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
