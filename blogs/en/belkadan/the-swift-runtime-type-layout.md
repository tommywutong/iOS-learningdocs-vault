---
title: 'The Swift Runtime: Type Layout'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/'
original_language: en
published: 2020-09-07
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:e6f5eb87ac6d74a2'
translated: false
---

> 原文：[The Swift Runtime: Type Layout](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [The Swift Runtime: Heap Objects](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/)

[The Swift Runtime: Type Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/) »

« [The Swift Runtime: Heap Objects](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/?tag=swift)

[The Swift Runtime: Type Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/?tag=swift) »

« [The Swift Runtime: Heap Objects](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/?tag=swift-runtime)

[The Swift Runtime: Type Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/?tag=swift-runtime) »

## [The Swift Runtime: Type Layout](#)

Welcome to the second in a series of posts on the [Swift runtime](https://belkadan.com/blog/tags/swift-runtime). The goal is to go over the functions of the Swift runtime, using what I learned in my [Swift on Mac OS 9 project](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/) as a reference. This time we’re going to be talking about how tuples and structs get laid out at run time.more

As mentioned previously, I implemented my stripped-down runtime in Swift as much as possible, though I had to use a few undocumented Swift features to do so. I’ll be showing excerpts of my runtime code throughout these posts, and you can check out the full thing [in the ppc-swift repository](https://belkadan.com/source/ppc-swift-project/tree/refs/heads/dev:/stdlib/_Runtime).

### Type layout

Type layout refers to taking a struct or tuple and deciding how to arrange the fields in memory, based on each field’s _size_ and _alignment._ When complete, you know the struct or tuple’s overall size and alignment in addition to the offset of each field. For an example, consider the following struct:

```
struct Product {
  var id: UInt16
  var amountInGrams: Float
  var isOnSale: Bool
}
```

Let’s not worry about whether this is a _good_ struct; we’re only thinking about how to lay out the fields in memory. The absolute simplest thing would be to put them one after another:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| `id` | `amountInGrams` | `isOnSale` |  |  |  |  |

But this isn’t valid, because Floats have a required _alignment_ of 4 bytes. ([This article from Red Hat explains alignment pretty well.](https://developers.redhat.com/blog/2016/06/01/how-to-avoid-wasting-megabytes-of-memory-a-few-bytes-at-a-time/)[1](#fn:alignment)) Taking that into account, we end up with this:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| `id` |  | `amountInGrams` | `isOnSale` |  |  |  |  |  |

The algorithm here is pretty simple: for each field, start with the next available offset and round up to match the required alignment. The size of the struct is the total number of bytes used (in this case 9), and the alignment is the maximum alignment of all the fields (in this case 4). But this isn’t the _only_ possible layout algorithm; for example, you could sort the largest fields first:

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| `amountInGrams` | `id` | `isOnSale` |  |  |  |  |

This would pack the whole struct into only 7 bytes while still following the alignment rules.

So what does Swift do? For now, it just does the simple thing: lay the fields out in order, rounding up to alignment boundaries. (This means you can actually save on memory by carefully ordering your fields, although this probably only matters if you have many many instances of your structs.) But that’s not officially guaranteed by the language except in two specific cases:

- If you’re on a platform with a [stable ABI](https://swift.org/blog/abi-stability-and-apple/) (in practice, Apple’s OSs), then any public struct marked `@frozen` in a module with [library evolution](https://swift.org/blog/swift-5-1-released/#module-stability) enabled must have this layout, so that both a library and its clients can agree on what the layout will be.
- [Tuples are guaranteed to have this layout.](https://forums.swift.org/t/how-to-define-structures-that-can-be-passed-to-c/23901/4)[2](#fn:tuple)

In practice, every struct defined in Swift has this layout, at least through Swift 5.2. It wouldn’t have made sense for me to change it, especially since the compiler and the runtime have to agree on how structs are laid out.

### Type layout…at run time?

The “Product” example I showed above was a struct that could be laid out completely at compile time. However, that’s not always possible. Consider this struct, designed specifically for teaching purposes:

```
struct Pair<First, Second> {
  var first: First
  var second: Second
}
```

What offset is `second` at? Well, obviously it’s going to depend on the size of `First`, and it’ll also depend on the alignment of `Second`. If the types of `First` and `Second` aren’t known at compile time, it’s up to the runtime to figure it out.[3](#fn:compiletime) But it’s more complicated than that. Consider this code:

```
// A.swift
func makePair<First, Second>(_ first: First, _ second: Second) -> Pair<First, Second> {
  return Pair(first: first, second: second)
}

// B.swift
let pair: Pair<Int, String> = makePair(1, "abc")
print(pair.second)
```

The function `makePair` has to use the runtime to lay out its Pair instances, but the caller in B.swift knows all the types, and is going to access the string directly. So not only does the runtime need to do type layout, but now you know why it has to be consistent with how the compiler does it.

### Show me some code!

Okay, but I warn you, it’s not super interesting!

Let’s start with the algorithm I breezed past above, for how to do in-order type layout:

```
var size: UInt = 0
var alignMask: UInt = 0
for field in fieldTypes {
  size.roundUpToAlignMask(field.alignMask)
  size += field.size
  alignMask = max(alignMask, field.alignMask)
}
return (size, alignMask)
```

This is brushing over quite a bit, but it’s a good place to start. Already, though, there’s one change from what I described above: we’re working in terms of an alignment _mask_ instead of an alignment. This is taking advantage of the fact that all alignments on Swift-supported systems are powers of 2, which means it’s easy to force something to be aligned by masking off any lower bits. (For an alignment of 8/`0b1000`, the alignment mask would be 7/`0b0111`.) Compare the following three functions:

```
extension UInt {
  mutating func roundUpToArbitraryAlignment(_ alignment: UInt) {
    let offset = self % alignment
    if offset > 0 {
      self += alignment &- offset
    }
  }

  mutating func fastRoundUpToArbitraryAlignment(_ alignment: UInt) {
    self += alignment &- 1
    self &-= self % alignment
  }

  mutating func roundUpToAlignMask(_ alignMask: UInt) {
    self += alignMask
    self &= ~alignMask
  }
}
```

The first is a simple implementation of “round up to the next multiple”: it checks if we’re already there, and if not it goes “the rest of the way up”. The second is an old trick to avoid the `if` check: if the original offset was 0, the amount we add will get subtracted right back off again, and otherwise it’ll push us over the next multiple.

The third one is the same idea as the second, but taking advantage of the equivalence of “subtract the remainder” and “mask off lower bits” when the alignment is a power of two. In this case, we add one less than the alignment, and the mask is one less than the alignment, so the value we store might as well be one less than the alignment.

What you see above really is the basic algorithm. The actual implementation of type layout takes the opportunity to compute a few other things as well: if any of the fields require custom copying or destruction logic (labeled `isNonPOD`, non-“plain old data”, after a similar C++ concept, though this is better modeled by what C++ calls non-“[trivially copyable](https://en.cppreference.com/w/cpp/named_req/TriviallyCopyable)”), and similarly if they require custom _moving_ logic (`isNonBitwiseTakable`).

Once all fields are looped over, two extra fields are filled in: the stride, which is the size rounded up to the alignment, and whether the type can be stored inline in Swift’s opaque object buffer representation. The latter is a simple condition—“fits in storage that’s big enough for three pointers and aligned for pointers, and still allows bitwise taking”—that I won’t really go into here; they’re mostly only used for `Any` and protocol-typed values (existentials). The stride is used when computing offsets into arrays, where you have several of the same type arranged one after another in memory. (Honestly, I’m not sure how much we’d lose to not compute this up front.)[4](#fn:stride)

### Run-time representation

The compiler and runtime have to agree on how to lay out types, but they _also_ have to agree on how that layout’s going to be represented. We can think of these as structs as well, but the definitions I’m using look a little funny:

```
struct TypeLayout {
  typealias Layout = (
    size: UInt,
    stride: UInt,
    flags: TypeLayoutFlags,
    extraInhabitantCount: UInt32
  )
  var `_`: Layout

  init(_ value: Layout) {
    self._ = value
  }
  
  static var initialLayoutForValueType: TypeLayout {
    return TypeLayout((size: 0, stride: 0, flags: .init(), extraInhabitantCount: 0))
  }
}
```

What am I trying to do here? Well, I’m a former Swift compiler developer myself! I don’t want to rely on more unsupported behavior than I have to, and remember I said above: struct layout in Swift is not guaranteed, but tuple layout is. So all of the runtime data structures you see in this series will be using a tuple wrapped in a struct, to make sure the layout is guaranteed consistent with what the compiler emits.

EDIT: I want to note that I consider this a hack; the “supported” way to get types with a specific layout in Swift is to define them in a C header. For this project I decided to go with the tuple approach because (a) I’m trying to keep as much of the runtime in Swift as possible, and (b) I’m working with a fixed version of the compiler, so it can’t change out from under me.

Okay, so why the underscore for a variable name? Well, it’s not going to mean anything to see it at a use site, so I wanted something small and relatively easy to ignore. The underscore is normally a keyword meaning “ignored”, but with backtick escaping it becomes a valid member name. I’m not sure I’d recommend this in a public project, but for this one-person one it seems a reasonable idiom to adopt.

In that TypeLayout struct, you’ll recognize `size` and `stride`, but `alignMask` is missing, and there’s a field we haven’t talked about at all: `extraInhabitantCount`. What’s going on with that? Well, alignments are never going to be _that_ big, so Swift only reserves 8 bits for the alignment mask. The other 24 bits in the UInt32 field are used for flags:

```
struct TypeLayoutFlags {
  var rawValue: UInt32 = 0
  
  var alignMask: UInt {
    get { UInt(self.rawValue & 0xFF) }
    set {
      self.rawValue &= ~0xFF
      self.rawValue |= UInt32(newValue)
    }
  }

  var isNonPOD: Bool {
    get { rawValue.extractBit(at: 16) }
    set { rawValue.updateBit(at: 16, to: newValue) }
  }

  var isNonInline: Bool {
    get { rawValue.extractBit(at: 17) }
    set { rawValue.updateBit(at: 17, to: newValue) }
  }

  var isNonBitwiseTakable: Bool {
    get { rawValue.extractBit(at: 20) }
    set { rawValue.updateBit(at: 20, to: newValue) }
  }
}
```

I’ve left out a few flags we haven’t talked about yet, and there are also a number that aren’t currently used for anything. `extractBit(at:)` and `updateBit(at:to:)` are helpers that do what they say; I’m not going to show them here.

As for the “extra inhabitant count”, that’s a count of memory representations that won’t ever be valid values of the type, meaning the runtime can use them to represent `nil` in Optionals. We’ll talk more about that when we talk about enums. For now, we can just talk about Swift’s strategy for computing the extra inhabitant count of structs and tuples: pick the element with the highest count and use that.[5](#fn:loop)

```
extraInhabitantCount = fieldTypes.lazy.map { $0.extraInhabitantCount }.max() ?? 0
```

### All together now

Here’s the final version of tuple type layout:

```
private func performBasicLayout<TypeLayouts>(
  _ layout: inout TypeLayout,
  _ fieldTypes: TypeLayouts,
  setOffset: (_ fieldIndex: Int, _ offset: UInt32) -> Void
) where TypeLayouts: Collection, TypeLayouts.Element == TypeLayout {
  for (i, field) in fieldTypes.enumerated() {
    layout._.size.roundUpToAlignMask(field._.flags.alignMask)
    setOffset(i, UInt32(layout._.size))

    layout._.size += field._.size

    layout._.flags.alignMask = max(layout._.flags.alignMask, field._.flags.alignMask)
    if field._.flags.isNonPOD {
      layout._.flags.isNonPOD = true
    }
    if field._.flags.isNonBitwiseTakable {
      layout._.flags.isNonBitwiseTakable = true
    }
  }

  layout.computeStride()
  layout.computeInline()
}

@_silgen_name("swift_getTupleTypeLayout")
func swift_getTupleTypeLayout(
  _ result: UnsafeMutablePointer<TypeLayout>,
  _ elementOffsets: UnsafeMutablePointer<UInt32>?,
  _ flags: TupleTypeFlags,
  _ rawElements: UnsafePointer<UnsafePointer<TypeLayout>>
) {
  result[] = TypeLayout.initialLayoutForValueType
  let fieldTypes = UnsafeBufferPointer(start: rawElements, count: flags.numElements)
  performBasicLayout(&result[], fieldTypes.lazy.map { $0[] }) {
    elementOffsets?[$0] = $1
  }
  result[]._.extraInhabitantCount = fieldTypes.lazy.map { $0[]._.extraInhabitantCount }.max() ?? 0
}

struct TupleTypeFlags {
  var rawValue: UInt

  var numElements: Int {
    Int(rawValue & 0xFFFF)
  }
}
```

You can see the underscores from before for guaranteed-layout structs, as well as an extra extension for pointers that I personally like:

```
extension UnsafePointer {
  subscript() -> Pointee {
    self.pointee
  }
}
```

There’s also another undocumented attribute, `@_silgen_name`. Like `@_cdecl` from last time, `@_silgen_name` allows specifying an unmangled name for a function defined in Swift; unlike `@_cdecl`, it does not change the calling convention. That implies that `swift_get­Tuple­TypeLayout` was added later on, once we were committing to using the Swift calling convention for runtime functions. (You can see the signatures of all the runtime functions in [RuntimeFunctions.def](https://github.com/apple/swift/blob/master/include/swift/Runtime/RuntimeFunctions.def).)

### What about structs?

For tuples, the compiler will go out of its way to _just_ ask for the layout whenever possible, and leave out the rest of the information about the type if possible. But structs don’t work that way—a struct with run-time layout computes it once and stores that in the type’s _runtime metadata,_ even if all you do is access a field. This function looks almost the same as `swift_get­Tuple­TypeLayout`, but has a little bit extra at the beginning and end:

```
@_cdecl("swift_initStructMetadata")
func swift_initStructMetadata(
  _ structType: TypeErasedMutablePointer<StructMetadata>,
  _ rawLayoutFlags: UInt,
  _ numFields: UInt,
  _ rawFieldTypes: TypeErasedPointer<UnsafePointer<TypeLayout>>,
  _ fieldOffsets: UnsafeMutablePointer<UInt32>
) {
  var layout = TypeLayout.initialLayoutForValueType
  let fieldTypes = UnsafeBufferPointer(
    start: rawFieldTypes.assumingMemoryBound(to: UnsafePointer<TypeLayout>.self),
    count: Int(numFields))

  performBasicLayout(&layout, fieldTypes.lazy.map { $0[] }) {
    // If the offsets are already correct, it might be immutable memory.
    if fieldOffsets[$0] != $1 { fieldOffsets[$0] = $1 }
  }

  layout._.extraInhabitantCount = fieldTypes.lazy.map { $0[]._.extraInhabitantCount }.max() ?? 0
  
  let layoutFlags = StructLayoutFlags(rawValue: rawLayoutFlags)
  let vwtable = structType.assumingMemoryBound(to: StructMetadata.self).getOrCreateMutableVWTableForInit(layoutFlags)
  vwtable[]._.typeLayout = layout
}
```

Unlike `swift_get­Tuple­TypeLayout`, this function uses `@_cdecl`, which means it has to use C-compatible types in its declaration. That means all these metadata structs defined in Swift aren’t going to be allowed, and so I made up a silly typealias to write what a pointer’s _intended_ to point to.

```
typealias TypeErasedMutablePointer<Pointee> = UnsafeMutableRawPointer
```

It’s not checked by the compiler in any way, but it’s a tiny bit of documentation for my own benefit. (I don’t love the name, but couldn’t think of anything better.)

The other new thing here is this “vwtable” thing, and the hint at a type called StructMetadata. We’ll talk a _lot_ more about these later, but for now you just need to know that every type has a pointer to a _value witness table_ that defines basic operations on the type, and that table includes the type layout information. `getOrCreate­Mutable­VWTable­ForInit(_:)` just determines whether or not the table can be modified in place; if not, it’ll allocate a new table, initialized with a copy of the original.

```
extension UnsafeMutablePointer where Pointee == StructMetadata {
  var valueWitnessTable: UnsafePointer<ValueWitnessTable> {
    get {
      UnsafeRawPointer(self).load(
        fromByteOffset: -MemoryLayout<UnsafePointer<ValueWitnessTable>>.size,
        as: UnsafePointer<ValueWitnessTable>.self)
    }
    nonmutating set {
      UnsafeMutableRawPointer(self).storeBytes(
        of: newValue,
        toByteOffset: -MemoryLayout<UnsafePointer<ValueWitnessTable>>.size,
        as: UnsafePointer<ValueWitnessTable>.self)
    }
  }

  func getOrCreateMutableVWTableForInit(
    _ flags: StructLayoutFlags
  ) -> UnsafeMutablePointer<ValueWitnessTable> {
    if flags.isValueWitnessTableMutable {
      return UnsafeMutablePointer<ValueWitnessTable>(mutating: self.valueWitnessTable)
    }
    let newVWT = UnsafeMutablePointer<ValueWitnessTable>.allocate(capacity: 1)
    newVWT.initialize(to: self.valueWitnessTable[])
    self.valueWitnessTable = UnsafePointer<ValueWitnessTable>(newVWT)
    return newVWT
  }
}
```

This isn’t everything you need to initialize a generic struct with particular arguments, but it’s a good start. We’ll pick up the rest later.

### Wrap-up

Now you know how the Swift runtime takes fields of a struct or elements of a tuple and lays them out in memory—not just the algorithm, but the actual implementation. [Next time we’ll start looking at the full run-time representation of types: _type metadata._](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/)

1. Thanks to [@matt_dz](https://twitter.com/matt_dz/status/1273749196911206400) for the recommmendation. [↩︎](#fnref:alignment)
2. The original wording by John McCall in 2017 left room for tuples to be broken up when stored in a struct; I think at this point that’s very unlikely, given the availability of features like [`MemoryLayout.offset(of:)`](https://developer.apple.com/documentation/swift/memorylayout/2996397-offset), which lets you ask for the offset of any stored property in a struct, including tuples. A tuple local variable may still be broken up for optimization purposes, though.

  After I first published this post, [Lily Ballard](https://twitter.com/LilyInTech) also prompted me to ask the Swift core team to clarify whether John’s comment really was a promise going forward. [Discussion is ongoing.](https://forums.swift.org/t/guarantee-in-memory-tuple-layout-or-dont/40122) [↩︎](#fnref:tuple)
3. In languages like C++ and Rust, generics are _instantiated_ or _monomorphized_ with concrete types as part of compilation; if a generic function calls another generic function, the top-level concrete type gets propagated all the way through. This places an interesting limitation on separately-compiled libraries: a library can’t provide a generic function or type unless its body is exposed to clients. On the other hand, Swift is one of few statically-typed languages to support run-time generics like this, because it requires extra indirection and a more complex runtime. [↩︎](#fnref:compiletime)
4. The most common algorithm used for structs in C is very much like the Swift layout algorithm, but with the addition of padding at the _end_ of a struct to make sure its size is a multiple of its alignment, meaning that the size and stride are always the same. This simplifies things, but it means that space is wasted when the struct is embedded in a larger struct—additional fields with smaller alignment can’t get packed into that padding. [↩︎](#fnref:stride)
5. Why isn’t this part of the loop we talked about above? The layout algorithm gets used in a few different places, and the need for the extra inhabitant count is different in different circumstances. [↩︎](#fnref:loop)

This entry was posted on [September](https://belkadan.com/blog/2020/09) 07, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Swift runtime](https://belkadan.com/blog/tags/swift-runtime)
