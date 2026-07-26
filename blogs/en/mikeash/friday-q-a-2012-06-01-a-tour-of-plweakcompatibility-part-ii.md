---
title: 'Friday Q&A 2012-06-01: A Tour of PLWeakCompatibility: Part II'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-06-01-a-tour-of-plweakcompatibility-part-ii.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5fb859d5d42fccc0'
translated: false
---

> 原文：[Friday Q&A 2012-06-01: A Tour of PLWeakCompatibility: Part II](https://www.mikeash.com/pyblog/friday-qa-2012-06-01-a-tour-of-plweakcompatibility-part-ii.html)　·　mikeash.com Friday Q&A

Posted at 2012-06-01 13:38 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-06-22: Objective-C Literals](https://www.mikeash.com/pyblog/friday-qa-2012-06-22-objective-c-literals.html)  
Previous article: [Friday Q&A 2012-05-18: A Tour of PLWeakCompatibility: Part I](https://www.mikeash.com/pyblog/friday-qa-2012-05-18-a-tour-of-plweakcompatibility-part-i.html)  
Tags: [arc](https://www.mikeash.com/pyblog/?tag=arc) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hack](https://www.mikeash.com/pyblog/?tag=hack) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-06-01: A Tour of PLWeakCompatibility: Part II

by [Mike Ash](https://www.mikeash.com/)

**Recall**  
The functions implemented by PLWeakCompatibility which are called directly by the compiler's generated code are:

```
    PLObjectPtr objc_loadWeakRetained(PLObjectPtr *location);
    PLObjectPtr objc_initWeak(PLObjectPtr *addr, PLObjectPtr val);
    void objc_destroyWeak(PLObjectPtr *addr);
    void objc_copyWeak(PLObjectPtr *to, PLObjectPtr *from);
    void objc_moveWeak(PLObjectPtr *to, PLObjectPtr *from);
    PLObjectPtr objc_loadWeak(PLObjectPtr *location);
    PLObjectPtr objc_storeWeak(PLObjectPtr *location, PLObjectPtr obj);
```

Where `PLObjectPtr` is just a typedef for `void *` and used as a way to prevent ARC from inserting memory management code into these functions where it's definitely not wanted. All of these functions start with code that calls through to the Objective-C runtime's implementation where available. When the official runtime functions aren't available, these seven functions are broken down and implemented in terms of three primitive functions:

```
    PLObjectPtr PLLoadWeakRetained(PLObjectPtr *location);
    void PLRegisterWeak(PLObjectPtr *location, PLObjectPtr obj);
    void PLUnregisterWeak(PLObjectPtr *location, PLObjectPtr obj);
```

The `PLLoadWeakRetained` function loads a weak reference out of the given location and either returns a retained reference to the object it contains, or `nil`. The `PLRegisterWeak` function registers a particular memory location as a weak reference to the given object, and `PLUnregisterWeak` removes that registration. The task that remains is then to implement these three functions.

**MAZeroingWeakRef**  
The goal is to make PLWeakCompatibility completely self-contained with its own zeroing weak reference implementation, which would necessarily be somewhat simple. However, we also wanted to make it use MAZeroingWeakRef where available, as the presence of that library in the app probably means that the programmer likes that implementation, and we might as well take advantage of its presence. Thus, the first task is to detect the presence of MAZeroingWeakRef, and then implement the three primitive functions using it, if it's present.

First, we need a way to detect whether MAZeroingWeakRef is present, and get a reference to the class if so. This is all wrapped up in a simple function that uses `NSClassFromString` to attempt to fetch the `MAZeroingWeakRef` class, within a `dispatch_once` call to minimize the overhead. It also has an extra flag that allows disabling the MAZeroingWeakRef functionality for testing purposes:

```
    static Class MAZWR = Nil;
    static bool mazwrEnabled = true;
    static inline bool has_mazwr () {
        if (!mazwrEnabled)
            return false;

        static dispatch_once_t lookup_once = 0;
        dispatch_once(&lookup_once, ^{
            MAZWR = NSClassFromString(@"MAZeroingWeakRef");
        });

        if (MAZWR != nil)
            return true;
        return false;
    }
```

Now code can simply call `has_mazwr`, and if it returns true, use `MAZWR` to get a reference to the class.

The strategy for implementing the three primitives using MAZeroingWeakRef is pretty straightforward. Each primitive gets a location where the weak reference is to be stored, and nothing says that this location is required to directly hold a pointer to the weakly referenced object. Thus, we use the passed-in location to store a pointer to a `MAZeroingWeakRef` instance which in turn references the original object. `PLRegisterWeak` will simply create a new instance of `MAZeroingWeakRef` and place it in the given location. `PLUnregisterWeak` will simply release that instance. And `PLLoadWeakRetained` can just call through to the object's `-target` method.

Each primitive function checks `has_mazwr` at the top to decide what to do. The beginning of each primitive function contains the `MAZeroingWeakRef` calls, and they are:

```
    static PLObjectPtr PLLoadWeakRetained(PLObjectPtr *location) {
        if (has_mazwr()) {
            MAZeroingWeakRef *mazrw = (__bridge MAZeroingWeakRef *) *location;
            return objc_retain([mazrw target]);
        }
        ...

    static void PLRegisterWeak(PLObjectPtr *location, PLObjectPtr obj) {
        if (has_mazwr()) {        
            MAZeroingWeakRef *ref = [[MAZWR alloc] initWithTarget: obj];
            *location = (__bridge_retained PLObjectPtr) ref;
            return;
        }
        ...

    static void PLUnregisterWeak(PLObjectPtr *location, PLObjectPtr obj) {
        if (has_mazwr()) {
            if (*location != nil)
                objc_release(*location);
            return;
        }
        ...
```

**The Built-In Implementation**  
Now for the real meat: the built-in zeroing weak reference implementation. The strategy is to swizzle out `release` and `dealloc` on target objects. The swizzled `release` method will add the object to a list of releasing objects, blocking anyone attempting to resolve a weak reference while the release is occurring, ensuring no weak reference can be resolved when an object's final `release` triggers its `dealloc`. The swizzled `dealloc` method will then clear out all weak references to the object.

The first thing we need is a mutex to protect all of the shared data structures:

```
    static pthread_mutex_t gWeakMutex;
```

We also need a way to track all of the weak references currently registered for any given object. This comes in the form of a `CFMutableDictionary` mapping objects to `CFMutableSet` instances containing the registered weak addresses:

```
    static CFMutableDictionaryRef gObjectToAddressesMap;
```

We're likely to see weak references to multiple instances of the same class, so we need to track which classes have been swizzled andavoid swizzling them twice. This is done by tracking the swizzled classes in a set:

```
    static CFMutableSetRef gSwizzledClasses;
```

The objects that are currently in the middle of a release call are stored in a bag:

```
    static CFMutableBagRef gReleasingObjects;
```

Since some code needs to wait around for `gReleasingObjects` to change, that means we also need a condition variable for them to wait on. (If you're unfamiliar with condition variables, I'll discuss that more later.)

```
    static pthread_cond_t gReleasingObjectsCond;
```

Some data also needs to be stored in thread-local storage. Two tables to assist with the swizzling process reside there. They get stored in structs accessed through a `pthread` thread-local storage key:

```
    static pthread_key_t gTLSKey;
```

For convenience, we also put all of the selectors necessary for swizzling into global variables:

```
    static SEL releaseSEL;
    static SEL releaseSELSwizzled;
    static SEL deallocSEL;
    static SEL deallocSELSwizzled;
```

Every primitive function needs to access these variables, and they all need to be initialized before use. This initialization is all wrapped in a `dispatch_once`:

```
    static void WeakInit(void) {
        static dispatch_once_t pred;
        dispatch_once(&pred, ^{
```

The first thing it does is initialize the mutex, using the recursive atribute::

```
            pthread_mutexattr_t attr;
            pthread_mutexattr_init(&attr);
            pthread_mutexattr_settype(&attr, PTHREAD_MUTEX_RECURSIVE);

            pthread_mutex_init(&gWeakMutex, &attr);

            pthread_mutexattr_destroy(&attr);
```

Next, the map of objects to addresses and the set of swizzled classes are created:

```
            gObjectToAddressesMap = CFDictionaryCreateMutable(NULL, 0, NULL, &kCFTypeDictionaryValueCallBacks);

            gSwizzledClasses = CFSetCreateMutable(NULL, 0, NULL);
```

By passing `NULL` for the dictionary key callbacks and the set callbacks, we ensure that CoreFoundation doesn't try to do any sort of memory management on them.

The releasing objects set is initialized, as well as the condition variable used to wait on it:

```
            gReleasingObjects = CFBagCreateMutable(NULL, 0, NULL);
            pthread_cond_init(&gReleasingObjectsCond, NULL);
```

Next, the `pthread` thread-local storage key is created. There's a bit of paranoia here with the error checking because this function can realistically fail. The number of thread-local storage keys that can be created is limited and relatively small: 512 keys on Mac OS X currently. This should be more than sufficient, but since it can realistically fail, I want it to fail early and obviously:

```
            int err = pthread_key_create(&gTLSKey, DestroyTLS);
            if (err != 0) {
                NSLog(@"Error calling pthread_key_create, we really can't recover from that: %s (%d)", strerror(err), err);
                abort();
            }
```

The `DestroyTLS` function frees the memory allocated for the thread-local storage. I'll show its implementation momentarily.

Finally, the selectors are initialized. We can't use the standard `@selector` construct for `release` and `dealloc`, because this is not allowed with ARC. Instead, we use `sel_getUid` (the Objective-C runtime equivalent of `NSSelectorFromString`) to fetch the selectors under ARC's nose:

```
            releaseSEL = sel_getUid("release");
            releaseSELSwizzled = sel_getUid("release_PLWeakCompatibility_swizzled");
            deallocSEL = sel_getUid("dealloc");
            deallocSELSwizzled = sel_getUid("dealloc_PLWeakCompatibility_swizzled");
        });
    }
```

Each primitive function the makes a call to `WeakInit` before it does anything else, ensuring that all of these variables are set up. I'll omit that call, as well as the `MAZeroingWeakRef` code, when discussing the implementation of those functions, just to keep things simple.

**Thread-Local Storage**  
A `pthread` thread-local storage key can be used to set and retrieve a single pointer per thread. To store multiple values, we allocate a struct which contains everything we want to store. We need two dictionaries which help the swizzled methods call through to their original values. Here is the struct:

```
    struct TLS {
        // Tables tracking the last class a swizzled method was sent to on an object
        CFMutableDictionaryRef lastReleaseClassTable;
        CFMutableDictionaryRef lastDeallocClassTable;
    };
```

Since this struct is used in a couple of places, we want a wrapper function that will retrieve it, creating it if on demand if nothing else has used the `TLS` struct on that thread yet. `pthread_getspecific` retrieves the current value, and if the current value is `NULL`, this function uses `pthread_setspecific` to set a new key:

```
    static struct TLS *GetTLS(void) {
        struct TLS *tls = pthread_getspecific(gTLSKey);
        if (tls == NULL) {
            tls = calloc(1, sizeof(*tls));
            tls->lastReleaseClassTable = CFDictionaryCreateMutable(NULL, 0, NULL, NULL);
            tls->lastDeallocClassTable = CFDictionaryCreateMutable(NULL, 0, NULL, NULL);
            pthread_setspecific(gTLSKey, tls);
        }
        return tls;
    }
```

We also need a function to destroy the `TLS` struct. This function was passed to `pthread_key_create`, and is automatically called by `pthread` when a thread is destroyed:

```
    static void DestroyTLS(void *ptr) {
        struct TLS *tls = ptr;
        if (tls != NULL && tls->lastReleaseClassTable) {
            CFRelease(tls->lastReleaseClassTable);
            CFRelease(tls->lastDeallocClassTable);
        }
        free(tls);
    }
```

With these in place, any thread can simply call `GetTLS()` and then manipulate the data in the struct, which is guaranteed to only be visible to the calling thread.

**The Primitive Functions**  
The implementation of `PLLoadWeakRetained` is relatively straightforward. It needs to acquire the global mutex, then retrieve the object pointer. If the object is currently being released, then it must wait until it's no longer being released.

First thing it does is acquire the global mutex, then try to fetch the value stored at the given location:

```
    static PLObjectPtr PLLoadWeakRetained(PLObjectPtr *location) {
        PLObjectPtr obj;
        pthread_mutex_lock(&gWeakMutex); {
            obj = *location;
```

Next it checks to see if the given object is in the list of releasing objects. If it's there, it uses `pthread_cond_wait` to block on the condition variable, then reloads the location to get the latest value:

```
        while (CFBagContainsValue(gReleasingObjects, obj)) {
            pthread_cond_wait(&gReleasingObjectsCond, &gWeakMutex);
            obj = *location;
        }
```

`pthread_cond_wait` releases the given mutex and then waits for somebody to signal the condition variable. Once signalled, it re-acquires the mutex and resumes execution. This allows the thread to block until another thread signals that the table of releasing objects changed, at which point it can re-examine it.

This is a `while` loop rather than a simple `if` statement for a couple of reasons. One is simply that the signalled change may not be for this object. There's a single condition variable for the whole table, and some other object may be the one that got removed.

The other reason is a bit more interesting and is called [spurious wakeup](http://en.wikipedia.org/wiki/Spurious_wakeup). In short, due to various implementation details, `pthread_cond_wait` may occasionally return even when nothing has signalled on the condition variable. Due to this, any call to `pthread_cond_wait` should always be wrapped in a loop, not a simple `if` statement.

Once the object (or `nil`) is obtained, we simply retain it, release the mutex, and return the retained object.

```
            objc_retain(obj);
        }
        pthread_mutex_unlock(&gWeakMutex);

        return obj;
    }
```

`PLRegisterWeak` is a little more complex. The first thing it does is fetch the set of registered addresses for the given object so it can add the new entry:

```
    static void PLRegisterWeak(PLObjectPtr *location, PLObjectPtr obj) {
        pthread_mutex_lock(&gWeakMutex); {
            CFMutableSetRef addresses = (CFMutableSetRef)CFDictionaryGetValue(gObjectToAddressesMap, obj);
```

That set won't exist if this is the first weak reference to the given object. In that case, this function has to create it:

```
            if (addresses == NULL) {
                addresses = CFSetCreateMutable(NULL, 0, NULL);
                CFDictionarySetValue(gObjectToAddressesMap, obj, addresses);
                CFRelease(addresses);
            }
```

Now that it has the set, the passed-in location is added to it:

```
            CFSetAddValue(addresses, location);
```

Finally, it calls a helper function to ensure that all of the appropriate swizzling has been done:

```
            EnsureDeallocationTrigger(obj);
        } pthread_mutex_unlock(&gWeakMutex);
    }
```

We'll get into that helper function's implementation shortly.

The implementation of `PLUnregisterWeak` is essentially the inverse of `PLRegisterWeak`, except that it doesn't have to worry about swizzling, which is simply left in place, and it doesn't bother to delete the addresses set when it becomes empty:

```
    static void PLUnregisterWeak(PLObjectPtr *location, PLObjectPtr obj) {
        pthread_mutex_lock(&gWeakMutex); {
            // Remove the location from the set of weakly referenced addresses.
            CFMutableSetRef addresses = (CFMutableSetRef)CFDictionaryGetValue(gObjectToAddressesMap, *location);
            if (addresses != NULL)
                CFSetRemoveValue(addresses, location);
        } pthread_mutex_unlock(&gWeakMutex);
    }
```

Let's look at `EnsureDeallocationTrigger`'s implementation now. The first thing it does is fetch the class of the given object, and bail out if that class has already been swizzled:

```
    static void EnsureDeallocationTrigger(PLObjectPtr obj) {
        Class c = object_getClass(obj);
        if (CFSetContainsValue(gSwizzledClasses, (__bridge const void *)c))
            return;
```

If it hasn't, it then swizzles `release` and `dealloc`, using a small helper function, and finally adds the class to the set of swizzled classes:

```
        Swizzle(c, releaseSEL, releaseSELSwizzled, (IMP)SwizzledReleaseIMP);
        Swizzle(c, deallocSEL, deallocSELSwizzled, (IMP)SwizzledDeallocIMP);

        CFSetAddValue(gSwizzledClasses, (__bridge const void *)c);
    }
```

The implementation of `Swizzle` is simple: it just uses `class_addMethod` to register the previous `IMP` under a new selector, and `class_replaceMethod` to place the new IMP into the original selector:

```
    static void Swizzle(Class c, SEL orig, SEL new, IMP newIMP) {
        Method m = class_getInstanceMethod(c, orig);
        IMP origIMP = method_getImplementation(m);
        class_addMethod(c, new, origIMP, method_getTypeEncoding(m));
        class_replaceMethod(c, orig, newIMP, method_getTypeEncoding(m));
    }
```

And that's just about it. All that remains are the implementations of `SwizzledReleaseIMP` and `SwizzledDeallocIMP`. Which, as it turns out, are pretty difficult and complex.

**The Subclass Problem**  
When possible, the best way to implement method swizzling is to store the original `IMP` in a global variable, which you then call as a function pointer:

```
    // original implementation
    void (*origIMP)(id, SEL);

    // swizzle code
    origIMP = (void *)method_getImplementation(origMethod);
    class_replaceMethod(class, selector, newIMP, method_getTypeEncoding(origMethod));

    // swizzled IMP
    void newIMP(id self, SEL _cmd)
    {
        // do stuff here
        ...

        // call the original
        origIMP(self, _cmd);
    }
```

However, this only works when you're only swizzling a single class. When swizzling multiple classes, there are multiple original implementations to keep track of. In that case, the best way to do things is to register the original implementation under a new selector on the same class, and look it up that way:

```
    // swizzle code
    IMP origIMP = method_getImplementation(origMethod);
    class_addMethod(class, @selector(swizzled_method), origIMP, method_getTypeEncoding(origMethod));
    class_replaceMethod(class, selector, newIMP, method_getTypeEncoding(origMethod));

    // swizzled IMP
    void newIMP(id self, SEL _cmd)
    {
        // do stuff here
        ...

        // look up the original
        Class class = object_getClass(self);
        void (*origIMP)(id, SEL) = (void *)(class_getMethodImplementation(class, @selector(swizzled_method));

        // call the original
        origIMP(self, _cmd);
    }
```

However, this only works if you only swizzle leaf classes. If you ever end up swizzling two classes where one is a superclass of the other, this ends up with infinite recursion and crashes.

To understand why, let's consider two classes, `A` and `B`, both of which override `dealloc`:

```
    @interface A : NSObject
    - (void)dealloc; // clean up stuff
    @end

    @interface B : A
    - (void)dealloc; // clean up in aisle three
    @end
```

Let's assume that we've swizzled `dealloc` on both `A` and `B` (presumably because something created a `__weak` reference to an instance of `A` and an instance of `B`). Now something releases an instance of `B`.

Because of the swizzling, the call to `dealloc` ends up invoking the swizzled implementation. So far so good.

The swizzled implementation looks up `-[B swizzled_dealloc]` and calls it. This calls the original implementation of `-[B dealloc]`. Again, so far so good. At the end of this original implementation, the method will call `[super dealloc]`, which ends up getting `-[A dealloc]`. Still good up to here.

`-[A dealloc]` is also the swizzled implementation, but that's fine. That implementation needs to be reentrant, but it has to be this way if we want to intercept calls to instances of both `A` and `B`. The swizzled implementation does its thing _again_, but is written to tolerate this. Then it calls through to the original implementation. And here is where things go wrong.

Check out the code that looks up the original implementation:

```
    Class class = object_getClass(self);
    void (*origIMP)(id, SEL) = (void *)(class_getMethodImplementation(class, @selector(swizzled_method));
```

Even though this is called from `A`, `object_getClass` still returns `B`. At runtime, there's no concept of "called from `A`." The object's class is `B`, and that's what it gets. So at the end of `-[A dealloc]`, where the swizzled implementation looks up and calls the original, it ends up calling `-[B swizzled_dealloc]` again! If that method somehow runs a second time without crashing, it will call back to `-[A dealloc]`, which calls back to `-[B swizzled_dealloc]`, and this continues until either some piece of code gets fed up with this abuse, or the infinite recursion runs out of stack space and crashes.

In order to solve this, the swizzled implementation needs some way to know which class it's attached to. This is trivial using `imp_implementationWithBlock` to create a slightly different swizzled implementation for each class. Unfortunately, `imp_implementationWithBlock` is only available on iOS 4.3 and later. Requiring it for `PLWeakCompatibility` would mean eliminating support for iOS 4.0-4.2, making it much less useful. We need to come up with some other way to handle this.

**Emulating `super`**  
The hypothetical call to `super` would walk up the class hierarchy, retrieving the original `IMP` from the next highest class each time, and calling that. By tracking the last class that we retrieved, we can emulate this. For each method, we set up a table that maps objects to the last class used for the call to the original `IMP`. By moving up the hierarchy from that class on each call, we can achieve the necessary behavior.

In the example above, the first call to 'dealloc' sees no table entry, so it calls `B`'s dealloc and puts `B` in the table. The next call sees `B`, calls `A`'s dealloc, and puts `A` in the table. The next call sees `A` and calls `NSObject`'s dealloc. This is all exactly as we want.

There's one extra trick needed here. Imagine yet another class in the hierarchy, `C`:

```
    @interface C : B
    // does not override dealloc
    @end
```

This runs into a problem. The first call sees no table entry, calls `C`'s dealloc, and puts `C` in the table. However, since `C` doesn't override `dealloc`, it's actually just `B`'s dealloc. The next call sees the `C` in the table and calls... `B`'s dealloc again. This is not good.

The trick is to search the class hierarchy for the topmost class with the given method implementation. The `TopClassImplementingMethod` function searches up the class hierarchy from the given class, looking for the point where the `IMP` for a given selector changes, and then returns the last class from before that point:

```
    static Class TopClassImplementingMethod(Class start, SEL sel) {
        IMP imp = class_getMethodImplementation(start, sel);

        Class previous = start;
        Class cursor = class_getSuperclass(previous);
        while (cursor != Nil) {
            if (imp != class_getMethodImplementation(cursor, sel))
                break;
            previous = cursor;
            cursor = class_getSuperclass(cursor);
        }

        return previous;
    }
```

By calling this function before putting an entry in the table, this solves the problem. The first call will see no table entry, call `C`'s dealloc (which is really `B`'s dealloc), but then place `B` in the table instead of `C`. The next call goes to `A`, then `NSObject` as we need it to.

These tables would run into conflicts if the same method were invoked multiple times on different threads. However, by placing these tables in thread-local storage, that problem is eliminated.

**Release**  
The first thing the `release` swizzle does is fetch the thread-local struct, since it's going to use the contents throughout the method:

```
    static void SwizzledReleaseIMP(PLObjectPtr self, SEL _cmd) {
        struct TLS *tls = GetTLS();
```

Next, we add `self` to the list of objects being released:

```
        pthread_mutex_lock(&gWeakMutex); {
            // Add this object to the list of releasing objects.
            CFBagAddValue(gReleasingObjects, self);
        } pthread_mutex_unlock(&gWeakMutex);
```

After that, we start on the fake `super` strategy. The first thing to do is see what the current table entry is:

```
        Class lastSent = (__bridge Class)CFDictionaryGetValue(tls->lastReleaseClassTable, self);
```

Then we pick a target class. If the table is empty, that's just the class of `self`. If the table contains a class, then we start with that class's superclass:

```
        Class targetClass = lastSent == Nil ? object_getClass(self) : class_getSuperclass(lastSent);
```

Then we use `TopClassImplementingMethod` to skip over classes that don't override `release`, and store the result back into the table:

```
        targetClass = TopClassImplementingMethod(targetClass, releaseSELSwizzled);
        CFDictionarySetValue(tls->lastReleaseClassTable, self, (__bridge void *)targetClass);
```

With the target class in hand, the code can fetch the `IMP` for `release` on that target class and call it:

```
        void (*origIMP)(PLObjectPtr, SEL) = (__typeof__(origIMP))class_getMethodImplementation(targetClass, releaseSELSwizzled);
        origIMP(self, _cmd);
```

At this point, the superclass's code has completed. If this call released the last reference to `self`, the object is now destroyed. The first thing to do is to clean up the class table so that the next call to `release` at this address (either the same object, if this `release` didn't destroy it, or a new object allocated at the same location):

```
        CFDictionaryRemoveValue(tls->lastReleaseClassTable, self);
```

Finally, we reacquire the mutex to remove `self` from the list of releasing objects, calling `pthread_cond_broadcast` to wake up any threads that might be waiting on this object:

```
        pthread_mutex_lock(&gWeakMutex); {
            // We're no longer releasing.
            CFBagRemoveValue(gReleasingObjects, self);
            pthread_cond_broadcast(&gReleasingObjectsCond);
        } pthread_mutex_unlock(&gWeakMutex);
    }
```

**Dealloc**  
The swizzled `dealloc` implementation is largely similar. Like the swizzled `release`, it starts off by fetching the thread-local storage struct:

```
    static void SwizzledDeallocIMP(PLObjectPtr self, SEL _cmd) {
        struct TLS *tls = GetTLS();
```

Next, it grabs the global lock and clears all weak references to `self` by fetching the addresses from the global map and iterating over them:

```
        pthread_mutex_lock(&gWeakMutex); {
            // Clear all weak references and delete the addresses set.
            CFSetRef addresses = CFDictionaryGetValue(gObjectToAddressesMap, self);
            if (addresses != NULL)
                CFSetApplyFunction(addresses, ClearAddress, NULL);
```

Note that `ClearAddress` is just a simple function that essentially does `*(void **)value = NULL` to zero out every entry in the set. Now taht the set is clear, it's no longer needed, so we remove it from the global map:

```
            CFDictionaryRemoveValue(gObjectToAddressesMap, self);
```

Finally, we notify anybody waiting on the list of releasing objects that it has changed. Technically, the list itself has not changed. However, anybody waiting on `self` will now find their weak reference contains `nil`, which isn't in the set, so we still want to notify listeners to recheck:

```
            pthread_cond_broadcast(&gReleasingObjectsCond);
        } pthread_mutex_unlock(&gWeakMutex);
```

With that out of the way, `dealloc` uses the same procedure as `release` to call through to the original implementation:

```
        Class lastSent = (__bridge Class)CFDictionaryGetValue(tls->lastDeallocClassTable, self);
        Class targetClass = lastSent == Nil ? object_getClass(self) : class_getSuperclass(lastSent);
        targetClass = TopClassImplementingMethod(targetClass, deallocSELSwizzled);
        CFDictionarySetValue(tls->lastDeallocClassTable, self, (__bridge void *)targetClass);

        // Call through to the original implementation.
        void (*origIMP)(PLObjectPtr, SEL) = (__typeof__(origIMP))class_getMethodImplementation(targetClass, deallocSELSwizzled);
        origIMP(self, _cmd);
```

At this point, `self` is destroyed. All that remains is to clean up the entry in the class table for it, to leave it pristine for the next object to occupy this address:

```
        CFDictionaryRemoveValue(tls->lastDeallocClassTable, self);
    }
```

**Conclusion**  
This is a tough problem to solve, but with careful thought and programming we're able to make it all work. Swizzling `release` and `dealloc` allows safely zeroing out weak references to a target object. A table that tracks all objects currently in the middle of a `release` ensures that nobody can ever obtain a reference to an object that's about to be destroyed. By tracking the class the swizzled method was sent to in an external table, we can safely swizzle these methods even when the swizzled method is called recursively.

That's it for today. Come back next time for more wacky fun in the world of Cocoa programming. Friday Q&A is driven by reader suggestions, so in the meantime, if you have a topic that you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-06-01-a-tour-of-plweakcompatibility-part-ii.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
