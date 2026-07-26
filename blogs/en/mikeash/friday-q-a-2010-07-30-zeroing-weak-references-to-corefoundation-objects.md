---
title: 'Friday Q&A 2010-07-30: Zeroing Weak References to CoreFoundation Objects'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-07-30-zeroing-weak-references-to-corefoundation-objects.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:825dc66eab42d190'
translated: false
---

> 原文：[Friday Q&A 2010-07-30: Zeroing Weak References to CoreFoundation Objects](https://www.mikeash.com/pyblog/friday-qa-2010-07-30-zeroing-weak-references-to-corefoundation-objects.html)　·　mikeash.com Friday Q&A

Posted at 2010-07-30 19:01 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-08-12: Implementing NSCoding](https://www.mikeash.com/pyblog/friday-qa-2010-08-12-implementing-nscoding.html)  
Previous article: [Introducing MAZeroingWeakRef](https://www.mikeash.com/pyblog/introducing-mazeroingweakref.html)  
Tags: [corefoundation](https://www.mikeash.com/pyblog/?tag=corefoundation) [evil](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hack](https://www.mikeash.com/pyblog/?tag=hack)

Friday Q&A 2010-07-30: Zeroing Weak References to CoreFoundation Objects

by [Mike Ash](https://www.mikeash.com/)

**Code**  
 Just as before, you can get the code for `MAZeroingWeakRef` from my public Subversion repository:

```
    svn co http://mikeash.com/svn/ZeroingWeakRef/
```

Or click the above link to browse it. If you already have a local copy from last time, be sure to update it, as I have made substantial changes since then.

**Prior Reading**  
 This post assumes fairly good knowledge of CoreFoundation and how CF-ObjC bridging works. If you haven't already, you may wish to read or at least refer to [Friday Q&A 2010-01-22: Toll Free Bridging Internals](https://www.mikeash.com/pyblog/friday-qa-2010-01-22-toll-free-bridging-internals.html).

**Recap**  
 A zeroing weak reference is a reference to an object which does not participate in keeping that object alive. When the target object is destroyed, the zeroing weak reference automatically becomes `NULL`. When a zeroing weak reference's target is requested, the caller is guaranteed to either get a valid reference, or `NULL`. This is useful for all kinds of things [as covered in the previous article](https://www.mikeash.com/pyblog/friday-qa-2010-07-16-zeroing-weak-references-in-objective-c.html).

In order to accomplish this in Cocoa, `MAZeroingWeakRef` overrides the `dealloc` method of the target object by dynamically creating a subclass of the target's class, and changing the class of the target. This overridden `dealloc` method zeroes out `MAZeroingWeakRef` objects that point to the target.

There is a problem with thread safety and resurrection if you stop there. Imagine one thread calls `release` on the last strong reference to an object, causing it to then call `dealloc`. Imagine that between these two, another thread accesses the object through a zeroing weak reference. Since `dealloc` has not yet been called, it returns a reference to the object. However, because the `dealloc` call is already set to go, the `retain/autorelease` dance done by `MAZeroingWeakRef` can't save the object from being destroyed. Disaster!

This problem is solved by also overriding `release`. By having `release` acquire a lock that's also used when retrieving a zeroing weak reference target, it's assured that this resurrection scenario can't occur.

**Toll-Free Bridged Objects**  
 This scheme works great for normal Objective-C objects, but fails hard for bridged CoreFoundation objects. Changing out the class of a bridged object causes infinite recursion. The first thing a CoreFoundation function does is check the class of the object it's being called on. If that class doesn't match the official `NSCF` class, it assumes it's a pure Objective-C class and calls through to the Objective-C equivalent method. The Objective-C equivalent method on an `NSCF` class just calls the CoreFoundation function. Rinse, lather, repeat, and crash.

The dynamic subclass wouldn't be strictly necessary in this case. I could instead swizzle out the `dealloc` and `release` methods on the `NSCF` class directly, and have them do my dirty work. This is a bit less efficient (since I'm affecting every object of that class, not just weak-referenced ones) but that shouldn't matter.

The trouble is that this doesn't work. If you call `CFRelease` on such an object, it goes directly to the refcounting and deallocation of that object without ever calling the Objective-C methods. So this solution can only catch one side of things, which is basically useless.

After working through all of this, I hunted around for a solution. Short of patching `CFRelease` (which I really didn't want to do, not the least of which because this approach won't work on the iPhone, where modifying executable code is forbidden) I couldn't come up with a way.

I nearly gave up on the problem, resigned to simply forbidding weak references to CoreFoundation objects, when I finally happened upon....

**The Solution**  
 I had started looking through the CoreFoundation source code (available from [opensource.apple.com](http://www.opensource.apple.com/)) trying to find a way to hook into release events when I happened up on this little gem in the code for `CFRelease`:

```
    void (*func)(CFTypeRef) = __CFRuntimeClassTable[typeID]->finalize;
    if (NULL != func) {
        func(cf);
    }
    // We recheck lowBits to see if the object has been retained again during
    // the finalization process.  This allows for the finalizer to resurrect,
    // but the main point is to allow finalizers to be able to manage the
    // removal of objects from uniquing caches, which may race with other threads
    // which are allocating (looking up and finding) objects from those caches,
    // which (that thread) would be the thing doing the extra retain in that case.
    if (isAllocator || OSAtomicCompareAndSwap32Barrier(1, 0, (int32_t *)&((CFRuntimeBase *)cf)->_rc)) {
        goto really_free;
    }
```

The comment about resurrection is key. While I can't intercept the `CFRelease` to eliminate the race condition, I can detect it and allow the object to resurrect so that I can recover from the situation. I was on my way!

Implementing this solution requires overriding the CoreFoundation finalize function. CoreFoundation has no supported mechanism for this, so I had to get down and dirty with the CF source code and hack my way in. This means that everything I'm doing is not entirely supported and could break, although I believe that this stuff is actually pretty stable.

**CoreFoundation Classes**  
 A CoreFoundation class is just a struct that looks like this:

```
    typedef struct __CFRuntimeClass {	// Version 0 struct
        CFIndex version;
        const char *className;
        void (*init)(CFTypeRef cf);
        CFTypeRef (*copy)(CFAllocatorRef allocator, CFTypeRef cf);
        void (*finalize)(CFTypeRef cf);
        Boolean (*equal)(CFTypeRef cf1, CFTypeRef cf2);
        CFHashCode (*hash)(CFTypeRef cf);
        CFStringRef (*copyFormattingDesc)(CFTypeRef cf, CFDictionaryRef formatOptions);	// str with retain
        CFStringRef (*copyDebugDesc)(CFTypeRef cf);	// str with retain
        void (*reclaim)(CFTypeRef cf);
    } CFRuntimeClass;
```

It's basically just a table with a few function pointers in it for common operations that all CF objects support. All class-specific functionality is implemented as functions and has no dynamic lookup at all (except for the stuff present in toll-free bridging support).

Overriding the finalize function then becomes easy. First, look up the `CFRuntimeClass` for the given CF type ID with this function:

```
    extern CFRuntimeClass * _CFRuntimeGetClassWithTypeID(CFTypeID typeID);
```

I can then replace the `finalize` function pointer with my own function. I still need to call through to the original, so I make my own table for the original function pointers, indexed by CF type ID:

```
    typedef void (*CFFinalizeFptr)(CFTypeRef);
    static CFFinalizeFptr *gCFOriginalFinalizes;
    static size_t gCFOriginalFinalizesSize;
```

If you'll remember from last time, my utility function `CreateCustomSubclass` is responsible for creating a dynamic Objective-C subclass for a given object. The original implementation checked to see if the object was a bridged CoreFoundation object and simply asserted if it was. The new implementation handles swizzling out the `finalize` function pointer to my custom function:

```
    static Class CreateCustomSubclass(Class class, id obj)
    {
        if(IsTollFreeBridged(class, obj))
        {
            CFTypeID typeID = CFGetTypeID(obj);
            CFRuntimeClass *cfclass = _CFRuntimeGetClassWithTypeID(typeID);
            
            if(typeID >= gCFOriginalFinalizesSize)
            {
                gCFOriginalFinalizesSize = typeID + 1;
                gCFOriginalFinalizes = realloc(gCFOriginalFinalizes, gCFOriginalFinalizesSize * sizeof(*gCFOriginalFinalizes));
            }
            
            do {
                gCFOriginalFinalizes[typeID] = cfclass->finalize;
            } while(!OSAtomicCompareAndSwapPtrBarrier(gCFOriginalFinalizes[typeID], CustomCFFinalize, (void *)&cfclass->finalize));
            return class;
        }
        else
            // original ObjC dynamic subclassing code is here
```

There's nothing too complicated here. The first part just gets the requisite information. The `if` statement in the middle handles resizing the table if it's too small. (CF type IDs are small integers, so a flat array indexed by them works nicely.) The last part swizzles out the original function pointer, using an atomic call to ensure that it's thread safe just in case anybody else happens to be trying the same thing at the exact same time.

With this change, it's now critical that `IsTollFreeBridged` be 100% reliable. The old implementation simply looked for a class name that started with `NSCF`, and that's not good enough. I came up with a completely reliable test using a private CoreFoundation table of Objective-C classes:

```
    extern Class *__CFRuntimeObjCClassTable;
```

This table maps a CF type ID to the `NSCF` Objective-C class. Checking for bridgedness is then just a matter of getting the type ID of the object in question, getting the bridged class of the type ID, and seeing if the object's class matches it or not:

```
    static BOOL IsTollFreeBridged(Class class, id obj)
    {
        CFTypeID typeID = CFGetTypeID(obj);
        Class tfbClass = __CFRuntimeObjCClassTable[typeID];
        return class == tfbClass;
    }
```

The `finalize` swizzling re-points to `CustomCFFinalize`. This function simply checks for resurrection by looking at `CFGetRetainCount`, and then if resurrection has not taken place, it clears out all weak references to the object and calls the original `finalize` function:

```
    static void CustomCFFinalize(CFTypeRef cf)
    {
        WhileLocked({
            if(CFGetRetainCount(cf) == 1)
            {
                ClearWeakRefsForObject((id)cf);
                void (*fptr)(CFTypeRef) = gCFOriginalFinalizes[CFGetTypeID(cf)];
                if(fptr)
                    fptr(cf);
            }
        });
    }
```

Easy! Right? Right...?

**Resurrection Comes Back From the Dead**  
 Unfortunately, there's a race condition here. Imagine the following sequence:

1. **Thread 1**

    1. `CFRelease(obj)`
    2. `CFRelease` calls `CustomCFFinalize`
    3. Before `CustomCFFinalize` begins executing, the thread is preempted
2. **Thread 2**

    1. `[ref target]` obtains reference to `obj`
    2. `obj` is retained and autoreleased by `MAZeroingWeakRef`
    3. The enclosing autorelease pool is drained, resulting in `CFRelease(obj)`
    4. `CFRelease` calls `CustomCFFinalize`
    5. `CustomCFFinalize` clears weak references and calls the original `finalize`
    6. `CustomCFFinalize` returns
3. **Thread 1**

    1. Resumes execution at the beginning of `CustomCFFinalize`
    2. `CustomCFFinalize` checks the retain count, which is still 1
    3. `CustomCFFinalize` calls the original `finalize` a second time on the same object
    4. A horrible flaming crash occurs

What's worse, `CFRelease` isn't even safe in the presence of resurrecting finalizers. It checks the object's reference count a second time after the finalizer returns. However, the object could have been resurrected and destroyed in the intervening time, causing a bad memory access. In order to make this safe, we _can't_ allow any possibility that the object is destroyed until `CFRetain` itself returns.

Thus there is an extremely narrow, difficult-to-hit, but entirely real race condition that could cause this code to crash.

**Hack Level Three**  
 In order to solve this problem, I divide CoreFoundation objects into two categories. Some objects are the target of a weak reference, and the rest are not. This serves two purposes. First, it allows me to take a fast path when destroying an object that was never the target of a weak reference. Second, I can track whether a referenced object can still potentially be resurrected or not.

This is implemented by simply keeping a `CFMutableSet` where referenced objects are stored. Checking the status of an object is simply a matter of testing set membership. Objects are inserted into the set when calling `RegisterRef`. Objects are removed when the finalize executes with a retain count of 1, which ensures that it can no longer be resurrected.

The new `CustomCFFinalize` is then split in two. If the object has weak references, it first checks for a retain count of 1 to see whether it's been resurrected:

```
static void CustomCFFinalize(CFTypeRef cf)
    {
        WhileLocked({
            if(CFSetContainsValue(gCFWeakTargets, cf))
            {
                if(CFGetRetainCount(cf) == 1)
                {
```

If the retain count is still 1 then the object has not been resurrected. It's still not safe to destroy, however, as multiple threads may be sitting in this spot. Instead, the code clears out all weak references, _retains_ the object to deliberately resurrect it, and then arranges for it to be released later:

```
                    ClearWeakRefsForObject((id)cf);
                    CFSetRemoveValue(gCFWeakTargets, cf);
                    CFRetain(cf);
                    CallCFReleaseLater(cf);
                }
            }
```

If the object has no weak references, then simply call through to the original finalize function without any fuss:

```
            else
            {
                void (*fptr)(CFTypeRef) = gCFOriginalFinalizes[CFGetTypeID(cf)];
                if(fptr)
                    fptr(cf);
            }
        });
    }
```

Easy enough, right? But how exactly does that `CallCFReleaseLater` function work?

Using `autorelease` would do the trick, except that this is pure CF code and there's no guarantee that the caller actually has an autorelease pool in place. A nice idea, but it just doesn't work out.

Some way to hook `CFRelease` to see when it exits would be ideal. But as discussed before, there's simply no available hook, so that goes out as well.

Ultimately I obtained some serious inspiration from Ed "Master of All Things Arcane" Wynne that it could really be done by using a completely insane technique similar to the cache-cleanup scheme in the Objective-C runtime.

**The Crazy Scheme**  
 To restate the problem: I need to call `CFRelease` on the object sometime after the original call to `CFRelease` has completed. Since there's no way to arrange this on the thread that made the original call to `CFRelease`, I make use of a background thread.

How can the background thread know when the original call to `CFRelease` has completed?

It's possible for one thread to access the PC (program counter, the location of the currently executing instruction) of another thread. Normally this is not very useful, but the Objective-C runtime uses it to see whether it's safe to destroy stale cache data by looking to see if any other threads are in a function that accesses it.

Likewise, this code can check the PC of the original calling thread and see if it's still within `CFRelease` or not. If it's not, then the call must have finished, so it's now safe to release the object again.

The only way (that I know of) to get the PC of another thread on OS X is to use mach calls, so the first step is to get a reference to the current mach thread. This reference is also "retained" (mach ports are reference counted, just like Objective-C objects) so that it doesn't go invalid in case the thread is destroyed in the mean time:

```
static void CallCFReleaseLater(CFTypeRef cf)
    {
        mach_port_t thread = pthread_mach_thread_np(pthread_self());
        mach_port_mod_refs(mach_task_self(), thread, MACH_PORT_RIGHT_SEND, 1 ); // "retain"
```

Next up, send this thread reference and the CF object pointer to a background thread. I use `NSOperationQueue` to handle the backgrounding. I create an `NSInvocationOperation` to handle the release (pointing it towards a class method on `MAZeroingWeakRef`, since it can't deal with pure functions) and add it to the queue. Everything is wrapped in an autorelease pool in case this code is being called from a context which doesn't already have one:

```
        NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
        SEL sel = @selector(releaseLater:fromThread:);
        NSInvocation *inv = [NSInvocation invocationWithMethodSignature: [MAZeroingWeakRef methodSignatureForSelector: sel]];
        [inv setTarget: [MAZeroingWeakRef class]];
        [inv setSelector: sel];
        [inv setArgument: &cf atIndex: 2];
        [inv setArgument: &thread atIndex: 3];
        
        NSInvocationOperation *op = [[NSInvocationOperation alloc] initWithInvocation: inv];
        [gCFDelayedDestructionQueue addOperation: op];
        [op release];
        [pool release];
    }
```

The code for `releaseLater:fromThread:` is based around a loop. It continuously checks the PC of the target thread until that PC has moved out of the target range. Once it's out, it releases the object as well as the thread that was passed in to it. To start with, the loop:

```
    + (void)releaseLater: (CFTypeRef)cf fromThread: (mach_port_t)thread
    {
        BOOL retry = YES;
        
        while(retry)
        {
```

Next, fetch the PC of the target thread. (`GetPC` is a helper function I'll get to in a moment.)

```
            BLOCK_QUALIFIER void *pc;
            // ensure that the PC is outside our inner code when fetching it,
            // so we don't have to check for all the nested calls
            WhileLocked({
                pc = GetPC(thread);
            });
```

Now start checking the PC for validity. First see if it contains anything at all. If not, assume a transient error occurred and try again (this may not be the best strategy...):

```
            if(pc)
            {
```

Next, see if the PC is within `CustomCFFinalize`. Since that's called from `CFRelease`, it's possible that the target is still in there, and we need to wait for it to exit. To do this, check the PC to see if it's between the start of that function and the start of the one following it. (The compiler lays out functions in order in memory, so the beginning of `IsTollFreeBridged` is right after the end of `CustomCFFinalize`):

```
                if(pc < (void *)CustomCFFinalize || pc > (void *)IsTollFreeBridged)
                {
```

If that test passes, see if the PC is within `CFRelease`. I don't know the order of functions in CoreFoundation so I can't use that same trick. Instead, I use the `dladdr` call. This returns the last symbol that comes before the specified address, among other info. I can just check that against `_CFRelease` (the private function that actually handles the guts of a `CFRelease` call). If it matches, try again later:

```
                    Dl_info info;
                    int success = dladdr(pc, &info;);
                    if(success)
                    {
                        if(info.dli_saddr != _CFRelease)
                        {
```

If all the tests pass, then it's good to go. Clear `retry` to indicate that the test succeeded, call `CFRelease`, and dispose of the thread reference:

```
                            retry = NO; // success!
                            CFRelease(cf);
                            mach_port_mod_refs(mach_task_self(), thread, MACH_PORT_RIGHT_SEND, -1 ); // "release"
                        }
                    }
                }
            }
        }
    }
```

One last thing, the `GetPC` function. The implementation is highly architecture-specific. The generalized part looks like this:

```
    static void *GetPC(mach_port_t thread)
    {
        // arch-specific code goes here
        
        kern_return_t ret = thread_get_state(thread, flavor, (thread_state_t)&state, &count;);
        if(ret == KERN_SUCCESS)
            return (void *)state.PC_REGISTER;
        else
            return NULL;
    }
```

The real code in the repository has conditionals that define `state`, `flavor`, and the rest for Intel 32/64, PPC 32/64, and ARM.

And that's it!

**Odds and Ends**  
 In the previous post, I mentioned the `COREFOUNDATION_HACK_LEVEL` macro that controls how much hack `MAZeroingWeakRef` contains. When set to 0, it makes use of no private API. It refuses to reference CoreFoundation objects, and detects them by checking the class name for an `NSCF` prefix. When set to 1, it only uses private API to make a reliable CoreFoundation object check. Level 1 is now the default.

When I wrote the previous post, I didn't actually know about this subtle resurrection race condition. As such, I've added an extra hack level. Hack level 2 uses private CoreFoundation calls to allow referencing CF objects, but does not eliminate the resurrection race condition I described above. Finally, the newly-added hack level 3 goes into full-on CoreFoundation hackery as described above, and eliminates the race condition by doing the final `CFRelease` in a background thread.

These can be controlled using the `COREFOUNDATION_HACK_LEVEL` macro at the top of the file. I recommend level 1 for Mac development (weak references to CoreFoundation objects are not commonly needed) and level 0 for iOS development (Apple gets their underwear in a twist over private API usage). However, if you're adventurous or need weak references to CF objects, you can set it to 3 and everything _should_ still work.... If you do, keep in mind that the really horrible hacks don't activate until you actually create a weak reference to a CF object, so you can enable it just in case you inadvertently reference a CF object, but not worry about it doing anything terrible in the normal case.

**Conclusion**  
 In the last post I showed how to create zeroing weak references to Objective-C objects with relative ease. In this post, I show that doing the same to CoreFoundation objects is, if not easy, at least possible. A great deal of mucking about with private APIs is required, but the solution should be fairly robust.

This kind of hackery is extremely challenging but it's also a lot of fun. The CoreFoundation source code is a valuable resource for this kind of thing, but as always you must beware of private symbols which may change in the future. Other low-level open source code like the Objective-C runtime can also be a handy read. Finally, `otx` is an extremely useful tool for when you need to see how a library works when Apple doesn't provide source.

That's it for this edition of Friday Q&A. Come back in two weeks for more wacky hijinks.

As always, Friday Q&A is driven by user ideas. If you have a topic that you would like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-07-30-zeroing-weak-references-to-corefoundation-objects.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
