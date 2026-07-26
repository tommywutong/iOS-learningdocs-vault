---
title: 'Objective-C Internals: Class Graph Implementation A brief look at the Objective-C runtime source code, focusing on the definition of object and class types, highlighting how inheritance is implemented'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/01/10/objc-class-graph-impl'
original_language: en
published: 2023-01-10
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:eda6c7fbf8e91717'
translated: false
---

> 原文：[Objective-C Internals: Class Graph Implementation A brief look at the Objective-C runtime source code, focusing on the definition of object and class types, highlighting how inheritance is implemented](https://alwaysprocessing.blog/2023/01/10/objc-class-graph-impl)　·　Always Processing (Brian T. Kelley)

# Objective-C Internals: Class Graph Implementation

![Two yellow English Labradors working on computers, with design papers scattered on the tabletop.](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/c8a0ec22-9d84-4e34-3f9d-bba189527d00/public)

A brief look at the Objective-C runtime source code, focusing on the definition of object and class types, highlighting how inheritance is implemented, special cases for the root class, and quirks related to metaclass lookup.

The previous post explored the [Objective-C class architecture](https://alwaysprocessing.blog/2023/01/02/objc-class-arch) and [illustrated](https://alwaysprocessing.blog/2023/01/02/objc-class-arch#architecture-diagram) an object graph for a class hierarchy. Here, we’ll build on those concepts by examining the class object graph implementation (classes, superclasses, and metaclasses).

Let’s start with the public definitions of some key types. In Objective-C, the `Class` type represents any class type, and the `id` type represents an instance of any class. The Objective-C runtime header [`objc.h`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc.h#L37-L46) defines these types:

```
/// An opaque type that represents an Objective-C class.
typedef struct objc_class *Class;

/// Represents an instance of a class.
struct objc_object {
    Class _Nonnull isa  OBJC_ISA_AVAILABILITY;
};

/// A pointer to an instance of a class.
typedef struct objc_object *id;
```

As mentioned in the previous post, Objective-C [classes are also objects](https://alwaysprocessing.blog/2023/01/02/objc-class-arch#method-dispatch), but this relation is not present in the public type definitions. We do see this relation, however, If we take a look at the internal type definitions.

First, [objc-private.h](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-private.h#L113-L246) contains the actual `objc_object` definition. While the internal definition has many non-virtual C++ member functions, its only member variable, `isa_storage`, corresponds to the (deprecated) `isa` instance variable. (I don’t know why the internal type is `char` array, but if I had to guess, it prevents accidental direct use given the various overloads of the field. I discuss more about the `isa` field in [this post](https://alwaysprocessing.blog/2023/01/19/objc-class-isa).)

```
struct objc_object {
    char isa_storage[sizeof(isa_t)];
};
```

Next, [objc-runtime-new.h](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.h#L2142-L2663) contains the `objc_class` data structure definition. It has a few member variables of its own, and, like `objc_object`, it has many non-virtual C++ member functions.

```
struct objc_class : objc_object {
    // Class ISA;
    Class superclass;
    cache_t cache;             // formerly cache pointer and vtable
    class_data_bits_t bits;    // class_rw_t * plus custom rr/alloc flags
};
```

Here, we see that `objc_class` derives from `objc_object` and thus inherits the `isa` field. So, a class object is implemented just like any other object type. Next is the `superclass` field, which points to the parent class object, if any. (The `cache` and `bits` are not part of the class graph construction, so we’ll explore those in the future.)

And that’s all that’s required to construct the Objective-C class graph: two data structures (`objc_object` and `objc_class`) and two fields (`isa` and `superclass`)!

## objc_class Member Functions

Next, let’s examine some of the [`objc_class` member functions](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.h#L2540-L2570) to learn about the implementation of the edges in the architecture diagram.

### Root Classes

```
bool isRootClass() {
    return getSuperclass() == nil;
}
```

A class is a root class if it does not have a superclass. However, this is uncommon in practice as virtually all Objective-C objects derive from [`NSObject`](https://developer.apple.com/documentation/objectivec/nsobject?language=objc) (or, in rare cases, [`NSProxy`](https://developer.apple.com/documentation/foundation/nsproxy?language=objc)). Note, therefore, that the root metaclass is _not_ a root class.

### Root Metaclasses

```
bool isRootMetaclass() {
    return ISA() == (Class)this;
}
```

The root metaclass has a self-referential `isa` pointer, which is how the runtime identifies root metaclasses. As far as I know, this is the only cycle in the class graph.

### Metaclass Identity

```
bool isMetaClass() const {
    return cache.getBit(FAST_CACHE_META);
}

// Like isMetaClass, but also valid on un-realized classes
bool isMetaClassMaybeUnrealized() {
    if (isStubClass())
        return false;
    return bits.flags() & RW_META;
}
```

A bit flag emitted by the compiler identifies a metaclass instance, which is the primary characteristic distinguishing a metaclass instance from a class instance.

Unrealized classes, which includes stub classes, are described in more detail in the [Objective-C Internals: Unrealized Classes (and Toll-Free Bridging)](https://alwaysprocessing.blog/2023/02/16/objc-unrealized-classes) post.

### Metaclass Retrieval

```
// NOT identical to this->ISA when this is a metaclass
Class getMeta() {
    if (isMetaClassMaybeUnrealized()) return (Class)this;
    else return this->ISA();
}
```

When retrieving the metaclass from some class instance, it’s necessary to check whether that instance is the metaclass. If it is the metaclass, it returns itself. Otherwise, the class instance returns the metaclass through its `isa` pointer.

## Compiler Output

The `objc_class` data structure is part of the Objective-C ABI, meaning the details of its size and field layout are known to third-party programs, which encode this information into their executable binaries. We can see this by examining the compiler output of the following trivial class definition.

```
#import <Foundation/Foundation.h>

@interface MyObject: NSObject
@end

@implementation MyObject
@end
```

Generating assembly for the above `MyObject.m` file by running `clang -S MyObject.m` will produce an assembly file containing the following snippet (and more).

```
.section    __DATA,__objc_data
_OBJC_CLASS_$_MyObject:
    .quad   _OBJC_METACLASS_$_MyObject
    .quad   _OBJC_CLASS_$_NSObject
    .quad   __objc_empty_cache
    .quad   0
    .quad   __OBJC_CLASS_RO_$_MyObject
_OBJC_METACLASS_$_MyObject:
    .quad   _OBJC_METACLASS_$_NSObject
    .quad   _OBJC_METACLASS_$_NSObject
    .quad   __objc_empty_cache
    .quad   0
    .quad   __OBJC_METACLASS_RO_$_MyObject
```

Here, we see that the code generated by the compiler aligns with the observations we drew from the architecture diagram in the previous post:

- The `MyClass` class object has:

    - An `isa` variable that points to the `MyClass` metaclass.
    - A `super` variable that points to the `NSObject` class object.
- The `MyClass` metaclass has:

    - An `isa` variable that points to the `NSObject` (root object) metaclass.
    - A `super` variable that points to the `NSObject` metaclass.

(As mentioned above, the `cache` and `bits` fields will be the subject of a future post.)
