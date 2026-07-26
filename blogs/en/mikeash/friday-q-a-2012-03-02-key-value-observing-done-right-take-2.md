---
title: 'Friday Q&A 2012-03-02: Key-Value Observing Done Right: Take 2'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-03-02-key-value-observing-done-right-take-2.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6928ebc07b61e6b8'
translated: false
---

> 原文：[Friday Q&A 2012-03-02: Key-Value Observing Done Right: Take 2](https://www.mikeash.com/pyblog/friday-qa-2012-03-02-key-value-observing-done-right-take-2.html)　·　mikeash.com Friday Q&A

Posted at 2012-03-02 14:09 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-03-09: Let's Build NSMutableArray](https://www.mikeash.com/pyblog/friday-qa-2012-03-09-lets-build-nsmutablearray.html)  
Previous article: [Friday Q&A 2012-02-17: Ring Buffers and Mirrored Memory: Part II](https://www.mikeash.com/pyblog/friday-qa-2012-02-17-ring-buffers-and-mirrored-memory-part-ii.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [followup](https://www.mikeash.com/pyblog/?tag=followup) [guest](https://www.mikeash.com/pyblog/?tag=guest) [kvo](https://www.mikeash.com/pyblog/?tag=kvo) [semi-evil](https://www.mikeash.com/pyblog/?tag=semi-evil)

Friday Q&A 2012-03-02: Key-Value Observing Done Right: Take 2

by [Gwynne Raskind](http://blog.darkrainfall.org/)

---

**Ruminations on Apple's efforts**  
Key-Value Observing has been around since Panther (10.3), and since then it has received three publicly-visible updates:

1. In Tiger, mutation types for unordered collections (sets) was added.
2. In Leopard, "initial" and "prior" observations, along with a much-improved means for registering dependent keys, were added.
3. In Lion (and iOS 5), methods were added for removing registered observations based on a passed context.

In Mike Ash's article in 2008, circa Leopard, he described three major issues. Of those, only one has been solved since (the missing context parameter to observation removal). The other two, a lack of custom selectors and the uselessness of the context pointer, remain unsolved, and more issues have arisen since:

- With Snow Leopard, we got blocks, but KVO has completely ignored them.
- KVO's inability to deal with objects whose observations are never unregistered has never even been challenged.
- got blocks and targeted observation removal (returning an object from the add call that could be used to remove that same observation later). KVO also missed that latter.
- KVO never had a "remove all observers on this object" or "remove all observations registered by this object" semantic, making subclassing and extension that much more painful.
- KVO has no syntax for registering more than one key path at a time for observation. Or for observing more than one object at a time.
- ) imposed an extra retain on both the observing and observed objects, leading to a tendency towards retain cycles and an inability to remove observations in a

  method.

All of these are things Apple should have dealt with, and bugs filed against all of these limitations resulted in only one change in two major OS releases.

It is my personal opinion that KVO received so little attention because it was originally implemented as nothing more than a piece of the puzzle behind Cooca bindings. Cocoa bindings have been, in the opinion of many (including myself), a dismal failure in their intended purpose of making UI easy to wire up to code. It still works for the things Apple uses it for, and that's good enough for them.

That wasn't good enough for me, though.

**Designing a better KVO**  
For a long time, I'd used `MAKVONotificationCenter` with some extra tweaks by the inspired Jerry Krinock (see the comments on [Mike's original article](https://www.mikeash.com/pyblog/key-value-observing-done-right.html#comment-c725ea36f22415152e31afb4c45e3d46) and myself which added basic blocks support as well as both less and more specific observer unregistration. But that implementation was a bit inelegant and still suffered from the retain cycle issue. I finally decided to sit down and hack out something a little more formal.

The "new and improved" KVO needed the following features, in my eyes:

- It had to solve all three of Mike's listed issues, and therefore had to be based on his original implementation to at least some extent.
- It needed to support blocks as observer callbacks.
- It needed to support "automatic deregistration", i.e. removing any observations an object had registered, or had registered on it, during deallocation.
- easier to register multiple key paths, and key paths on multiple objects.
- to retain observer or observee.

**Implementing the new and improved KVO**  
The first step was to build the interface for this new version of KVO. Starting from `MAKVONotificationCenter`, I added;

- A flag to turn off the automatic deregistration behavior. Since a tiny bit of runtime trickery was definitely going to be involved in that, I figured it'd be best to be able to shut it off on demand.
- A protocol for an "observation". This would be a generic object returned by observation registration methods that could be used to remove that specific registration. It could be queried as to whether the registration was still valid.
- ,

  ,

  , and

  got this support for free.
- . This object would be passed to an observation block and provide convenient access to everything normally hidden in a change dictionary.
- The category on NSObject to provide the selector- and block-based registration methods, as well as the complementary unregistration methods. I also put in "opposite sentiment" methods, since I don't like KVO's order of doing things.

  KVO's original methods go "`[target addObserver:observer ...]`". To me, telling the target of the observation to add an observer is backwards. So I added "`[observer observeTarget:target ...]`" methods, which had the daunting and difficult task of sending the parameters to `MAKVONoticationCenter`'s methods in the opposite order.
- In that same category, methods for unregistering observations based on any combination of observer, target, key path, selector, including none.

Starting from Mike's implementation, adding blocks support was quite trivial:

```
    #if NS_BLOCKS_AVAILABLE
            if (_selector)
    #endif
                ((void (*)(id, SEL, NSString *, id, NSDictionary *, id))objc_msgSend)(_observer, _selector, keyPath, object, change, _userInfo);
    #if NS_BLOCKS_AVAILABLE
            else
            {
                MAKVONotification       *notification = nil;

                // Pass object instead of _target as the notification object so that
                //  array observations will work as expected.
                notification = [[MAKVONotification alloc] initWithObserver:_observer object:object keyPath:keyPath change:change];
                ((void (^)(MAKVONotification *))_userInfo)(notification);
            }
    #endif
```

The appropriate "register an observervation" routines simply passed the helper object a `NULL` selector and the block as the user info. `MAKVONotification`'s implementation was very trivial, just passing it the appropriate data and adding a few accessors to grab the data from the dictionary.

The code for handling "key path sets" was also pretty trivial:

```
    NSMutableSet                *keyPaths = [NSMutableSet set];

    for (NSString *path in [keyPath ma_keyPathsAsSetOfStrings])
        [keyPaths addObject:path];

    _MAKVONotificationHelper    *helper = [[_MAKVONotificationHelper alloc] initWithObserver:observer object:target keyPaths:keyPaths selector:selector userInfo:userInfo options:options];
```

The key paths are copied into a set to avoid the requirement that the original key paths object (or the object it returns) have a persistent and immutable lifetime. The default implementations I provided for `NSArray` and `NSSet`, for example, return `self` as the "set of strings", and they could easily be mutable, which would be trouble later when the helper object needed to unregister its observation.

Making it possible to observe more than one object at a time was done by detecting an array target:

```
    for (NSString *keyPath in _keyPaths)
    {
        if ([target isKindOfClass:[NSArray class]])
        {
            [target addObserver:self toObjectsAtIndexes:[NSIndexSet indexSetWithIndexesInRange:NSMakeRange(0, [target count])]
                     forKeyPath:keyPath options:options context:&MAKVONotificationHelperMagicContext];
        }
        else
            [target addObserver:self forKeyPath:keyPath options:options context:&MAKVONotificationHelperMagicContext];
    }
```

Rather than using a central dictionary of helpers to track observations, which required expensive string building and was unreliable in any case for blocks, I added each helper object to both the observer and target as an associated object:

```
    NSMutableSet                *observerHelpers = nil;

    if (_observer) {
        @synchronized (_observer)
        {
            if (!(observerHelpers = objc_getAssociatedObject(_observer, &MAKVONotificationCenter_HelpersKey)))
                objc_setAssociatedObject(_observer, &MAKVONotificationCenter_HelpersKey, observerHelpers = [NSMutableSet set], OBJC_ASSOCIATION_RETAIN_NONATOMIC);
        }
        @synchronized (observerHelpers) { [observerHelpers addObject:self]; }
    }
```

Some may object to the condensed value-of-assignment syntax I used here, but it works. The `@synchronized` blocks make the operations thread-safe. Now removing a particular observation based on some combination of target, observer, key path, and selector becomes relatively simple:

```
    - (void)removeObserver:(id)observer object:(id)target keyPath:(id<MAKVOKeyPathSet>)keyPath selector:(SEL)selector
    {
        NSParameterAssert(observer || target);  // at least one of observer or target must be non-nil

        @autoreleasepool
        {
            NSMutableSet                *observerHelpers = objc_getAssociatedObject(observer, &MAKVONotificationCenter_HelpersKey) ?: [NSMutableSet set],
                                        *targetHelpers = objc_getAssociatedObject(target, &MAKVONotificationCenter_HelpersKey) ?: [NSMutableSet set],
                                        *allHelpers = [NSMutableSet set],
                                        *keyPaths = [NSMutableSet set];

            for (NSString *path in [keyPath ma_keyPathsAsSetOfStrings])
                [keyPaths addObject:path];
            @synchronized (observerHelpers) { [allHelpers unionSet:observerHelpers]; }
            @synchronized (targetHelpers) { [allHelpers unionSet:targetHelpers]; }

            for (_MAKVONotificationHelper *helper in allHelpers)
            {
                if ((!observer || helper->_observer == observer) &&
                    (!target || helper->_target == target) &&
                    (!keyPath || [helper->_keyPaths isEqualToSet:keyPaths]) &&
                    (!selector || helper->_selector == selector))
                {
                    [helper deregister];
                }
            }
        }
    }
```

First, get the list of helpers on both target and observer. I make heavy use of the fact that sending messages to `nil` is harmless and always returns `nil` to avoid extra checks, at the cost of a small allocation or two. Then build the list of key paths into a set, and combine the target and observer's helper lists as a single set, thread-safely. Because sets are unique collections, there will be no duplicate helpers in this combined list.

Now loop over all the helpers in that list and check whether each one matches the criteria specified - does it have the right observer, the right target, the right set of key paths, and the right selector? (Note: The code checks for exact equality of key path sets, rather than whether the helper being checked observes "any" of the paths passed instead of "all" of them. It didn't strike me that it'd be worth the extra effort to add the extra checks.) If so, deregister that helper, which will handle its own thread safety.

**Automatically removing KVO notifications at object deallocation**  
The most complicated new feature of this improved KVO was no longer having to find a place to call `[self removeAllObservations]`, even if that place was `-dealloc`. This was in spirit with ARC's lack of need to call `[super dealloc]`; I almost never need to remove an observation before the observer or target is deallocated, and keeping track of when to do so can get pretty arduous.

The most obvious way to always unregister observations at `dealloc` is to do it from the `-dealloc` method. That meant either dynamic subclassing or swizzling. Since KVO already does dynamic subclassing, that was a layer of complexity I wasn't prepared to delve into. I chose method swizzling.

My `MAKVONotificationCenter` calls `-_swizzleObjectClassIfNeeded:` on both the observer and target objects. It looks like this:

```
    - (void)_swizzleObjectClassIfNeeded:(id)object
    {
        if (!object)
            return;
        @synchronized (MAKVONotificationCenter_swizzledClasses)
        {
            Class           class = [object class];//object_getClass(object);

            if ([MAKVONotificationCenter_swizzledClasses containsObject:class])
                return;

            SEL             deallocSel = NSSelectorFromString(@"dealloc");/*@selector(dealloc)*/
            Method          dealloc = class_getInstanceMethod(class, deallocSel);
            IMP             origImpl = method_getImplementation(dealloc),
                            newImpl = imp_implementationWithBlock(/* ... snip ... */        
            class_replaceMethod(class, deallocSel, newImpl, method_getTypeEncoding(dealloc));

            [MAKVONotificationCenter_swizzledClasses addObject:class];
        }
    }
```

The first thing to do is check whether this particular class has been swizzled before. We want the class the object thinks it is here, not the class it actually is - with KVO, these differ, and swizzling KVO's dynamic subclasses turned out to cause very strange behaviors. If it has been swizzled, do nothing. I don't check whether a superclass or subclass of the given class has been swizzled before, because doing it multiple times in the hierarchy is harmless, resulting in a little extra useless work at worst.

Next, retrieve the `SEL` for `-dealloc`; it's not possible to use `@selector(dealloc)` in ARC mode, so I have to cheat the compiler with `NSSelectorFromString()`. I get the instance method for `dealloc`, and its original implementation. Then I create a new implementation from a block using Lion's delightful `imp_implementationWithBlock()` API - I'll describe the implementation itself below. Finally, I replace the the original `dealloc` on the class with the new one and add the class to the list of swizzled classes.

Here's the new `dealloc` implementation itself:

```
    (__bridge void *)^ (void *obj)
    {
        @autoreleasepool
        {
            for (_MAKVONotificationHelper *observation in [objc_getAssociatedObject((__bridge id)obj, &MAKVONotificationCenter_HelpersKey) copy])
            {
                // It's necessary to check the option here, as a particular
                //  observation may want manual deregistration while others
                //  on objects of the same class (or even the same object)
                //  don't.
                if (!(observation->_options & MAKeyValueObservingOptionUnregisterManually))
                    [observation deregister];
            }
        }
        ((void (*)(void *, SEL))origImpl)(obj, deallocSel);
    };
```

There's quite a bit to notice here. First, notice I cast the block itself to a `(__bridge void *)` - this is to keep ARC quiet about casting a block (which is an object) to its pointer form, as required by the C API.

Next, the block takes as its parameter a `void` pointer, rather than an `id`. This certainly seems counterintuitive; after all, the object passed to an implementation block is `self`! Once again, ARC has the answer. Under ARC, all parameters to a function (which a block is) are automatically sent a `retain` message when the function is entered. But since this is the implementation of a `dealloc` method, the result is attempted object resurrection, which corrupts memory. Much hilarity ensues. Forcing the object to be a plain pointer hides it from ARC. This was better than marking it as `__unsafe_unretained` because the semantics are clearer.

The entire body of the method is wrapped in an autorelease pool, as there's the potential for quite a lot of work to happen here and it'd be nice not to have all that sitting around until the next event loop.

Next, the set of helpers registered for this object is looped over. Remember, this set will include both helpers that have the object as an observer and those that have it as a target, since a helper is always added to both its observer and target. We check for the manual unregistration option, and if it's unset, unregister the helper. No thread safety is needed here; an object that is being deallocated can not be being used from multiple threads, or the program is already going to crash no matter what we do.

Finally, we call through to the original implementation of `dealloc`, which the block captured from its surrounding context. This is the beauty of using a block implementation; there's no need to stash the original `dealloc` anywhere at all; the block will do it for us. This is also why it's safe to swizzle subclasses. If somehow a class _does_ get swizzled twice (say, a class that has a `dealloc` and then a subclass of it that doesn't), all that will happen is that two swizzled blocks will be called, followed by the correct original `dealloc`.

**The helper is using `__unsafe_unretained` references! Why not `__weak` ones? What are you trying to pull here!?**  
If you've been looking at the code while reading this, you may have noticed that the `_MAKVONotificationHelper` object that does most of the magic holds `__unsafe_unretained` references to its observer and target. Wouldn't it make more sense to use the safer zeroing weak references ARC so helpfully provides?

Well, no. Here's why:

- isn't available on OS X 10.6 / iOS 4.x. While there are already other APIs in use (particularly

  ) that break backwards compatibility, they're not

  hard to work around if you want to, and there are other reasons not to use ZWRs.
- . That would mean you couldn't use such objects as observers or make them the target of observations.
- in the presence of a swizzled

  method! Either observer or target will always remove the helper before it goes away, at which point it's gone from the other as well. And if the caller happened to pass the "I want to unregister manually" flag, the semantics of original KVO return: It was already illegal/a crashing bug to deallocate an object with registered observers. Making these proper

  references would only mask the problem temporarily, not solve it.

**Who needs an observer at all?**  
During the development of all these changes, Mike Ash and Tony Xiao were following along fairly closely. Tony in particular came up with a particularly clever method in the `NSObject` category:

```
    - (id<MAKVOObservation>)addObservationKeyPath:(id<MAKVOKeyPathSet>)keyPath options:(NSKeyValueObservingOptions)options block:(void (^)(MAKVONotification *notification))block;
```

This method questions the basic assumption that there needs to be an "observer" object at all for KVO to work! With a block-based callback, the only important object is the one being observed. Who the observer is doesn't matter at all, and KVO's own internal requirements are satisfied with the helper object as the observer. While in practice the observer is still important, since the block will almost certainly reference it, there's no conceptually clear reason to have it there.

Tony was also responsible for the discussion that led to `__weak` observer and target references being replaced with `__unsafe_unretained` ones. He was a big help, and here's my shout out to him saying, "Thanks, Tony!"

**Conclusion**  
The rest of the code in the file is pretty much boilerplate stuff and is fairly straightforward, so that wraps up my discussion, other than to mention that the unit tests I wrote were invaluable in making sure the code worked. Unit tests are a Good Thing, people!

That's all for this week for me, I'll be back in three weeks after Mike's two-parter on rebuilding Cocoa collection classes from scratch. As always, thanks for reading!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
