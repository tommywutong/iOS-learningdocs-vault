---
title: 'Friday Q&A 2010-05-28: Leopard Collection Classes'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-05-28-leopard-collection-classes.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7081caa7de1586e4'
translated: false
---

> 原文：[Friday Q&A 2010-05-28: Leopard Collection Classes](https://www.mikeash.com/pyblog/friday-qa-2010-05-28-leopard-collection-classes.html)　·　mikeash.com Friday Q&A

Posted at 2010-05-28 16:43 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-06-18: Implementing Equality and Hashing](https://www.mikeash.com/pyblog/friday-qa-2010-06-18-implementing-equality-and-hashing.html)  
Previous article: [Some Light Reading](https://www.mikeash.com/pyblog/some-light-reading.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [collections](https://www.mikeash.com/pyblog/?tag=collections) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2010-05-28: Leopard Collection Classes

by [Mike Ash](https://www.mikeash.com/)

**Introduction**  
 These classes were introduced in 10.5 and it appears that their main purpose was to add some useful capabilities for the newly-introduced Cocoa garbage collection support. However, they add a lot of other useful capabilities beyond that as well.

Each of these classes is the counterpart of a more traditional Foundation collection class. `NSPointerArray` is the counterpart of `NSArray`, `NSHashTable` is the counterpart of `NSSet`, and `NSMapTable` is the counterpart of `NSDictionary`. They are not identical, but share a lot of behaviors, and are the same basic kind of container.

One nice feature of Cocoa garbage collection (and many other collectors) is zeroing weak references. These are references to an object which don't keep that object alive. Instead, they point to the object while it's alive, but if and when it gets garbage collected, the collector zeroes out the reference. This can be really useful for object caches, parent-child object relationships, automatic deregistration of observers and others.

Individual weak references are easy to use: simply prepend `__weak` to an object pointer variable's type and that variable becomes a weak reference. (Note: this does not work for local variables.) The standard collections all hold strong references to their contents. One of the reasons for these new collection classes was that they can be configured to hold weak references to their contents, greatly expanding the uses for weak references.

These classes are also much more flexible in general. They can hold `NULL` values, they can be configured to hold opaque non-object pointers, plain integers, or even pointers to memory with custom comparison/destruction operations.

**`NSPointerArray`**  
 This class is a lot like an `NSMutableArray`, but with the `id` objects replaced with `void *`, and many fewer convenience functions.

The major difference from `NSMutableArray` is in how you create a new `NSPointerArray`. The class has two initializers:

```
    - initWithOptions:(NSPointerFunctionsOptions)options;
    - initWithPointerFunctions:(NSPointerFunctions *)functions;
```

This is where the flexibility comes in. The parameters for these initialiers allow you to fully specify how the

treats its contents. You can use an

any time you want an

that points to special kinds of objects or otherwise needs special treatment.

**`NSPointerFunctions`**  
 `NSPointerFunctions` is a class whose main purpose is to hold a bunch of function pointers. There are function pointers for hashing, equality, memory management, and more. There are also two flags you can set to have it use different garbage collection read/write barriers. By stuffing function pointers into this class, you can specify how everything works.

Let's build an example. We'll create an NSPointerFunctions object that deals in pointers to integers. Not too useful, but a good exercise.

The first thing to do is to define all of the various functions that will be needed. Hashing is easy, just return the integer that the pointer points to:

```
    static NSUInteger Hash(const void *item, NSUInteger (*size)(const void *item))
    {
        return *(const int *)item;
    }
```

Equality is just as easy, dereference both pointers and compare:

```
    static BOOL IsEqual(const void *item1, const void *item2, NSUInteger (*size)(const void *item))
    {
        return *(const int *)item1 == *(const int *)item2;
    }
```

Note the final

parameter to both functions. If necessary, this will get the size of the pointed-to object. We already know the size, so there's no need to use it. Since it's unnecessary, I won't provide a size function to the

object either.

For the description, we just return a simple string using the integer obtained from dereferencing the pointer:

```
    static NSString *Description(const void *item)
    {
        return [NSString stringWithFormat: @"%d", *(const int *)item];
    }
```

Relinquish and acquire are a bit trickier. They assume reference counting memory management, but I want to use plain

and

. I decided to just have relinquish always free the item, and acquire return a copy. The relinquish function is simple:

```
    static void Relinquish(const void *item, NSUInteger (*size)(const void *item))
    {
        free((void *)item);
    }
```

The acquire function isn't much more complicated. It

s some new memory, copies the value, and returns the new pointer:

```
    static void *Acquire(const void *src, NSUInteger (*size)(const void *item), BOOL shouldCopy)
    {
        int *newPtr = malloc(sizeof(int));
        *newPtr = *(const int *)src;
        return newPtr;
    }
```

And now with all of this in place, we can create a new

, and a new

from it:

```
    NSPointerFunctions *functions = [[NSPointerFunctions alloc] init];
    [functions setHashFunction: Hash];
    [functions setIsEqualFunction: IsEqual];
    [functions setDescriptionFunction: Description];
    [functions setRelinquishFunction: Relinquish];
    [functions setAcquireFunction: Acquire];
    
    NSPointerArray *array = [NSPointerArray pointerArrayWithPointerFunctions: functions];
    
    int one = 1, two = 2, three = 3;
    [array addPointer: &one;];
    [array addPointer: &two;];
    [array addPointer: &three;];
```

And it all works.

**NSPointerOptions**  
 It may work, but that was a gigantic hassle. Fortunately, Apple has provided a bunch of pre-baked `NSPointerFunctions` to work with. These can be accessed by using `NSPointerFunctionsOptions` constants.

`NSPointerFunctionsOptions` is composed of three parts. There are memory options, personalities, and flags.

Memory options determine memory management. Using `NSPointerFunctionsStrongMemory` will get you the behavior of the more standard Foundation collection classes: a strong reference for garbage collection, and a retained reference for manual memory management. `NSPointerFunctionsZeroingWeakMemory` will get you zeroing weak references under garbage collection and, I believe, a non-retained reference under manual memory management.There are also options for `malloc`/`free` management, for Mach virtual memory, and for completely ignoring memory management.

Personalities determine hashing and equality. `NSPointerFunctionsObjectPersonality` provides the standard Foundation behavior of using `hash` and `isEqual:`. You can also use `NSPointerFunctionsObjectPointerPersonality`, which treats the contents as objects, but uses direct pointer value comparison; this is useful if you need a collection to work with object identity rather than value. `NSPointerFunctionsIntegerPersonality` allows storing pointer-sized integers directly in the container. Note that unlike the toy example above, this doesn't deal with _pointers_ to integers, but rather integers directly, like storing `(void *)42`. This is useful if you need a collection that stores integers and don't want the code and runtime overhead of packing the integers into objects.

Apple has only given us one flag at the moment: `NSPointerFunctionsCopyIn`. When set, this flag will cause newly inserted pointers to be copied rather than simply retained. What exactly this means will depend on the personality set, but in the case of object personalities, it will use `NSCopying`.

Some examples:

- .
- .
- memory, copied when inserted:

  .

As you can see, there's a lot of flexibility to be had here without ever having to define your own functions.

Now that you know how all of those work, let's look at the remaining two classes.

**`NSHashTable`**  
 `NSHashTable` is the rough equivalent of `NSMutableSet`. It's an unordered collection of objects, using hashing to allow for fast access. Again, the basic functionality is the same, but without some of the more advanced methods. And again, it has two initializers which take pointer functions and options.

There is one extra factory method on `NSHashTable`:

```
    + (id)hashTableWithWeakObjects;
```

Apparently Apple thought that this was a common enough use to justify making it more convenient to create a new object of this type.

Like `NSPointerArray`, you can use `NSHashTable` any time you want an `NSSet` but with some different capabilities in terms of how it treats its contents.

**`NSMapTable`**  
 `NSMapTable` is the final class of the three, and is the rough equivalent of `NSDictionary`. It's an unordered collection of key/object pairs, with fast access to the objects by looking them up through their keys. Like the others, it has the standard two initializers to tell it how to act.

`NSMapTable` also has four extra factory methods:

```
    + (id)mapTableWithStrongToStrongObjects;
    + (id)mapTableWithWeakToStrongObjects;
    + (id)mapTableWithStrongToWeakObjects;
    + (id)mapTableWithWeakToWeakObjects;
```

This gives you all four possible combinations of weak and strong.

As with the others, you can use `NSMapTable` in any case where you'd normally want an `NSDictionary` but need a little extra flexibility.

In particular, `[NSMapTable mapTableWithStrongToStrongObjects` will give you an object which behaves much like an `NSDictionary` but which doesn't copy its keys. This is useful in all kinds of situtaions, and can save a lot of headache.

**Comparison with CoreFoundation**  
 Those of you who are intimately familiar with CoreFoundation collections probably nodded a lot at the `NSPointerFunctions stuff`. CoreFoundation collections such as `CFArray` require nearly identical functions to determine how they treat their contents. Given this, what are the advantages of each?

The new Cocoa classes are largely useful because they're vastly more convenient to set up. CoreFoundation has no equivalent for a lot of the built-in `NSPointerOptions` functionality, which would require you to build them all yourself. There is not, as far as I know, any way to do zeroing weak references with CoreFoundation collections. Toll-free bridging is also inconsistent when it comes to custom behavior: you can build a `CFDictionary` with callbacks that don't copy their keys, but using `[customDictionary setObject: obj forKey: key]` will still copy the key even though you expressly told it not to! (For any Apple employees reading this, I've filed this as [bug #4350677](rdar://4350677), and it was returned as "behaves correctly".)

Custom CoreFoundation collections can be better due to toll-free bridging, which allows you to treat them as standard `NSArray`s and so forth. However, you must be careful when passing these to code you don't own, as they may make assumptions about the behavior of the collection which your custom callbacks don't respect. And as noted above, the behavior of custom callbacks with toll-free bridging is inconsistent, so watch out!

All in all, each one has its place. In pure Cocoa code, the new Cocoa classes are generally more convenient and can be more powerful.

**Conclusion**  
 The new collection classes added to Cocoa in 10.5 are a powerful, flexible addition to Foundation. They easily allow useful behaviors like storing weak references and raw integers, or just creating an object map that doesn't copy its keys.

That's it for this Friday Q&A. Come back in another two weeks for the next one, unless I decide that working it in around WWDC is too much, in which case I'll shoot for the week after. And if you're going to WWDC too, say hi!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
