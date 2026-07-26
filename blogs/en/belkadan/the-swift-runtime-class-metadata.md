---
title: 'The Swift Runtime: Class Metadata'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/'
original_language: en
published: 2020-09-29
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ddc2ffc7f0d896d4'
translated: false
---

> 原文：[The Swift Runtime: Class Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [The Swift Runtime: Uniquing Caches](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/)

[The Swift Runtime: Class Metadata Initialization](https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/) »

« [The Swift Runtime: Uniquing Caches](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/?tag=swift)

[The Swift Runtime: Class Metadata Initialization](https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/?tag=swift) »

« [The Swift Runtime: Uniquing Caches](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/?tag=swift-runtime)

[The Swift Runtime: Class Metadata Initialization](https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/?tag=swift-runtime) »

## [The Swift Runtime: Class Metadata](#)

Welcome to the fifth in a series of posts on the [Swift runtime](https://belkadan.com/blog/tags/swift-runtime). The goal is to go over the functions of the Swift runtime, using what I learned in my [Swift on Mac OS 9 project](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/) as a reference. Last time we finished talking about how the metadata for structs and enums gets set up; this time we’re going to talk about classes.

As mentioned previously, I implemented my stripped-down runtime in Swift as much as possible, though I had to use a few undocumented Swift features to do so. I’ll be showing excerpts of my runtime code throughout these posts, and you can check out the full thing [in the ppc-swift repository](https://belkadan.com/source/ppc-swift-project/tree/refs/heads/dev:/stdlib/_Runtime).

### Structs and classes

One way in which Swift differs from some of its contemporaries (Rust, Go, Kotlin) is that it makes a distinction between structs and classes. The biggest difference is that struct instances are passed around by _value_ and class instances by _reference._^[1](#fn:semantics) But both structs and classes can have stored properties, declare methods, and conform to protocols. There’s just a few important ways that structs and classes differ:^[2](#fn:diagram)

- Because class instances aren’t implicitly copied when you do an assignment or call a function, they can have _deinitializers_ to clean up resources. ([Move-only value types will also be able to do this.](https://github.com/apple/swift/blob/master/docs/OwnershipManifesto.md))
- Because class instances are allocated in one place and stay there for their whole life, their address in memory can be used to uniquely [identify](https://developer.apple.com/documentation/swift/objectidentifier) them, at least while they’re alive. (Raw pointers work like this too.)
- Because class instances [carry their type](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/) with them, they can exhibit _polymorphic behavior_ without using generics. In practice this means “you can inherit from another class and override its methods”. (Protocol-typed values work like this too.)

You can see that you can build something very much like classes out of the component parts of move-only types, pointers, and protocol-typed values (what Rust would spell `Arc<dyn View>`), but Swift still found it useful to bundle all that behavior together, especially since it had to support interoperation with Objective-C from the get-go.

On the implementation side, there are a number of differences that fall out of this design (and from some other implementation choices in the language). Let’s take a look.

### The structure of class metadata

Remember how simple struct metadata was?

| Struct metadata |
|---|
| value witness table |
| kind* |
| type descriptor |

* remember, the value witness table pointer is stored _before_ the table; the “kind” field is the “first” value, i.e. the value at offset 0.

Yeah, classes ain’t so simple.

| Class metadata |
|---|
| destroyer |
| value witness table |
| kind* |
| superclass |
| _ObjC method cache_ |
| _ObjC method cache_ |
| _ObjC-compatible data_ |
| flags |
| instance “address point” |
| instance size |
| instance align mask + some reserved bits |
| class size |
| class “address point” |
| type descriptor |
| ivar destroyer |
| (methods and generic args) |
| (methods and generic args) |
| … |

* “kind” is still at offset 0.

There’s a lot going on there! What _is_ all this stuff? Why can’t we get away with storing all the interesting stuff in the type descriptor again? Why do we need any of this? *takes a deep breath* Okay, let’s go through it step by step:

- The **destroyer** calls the deinitializer and then deallocates the class’s memory. We talked about it in [the first post in this series](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/).
- We _still_ haven’t talked in depth about **value witness tables**, and we still aren’t going to, but every class has the same one, since all “values” used to manipulate classes are just references, and all object references behave the same.^[3](#fn:objc)
- Every metadata has a **kind**. As noted in [the first post in this series](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/), the kind for classes is carefully chosen not to overlap with any valid addresses…except on modern Apple platforms, where it’s replaced by a pointer to a “[metaclass](http://www.sealiesoftware.com/blog/archive/2009/04/14/objc_explain_Classes_and_metaclasses.html)” object for compatibility with Objective-C.
- Classes can have **superclasses**! And if they don’t have one, the field is `nil`.
- The next three fields are for compatibility with Objective-C. Swift does not use them for anything, and in fact [they’ve been removed upstream for non-Apple platforms](https://github.com/apple/swift/pull/31811), only a few weeks after I cut my own branch for this project. ([Thanks to Alejandro for the tip.](https://twitter.com/aalonso128/status/1310992586543443969))
- The **flags** are, well, flags, but I didn’t need any of the info they store in my runtime.
- The “**address point**” of an instance specifies whether any fields should be allocated _before_ the object’s metadata pointer when the class is instantiated. Why would you want to do this? Well, it would mean that even when you subclassed a class, you’d still be able to reference “the first ‘negative’ field” without having to know how big the superclass is.

  Swift currently does not implement this (i.e. the field is always 0), so I didn’t worry about it in my own runtime, but _in theory_ the real compiler and runtime could start using it.
- The **size** and **alignment** of instances has to be stored in the metadata because the type layout in the value witness table is the layout of a reference, not the layout of the actual class instance. Since you can’t have really big alignments anyway, some of the bits in this field are reserved for the runtime to store arbitrary data. For us that’s unused.
- The class metadata also has a **size** and **address point**, which are much the same as for instances. Instead of stored properties, though, we’re counting methods and generic arguments that need to get stored in the class.

  This isn’t actually used for much, because it’s not often that you need to know how much memory the class metadata _itself_ takes up. It’s used by the Objective-C runtime for dynamic subclassing, because dynamic subclasses are also going to expect the Swift methods and generic arguments to be there, and by reflection that wants to read the _entire_ metadata. Neither of things are relevant for my runtime.
- We talked about **type descriptors** when we talked about [struct metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata#representing-types-at-run-time): they have information on how to instantiate generic classes, and also store extra metadata for both generic and non-generic classes.
- The **ivar destroyer** is used in the special case of a failable initializer that fails _before_ calling `super.init` but _after_ a subclass has been initialized. In that case, the subclass’s fields have already been initialized, but running the full deinitializer wouldn’t be safe. (I didn’t actually implement support for this—it uses the runtime function `swift_dealloc­Partial­ClassInstance`—but it’s not complicated.)
- And finally we’ve got methods and generic arguments: first the generic args of the root class, if any, then the methods, then the generic args of the first-level subclass, then the methods, and so on. The methods form a vtable, or _virtual dispatch table,_ and so overrides are implemented by replacing a method pointer in the “superclass’s section” of methods.

  (My colleague [David Smith](https://twitter.com/Catfish_Man) has commented that it’s odd that Swift made method calls so efficient—an offset lookup in the class metadata—and then turned around and endorsed patterns that didn’t involve class hierarchies. Making method dispatch as fast as C++’s is a constraint that cuts off some [interesting ideas](http://www.sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html).)

Honestly this tour of class metadata is probably more informative than the runtime functions associated with classes, but we’ll go through those too.

## Allocating generic class metadata

Classes, structs, and enums all use the same entry point for accessing possibly-cached metadata, [`swift_get­GenericMetadata`](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/). But when it comes to actually _allocating_ that metadata, the needs are different for classes. It starts out with a fairly familiar pattern:

```
@_cdecl("swift_allocateGenericClassMetadata")
func swift_allocateGenericClassMetadata(
  _ rawDescription: TypeErasedPointer<ClassDescriptor>,
  _ arguments: UnsafePointer<UnsafeRawPointer>,
  _ rawPattern: TypeErasedPointer<GenericValueMetadataPattern>
) -> TypeErasedPointer<ClassMetadata> {
  let description = rawDescription.assumingMemoryBound(to: ClassDescriptor.self)
  let pattern = rawPattern.assumingMemoryBound(to: GenericClassMetadataPattern.self)

  let allocationBounds = description[].metadataBounds
```

The very first thing we need to know is the “bounds” of the metadata, which in this case means its negative and positive extents. This will give us the total size we need to allocate, as well as where to put the “zero offset” pointer that we’ll eventually end up returning. I’ve factored that out into a helper property on ClassDescriptor:

```
var metadataBounds: ClassMetadataBounds {
  let immediateMembersOffsetInWords =
    self._.metadataPositiveSizeInWords &- self._.numImmediateMembers
  let immediateMembersOffset =
    Int(immediateMembersOffsetInWords) &* MemoryLayout<Int>.size
  return ClassMetadataBounds(
    negativeSizeInWords: self._.metadataNegativeSizeInWords,
    positiveSizeInWords: self._.metadataPositiveSizeInWords,
    immediateMembersOffset: immediateMembersOffset)
}
```

We’ll come back to `immediateMembersOffset` soon. For now, this gives us enough info to actually call the allocator.

```
let bytes = swift_slowAlloc(
  size: allocationBounds.totalSizeInBytes,
  alignMask: MemoryLayout<UnsafeRawPointer>.alignment &- 1)
let rawMetadata = (bytes + allocationBounds.addressPointOffsetInBytes)
let metadata = rawMetadata.bindMemory(to: ClassMetadata.self, capacity: 1)
```

Aside: Wait, what happens if the superclass size changes? Won’t these values be invalidated? Indeed they will, but in Swift that’s a change that requires recompiling clients unless the base library is built with [library evolution support](https://swift.org/blog/library-evolution/) (or unless one of the class’s ancestors comes from Objective-C). My Swift-on-Classic runtime doesn’t support that, so I just left out all of that logic.

Now that we have our allocated metadata, we’ll start by filling in the “negative offset” fields:

```
rawMetadata.storeBytes(
  of: pattern.destroyFn[],
  toByteOffset: -2 &* MemoryLayout<Int>.size,
  as: Optional<UnsafeRawPointer>.self)
rawMetadata.storeBytes(
  of: swift_getObjectValueWitnessTable(),
  toByteOffset: -1 &* MemoryLayout<Int>.size,
  as: UnsafePointer<ValueWitnessTable>.self)
```

And then the regular fields:

```
metadata[]._.base.rawKind = TypeMetadata.Kind.class.rawValue
metadata[]._.superclass = nil
// This is an "is Swift" bit that isn't really needed on non-ObjC platforms.
metadata[]._.objcCompatibleData = 1
metadata[]._.flags = pattern[]._.classFlags

// Layout, filled in later.
metadata[]._.instanceAddressPoint = 0
metadata[]._.instanceSize = 0
metadata[]._.instanceAlignMask = 0

metadata[]._.classSize = UInt32(bounds.totalSizeInBytes)
metadata[]._.classAddressPoint = UInt32(bounds.addressPointOffsetInBytes)

metadata[]._.description = description
metadata[]._.ivarDestroyer = pattern.ivarDestroyer?[]
```

As you can see, there’s not much going on there! Most of the information is either copied directly from what we already have, or gets a dummy value to be filled in later. Is that really all we have to do?

Well, not quite. Turns out I skipped over two things from before: the “extra data” pattern that’s also in [struct metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata#filling-in-the-fields), and an additional data pattern that’s used for the class’s “immediate” members: the members that can be overridden but are not themselves overrides. The former actually adds on to the allocation size of the class; the latter is already included. So the first part of `swift_allocate­Generic­ClassMetadata` actually looks like this:

```
let bounds = description[].metadataBounds
var allocationBounds = bounds
if let extraDataPattern = pattern.extraDataPattern {
  allocationBounds.positiveSizeInWords &+=
    UInt32(extraDataPattern[]._.offsetInWords) &+
    UInt32(extraDataPattern[]._.sizeInWords)
}
```

And once we have our metadata, we need to initialize it from those patterns:

```
if let extraDataPattern = pattern.extraDataPattern {
  // Note: not using allocationBounds here
  let extraDataOffset =
    Int(bounds.positiveSizeInWords) &* MemoryLayout<Int>.size
  (rawMetadata + extraDataOffset).initialize(from: extraDataPattern)
}

let immediateMembers = rawMetadata + bounds.immediateMembersOffset
memset(
  immediateMembers,
  0,
  Int(description[]._.numImmediateMembers) &* MemoryLayout<Int>.size)
if let immediateMembersPattern = pattern.immediateMembersPattern {
  immediateMembers.initialize(from: immediateMembersPattern)
}
```

Okay, _now_ we’ve got everything initialized. There’s one last thing to do, and it’s the same as for structs: store the generic arguments in the metadata.

```
installGenericArguments(
  in: rawMetadata.assumingMemoryBound(to: TypeMetadata.self),
  at: bounds.immediateMembersOffset,
  description: rawDescription.assumingMemoryBound(to: TypeContextDescriptor.self),
  from: arguments)
return UnsafeRawPointer(rawMetadata)
```

We saw `installGenericArguments(in‍:at‍:description‍:from‍:)` [back in the third entry in this series](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata#filling-in-the-fields). Nothing’s changed, except that the offset of the generic arguments is based on the particular class’s bounds. As noted, it goes at the beginning of the “immediate members” section.

With that, our class is allocated…but we can hardly say it’s ready to use.

## Wrap-up

This post is getting a bit long, so I’m going to call it here, even though we only went through one function. [Next time we’ll look at the other half of class metadata initialization](https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/), which is mostly about filling in data from the superclass.

1. This isn’t _quite_ the same as “value semantics” vs. “reference semantics”, which is a whole talk in and of itself. In fact, [Alexis Gallagher gave such a talk in 2016](https://academy.realm.io/posts/swift-gallagher-value-semantics/), so you can check that out if you’re interested. [↩︎](#fnref:semantics)
2. I made an [exploratory diagram](https://twitter.com/UINT_MIN/status/902355871404965889) about this a while back. [↩︎](#fnref:diagram)
3. This is not quite true when Swift has to interoperate with Objective-C! Because [not all Objective-C objects are represented as pointers](https://mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html), there are slightly different rules for what the runtime can do with them. I’m not going to go into that in detail here, but the main thing is that there are more _spare bits_ for Swift object references, and that lets them get packed more tightly into certain enums. [↩︎](#fnref:objc)

This entry was posted on [September](https://belkadan.com/blog/2020/09) 29, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Swift runtime](https://belkadan.com/blog/tags/swift-runtime)
