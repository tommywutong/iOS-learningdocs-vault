---
title: 'NSMapTable: more than an NSDictionary for weak pointers | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/07/nsmaptable-more-than-nsdictionary-for.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:80abcfdd0e6d2b95'
translated: false
---

> 原文：[NSMapTable: more than an NSDictionary for weak pointers | Cocoa with Love](https://www.cocoawithlove.com/2008/07/nsmaptable-more-than-nsdictionary-for.html)　·　Cocoa with Love (Matt Gallagher)

NSMapTable is collection class that was introduced in Mac OS X 10.5 (Leopard). At first glance, it would appear to be most useful as an NSDictionary replacement that can choose between "strong" and "weak" pointers. In this post, I'll show you why it is also useful outside garbage collection and how it can do things that NSDictionary can't (or shouldn't) do.

## More Cocoa for your Leopard

Cocoa added a few new collections classes in Mac OS X 10.5 (Leopard). These included:

- [NSPointerArray](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Classes/NSPointerArray_Class/index.html)
- [NSHashTable](http://developer.apple.com/documentation/Cocoa/Reference/NSHashTable_class/index.html)
- [NSMapTable](http://developer.apple.com/documentation/Cocoa/Reference/NSMapTable_class/index.html)

NSPointerArray is completely new but most of NSHashTable and NSMapTable's functionality was previously available through the [opaque Foundation C structs of the same names](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Miscellaneous/Foundation_Functions/Reference/reference.html).

In some respects, these new classes work like NSMutableArray, NSMutableSet and NSMutableDictionary respectively but give the option of working with "weak" garbage collected pointers. If you're using Objective-C 2.0 with Garbage Collection, you should [know what "weak" means](http://developer.apple.com/documentation/Cocoa/Conceptual/GarbageCollection/Articles/gcDesignPatterns.html) with respect to your pointers, so the advantage of using this option should be clear.

NSPointerArray can also be used for pure pointers (pointers that are not necessarily Objective-C classes) but the NSHashTable and NSMutableArray classes both require their contents to be Objective-C objects.

In a general sense though, NSPointerArray and NSHashTable fill the same design role as NSMutableArray and NSMutableSet (an ordered array and an unordered set respectively).

NSMapTable is different because it can fill roles in your design that NSMutableDictionary couldn't (or shouldn't).

## Limitations of NSDictionary

NSDictionary provides a key-to-object mapping. In essence, NSDictionary stores the "objects" in locations indexed by the "keys".

Since the objects are stored at specific locations, NSDictionary requires that the key's value doesn't change (otherwise the object would suddenly be at the wrong location for its key). To ensure this requirement is maintained, NSDictionary always copies the keys to its own private location.

This key copying behavior is fundamental to how NSDictionary works but is also a limitation: you can only use an Objective-C object as a key in an NSDictionary if it supports the NSCopying protocol. Further, the key should be small and efficient enough that copying is does not burden CPU or memory.

This means that NSDictionary is really only suited to "value"-type objects as keys (eg. small strings and numbers). It is not ideal for modelling mappings from fully fledged objects to other objects.

## Object to Object mappings

NSMapTable (as the name implies) is more suited to mapping in a general sense. Depending on how it is constructed, NSMapTable can handle the "key-to-object" style mapping of an NSDictionary but it can also handle "object-to-object" mappings — also known as an "[associative array](http://en.wikipedia.org/wiki/Associative_array)" or simply a "[map](http://www.sgi.com/tech/stl/Map.html)".

For example, an NSMapTable constructed as follows:

```objc
NSMapTable *keyToObjectMapping =
    [NSMapTable
        mapTableWithKeyOptions:NSMapTableCopyIn
        valueOptions:NSMapTableStrongMemory];
```

will work much the same as an NSMutableDictionary, copying its "key" values and retaining its "object" values.

A pure object-to-object mapping could be constructed as follows:

```objc
NSMapTable *objectToObjectMapping =
    [NSMapTable mapTableWithStrongToStrongObjects];
```

An object-to-object behavior could previously be emulated using an NSDictionary if all the keys were NSNumbers containing the memory address of the source object in the mapping (don't laugh, I've seen it done) but outside of this run-around, NSMapTable offers a true object-to-object mapping for the first time in a Cocoa collection class.

## Options for NSMapTable

The options provided to NSMapTable are composed of three parts: a "memory option", a "personality option" and the "copy in" flag. You may use one option for each part (there are default behaviors that will be used if no option is provided for the part). The parts are all bit flags (binary "or" them together to combine parts).

Officially, NSMapTable allows the following options:

- NSMapTableStrongMemory

  (a "memory option")
- NSMapTableWeakMemory

  (a "memory option")
- NSMapTableObjectPointerPersonality

  (a "personality option")
- NSMapTableCopyIn

  (a "copy option")

NSMapTableStrongMemory is the default "memory option". However, the default "personality option" and the default "copy in" behaviors don't have names so these two values can be considered implicitly included in the list.

### Memory options

Since "strong" and "weak" are terms associated with Garbage Collection in Objective-C, it may not be obvious that these options can be used outside of Garbage Collected code (manually managed memory as Apple calls it).

Outside garbage collection, the following definitions apply:

- : use retain and release
- : don't use retain and release

NSMapTable only permits NSPointerFunctionsOptions "personality options" that correspond to Objective-C objects. There are other NSPointerFunctionsOptions "personality options" where the behavior for "strong" pointers does not include retain and release but these options are not permitted for NSMapTable.

> The pointer will not be zeroed as in a garbage collected environment so you must be careful not to dereference the pointer if it is released.

### Personality options

The NSMapTableObjectPointerPersonality option is used to control whether the isEqualTo: and hash methods on the object are used when adding the object to the collection.

- The object's pointer value is used for direct comparison and bit-shifted hash generation (

  isEqualTo:

  and

  hash

  methods are

  used).
- (default behavior)

  The

  hash

  and

  isEqualTo:

  methods will invoked on the key to determine a storage location in the

  NSMapTable

  . The return values of these methods should not change (be immutable) for the duration that the key is used in the

  NSMapTable

  .

Both behaviors imply that the content implements the NSObject protocol, so methods in this protocol may also be invoked on the keys and objects. In particular, the description method may be invoked on NSMapTable contained keys and objects regardless of the personality option used. The NSMapTable will only support NSCoding if all keys and objects implement the NSCoding protocol too.

### Copy options

If NSMapTableCopyIn is specified, the NSMapTable makes its own copies of data using the NSCopying protocol when they are added. If you don't specify this option (default behavior) no copy will be made.
