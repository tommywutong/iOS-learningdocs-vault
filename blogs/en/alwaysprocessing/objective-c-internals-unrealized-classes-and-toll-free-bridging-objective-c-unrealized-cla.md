---
title: 'Objective-C Internals: Unrealized Classes (and Toll-Free Bridging) Objective-C unrealized classes may refer to future classes or class stubs. Future classes (a private runtime feature) facilitate toll'
source: Always Processing (Brian T. Kelley)
source_key: alwaysprocessing
source_url: 'https://alwaysprocessing.blog/2023/02/16/objc-unrealized-classes'
original_language: en
published: 2023-02-16
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a35b9c1ea90ab378'
translated: false
---

> 原文：[Objective-C Internals: Unrealized Classes (and Toll-Free Bridging) Objective-C unrealized classes may refer to future classes or class stubs. Future classes (a private runtime feature) facilitate toll](https://alwaysprocessing.blog/2023/02/16/objc-unrealized-classes)　·　Always Processing (Brian T. Kelley)

# Objective-C Internals: Unrealized Classes (and Toll-Free Bridging)

![Two Labradors sitting in front of a computer under a bridge. Presumably they are avoiding a toll.](https://alwaysprocessing.blog/cdn-cgi/imagedelivery/WFfM6PwcxpVzRRpdvDWNtg/c34a57c8-254d-4af6-e20a-c518c2f76f00/public)

Objective-C unrealized classes may refer to future classes or class stubs. Future classes (a private runtime feature) facilitate toll-free bridging with CoreFoundation. And, class stubs are emitted by the Swift compiler to support interoperability between the stable Swift ABI and Objective-C.

An earlier post that explored the Objective-C class implementation ignored^[[1](#_footnotedef_1)] an interesting detail of the functions used to [identify a metaclass](https://alwaysprocessing.blog/2023/01/10/objc-class-graph-impl#metaclass-identity): the concept of _unrealized classes_.

```
// Like isMetaClass, but also valid on un-realized classes
bool isMetaClassMaybeUnrealized() { /* ... */ }
```

An _unrealized class_ is a partially initialized metaclass where only the class name is known. There are two types of unrealized metaclasses: future classes and class stubs.

## Future Classes

The Objective-C runtime in Mac OS X 10.5 introduced future classes as a private runtime feature to clean up the [toll-free bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html) implementation. Surprisingly, this is actually documented in [`objc_getFutureClass`](https://developer.apple.com/documentation/objectivec/1441638-objc_getfutureclass):

> Used by CoreFoundation’s toll-free bridging. Do not call this function yourself.

### Toll-Free Bridging

First, let’s briefly look at the toll-free bridging implementation. Mac OS X Developer Preview 1 [introduced the CoreFoundation framework and "toll-free bridging."](https://developer.apple.com/library/archive/releasenotes/Foundation/RN-FoundationOlderNotes/index.html) In short, toll-free bridging allows developers to freely cast between bridged CoreFoundation and Foundation types (e.g., casting `CFArrayRef` to/from `NSArray *`) to pass one type as if it were the other, without incurring any runtime overhead. In addition, user-defined subclasses of toll-free bridged Foundation classes are fully supported.

A full exploration of toll-free bridging is beyond the scope of this post, but you can [read more here](https://ridiculousfish.com/blog/posts/bridge.html). We only need two highlight two key implementation details to understand its use of the Objective-C runtime.

First, all CoreFoundation objects have an Objective-C-compatible `isa` field as their first member. From [CFRuntime.h](https://github.com/apple-oss-distributions/CF/blob/CF-368.25/Base.subproj/CFRuntime.h#L207):

```
typedef struct __CFRuntimeBase {
    void *_isa;
    // ...
} CFRuntimeBase;
```

Second, each CoreFoundation function with a Foundation equivalent (e.g., [`CFArrayGetCount()`](https://github.com/apple-oss-distributions/CF/blob/CF-368.25/Collections.subproj/CFArray.c#L603-L607) and `-[NSArray count]`) will call the Objective-C implementation if the `isa` does not match the `isa` of the bridged CoreFoundation type, which is what provides the bridging support for user-defined Foundation subclasses. ([CFInternal.h](https://github.com/apple-oss-distributions/CF/blob/CF-368.25/Base.subproj/CFInternal.h#L470-L472) defines the Objective-C dispatch macro.)

```
CFIndex CFArrayGetCount(CFArrayRef array) {
    CF_OBJC_FUNCDISPATCH0(__kCFArrayTypeID, CFIndex, array, "count");
    __CFGenericValidateType(array, __kCFArrayTypeID);
    return __CFArrayGetCount(array);
}

#define CF_OBJC_FUNCDISPATCH0(typeID, rettype, obj, sel) \
    if (__builtin_expect(CF_IS_OBJC(typeID, obj), 0)) \
    {rettype (*func)(const void *, SEL) = (void *)__CFSendObjCMsg; \
    static SEL s = NULL; if (!s) s = sel_registerName(sel); \
    return func((const void *)obj, s);}

CF_INLINE int CF_IS_OBJC(CFTypeID typeID, const void *obj) {
    return (((CFRuntimeBase *)obj)->_isa != __CFISAForTypeID(typeID) && ((CFRuntimeBase *)obj)->_isa > (void *)0xFFF);
}
```

How CoreFoundation obtains the `isa` pointer shared with Foundation is the subject of the remainder of this section.

### Mac OS X 10.0 - Mac OS X 10.4 "Tiger"

The original implementation of toll-free bridging was quite elaborate. Foundation defines the public Objective-C classes (e.g., `NSObject`, `NSArray`, `NSMutableArray`), the private implementation of [class clusters](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/ClassClusters/ClassClusters.html) (e.g., `NSCFArray`), and a bridging placeholder (e.g., `NSCFArray__`), which is a trivial subclass of the bridged implementation.

When Foundation is loaded, it calls CoreFoundation’s [`__CFSetupFoundationBridging()`](https://github.com/apple-oss-distributions/CF/blob/CF-368.25/Base.subproj/ForFoundationOnly.h#L52-L53) function, which does two things:

1. Calls [`__CFInitialize()`](https://github.com/apple-oss-distributions/CF/blob/CF-368.25/Base.subproj/CFRuntime.c#L738-L739). One of the first initialization steps allocates memory for each entry in the `__CFRuntimeObjCClassTable`, which maps `CFTypeID`s to their bridged Objective-C `Class`. The `objc_class` allocated here ([recall](https://alwaysprocessing.blog/2023/01/10/objc-class-graph-impl#preamble) that `Class` is a `typedef` for `objc_class *`) will become the toll-free bridged class instance shared between CoreFoundation and Foundation in the next step. The pointer value is reserved early in the initialization process to be available to CoreFoundation objects allocated in subsequent initialization steps to guarantee those objects bridge correctly.
2. For each bridged type, looks up the placeholder subclass and, if present, calls [`_CFRuntimeSetupBridging()`](https://github.com/apple-oss-distributions/CF/blob/CF-368.25/Base.subproj/CFRuntime.c#L204-L209).

    1. `_CFRuntimeSetupBridging()` makes a bitwise copy of the placeholder’s `objc_class` struct into the memory allocated in the previous step.
    2. CoreFoundation then poses its bitwise copy of the placeholder class as the bridged implementation.

```
void __CFSetupFoundationBridging(void *, void *, void *, void *) {
    // ...
    __CFInitialize();
    // ...
    Class aClass = objc_lookUpClass("NSCFArray__");
    if (arrayClass != Nil) {
        _CFRuntimeSetupBridging(CFArrayGetTypeID(), aClass->super_class, aClass);
    }
    aClass = objc_lookUpClass("NSCFDictionary__");
    if (aClass != Nil) {
        _CFRuntimeSetupBridging(CFDictionaryGetTypeID(), aClass->super_class, aClass);
    }
    // ...
}

void __CFInitialize(void) {
    // ...
    __CFRuntimeObjCClassTable[CFDictionaryGetTypeID()] = calloc(sizeof(struct objc_class), 1);
    __CFRuntimeObjCClassTable[CFArrayGetTypeID()] = calloc(sizeof(struct objc_class), 1);
    // ...
}

Boolean _CFRuntimeSetupBridging(CFTypeID typeID, struct objc_class *mainClass, struct objc_class *subClass) {
    void *isa = __CFISAForTypeID(typeID);
    memmove(isa, subClass, sizeof(struct objc_class));
    class_poseAs(isa, mainClass);
    return true;
}
```

Posing is a deprecated feature of the Objective-C runtime (and was removed in Objective-C 2) that effectively allows a subclass to subsume the identity of its superclass. The posing class takes the original class’s name, and, to preserve name uniqueness, the runtime then prepends a `%` to the original class’s name and `_%` to the original metaclass’s name. So, continuing with the array example, `NSCFArray__` becomes `NSCFArray`, and the original `NSCFArray` becomes `%NSCFArray`.

The posed class instance receives all messages sent to the original class instance. After the above bridging is complete, any message sent to the `NSCFArray` class (e.g., `alloc`), for example, is received by the class posing as `NSCFArray` (i.e., `NSCFArray__`). This redirection, therefore, causes Foundation to create new objects using the posed class type. Then, when a passing Foundation object to CoreFoundation as a `CFTypeRef`, `CF_IS_OBJC` returns `false` because the object has the `isa` identifying it as the private bridged type (so Objective-C dispatch to a user-defined subclass is not required). Because it’s a private class, CoreFoundation can access its internals directly.

### Mac OS X 10.5 "Leopard" and Later, and iOS

Future classes vastly simplify the implementation of toll-free bridging. In Mac OS X 10.5 and later, the bridging configuration still occurs in `__CFInitialize()`, but with a few key differences:

1. `__CFInitialize()` is called when the dynamic linker loads the framework, removing any initialization dependency on downstream code.
2. For each bridged type, CoreFoundation calls `objc_getFutureClass()` with the class name and populates the `__CFRuntimeObjCClassTable` with the `Class` pointer returned by the runtime.

    - If the class is already loaded, the runtime returns its instance pointer.
    - Otherwise, the runtime [allocates an `objc_class` instance](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L2996-L3019) with the given name and returns a pointer to this "future" class. Then, when the process later loads a class with that name, the runtime [copies the class definition](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L3406-L3436) into the previously allocated memory (similar to `_CFRuntimeSetupBridging()` in previous versions) and [remaps the class definition](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L1976-L1997) loaded from the binary image to the previously allocated class definition (similar to posing). Despite the similarities, this strategy simplifies both the Objective-C runtime and CoreFoundation implementations.

The following is an approximation of the new [Core Foundation implementation in Leopard](https://github.com/apple-oss-distributions/CF/blob/CF-476.10/CFRuntime.c#L723).

```
static void __CFInitialize(void) __attribute__ ((constructor));
static void __CFInitialize(void) {
    // ...
    _CFRuntimeBridgeClasses(0x10/*CFDictionaryGetTypeID()*/, "NSCFDictionary");
    _CFRuntimeBridgeClasses(0x11/*CFArrayGetTypeID()*/, "NSCFArray");
    // ...
}

void _CFRuntimeBridgeClasses(CFTypeID cf_typeID, const char *objc_classname) {
    __CFRuntimeObjCClassTable[cf_typeID] = objc_getFutureClass(objc_classname);
}
```

There’s no requirement that a future class becomes realized during the lifetime of a process. However, the process will crash if a future class receives any messages. I spot-checked the use of a future class with Objective-C runtime functions, and the functions I tested worked correctly, even if by accident.

## Stub Classes

The Objective-C runtime in macOS 10.15 and iOS 13 introduced stub classes to support the stable Swift ABI. A stub class is emitted by the Swift compiler when:

1. A Swift class type is declared to be representable in Objective-C via the `@objc` attribute, which includes any class inheriting from `NSObject`, whether directly or indirectly.
2. The Swift class from (1) is compiled into a dynamic library (which includes frameworks) that has [_library evolution_](https://www.swift.org/blog/library-evolution/) enabled (using the `-enable-library-evolution` build flag). Library Evolution is also referred to as resilience or ABI stability.
3. A Swift class in another module imports the module from (2) and subclasses the class defined in (1). When this derived Swift class is compiled, the compiler will emit the Objective-C class metadata as a class stub.

I performed a cursory investigation into why a stub is necessary for this scenario but couldn’t draw any conclusions. I suppose the answer will have to wait for the Swift Internals series 🙃. But, we can examine how the Objective-C runtime handles class stubs.

An `isa` value of 1 through 15, inclusive, [identifies](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.h#L2426-L2429) an `objc_class` instance as a stub class. Currently, `isa` [values other than 1 are reserved](https://github.com/apple/swift/blob/swift-5.7.3-RELEASE/docs/ObjCInterop.md#stub-classes).

```
bool isStubClass() const {
    uintptr_t isa = (uintptr_t)isaBits();
    return 1 <= isa && isa < 16;
}
```

If `objc_getClassList()` or `objc_copyClassList()` is called, the runtime will initialize, as necessary, all the stub classes loaded into the process. Otherwise, stub classes are initialized on demand when the class object is required.

The Objective-C header generated by the Swift compiler adds an `__attribute__((objc_class_stub))` to the class interface, which instructs Clang to get the class object via a call to [`objc_loadClassref()`](https://github.com/apple-oss-distributions/objc4/blob/689525d556eb3dee1ffb700423bccf5ecc501dbf/runtime/objc-runtime-new.mm#L2049-L2062) instead of referencing a class symbol directly. The runtime function calls the Swift initializer to generate the `Class` object on the first access and stores the result in the stub for future accesses.

I am looking forward to the day when I can write a post about what Swift feature makes this extra indirection necessary!

---

[1](#_footnoteref_1). The class implementation post has been updated to acknowledge the unrealized class detail and to link to this post.
