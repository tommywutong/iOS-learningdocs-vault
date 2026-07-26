---
title: 'The Swift Runtime: Heap Objects'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/'
original_language: en
published: 2020-08-31
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b83291eb996539da'
translated: false
---

> 原文：[The Swift Runtime: Heap Objects](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Objective-Rust](https://belkadan.com/blog/2020/08/Objective-Rust/)

[The Swift Runtime: Type Layout](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/) »

« [Objective-Rust](https://belkadan.com/blog/2020/08/Objective-Rust/?tag=swift)

[The Swift Runtime: Type Layout](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/?tag=swift) »

[The Swift Runtime: Type Layout](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/?tag=swift-runtime) »

## [The Swift Runtime: Heap Objects](#)

Welcome to the first in a series of posts on the [Swift runtime](https://belkadan.com/blog/tags/swift-runtime). The goal is to go over the functions of the Swift runtime, using what I learned in my [Swift on Mac OS 9 project](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/) as a reference. Today we’re going to start with the basis of both class instances and closures: heap objects.

Note that this will not be an exhaustive guide to the entire Swift runtime. There are several parts I didn’t implement in my project, and I have a feeling this series will be long enough as it is.

As mentioned previously, I implemented my stripped-down runtime in Swift as much as possible, though I had to use a few undocumented Swift features to do so. I’ll be showing excerpts of my runtime code throughout these posts, and you can check out the full thing [in the ppc-swift repository](https://belkadan.com/source/ppc-swift-project/tree/refs/heads/dev:/stdlib/_Runtime).

### The basics

While instances of different classes all have different data in them, they all start with the same two hidden fields:

| Heap object header |
|---|
| isa pointer |
| reference count |

The isa pointer is used for a few things, mainly calling overridable methods and making sure the destructor of a class is called properly.^[1](#fn:isa) The reference count field is very complicated in the real Swift runtime (at the very least, it has to handle normal retains and the tracking for `unowned` and `weak`), but for my project I simplified it down to just tracking normal strong references.

The lifetime of an object starts with allocation:

```
@_cdecl("swift_allocObject")
func swift_allocObject(
  rawMetadata: UnsafeRawPointer,
  requiredSize: Int,
  requiredAlignmentMask: Int
) -> UnsafeMutableRawPointer {
  let result = UnsafeMutableRawPointer(NewPtrClear(requiredSize)!)
  result.storeBytes(of: rawMetadata, as: UnsafeRawPointer.self)
  return result
}
```

It’s pretty simple. It allocates an object using the operating system’s allocator (in this case, `NewPtrClear`), and puts the _metadata_ pointer (the class) in the first field. I’ve chosen to have the reference count field have a _biased_ representation, so that the initial “0” value represents a retain count of “1”. I get that 0 implicitly from `NewPtrClear`, so it doesn’t even get set explicitly.

(You can also see this isn’t a perfect implementation of `swift_allocObject`; if the required alignment is greater than what `NewPtrClear` provides, the code that calls this could easily crash.)

_You’re going to see that `@_cdecl` a lot in this series. The real Swift runtime functions are all defined in C++, so for simplicity’s sake they’re all using unmangled names—the name of the function is the name of the symbol. The runtime also started before Swift had its own calling convention, so the functions that have been around the longest use C’s calling convention instead. `@_cdecl` isn’t a supported attribute yet, but [you can help make it one](https://forums.swift.org/t/best-way-to-call-a-swift-function-from-c/9829/6)!_

Once an object is alive, it gets retained

```
@_cdecl("swift_retain")
func swift_retain(
  _ maybeObjectRef: UnsafeMutableRawPointer?
) -> UnsafeMutableRawPointer? {
  guard let rawObjectRef = maybeObjectRef else { return maybeObjectRef }
  IncrementAtomic((rawObjectRef + 4).assumingMemoryBound(to: Int32.self))
  return rawObjectRef
}
```

and released (and eventually destroyed).

```
@_cdecl("swift_release")
func swift_release(
  _ maybeObjectRef: UnsafeMutableRawPointer?
) {
  guard let rawObjectRef = maybeObjectRef else { return }
  let oldRefCount = DecrementAtomic((rawObjectRef + 4).assumingMemoryBound(to: Int32.self))
  guard oldRefCount == 0 else { return }

  let metadata = rawObjectRef.load(as: UnsafePointer<TypeMetadata>.self)
  let destroyPtr = UnsafeRawPointer(metadata) - 8
  swift_invokeDestroyer(destroyPtr, rawObjectRef)
}
```

I’m showing these together so it’s clear that they’re duals: both of them start by checking for `nil`, and then atomically increment or decrement the second field of the object. Again, this is a simplification compared to what the real runtime does, but because retaining and releasing objects can happen a lot, even the real runtime tries to be this fast in the common case.

The way Swift’s flavor of automatic reference counting works is that destruction of the object happens synchronously when the last reference goes away. So while `swift_retain` ends after updating the reference count, `swift_release` has to check to see if the object should be destroyed. If the old reference count representation was 0 (remember, it’s a biased representation), then this release is for the last reference, and it’s time to destroy the object. As mentioned above, this information is stored relative to the class metadata, whose address we get by loading the first field of the object.^[2](#fn:negative)

The destructor has a slightly different calling convention than a normal Swift function, so it’s not actually possible to write a 100% correct call to it in Swift. Instead, I have a C++ helper, `swift_invokeDestroyer`, to call it correctly, which has to be compiled using a Swift-compatible version of Clang. (I’m not going to bother showing that here.)

The destructor’s job is to call the deinitializer, if the class has one, and then deallocate the object. There’s a runtime function for that too:

```
@_cdecl("swift_deallocClassInstance")
func swift_deallocClassInstance(
  _ object: UnsafeMutableRawPointer,
  allocatedSize: Int,
  allocatedAlignmentMask: Int
) {
  DisposePtr(object.assumingMemoryBound(to: CChar.self))
}
```

This is just calling the OS memory deallocator, with an `assumingMemoryBound(to:)` to match up the type with the C declaration. You’ll notice `allocatedSize` and `allocatedAlignmentMask` aren’t used here; it turns out they’re **not trustworthy**. The values that get passed match the default size and alignment of the class, but if the class has “tail allocation” (like [ManagedBuffer](https://developer.apple.com/documentation/swift/managedbuffer), or the backing storage of Array), then that size and even the alignment may be wrong! Good thing they’re not needed in my implementation anyway.

### Closures

I hope it’s clear how this all works for classes, but how about closures? Turns out closures _also_ have two parts:

| Closure value |
|---|
| function pointer |
| reference to captures |

The first field of a closure is a function pointer with a special calling convention: it takes the arguments of the closure as well as an additional argument for accessing any captured bindings (parameters, variables, or constants, or explicitly-specified bindings from a capture list). This additional argument is loaded from the second field, and you can think of it as a sort of “anonymous class” that stores the captures. Passing around a closure means retaining and releasing this “captures object”, and it’s destroyed when the reference count hits 0 like any other object. If the closure doesn’t have any captures, this field will be `nil`.^[3](#fn:blocks)

### Core Foundation

Before Swift, Objective-C was the main way to program for Apple OSs. But if you were in just plain C, there was an even lower object-oriented layer you can use, called _Core Foundation._ This was an Objective-C-compatible object system that presented a plain C interface, and it still exists today (though these days most of Core Foundation is implemented in Objective-C too). Since some APIs still use Core Foundation, the first release of Swift had built-in support for tracking CF objects with automatic reference counting (as well as Swift and Objective-C objects).

But Core Foundation was used for another purpose, too: [it was a bridge between the _Toolbox_ APIs of Mac OS 9 and the _Cocoa_ APIs of Mac OS X (now “macOS”)](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/#whats-a-mac-osnbsp9). And that means it’s present and available on Mac OS 9 too, and _that_ means that my own runtime project needs to handle CF objects too. A CF object isn’t necessarily going to have the same layout as a Swift object, so `swift_retain` and `swift_release` can’t poke at the bits to directly increment or decrement the reference count. However…

> Convenient discovery for my further explorations: CF types under Classic still had their first word reserved for an isa pointer, but it never got set to anything. That means I can differentiate Swift and CF objects by whether the first word is null!
> 
> — Jordan Rose (@UINT_MIN) [April 9, 2020](https://twitter.com/UINT_MIN/status/1248154940318482432?ref_src=twsrc%5Etfw)

So my actual version of `swift_retain` looks like this:

```
@_cdecl("swift_retain")
func swift_retain(
  _ maybeObjectRef: UnsafeMutableRawPointer?
) -> UnsafeMutableRawPointer? {
  guard let rawObjectRef = maybeObjectRef else { return maybeObjectRef }
  // NEW
  guard isNativeSwiftObject(rawObjectRef) else {
    return _CFRetain(rawObjectRef)
  }
  IncrementAtomic((rawObjectRef + 4).assumingMemoryBound(to: Int32.self))
  return rawObjectRef
}
```

(Note that I had to provide a C wrapper function for `CFRetain`, since normally Swift prevents you from calling it directly and messing up ARC.)

And in order to handle both the Classic and [Carbon](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/#whats-a-mac-osnbsp9) environments, `isNativeSwiftObject` looks like this:

```
private func isNativeSwiftObject(_ objectRef: UnsafeRawPointer) -> Bool {
  let lowestValidPointer = 0x1000

  // Some CF types do not have isa pointers.
  let isaField = objectRef.load(as: UInt.self)
  guard isaField >= lowestValidPointer else {
    return false
  }
  let type = UnsafeRawPointer(bitPattern: isaField)!

  // ObjC classes have an isa pointer too (like objects),
  // while the types of Swift heap allocations do not
  // (except on modern Apple platforms,
  // where Swift classes are valid ObjC classes).
  let possibleMetaclassPointer = type.load(as: UInt.self)
  return possibleMetaclassPointer < lowestValidPointer
}
```

Where’s that `0x1000` come from?^[4](#fn:cf) On many modern operating systems, including Mac OS X, a section at the low end of the “address space” is reserved to catch bugs that show up as null pointer dereferencing. Mac OS 9 doesn’t _quite_ have this guarantee, but fortunately it reserves the bottom part of memory for various bits of the OS, and so we can rely on values below `0x1000` not being used for application memory. So what we end up checking looks like this:

| First field of object | First field of type | Classification |
|---|---|---|
| `0..<­0x1000` | (N/A) | CF (non-ObjC) |
| `0x1000...` | `0..<­0x1000` | **Swift** |
| `0x1000...` | `0x1000...` | CF (ObjC) |

That classification lets us decide whether to use the reference counting we just implemented or defer to CFRetain, and with that, we have ARC working for CF objects on Mac OS 9, and even on Mac OS X under Carbon.

### …and the rest

There’s a few more heap-object-related functions, but none of them are too exciting. `swift_isUniquely­Referenced_­nonNull_native` is simply a check that the reference count field is 0. `swift_init­StackObject` is like `swift_alloc­ClassInstance`, except the memory’s already allocated. There are a few others, but the only other interesting one is `swift_init­StaticObject`:

```
@_cdecl("swift_initStaticObject")
func swift_initStaticObject(
  _ metadata: UnsafeRawPointer,
  _ object: UnsafeMutableRawPointer
) -> UnsafeMutableRawPointer {
  let token = (object - MemoryLayout<UInt32>.size).assumingMemoryBound(to: UInt32.self)
  swift_once(token) {
    object.storeBytes(of: metadata, as: UnsafeRawPointer.self)
  }
  return object
}
```

This is an optimization for when the compiler sees a global `let` whose type is a class instance. If the compiler can guarantee the size of the class at compile time, the object’s data can be located in static memory rather than on the heap.^[5](#fn:immortal) The compiler has to fold in the initialization of the global in this case, so it calls the `swift_once` helper that ensures that the object is only initialized once. And `swift_init­StaticObject` isn’t passed a separate argument for the “token”; it’s got a contract with the compiler that there’ll be one just before the object data.

How does `swift_once` work? The real one calls something that already exists on the platform to do its dirty work, either [`dispatch_once`](https://developer.apple.com/documentation/dispatch/1447167-dispatch_once_f) or [`std::call_once`](https://en.cppreference.com/w/cpp/thread/call_once). But neither is available on Mac OS 9, so I had to make my own:

```
func swift_once(
  _ token: UnsafeMutablePointer<UInt32>,
  _ action: () -> Void
) {
  if CompareAndSwap(0, 1, token) {
    action()
    token.pointee = 2
  } else {
    while token.pointee != 2 {
      MPYield()
    }
  }
}

@_cdecl("swift_once")
func swift_once(
  _ flag: UnsafeMutablePointer<UInt32>,
  _ action: @convention(c) (UnsafeMutableRawPointer) -> Void,
  _ context: UnsafeMutableRawPointer
) {
  swift_once { action(context) }
}
```

What’s here is a little state machine: if `token` is 0, nothing’s happened; if it’s 1, initialization is in progress; and if it’s 2, it’s complete. The code uses a `CompareAndSwap` to make sure that only one thread will actually try to run the action, and if that fails, it’ll wait until the initialization is complete, letting another thread run if necessary.^[6](#fn:threading) (The “MP” stands for “multiprocessing”, the name of the Classic Mac OS library that implemented preemptive threading.)

The second overload is the one with the C-compatible interface that the compiler uses for normal, unoptimized global initialization.

### Wrap-up

Whew! We went through six functions, and it still ended up being a fair bit. And I hate to say it, but this was the easiest one. The rest of the runtime has a lot more structured data, so for later blog posts we’ll be going through some actual types, and some much more complicated operations. [Next up: layout of structs and tuples](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/).

1. The “isa” pointer is so called because it points to the class that the object “is a(n)” instance of, e.g. “`superview` is a `View`”. [↩︎](#fnref:isa)
2. If you’re wondering why the “destroyer” is located at a _negative_ offset, it’s because Swift classes are designed to be compatible with Objective-C, and Objective-C _doesn’t_ have an explicit pointer to a function that will deinitialize and deallocate a class instance; it just calls the method named `dealloc`. The Swift destroyer could go _after_ the Objective-C fields, but that’d be a waste for other types of reference-counted heap objects, like closure captures. And it could go _immediately_ before the type metadata, at an offset of `-4` (pointers are 32 bits on Mac OS 9), but that’s already in use for the _value witness table,_ which we’ll talk about in a later post. [↩︎](#fnref:negative)
3. Note that this is different from the Clang / Objective-C approach, [blocks](https://clang.llvm.org/docs/BlockLanguageSpec.html). A block is implemented as a normal object with an isa pointer, with the function pointer being treated as a field along with all the captures. That means it can be passed around as a normal object reference, with no special rules for how to retain and release it…but it also means that closures that don’t capture anything have a larger minimum overhead than they do in Swift. Everything’s a tradeoff! [↩︎](#fnref:blocks)
4. The _idea_ came from the Core Foundation project itself, where a macro called `CF_IS_OBJC` in [CFInternal.h](https://opensource.apple.com/source/CF/CF-368.28/Base.subproj/CFInternal.h.auto.html) tests whether an object is a native _Core Foundation_ type or a “bridged” Objective-C type. This macro also uses `0x1000` (actually `0xFFF`) as the boundary value, though it only has to deal with Mac OS X. [↩︎](#fnref:cf)
5. The real runtime also gives the object a special reference count that indicates that it’s immortal. I didn’t bother with that in my implementation. [↩︎](#fnref:immortal)
6. Technically this still breaks Swift’s formal [memory access rules](https://github.com/apple/swift-evolution/blob/master/proposals/0282-atomics.md) by reading from the pointer while another thread might be in the middle of modifying it. Swift doesn’t currently have a way to tell the _compiler_ to do a “safe” read here. We’re just lucky that the code the compiler emits for a single-threaded mode is going to work for a multi-threaded mode as well. [↩︎](#fnref:threading)

This entry was posted on [August](https://belkadan.com/blog/2020/08) 31, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Swift runtime](https://belkadan.com/blog/tags/swift-runtime)
