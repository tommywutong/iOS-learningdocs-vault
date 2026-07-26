---
title: 'The Swift Runtime: Uniquing Caches'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/'
original_language: en
published: 2020-09-21
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0ae1d1f225573ab9'
translated: false
---

> 原文：[The Swift Runtime: Uniquing Caches](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [The Swift Runtime: Type Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/)

[The Swift Runtime: Class Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/) »

« [The Swift Runtime: Type Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/?tag=swift)

[The Swift Runtime: Class Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/?tag=swift) »

« [The Swift Runtime: Type Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/?tag=swift-runtime)

[The Swift Runtime: Class Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/?tag=swift-runtime) »

## [The Swift Runtime: Uniquing Caches](#)

Welcome to the fourth in a series of posts on the [Swift runtime](https://belkadan.com/blog/tags/swift-runtime). The goal is to go over the functions of the Swift runtime, using what I learned in my [Swift on Mac OS 9 project](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/) as a reference. This time we’re going to be talking about the caches used to unique type metadata (and other things that need uniquing).

As mentioned previously, I implemented my stripped-down runtime in Swift as much as possible, though I had to use a few undocumented Swift features to do so. I’ll be showing excerpts of my runtime code throughout these posts, and you can check out the full thing [in the ppc-swift repository](https://belkadan.com/source/ppc-swift-project/tree/refs/heads/dev:/stdlib/_Runtime).

### Picking up where we left off

[When we left off](https://belkadan.com/blog/2020/07/Swift-Runtime-Type-Metadata/), we had just finished `swift_allocate­Generic­ValueMetadata`, which is used to instantiate generic types with their arguments. But `swift_allocate­Generic­ValueMetadata` isn’t called directly; it only shows up when metadata needs to be created for the first time. What actually gets called is a different function, `swift_get­GenericMetadata`.

```
@_silgen_name("swift_getGenericMetadata")
func swift_getGenericMetadata(
  _ request: MetadataRequest,
  _ arguments: UnsafePointer<UnsafeRawPointer>?,
  _ description: UnsafePointer<TypeContextDescriptor>
) -> MetadataResponse
```

We’re going to work backwards on this one. We know we’re going to need a cache eventually (so that we don’t end up with thousands of copies of `Array<Int>` in memory), but in the non-cached case, we have to call `swift_allocate­Generic­ValueMetadata`. Right?

```
let genericMetadataHeader = description.fullGenericContextHeader

let pattern = genericMetadataHeader.instantiationPattern
let rawMetadata = pattern.instantiationFunction[](description, arguments, pattern)
let metadata = rawMetadata.assumingMemoryBound(to: TypeMetadata.self)

if metadata.valueWitnessTable[]._.typeLayout._.flags.isIncomplete {
  var completionContext = MetadataCompletionContext()
  _ = pattern.completionFunction![](metadata, &completionContext, pattern)
}

return MetadataResponse(metadata: metadata, state: .complete)
```

Ooookay, maybe not. We do get the “pattern” that was mentioned last time, but instead of passing it to `swift_allocate­Generic­ValueMetadata`, we call some sort of “instantiation function” stored in the pattern. This is an opportunity for the compiler to insert some custom logic before actually doing the allocation, such as properly signing the arguments for [pointer authentication](https://developer.apple.com/documentation/security/preparing_your_app_to_work_with_pointer_authentication). But it will eventually call `swift_allocate­Generic­ValueMetadata` and give us our new metadata back.

And then we have a _second_ callback that we call immediately if the type is “incomplete” after being instantiated. What’s that about? Turns out the real Swift runtime is set up to handle [circular dependencies between types](https://bugs.swift.org/browse/SR-263), while my implementation, uh, does not. In the real Swift runtime, metadata is instantiated for a type, which can cause its dependencies to be instantiated, but the completion functions for these newly-instantiated metadata allocations don’t get called until all the dependencies have been instantiated and recorded in the cache-we-have-yet-to-build. This, along with making sure that dependencies still only access the basic information in a type (usually just its identity and generic arguments), solves the circular dependency problem. I decided to just not support this, since most types don’t have circular dependencies at instantiation time.^[1](#fn:circular) (By the way, the handling of circular dependencies is also what that `request` parameter is about. We’re just going to ignore it.)

So, the _instantiation function_ allocates and fills in the generic metadata as much as it can, and then there may also be a _completion function_ that does some additional work to make a complete, ready-to-use type. Makes sense, I hope!

### Where do these functions come from?

We’re going to take a detour to investigate those two properties `instantiationFunction` and `completionFunction`. Like `fullGenericContextHeader` last time, these are defined directly on the pointer because they need to compute a new pointer relative to the first one. Unlike `fullGenericContextHeader`, the new pointer is located elsewhere in memory, rather than being before or after the pattern.

```
struct RelativePointerOffset<Pointee> {
  var value: Int32
}

extension UnsafePointer {
  func applying<NewPointee>(
    _ offset: RelativePointerOffset<NewPointee>,
    additionalOffset: Int = 0
  ) -> UnsafePointer<NewPointee>? {
    if offset.value == 0 { return nil }
    let newPointer = UnsafeRawPointer(self) + Int(offset.value) + additionalOffset
    return newPointer.assumingMemoryBound(to: NewPointee.self)
  }
}

extension UnsafePointer where Pointee == GenericMetadataPattern {
  var instantiationFunction: UnsafePointer<GenericMetadataPattern.Instantiator> {
    return self.applying(self[]._.instantiationFunction)!
  }
}
```

Why use these _relative pointers?_ Well, consider the normal way to refer to something elsewhere in memory: a regular pointer. With a [64-bit address space](https://en.wikipedia.org/wiki/64-bit_computing), pointers take up 64 bits in memory, and because it’s not specified where a library might be loaded in memory, a pointer in static data needs to get “fixed up” to point to the right place when an app is launched. This process, part of _dynamic linking,_ is usually heavily optimized, but it’s still better to not have to do the work at all.

Relative pointers offer a more efficient alternative when referring to something that’s known to be in the same library or executable. By assuming that a single compiled binary will never be more than 2[GiB](https://en.wikipedia.org/wiki/Gibibyte) in size, it can refer to another address with a signed 32-bit offset. And as long as a library is always loaded all in one chunk, that offset is independent of what address the library is loaded at. The tradeoff is that when it’s actually time to _use_ the pointer, it’s not just a load; it now needs an addition as well. But that’s a very fast operation. ([My former coworkers went into detail on relative pointers and more in a talk at the 2018 LLVM Developers’ Meeting.](https://youtu.be/G3bpj-4tWVU))

Oh, and that “additional offset” argument is needed for whenever a relative pointer is accessed that _isn’t_ the first field of the pointed-to struct. Ideally I’d use [`MemoryLayout.offset(of:)`](https://developer.apple.com/documentation/swift/memorylayout/2996397-offset) for this, but [that’s not a compile-time constant](https://bugs.swift.org/browse/SR-12961), and I didn’t actually implement a run-time representation of key paths for this project, so that wasn’t an option.

But that’s what’s going on here: the generic metadata pattern stores a relative reference to the instantiation function, and I’ve defined a convenience property to resolve that relative reference.^[2](#fn:functions)

### Choosing our cache key

Okay, let’s get back to the plot. The way caching works, we need to write code that looks something like this:

```
let key = Key(uniquing constraints)
if let existingValue = cache[key] {
  return existingValue
}
let newValue = makeValue()
cache[key] = newValue
return newValue
```

We’ve already talked about how the “make value” part will work, but what do we do for the “key”? For a “uniquing” cache like this one, the key needs to uniquely describe the created value. So, what uniquely describes a generic type in Swift? The base type and the generic arguments, which we’re passed as arguments.

```
@_silgen_name("swift_getGenericMetadata")
func swift_getGenericMetadata(
  _ request: MetadataRequest,
  _ arguments: UnsafePointer<UnsafeRawPointer>?,
  _ description: UnsafePointer<TypeContextDescriptor>
) -> MetadataResponse
```

…hm. How do we know how many arguments there are? Oh, yeah, it’ll be in the `description`. But, hm, which count do we use?

```
struct GenericContextDescriptorHeader {
  var `_`: (
    numParams: UInt16,
    numRequirements: UInt16,
    numKeyArguments: UInt16,
    numExtraArguments: UInt16
  )
  
  var totalArgumentCount: Int {
    Int(self._.numKeyArguments) &+ Int(self._.numExtraArguments)
  }
}
```

When I started, I would have thought `numParams` was the right value, but it turns out there’s a bit more to generic types than that. We’ve been talking about `Array<Int>`, but what about `Set<Int>`? In this case, there’s actually going to be two separate low-level generic arguments: the type `Int`, and the conformance `Int: Hashable`. These are what’re counted as “key arguments” (as in “cache key”).

| Type | `num` `Params` | `num` `Require` `ments` | `num` `Key` `Argu``ments` | `num` `Extra` `Argu``ments` |
|---|---|---|---|---|
| `Array<T>` | 1 | 0 | 1 | 0 |
| `Set<T: Hashable>` | 1 | 1 | 2 | 0 |
| `Dictionary<K: Hashable, V>` | 2 | 1 | 3 | 0 |
| `Unmanaged<T: AnyObject>` | 1 | 1 | 1 | 0 |
| `Combine.Concatenate<` ` P: Publisher, S: Publisher` `> where P.Output == S.Output,` `P.Failure == S.Failure` | 2 | 4 | 4 | 0 |
| `extension Array` `where Element == Int {` ` struct Contrived {}` `}` | 1 | 1 | 0 | 0 |

The “key” to understanding the above examples is that the number of key arguments is equal to the number of parameters (including those in parent scopes), minus the parameters that are constrained to be concrete types, plus the number of conformance constraints.^[3](#fn:objc-protos) All other kinds of constraints, whether layout (class-bound), superclass, or same-type, can be derived directly from the type without a global lookup.

So, why are _these_ the key arguments instead of the parameters? Well, first of all, the parameters might include types that don’t need to be passed in at run time, like `Array.Element` in the `Contrived` example. But the other reason is a way to deal with conflicting conformances defined in different modules. If two different modules define different conformances to Hashable for the same type, a Set created in one module won’t produce the right results when used from the other! The Swift community is still trying to work out what to do about this in general, but the runtime, at least, will keep you from getting garbage results: it considers these two Sets to be different types even though they might have the same element type. That’s what we get from including conformances in the key arguments.^[4](#fn:witness-tables)

And what’s up with that empty `numExtraArguments` entry? Well, it’s currently unused, but my former coworker John McCall confirms [it was _once_ used for conformances](https://twitter.com/pathofshrines/status/1282452532451844097), i.e. they were _not_ considered key arguments in the past. So you can see that the idea of “conflicting conformances” is a tricky one. (In the future, the compiler could use this functionality to add extra “generic arguments” that aren’t part of the uniquing key, though I’m not sure what those would be.)

So: the information we need to uniquely identify a type is “the type descriptor” and the list of “key arguments”. The compiler actually provides room for a per-type cache, so we really just want the list of key arguments.

```
let genericMetadataHeader = description.fullGenericContextHeader
let keyArguments = UnsafeBufferPointer(
  start: arguments,
  count: Int(genericMetadataHeader[]._.base._.numKeyArguments))
```

That’s…not so bad, actually! And when we go to compare two instantiations, we can just compare the opaque pointers that uniquely represent the types and conformances.

### The actual cache

A cache that never removes anything can easily be implemented with a plain dictionary, and if we had the full Swift standard library at our fingertips we might reach for Dictionary to do that. There are two problems with that, though: I never got to implementing support for Hashable and Set and Dictionary in this project, and even if I did, they’d depend on the very runtime function we’re implementing! But fortunately there’s a second option on Mac OS 9: Core Foundation. [I mentioned Core Foundation way back in the first post in the series](https://belkadan.com/blog/2020/07/Swift-Runtime-Heap-Objects/#core-foundation); now we’re going to make that very work pay off by using it to implement our runtime cache.

CF’s dictionary type, [CFDictionary](https://developer.apple.com/documentation/corefoundation/cfdictionary-rum), is still around today. It works a lot like a Swift dictionary, but with the limitation that its keys and values fit in a single pointer. Because CF doesn’t exactly have a concept like “Any” (or AnyHashable), it also allows you to [manually customize the operations](https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks) it performs to compare and copy around keys and values. It also has predefined operations to support keys or values that are CF objects, and falls back to bitwise manipulation of the pointers themselves when the operations are absent. That’s good enough for us.

Because CFDictionary is so flexible, its API is defined in terms of UnsafeRawPointer, which isn’t so convenient. Let’s add some helpers to deal with that.

```
extension CFMutableDictionary {
  private func withObjectAsKey<Result>(
    _ object: AnyObject,
    do body: (UnsafeMutableRawPointer) -> Result
  ) -> Result {
    return withExtendedLifetime(object) {
      let opaqueObject = Unmanaged.passUnretained(object).toOpaque()
      return body(opaqueObject)
    }
  }

  internal subscript(_ object: AnyObject) -> UnsafeRawPointer? {
    get {
      withObjectAsKey(object) {
        CFDictionaryGetValue(self, $0)
      }
    }
    set {
      withObjectAsKey(object) {
        CFDictionarySetValue(self, $0, newValue)
      }
    }
  }
}
```

There’s nothing too complicated going on here, but it will allow us to use CF objects as keys and raw pointers as values. This isn’t checked, unfortunately, but it’s hardly the least safe thing we’re doing in the runtime, which is manipulating raw pointers left and right. The one complication is the use of `withExtendedLifetime`, which ensures that the object is not deallocated before the opaque reference to it is used as a key.

Now we can fill out the rest of our cache logic:

```
let rawArguments = UnsafeRawBufferPointer(keyArguments)
let cacheKey = CFDataCreate(nil,
  rawArguments.baseAddress?.assumingMemoryBound(to: UInt8.self),
  rawArguments.count).takeRetainedValue()

if let result = genericMetadataCache[cacheKey] {
  return MetadataResponse(
    metadata: result.assumingMemoryBound(to: TypeMetadata.self),
    state: .complete)
}

let pattern = genericMetadataHeader.instantiationPattern
let rawMetadata = pattern.instantiationFunction[](description, arguments, pattern)
let metadata = rawMetadata.assumingMemoryBound(to: TypeMetadata.self)

if metadata.valueWitnessTable[]._.typeLayout._.flags.isIncomplete {
  var completionContext = MetadataCompletionContext()
  _ = pattern.completionFunction![](metadata, &completionContext, pattern)
}

genericMetadataCache[cacheKey] = UnsafeRawPointer(metadata)
return MetadataResponse(metadata: metadata, state: .complete)
```

If you have a sharp eye, you might notice we’re using `takeRetainedValue()` on the result of [a CF function that’s not supposed to use Unmanaged](https://developer.apple.com/documentation/corefoundation/1542359-cfdatacreate). Shouldn’t be surprising if you think about it, though: [`CF_IMPLICIT_BRIDGING_ENABLED`](https://asciiwwdc.com/2013/sessions/404) wouldn’t have existed before Automatic Reference Counting did! Unfortunately, there’s not a quick way to enable it without editing the headers, and I’ve managed to avoid doing that so far. So CF APIs will all return Unmanaged on Classic Mac OS. Oh well.

Still, with this, we’re almost there! But…where does the cache come from? How does it get set up in the first place?

### Lazy cache initialization

Our cache is a CFDictionary (well, a CFMutableDictionary), and that’s not something we can create at compile time. (Not that we’d want to—that’d be a real waste of memory if your program never uses a particular generic type!) What the compiler _does_ give us is a pointer-sized bit of global static memory initialized to 0, accessible through the type descriptor.

We’re going to need other lazily-initialized caches in other parts of the runtime, so let’s make another helper:

```
func lazyInitialize<Object: AnyObject>(
  _ rawStorage: inout UInt,
  by create: () -> Object
) -> Object {
  if rawStorage == 0 {
    rawStorage = UInt(bitPattern: Unmanaged.passRetained(create()).toOpaque())
  }
  let opaquePtr = UnsafeRawPointer(bitPattern: rawStorage)!
  return Unmanaged<Object>.fromOpaque(opaquePtr).takeUnretainedValue()
}
```

The use of `passRetained(_:)` here with no corresponding `takeRetainedValue()` means that the created object will never be deallocated, but that’s what we want for a cache that lasts the lifetime of the program. The actual initialization is then pretty straightforward:

```
let rawCachePtr = genericMetadataHeader.instantiationCache
let genericMetadataCache: CFMutableDictionary = lazyInitialize(&rawCachePtr[]) {
  var keyCallbacks = kCFTypeDictionaryKeyCallBacks
  return CFDictionaryCreateMutable(
    /*allocator*/nil,
    /*maxCapacity*/0,
    &keyCallbacks,
    /*valueCallbacks*/nil
  ).takeRetainedValue()
}
```

Now we have our cache, we know what we’re going to do with it, and we know how to instantiate the new type metadata if it’s not already in the cache. We’re almost, _almost_ done with `swift_get­GenericMetadata`. There’s just one last thing we have to take care of…and indeed, I didn’t bother to finish implementing it before the “[ROSE-8 on Mac OS 9](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/)” post.

### Synchronization

See, even though Classic Mac OS apps use cooperative multitasking between programs, they _also_ support spinning off preemptive tasks—what we think of as threads on UNIXy systems like modern macOS. And since our caches are shared globally across threads, we need to make sure two threads don’t try to update the cache at the same time. Neither CFDictionary nor our `lazyInitialize` function are thread-safe. The simplest way to deal with this is to add a lock, which Classic Mac OS calls _entering a critical region._

```
func withMetadataLock<Result>(do body: () -> Result) -> Result {
  guard _MPIsFullyInitialized() else { return body() }

  _ = MPEnterCriticalRegion(criticalRegionID, /*timeout*/Duration(kDurationForever))
  defer { MPExitCriticalRegion(criticalRegionID) }

  return body()
}
```

This isn’t a _great_ implementation because the main, cooperative task can get blocked waiting for a preemptive task, and that’ll lock up _all_ the cooperative work on the machine until the other task exits the critical region. But it’s good enough—I can’t figure out how to yield to other programs on the system but not process any events in the current program. (Maybe that just doesn’t make sense in a cooperative world.) Note that if the multiprocessing library is _not_ fully initialized, preemptive tasks aren’t supported, and so we don’t have to worry about thread safety.

We’ve introduced another problem, though: where does `criticalRegionID` come from? We have to allocate _that_ globally, and we have to do _that_ without locking. The trick is to use [atomic compare-and-swap](https://en.wikipedia.org/wiki/Compare-and-swap):

```
if rawCriticalRegionID == 0 {
  var newCriticalRegionID: MPCriticalRegionID?
  _ = MPCreateCriticalRegion(&newCriticalRegionID)
  let rawNewRegionID = UInt32(UInt(bitPattern: newCriticalRegionID))
  if CompareAndSwap(/*expected*/0, rawNewRegionID, &rawCriticalRegionID) {
    // If we lost the race, delete the region we created and use the other one.
    MPDeleteCriticalRegion(newCriticalRegionID)
  }
}
let criticalRegionID = MPCriticalRegionID(bitPattern: UInt(rawCriticalRegionID))!
```

It’s a little awkward because `CompareAndSwap` is defined in terms of UInt32 rather than UInt, but it basically works. This is a pretty standard pattern for lazy initialization, but generally you **don’t want to roll your own synchronization**. Between the rules about what the compiler is allowed to optimize and the rules about what the CPU guarantees, it’s _really hard_ to assume you’ve covered all your bases and not left a bug in there. Heck, it’s hard enough to do that with locks! In this case I _think_ this code is safe (assuming `CompareAndSwap` is implemented correctly and conservatively) because there are only three possibilities:

1. The current thread reads a non-zero value, which will be a valid region ID. That value might get reused for the second reference to `rawCriticalRegionID` instead of reading the global again, but that’s okay.
2. The current thread reads a 0, successfully sets the region ID with `CompareAndSwap`, and then reads the value that was just set. The compiler can’t optimize out the second read because `CompareAndSwap` might have changed the global.
3. The current thread reads a 0, _whether correct or not,_ but then fails to set the region ID in `CompareAndSwap`. At that point the compiler doesn’t know _why_ the `CompareAndSwap` failed and still has to assume that it might have changed the global, so the second read still happens.

The reason this works is because the initialization is effectively a one-time, one-way transition. If we had to distinguish between a first compare-and-swap and a subsequent one, this might get a lot more complicated. And I should also note that **this still breaks the [formal rules](https://github.com/apple/swift-evolution/blob/master/proposals/0282-atomics.md)** by reading from a global variable while another thread might be in the middle of modifying it. Swift doesn’t currently have a way to tell the _compiler_ to do a “safe” read. We’re just lucky that the code the compiler emits for a single-threaded mode is going to work for a multi-threaded mode as well.

…oh, and we are also relying on the fact that passing a global variable `inout` to an API that expects a pointer is going to actually use the storage address of that global variable, rather than a temporary.^[5](#fn:global)

But with this helper, we can now protect all of our global-state-modifying work with a “critical region”. That gives us the final version of `swift_get­GenericMetadata`:

```
@_silgen_name("swift_getGenericMetadata")
func swift_getGenericMetadata(
  _ request: MetadataRequest,
  _ arguments: UnsafePointer<UnsafeRawPointer>?,
  _ description: UnsafePointer<TypeContextDescriptor>
) -> MetadataResponse {
  return withMetadataLock {
    let genericMetadataHeader = description.fullGenericContextHeader

    let rawCachePtr = genericMetadataHeader.instantiationCache
    let genericMetadataCache: CFMutableDictionary = lazyInitialize(&rawCachePtr[]) {
      var keyCallbacks = kCFTypeDictionaryKeyCallBacks
      return CFDictionaryCreateMutable(
        /*allocator*/nil,
        /*maxCapacity*/0,
        &keyCallbacks,
        /*valueCallbacks*/nil
      ).takeRetainedValue()
    }

    let keyArguments = UnsafeBufferPointer(
      start: arguments,
      count: Int(genericMetadataHeader[]._.base._.numKeyArguments))
    let rawArguments = UnsafeRawBufferPointer(keyArguments)
    let cacheKey = CFDataCreate(nil,
      rawArguments.baseAddress?.assumingMemoryBound(to: UInt8.self),
      rawArguments.count).takeRetainedValue()

    if let result = genericMetadataCache[cacheKey] {
      return MetadataResponse(
        metadata: result.assumingMemoryBound(to: TypeMetadata.self),
        state: .complete)
    }

    let pattern = genericMetadataHeader.instantiationPattern
    let rawMetadata = pattern.instantiationFunction[](description, arguments, pattern)
    let metadata = rawMetadata.assumingMemoryBound(to: TypeMetadata.self)
    
    if metadata.valueWitnessTable[]._.typeLayout._.flags.isIncomplete {
      var completionContext = MetadataCompletionContext()
      _ = pattern.completionFunction![](metadata, &completionContext, pattern)
    }
    
    genericMetadataCache[cacheKey] = UnsafeRawPointer(metadata)
    return MetadataResponse(metadata: metadata, state: .complete)
  }
}
```

### Wrap-up

We now know how a generic type gets instantiated, from the initial call to `swift_get­GenericMetadata` down to the layout of the type, with synchronization, caching, and the generic arguments handled along the way. [Next time we’ll talk about how the process differs for class metadata.](https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/)

1. Even real Swift didn’t implement correct handling of circular dependencies [until Swift 4.2](https://bugs.swift.org/browse/SR-263). [↩︎](#fnref:circular)
2. There’s actually something else interesting going on here, which is that we’re talking about a relative reference to a _function._ In Swift, references to functions aren’t represented using UnsafePointer; they have their own type.

  ```
  typealias Instantiator = @convention(c) (
    _ type: TypeErasedPointer<TypeContextDescriptor>,
    _ data: UnsafePointer<UnsafeRawPointer>?,
    _ pattern: TypeErasedPointer<GenericMetadataPattern>
  ) -> TypeErasedPointer<TypeMetadata>
  ```

  Normally that would mean having to [bitcast](https://developer.apple.com/documentation/swift/1641250-unsafebitcast) the resulting pointer to a function reference—there’s currently no other way to convert between the Unsafe*Pointer family and `@convention(c)` function references. But there’s a _second_ wrinkle that comes from using Classic Mac OS: a function pointer in Classic Mac OS doesn’t point directly at the start of a function. Instead, it points into a binary’s “table of contents”, which contains both the function and what’s effectively a secret argument for accessing globals in the library (known as a “base pointer”). Calling a function through a function pointer means loading that hidden argument into a register, then loading the actual address of the function’s code, and _then_ jumping to it.

  So how does this work with relative references? In theory, we could store a relative reference into the table of contents, which would then turn into a regular function pointer when loaded. But that’s not supported by the object file format I was using, though I don’t remember [which part of the convoluted chain](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/#gathering-materials) broke down. (It’s entirely possible that the table of contents _can_ be loaded at a different address from the constant data in a PowerPC program, which would prevent using any sort of compile-time offset to refer into it.) So I went with a simpler answer: [add an extra level of indirection](https://en.wikipedia.org/wiki/Fundamental_theorem_of_software_engineering). In practice, this means I’m not getting most of the benefits of relative references, especially since Classic Mac OS has a 32-bit address space. But it does mean the data containing the relative reference can be still be stored in constant memory, and it was easier to change the compiler to insert a level of indirection for function pointers than it would have been to only use relative references conditionally. At least, I think it was.

  Relative references _are_ used unaltered for plenty of other bits of static data; it’s only function pointers that need this special treatment. [↩︎](#fnref:functions)
3. Conformances to Objective-C protocols don’t count as key arguments, however. At run time, an Objective-C protocol conformance is just a marker saying “yes, this type supports these methods”, so there’s no point in storing a reference to that marker in the type once you know the constraint is satisfied. [↩︎](#fnref:objc-protos)
4. In the real Swift runtime, this is made more complicated because the compiler _synthesizes_ conformances for types imported from C. In this case, we _don’t_ want to treat conformances defined in different modules as potentially conflicting, and this is recorded in the _witness tables,_ the run-time representation of a conformance. In that case, two conformances would be compatible if they are defined on the same type with the same protocol and both marked compiler-synthesized-and-non-unique, which means we can’t just compare two lists of key arguments as opaque pointers. I never got around to implementing this in my Classic Mac OS runtime, so in theory I could run into this problem passing around sets of CF types or whatever. [↩︎](#fnref:witness-tables)
5. [I tried to find a good citation for this rule](https://forums.swift.org/t/lazyweb-citation-for-stored-globals-have-stable-addresses/40451) but was unsuccessful! There are definitely programs relying on it, though, and we Swift compiler developers have said it informally on the Swift forums many times. [↩︎](#fnref:global)

This entry was posted on [September](https://belkadan.com/blog/2020/09) 21, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Swift runtime](https://belkadan.com/blog/tags/swift-runtime)
