---
title: 'The Swift Runtime: Type Metadata'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/'
original_language: en
published: 2020-09-14
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:ce8250a287e54d79'
translated: false
---

> 原文：[The Swift Runtime: Type Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [The Swift Runtime: Type Layout](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/)

[The Swift Runtime: Uniquing Caches](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/) »

« [The Swift Runtime: Type Layout](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/?tag=swift)

[The Swift Runtime: Uniquing Caches](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/?tag=swift) »

« [The Swift Runtime: Type Layout](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/?tag=swift-runtime)

[The Swift Runtime: Uniquing Caches](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/?tag=swift-runtime) »

## [The Swift Runtime: Type Metadata](#)

Welcome to the third in a series of posts on the [Swift runtime](https://belkadan.com/blog/tags/swift-runtime). The goal is to go over the functions of the Swift runtime, using what I learned in my [Swift on Mac OS 9 project](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/) as a reference. This time we’re going to be talking about _type metadata,_ the representation of types at run time.more

As mentioned previously, I implemented my stripped-down runtime in Swift as much as possible, though I had to use a few undocumented Swift features to do so. I’ll be showing excerpts of my runtime code throughout these posts, and you can check out the full thing [in the ppc-swift repository](https://belkadan.com/source/ppc-swift-project/tree/refs/heads/dev:/stdlib/_Runtime).

### Background

In some languages, types are purely a compile-time concept. They provide a communication channel between the developer and the compiler that allows for catching mistakes (“that’s a floating-point number, not a pointer”), abstracting operations (“read from the third field” rather than “read the two-byte value at offset 8”), and optimization (“this unsigned integer will never be less than 0”). But many other languages—probably _most_ languages these days—have at least some run-time uses of types as well, such as validating types (“cast this to a table view”), doing different things based on type (“override this method”), and inspecting information about a type and its instances (“dump the contents of this struct”). And some languages _only_ use types in run-time ways, foregoing any compile-time use.

Swift is one of the in-between languages that uses types both for compile-time and run-time purposes. The most obvious run-time use of a type is when you explicitly write `Array<Int>.self`, but they also come up when using a generic type or function, converting a concrete value to a protocol type, or calling an overridable method on a class. Therefore, there must be information present at run time to represent a type.

### Representing types at run time

In Swift, types are represented by unique pointers to structured data, which can be statically or dynamically allocated. This data has a different representation based on _what_ kind of type we’re talking about, so if we’re not sure what kind of type we have, there are only two fields we can access safely: a **kind** field at offset 0, and a **value witness table** pointer just _before_ the start of the type metadata.[1](#fn:vwt) To get at any other information, we have to check the kind first and then cast to the appropriate type.

In this post, we’re going to focus on struct metadata, which actually shares its layout with enum metadata. Struct metadata adds one more required field: a pointer to the **type context descriptor**. What’s that? If type metadata represents a fully concrete type like `Array<Int>`, a type descriptor represents a type declaration like `Array`. It turns out _this_ is where most of the interesting reflection information is for a type, such as its name, a description of its fields or cases, and the constraints on its generic parameters, if any. There’s no reason to have a separate copy of this for every concrete instantiation of a generic type, so Swift stores it separately. (The type descriptor is also the key used to look up whether a type conforms to a protocol, since that has to work regardless of what generic arguments are currently being used.)

What `Array<Int>` _does_ need to store is, well, `Int`—that is, any generic arguments, plus conformances that satisfy constraints on those generic arguments. These get stored immediately following the main struct metadata, which means the total allocation size for generic struct metatata is going to be “2 pointers + 1 pointer-sized kind field + some amount of extra data”. The runtime doesn’t actually have to touch these much; it just copies them in and lets individual methods of the type access them as necessary.

So let’s start building our generic struct metadata allocation function:

```
@_cdecl("swift_allocateGenericValueMetadata")
func swift_allocateGenericValueMetadata(
  _ rawDescription: TypeErasedPointer<TypeContextDescriptor>,
  _ arguments: UnsafePointer<UnsafeRawPointer>,
  _ pattern: TypeErasedPointer<GenericValueMetadataPattern>,
  _ extraDataSize: UInt
) -> TypeErasedPointer<ValueMetadata> {
  let description = rawDescription.assumingMemoryBound(to: TypeContextDescriptor.self)

  let headerSize = MemoryLayout<UnsafePointer<ValueWitnessTable>>.size
  let totalSize = headerSize + MemoryLayout<ValueMetadata>.size + Int(extraDataSize)
  let bytes = UnsafeMutableRawPointer(NewPtr(totalSize)!)

  let rawMetadata = (bytes + headerSize)
  // Simplified for this post;
  // really we have to check whether it's a struct or an enum.
  _ = rawMetadata.bindMemory(to: StructMetadata.self, capacity: 1)

  // Hand-waving part 1 (will be explained below)
  initializeValueMetadata(
    rawMetadata.assumingMemoryBound(to: ValueMetadata.self),
    description: description,
    from: pattern.assumingMemoryBound(to: GenericValueMetadataPattern.self))

  // Hand-waving part 2 (will be explained below, also applies to classes)
  installGenericArguments(
    in: rawMetadata.assumingMemoryBound(to: TypeMetadata.self),
    at: MemoryLayout<ValueMetadata>.size,
    description: description,
    from: arguments)

  return UnsafeRawPointer(rawMetadata)
}
```

`swift_allocate­Generic­ValueMetadata` is handed a type descriptor and some generic arguments, but it’s also given a _pattern_ and an “extra data size” value. What are those for? Well, the “extra data size” represents that extra space that’s needed for generic arguments…and for anything else that’s associated with the type. (Remember those “field offsets” from the previous post?) The pattern’s going to be used in `initializeValueMetadata` to, well, set up the metadata, and then `installGenericArguments` copies in the generic arguments just after the fixed-size metadata. Pretty straightforward, huh?

### Filling in the fields

Let’s “zoom in” on those helper functions, starting with `initializeValueMetadata`. This is going to have to set the kind and value witness table pointer, and I guess copy in the description pointer too.

```
private func initializeValueMetadata(
  _ metadata: UnsafeMutablePointer<ValueMetadata>,
  description: UnsafePointer<TypeContextDescriptor>,
  from pattern: UnsafePointer<GenericValueMetadataPattern>
) {
  UnsafeMutableRawPointer(metadata).storeBytes(
    of: pattern.valueWitnesses,
    toByteOffset: -MemoryLayout<UnsafeRawPointer>.stride,
    as: UnsafePointer<ValueWitnessTable>.self)
  metadata[]._.base.rawKind = pattern[]._.base._.flags.value_metadataKind
  metadata[]._.description = description

  if pattern[]._.base._.flags.hasExtraDataPattern {
    let extraData = UnsafeMutableRawPointer(metadata + 1)
    extraData.initialize(from: pattern.extraDataPattern)
  }
}
```

I’m not going to show the full layouts of these structs this time, but you can see how ValueMetadata has a `base` field that represents the TypeMetadata part, and GenericValueMetadataPattern has a `base` field that represents a general GenericMetadataPattern, which makes this a sort of subclassing. The value witness pointer comes from the pattern rather than the type descriptor, which allows the type descriptor data to be stored in true-constant memory (by not referencing anything from other libraries). Curiously, the kind comes from the pattern as well; I would have expected it to be derived from the type descriptor’s kind. (It’s not going to be exactly the same, though, because optionals are so important that they get their own metadata kind, despite being a kind of enum.)

The other thing this function does is copy in an “extra data pattern”, doing so just after the ValueMetadata’s required fields in memory. (That’s what the `UnsafeMutableRawPointer(metadata + 1)` means.) This isn’t going to be the generic arguments yet, since they were passed separately, but it can include literal values, or just zeroing out a bunch of that extra data for use later.

```
extension UnsafeMutableRawPointer {
  func initialize(from pattern: UnsafePointer<GenericMetadataPartialPattern>) {
    let offsetInBytes = Int(pattern[]._.offsetInWords) &* MemoryLayout<UInt>.size
    memset(self, 0, offsetInBytes)
    (self + offsetInBytes).copyMemory(
      from: pattern.data,
      byteCount: Int(pattern[]._.sizeInWords) &* MemoryLayout<UInt>.size)
  }
}
```

This mix of C and Swift low-level memory operations is an attempt to adhere to Swift’s [pointer type rules](https://twitter.com/AirspeedSwift/status/1276565629609230336). Swift’s pointers don’t give us a great way to zero out memory _without_ giving it a type, or to copy memory that’s known to contain only values of unknown but trivial type _and_ preserve those types. (`copyMemory` preserves the current type instead of overwriting it.)

At this point, all that’s left to do is copy in the generic arguments. This is essentially trivial:

```
private func installGenericArguments(
  in metadata: UnsafeMutablePointer<TypeMetadata>,
  at offset: Int,
  description: UnsafePointer<TypeContextDescriptor>,
  from arguments: UnsafePointer<UnsafeRawPointer>
{
  let generics = description.fullGenericContextHeader!
  let argumentStart = UnsafeMutableRawPointer(metadata) + byteOffset
  argumentStart.initializeMemory(
    as: UnsafeRawPointer.self,
    from: arguments,
    count: generics[]._.base.totalArgumentCount)
}
```

Are you getting the hang of reading those pointer-to-structs-with-tuple-layout expressions? Then you might notice there’s one here that doesn’t quite fit: `description` is a pointer, but we’re accessing `fullGenericContextHeader` directly on it. What does that mean? Turns out, not too much: it’s just trying to access data stored at the end of the type descriptor, and to do that it needs to compute a new pointer.

```
extension UnsafePointer where Pointee == TypeContextDescriptor {
  var fullGenericContextHeader: UnsafePointer<TypeGenericContextDescriptorHeader> {
    let trailingObjectPtr: UnsafeRawPointer
    switch self[]._.base._.flags.kind {
    case .struct:
      trailingObjectPtr = UnsafeRawPointer(self) + MemoryLayout<StructDescriptor>.stride
    case .class:
      trailingObjectPtr = UnsafeRawPointer(self) + MemoryLayout<ClassDescriptor>.stride
    case .enum:
      trailingObjectPtr = UnsafeRawPointer(self) + MemoryLayout<EnumDescriptor>.stride
    default:
      fatalError()
    }
    return trailingObjectPtr.assumingMemoryBound(to: TypeGenericContextDescriptorHeader.self)
  }
}
```

That’s it, we’ve built a valid generic type!

### Wrap-up

We now know how the type metadata for a generic type gets built at run time: given a type descriptor, a pattern, and some generic arguments, a new type is allocated and filled in. But where’s the call to [`swift_init­StructMetadata`](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/#what-about-structs) from last time? And who calls `swift_allocate­Generic­ValueMetadata`, anyway? It can’t just get called every time someone needs the type for `Array<Int>`, because that could end up allocating thousands of copies of the same type. [We need some form of caching instead, and we’ll pick that up next time.](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/)

1. As mentioned briefly in the previous post, the value witness table defines basic operations on the type, which is necessary for a fully generic function. (When you say `var x: T = y`, how much memory is allocated for `x`, and how does it initialize each of its fields from `y`?) It’s at a negative offset so that Swift class types can have a layout compatible with Objective-C class types on modern Apple platforms. [↩︎](#fnref:vwt)

This entry was posted on [September](https://belkadan.com/blog/2020/09) 14, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Swift runtime](https://belkadan.com/blog/tags/swift-runtime)
