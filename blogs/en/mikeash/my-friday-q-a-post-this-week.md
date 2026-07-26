---
title: 'my Friday Q&A post this week'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-07-16-zeroing-weak-references-in-objective-c.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b29d67a58328e208'
translated: false
---

> 原文：[my Friday Q&A post this week](https://www.mikeash.com/pyblog/friday-qa-2010-07-16-zeroing-weak-references-in-objective-c.html)　·　mikeash.com Friday Q&A

Posted at 2010-07-16 20:18 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Introducing MAZeroingWeakRef](https://www.mikeash.com/pyblog/introducing-mazeroingweakref.html)  
Previous article: [Friday Q&A 2010-07-02: Background Timers](https://www.mikeash.com/pyblog/friday-qa-2010-07-02-background-timers.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [garbagecollection](https://www.mikeash.com/pyblog/?tag=garbagecollection) [hack](https://www.mikeash.com/pyblog/?tag=hack) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2010-07-16: Zeroing Weak References in Objective-C

by [Mike Ash](https://www.mikeash.com/)

**Weak References**  
 First, what is a weak reference? Simply put, a weak reference is a reference (pointer, in Objective-C land) to an object which does not participate in keeping that object alive. For example, using memory management, this setter creates a weak reference to the new object:

```
    - (void)setFoo: (id)newFoo
    {
        _foo = newFoo;
    }
```

Because the setter does not use

, the reference does not keep the new object alive. It will stay alive as long as it's retained by other references, of course. But once those go away, the object will be deallocated even if

still points to it.

Weak references are common in Cocoa in order to deal with [retain cycles](https://www.mikeash.com/pyblog/friday-qa-2010-04-30-dealing-with-retain-cycles.html). Delegates in Cocoa are almost always weak references for exactly this reason.

**Zeroing Weak References**  
 Weak references are useful for things like avoiding retain cycles, but their utility is limited due to their inherent danger. With a plain weak reference in Objective-C, when the target object is destroyed, you're left with a dangling pointer. If your code tries to use that pointer, it will crash or worse.

Zeroing weak references eliminate this danger. They work just like a regular weak reference, except that when the target object is destroyed, they automatically become `nil`. At any time you access an object through a zeroing weak reference, you're guaranteed to either access a valid, live object, or get `nil`. As long as your code can handle `nil`, then you're perfectly safe.

Because of this safety, a zeroing weak reference can be useful for much more than the unsafe kind. One example is an object cache. An object cache using weak references can refer to objects as long as they're alive, and then let them deallocate when no longer needed. If a client requests an object that's still alive, it can obtain it without having to create a new object. If the object has already been destroyed, the cache can safely create a new object.

They can be used for much more mundane purposes as well, for any case where you want to keep a reference to an object but don't want to keep that object in memory beyond its normal lifetime. For example, you might track a window but not want to keep it in memory after it's closed. You could deal with this by setting up a notification observer and seeing when the window goes away, but a zeroing weak reference is a much simpler way to do it. As another example, a zeroing weak reference to `self` used in a block can prevent a retain cycle while ensuring that your program doesn't crash if the block is called after `self` is deallocated. Even a standard delegate pointer is made better with a zeroing weak reference, as it eliminates rare but annoying bugs which can appear if the delegate is deallocated before the object that points to it.

If you're using garbage collection in Objective-C, then good news! The Objective-C garbage collector already supports zeroing weak references using the type modifier `__weak`. You can just declare any instance variable like so:

```
    __weak id _foo;
```

And it's automatically a zeroing weak reference. The compiler takes care of emitting the appropriate read/write barriers so that access is always safe.

What if you aren't using garbage collection, though? While it would be great if we all could, many of us can't for various reasons, one of the most common being that garbage collection simply isn't supported on iOS. Well, until now you've been out of luck when it comes to zeroing weak references with manual memory management in Objective-C.

**Introducing `MAZeroingWeakRef`**  
 Those of us who use manual memory management can now benefit from zeroing weak references! `MAZeroingWeakRef` implements the following interface:

```
    @interface MAZeroingWeakRef : NSObject
    {
        id _target;
    }
    
    + (id)refWithTarget: (id)target;
    
    - (id)initWithTarget: (id)target;
    
    - (void)setCleanupBlock: (void (^)(id target))block;
    
    - (id)target;
    
    @end
```

Usage is extremely simple. Initialize it with a target object. Retrieve the target object when you need to use it. The

method will either return the target object (retained/autoreleased to guarantee that it will stay alive until you're done with it) or, if the target has already been destroyed, it will return

.

The `-setCleanupBlock:` method exists for more advanced uses. Normally a zeroing weak reference is a passive object. You can query its target at any time, and it either gives you an object or `nil`. But sometimes you want to take some additional action when the reference is zeroed out, such as unregistering a notification observer. The block passed to `-setCleanupBlock:` runs when the reference is zeroed out, allowin gyou to set up additional actions like that.

As an example, here's how to write the standard delegate pattern using `MAZeroingWeakRef`:

```
    // instance variable
    MAZeroingWeakRef *_delegateRef;
    
    // setter
    - (void)setDelegate: (id)newDelegate
    {
        [_delegateRef release];
        _delegateRef = [[MAZeroingWeakRef alloc] initWithTarget: newDelegate];
    }
    
    - (void)doSomethingAndCallDelegate
    {
        [self _doSomething];
        
        id delegate = [_delegateRef target];
        if([delegate respondsToSelector: @selector(someDelegateMethod)])
            [delegate someDelegateMethod];
    }
```

This is only slightly harder than using normal, dangerous weak references, and provides complete safety. (If you use this pattern, remember that you must now release

in

!)

`MAZeroingWeakRef` is completely thread safe, both in terms of accessing it from multiple threads, and in terms of having the target object be destroyed in one thread while the weak reference is accessed from another thread.

**How Does it Work?**  
 The concept of how a zeroing weak reference works is pretty straightforward. Track all such references to a target. When an object is destroyed, zero out all of those references before calling `dealloc`. Wrap everything in a lock so that it's thread safe.

The details of how to accomplish each step can get tricky, though.

Tracking all zeroing weak references to a target isn't too tough. A global `CFMutableDictionary` maps targets to `CFMutableSet` objects which hold the zeroing weak references to each target. I use the CF classes so that I can customize the memory management; I don't want the targets or weak references to be retained.

Zeroing all of the weak references before calling `dealloc` gets a little trickier....

The answer to that is to use dynamic subclassing, as done in the implementation of [Key-Value Observing](http://www.mikeash.com/pyblog/friday-qa-2009-01-23.html). When an object is targeted by a zeroing weak reference, a new subclass of that object's class is created. The `-dealloc` method of the new subclass takes care of zeroing out all of the weak references and then calls through to `super` so that the normal chain of deallocations can occur. The new subclass also overrides `-release` to take a lock so that everything is thread safe. (Without that override, it would be possible for one thread to `release` an object with a retain count of 1 at the same time that another thread retrieved the object from a `MAZeroingWeakRef`. The retrieval would then try to resurrect the object after it had already been marked for destruction, which is illegal.)

Of course you don't want to make a new subclass for every single targeted object, but only one subclass is necessary per target class. A small table of overridden classes ensures that no more than one new subclass is created for each normal class.

As the final step, the class of the target object is set to be the new subclass, ensuring that the new methods take effect.

**CoreFoundation Trickiness**  
 The above strategy runs into a snag with [toll-free bridged classes like `NSCFString`](http://www.mikeash.com/pyblog/friday-qa-2010-01-22-toll-free-bridging-internals.html). Because of the way they're implemented, changing the class of such an object causes infinite recursion and a crash the moment that something tries to use them. The CoreFoundation code sees the changed class, assumes it's a pure Objective-C class, and calls through to the equivalent Objective-C method. The `NSCF` method then calls back to CoreFoundation. A crash rapidly ensues.

While I did figure out a solution to this problem, it is so hairy and complicated that I will save it for a separate article to be posted in two weeks.

**Code**  
 As usual, you can get the code for `MAZeroingWeakRef` from my public Subversion repository:

```
    svn co http://mikeash.com/svn/ZeroingWeakRef/
```

Or just click the link above to browse the code.

I will be walking through a somewhat abbreviated version of `MAZeroingWeakRef`. Due to the crazy nature of the CoreFoundation workaround I mentioned above, I will skip over those parts and only discuss the sane Objective-C bits this week. There is a macro called `COREFOUNDATION_HACK_LEVEL` which allows control over how much CoreFoundation hackery is enabled. At level `2` you get full-on hackery with full support for weak references to CoreFoundation objects. With level `1`, some less important private symbols are referenced and used to reliably decide whether an object is bridged or not, and the code simply asserts if trying to create a weak reference to a bridged object. At level `0`, the code asserts when trying to create a weak reference to a bridged object, and checks for bridging simply by looking for a prefix of `NSCF` in the class name. For this week, I will be discussing the code as if it were compiled with level `0`.

**Globals**  
 `MAZeroingWeakRef` makes use of some global variables for various housekeeping uses. First off is a mutex:

```
    static pthread_mutex_t gMutex;
```

This is used to protect the other global data structures, as well as the table of zeroing weak references that's attached to each target object.

Next up, a `CFMutableDictionary` is needed to map the target objects to the weak references which target them:

```
    static CFMutableDictionaryRef gObjectWeakRefsMap; // maps (non-retained) objects to CFMutableSetRefs containing weak refs
```

Next, an

is used to track the dynamic subclasses that are created, and an

is used to map from normal classes to their dynamic subclasses:

```
    static NSMutableSet *gCustomSubclasses;
    static NSMutableDictionary *gCustomSubclassMap; // maps regular classes to their custom subclasses
```

Finally, implement

to set up all of these variables. The only tricky business here is that it uses a recursive mutex rather than a regular one. There are cases where the critical section can be re-entered, such as creating a

pointing to another

, and using a recursive mutex allows that to function.

```
    + (void)initialize
    {
        if(self == [MAZeroingWeakRef class])
        {
            CFStringCreateMutable(NULL, 0);
            pthread_mutexattr_t mutexattr;
            pthread_mutexattr_init(&mutexattr;);
            pthread_mutexattr_settype(&mutexattr, PTHREAD_MUTEX_RECURSIVE);
            pthread_mutex_init(&gMutex, &mutexattr;);
            pthread_mutexattr_destroy(&mutexattr;);
            
            gCustomSubclasses = [[NSMutableSet alloc] init];
            gCustomSubclassMap = [[NSMutableDictionary alloc] init];
        }
    }
```

I also write a quick helper to execute a block of code while holding the lock:

```
    static void WhileLocked(void (^block)(void))
    {
        pthread_mutex_lock(&gMutex;);
        block();
        pthread_mutex_unlock(&gMutex;);
    }
```

And three more helpers to deal with adding a weak reference to an object's

, removing a weak reference from an object, and clearing out all weak references to an object:

```
    static void AddWeakRefToObject(id obj, MAZeroingWeakRef *ref)
    {
        CFMutableSetRef set = (void *)CFDictionaryGetValue(gObjectWeakRefsMap, obj);
        if(!set)
        {
            set = CFSetCreateMutable(NULL, 0, NULL);
            CFDictionarySetValue(gObjectWeakRefsMap, obj, set);
            CFRelease(set);
        }
        CFSetAddValue(set, ref);
    }
    
    static void RemoveWeakRefFromObject(id obj, MAZeroingWeakRef *ref)
    {
        CFMutableSetRef set = (void *)CFDictionaryGetValue(gObjectWeakRefsMap, obj);
        CFSetRemoveValue(set, ref);
    }
    
    static void ClearWeakRefsForObject(id obj)
    {
        CFMutableSetRef set = (void *)CFDictionaryGetValue(gObjectWeakRefsMap, obj);
        [(NSSet *)set makeObjectsPerformSelector: @selector(_zeroTarget)];
        CFDictionaryRemoveValue(gObjectWeakRefsMap, obj);
    }
```

With those basics in place, I'll now take a top-down approach to the rest of the implementation.

First, the convenience constructor and initializer. Mostly straightforward:

```
    + (id)refWithTarget: (id)target
    {
        return [[[self alloc] initWithTarget: target] autorelease];
    }
    
    - (id)initWithTarget: (id)target
    {
        if((self = [self init]))
        {
            _target = target;
            RegisterRef(self, target);
        }
        return self;
    }
```

The only tricky bit is that call to

. That's an internal utility function which takes care of connecting the weak reference object to the target object, subclassing the target's class if necessary, and changing the target's class to be the custom subclass.

The `dealloc` implementation similarly calls a utility function to remove the weak reference object:

```
    - (void)dealloc
    {
        UnregisterRef(self);
        [_cleanupBlock release];
        [super dealloc];
    }
```

Toss in a simple

method so we can see what's going on internally:

```
    - (NSString *)description
    {
        return [NSString stringWithFormat: @"<%@: %p -> %@>", [self class], self, [self target]];
    }
```

And a standard setter for setting the cleanup block:

```
    - (void)setCleanupBlock: (void (^)(id target))block
    {
        block = [block copy];
        [_cleanupBlock release];
        _cleanupBlock = block;
    }
```

The

method gets a little more complicated. Because the target can be destroyed at any time, it needs to fetch its value while holding the global weak reference lock. It also needs to retain the target while holding that lock, to ensure that, if the target is alive, it

alive until the receiver is done using it. This is of course balanced with an autorelease afterwards:

```
    - (id)target
    {
        __block id ret;
        WhileLocked(^{
            ret = [_target retain];
        });
        return [ret autorelease];
    }
```

Finally there's a private method used to zero out the target, which is called by the internal machinery when the target object is deallocated. Since the global lock is already held by that machinery, there's no need to explicitly lock it here too. This method simply calls and releases the cleanup block if there is one, and clears out the target;

```
    - (void)_zeroTarget
    {
        if(_cleanupBlock)
        {
            _cleanupBlock(_target);
            [_cleanupBlock release];
            _cleanupBlock = nil;
        }
        _target = nil;
    }
```

And that's it! Easy, right? Of course, all the interesting bits are in those utility functions, the utility functions

call, and on and on....

**Implementation of Utility Functions**  
 The implementation of `UnregisterRef` is simple. Get the target out of the `MAZeroingWeakRef`, get the table of references to the target, and remove the given reference. Wrap it all in a lock to ensure that the target can't be deallocated in the middle of this operation:

```
    static void UnregisterRef(MAZeroingWeakRef *ref)
    {
        WhileLocked(^{
            id target = ref->_target;
            
            if(target)
                RemoveWeakRefFromObject(target, ref);
        });
    }
```

is similar. In addition to adding the reference to the table of references, it also calls

. That function will, if necessary, create a new custom subclass and set the class of the target object to that subclass.

```
    static void RegisterRef(MAZeroingWeakRef *ref, id target)
    {
        WhileLocked(^{
            EnsureCustomSubclass(target);
            AddWeakRefToObject(target, ref);
        });
    }
```

The implementation of

is broken into many pieces. First it checks to see if the object is

an instance of a custom subclass. If it is, then nothing has to be done. If it's not, it then looks up the custom subclass that corresponds to the object's current class, and sets the class of the target object accordingly. If no custom subclass has yet been created, it creates it.

```
    static void EnsureCustomSubclass(id obj)
    {
        if(!GetCustomSubclass(obj))
        {
            Class class = object_getClass(obj);
            Class subclass = [gCustomSubclassMap objectForKey: class];
            if(!subclass)
            {
                subclass = CreateCustomSubclass(class, obj);
                [gCustomSubclassMap setObject: subclass forKey: class];
                [gCustomSubclasses addObject: subclass];
            }
            object_setClass(obj, subclass);
        }
    }
```

The implementation of

is easy. Get the object's class, and check to see if it's in the

set. If not, get the superclass, and follow it up the chain until one is found. If none are found, then there is no custom subclass for this object. (The reason for following the chain is so that this code will still behave correctly even if some other code, such as Key-Value Observing, sets its own custom subclass after

set one.)

```
    static Class GetCustomSubclass(id obj)
    {
        Class class = object_getClass(obj);
        while(class && ![gCustomSubclasses containsObject: class])
            class = class_getSuperclass(class);
        return class;
    }
```

Again, not too hard. The real fun begins in

. The first thing it does is check to see if the object is a CoreFoundation toll-free bridged object. As I discussed above, the subclassing approach breaks for those objects, so they need to be rejected:

```
    static Class CreateCustomSubclass(Class class, id obj)
    {
        if(IsTollFreeBridged(class, obj))
        {
            NSCAssert(0, @"Cannot create zeroing weak reference to object of type %@ with COREFOUNDATION_HACK_LEVEL set to %d", class, COREFOUNDATION_HACK_LEVEL);
            return class;
        }
        else
        {
```

(

is the

which determines how much CoreFoundation hackery to enable. As I mentioned above, I'm going through the code as through it's not enabled.)

The implementation of `IsTollFreeBridged` simply checks to see if the class name starts with `NSCF`:

```
    static BOOL IsTollFreeBridged(Class class, id obj)
    {
        return [NSStringFromClass(class) hasPrefix: @"NSCF"];
    }
```

For the

branch, the first order of business is to create a name for the new class. Since Objective-C class names have to be unique, it constructs a new name based on the original name and a unique suffix:

```
            NSString *newName = [NSString stringWithFormat: @"%s_MAZeroingWeakRefSubclass", class_getName(class)];
            const char *newNameC = [newName UTF8String];
```

Next, call

to create a new class pair. (In Objective-C, each class has a corresponding metaclass, which is related to how the runtime works. The

function creates both in one shot.)

```
            Class subclass = objc_allocateClassPair(class, newNameC, 0);
```

The new class implements two methods,

and

. The next step is then to add those two methods to the class, pointing them to the functions which implement them:

```
            Method release = class_getInstanceMethod(class, @selector(release));
            Method dealloc = class_getInstanceMethod(class, @selector(dealloc));
            class_addMethod(subclass, @selector(release), (IMP)CustomSubclassRelease, method_getTypeEncoding(release));
            class_addMethod(subclass, @selector(dealloc), (IMP)CustomSubclassDealloc, method_getTypeEncoding(dealloc));
```

Finally, call

to register the new class with the runtime, and return the newly created class:

```
            objc_registerClassPair(subclass);
            
            return subclass;
        }
    }
```

Next,

. Conceptually, the implementation of this class is simple. Acquire the global weak reference lock, and call

while it's acquired. The purpose of this is to ensure that the final release for an object and its deallocation happens atomically, and an object can't be resurrected in between the two by a weak reference that hasn't yet been zeroed out.

The trouble is that simply writing `[super release]` won't work, because the compiler only allows that in a true, compile-time method implementation. In order to perform the equivalent action, it's necessary to figure out the superclass of the custom weak reference subclass. This is done using a simple helper function which calls `GetCustomSubclass` and returns the superclass of that class:

```
    static Class GetRealSuperclass(id obj)
    {
        Class class = GetCustomSubclass(obj);
        NSCAssert(class, @"Coudn't find ZeroingWeakRef subclass in hierarchy starting from %@, should never happen", object_getClass(obj));
        return class_getSuperclass(class);
    }
```

With that helper in place, the implementation of

can use it to look up the superclass, use that to look up the superclass's implementation of

, and then call that with the lock held:

```
    static void CustomSubclassRelease(id self, SEL _cmd)
    {
        Class superclass = GetRealSuperclass(self);
        IMP superRelease = class_getMethodImplementation(superclass, @selector(release));
        WhileLocked(^{
            ((void (*)(id, SEL))superRelease)(self, _cmd);
        });
    }
```

Almost done! The one remaining function is

. It gets the table of weak references to the object and tells all of them to

. It then invokes the superclass implementation of

using the same technique as

uses.

```
    static void CustomSubclassDealloc(id self, SEL _cmd)
    {
        ClearWeakRefsForObject(self);
        Class superclass = GetRealSuperclass(self);
        IMP superDealloc = class_getMethodImplementation(superclass, @selector(dealloc));
        ((void (*)(id, SEL))superDealloc)(self, _cmd);
    }
```

That's it! You now have zeroing weak references to Objective-C objects (except to bridged CoreFoundation objects, which I'll get to next week).

**Examples:**  
 Basic usage of `MAZeroingWeakRef` is simple:

```
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    NSObject *obj = [[NSObject alloc] init];
    MAZeroingWeakRef *ref = [[MAZeroingWeakRef alloc] initWithTarget: obj];
    
    NSLog(@"%@", [ref target]);
    [obj release];
    [pool release];
    
    NSLog(@"%@", [ref target]);
```

The first

will print the object, and the second will print

. The autorelease pool is used to ensure that the object is truly destroyed, because the use of

will put the object into the pool and otherwise it will stay alive longer.

Using a cleanup block is similarly simple:

```
    NSObject *obj = [[NSObject alloc] init];
    MAZeroingWeakRef *ref = [[MAZeroingWeakRef alloc] initWithTarget: obj];
    [ref setCleanupBlock: ^(id target) { NSLog(@"Cleaned object %p!", target); }];
    [obj release];
```

The log will print when

is called. Of course you can take more actions than simply printing. However, because the cleanup block is called while the global weak reference lock is held, you should try to keep your activities in there to a minimum. If you need to do a lot of work, set up a deferred call, using

, GCD, NSOperationQueue, etc. and do the extra work there.

A simple way to turn a regular instance variable into a zeroing weak reference is to use `MAZeroingWeakRef` in your getter and setter, and then make sure to always use your getter in other code:

```
    // ivar
    MAZeroingWeakRef *_somethingWeakRef;
    
    // accessors
    - (void)setSomething: (Something *)newSomething
    {
        [_somethingWeakRef release];
        _somethingWeakRef = [[MAZeroingWeakRef alloc] initWithTarget: newSomething];
    }
    
    - (Something *)something
    {
        return [_somethingWeakRef target];
    }
    
    // use
    - (void)doThing
    {
        [[self something] doThingWithObject: self];
    }
```

And of course if you do that, you have to be sure to release your reference in

, just like any other object you allocate. Just don't release the target.

For a more advanced use, here's an addition to `NSNotificationCenter` that eliminates the need to manually remove an observer in `dealloc`:

```
    @implementation NSNotificationCenter (MAZeroingWeakRefAdditions)
    
    - (void)addWeakObserver: (id)observer selector: (SEL)selector name: (NSString *)name object: (NSString *)object
    {
        [self addObserver: observer selector: selector name: name object: object];
        
        MAZeroingWeakRef *ref = [[MAZeroingWeakRef alloc] initWithTarget: observer];
        [ref setCleanupBlock: ^(id target) {
            [self removeObserver: target name: name object: object];
            [ref autorelease];
        }];
    }
    
    @end
```

Note the use of a cleanup block to remove the notification observer when the object is destroyed. All you have to do is call

instead of

in notification observers, and you'll never again forget to remove an observer in

.

Similarly, if you're tired of mysterious crashes caused by NSTableView data sources being deallocated before the views themselves, you can easily fix it:

```
    @implementation NSTableView (MAZeroingWeakRefAdditions)
    
    - (void)setWeakDataSource: (id <NSTableViewDataSource>)source
    {
        [self setDataSource: source];
        
        MAZeroingWeakRef *ref = [[MAZeroingWeakRef alloc] initWithTarget: observer];
        [ref setCleanupBlock: ^(id target) {
            if([self dataSource] == target) // double check for safety
                [self setDataSource: nil];
            [ref autorelease];
        }];
    }
    
    @end
```

If you anticipate a scenario where you change the data source of a table view frequently, you'll want to write some more sophisticated code to clear out the old weak reference when adding a new one. However that is not a common scenario.

Essentially, any time you have a weak reference (an object reference that you don't retain or copy), you should use a `MAZeroingWeakRef` instead of a raw unretained pointer. It will save you trouble and pain and is extremely easy to use.

**ZeroingCollections**  
 The repository includes `MAWeakArray` and `MAWeakDictionary`, subclasses of `NSMutableArray` and `NSMutableDictionary` which use zeroing weak references to their contents. `MAWeakDictionary` uses strong keys to weak objects, which would be useful for many caching scenarios. I won't go through their code here, but they're simple, and you can look at the code in the repository if you're curious.

Although I didn't write them, it would be possible to creat a weak version of `NSMutableSet` and `NSMutableDictionary` which uses weak keys instead of, or in addition to, weak objects. These would be trickier due to hashing/equality issues with the weak references, but could certainly be done.

**Conclusion**  
 Zeroing weak references are an extremely useful construct present in many languages. Even Objective-C has them when running under garbage collection, but without GC, Objective-C code has been stuck using non-zeroing weak references, which are tricky and dangerous.

`MAZeroingWeakRef` brings zeroing weak references to manual memory managed Objective-C. Although it uses some trickery on the inside, the API is extremely simple to use. By automatically zeroing weak references, you avoid many potential crashers and data corruption. Zeroing weak references can also be used for things like object caches where non-zeroing weak references aren't very practical at all.

The code is made available under a BSD license.

For the next Friday Q&A in two weeks, I will discuss how `MAZeroingWeakRef` works around the problems with CoreFoundation objects. Until then, enjoy!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
