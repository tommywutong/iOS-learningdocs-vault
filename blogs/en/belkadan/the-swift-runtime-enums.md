---
title: 'The Swift Runtime: Enums'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/10/Swift-Runtime-Enums/'
original_language: en
published: 2020-10-20
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:41f2ef88872bcf87'
translated: false
---

> 原文：[The Swift Runtime: Enums](https://belkadan.com/blog/2020/10/Swift-Runtime-Enums/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [The Swift Runtime: Class Metadata Initialization](https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/)

[Negotiate Your Offers!](https://belkadan.com/blog/2020/11/Negotiate-Your-Offers/) »

« [The Swift Runtime: Class Metadata Initialization](https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/?tag=swift)

[Swift Regret: Protocol Syntax](https://belkadan.com/blog/2021/08/Swift-Regret-Protocol-Syntax/?tag=swift) »

« [The Swift Runtime: Class Metadata Initialization](https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/?tag=swift-runtime)

## [The Swift Runtime: Enums](#)

Welcome to the seventh in a series of posts on the [Swift runtime](https://belkadan.com/blog/tags/swift-runtime). The goal is to go over the functions of the Swift runtime, using what I learned in my [Swift on Mac OS 9 project](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/) as a reference. We’ve talked about structs and classes, so the obvious next choice is enums, the last of Swift’s three “concrete” user-definable types.more

As mentioned previously, I implemented my stripped-down runtime in Swift as much as possible, though I had to use a few undocumented Swift features to do so. I’ll be showing excerpts of my runtime code throughout these posts, and you can check out the full thing [in the ppc-swift repository](https://belkadan.com/source/ppc-swift-project/tree/refs/heads/dev:/stdlib/_Runtime).

### “Discriminated unions”

Enums in Swift are defined by a set of cases, each of which may or may not have a payload. The most famous enum is Optional[1](#fn:bool), which has one case with a payload and one without:

```
enum Optional<Wrapped> {
  case none
  case some(Wrapped)
}
```

Optional is so important in Swift that it has its own [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar) (`Int?` instead of `Optional<Int>`), an implicit conversion (`Int` converts to `Optional<Int>`), and dedicated language features (`if let`, `?.`, etc). But the underlying functionality of Optional is available to anyone who defines their own enum with the same form:

```
enum Maybe<Value> {
  case just(Value)
  case nothing
}
```

The functionality of an enum-with-payloads is often known as a [discriminated union](https://en.wikipedia.org/wiki/Tagged_union), among several other names. Swift chose to call it an “enum” after the much simpler C feature (which doesn’t support payloads), but during its development we called them “one-ofs” (from [CLU, the earliest language to have type-safe discriminated unions](https://en.wikipedia.org/wiki/CLU_(programming_language))), and then “[unions](https://github.com/apple/swift/commit/674a03b08583037a0e1906266fdb5a5f0065dc87)” before settling on “enums”. Rust uses “enum” too, so we’re in good company.

Anyway, I’ve talked a lot about enums to an audience that probably already gets it, so let’s go under the hood. The compiler divides Swift enums into three groups: no-payload, single-payload, and multi-payload. We’ll talk about each of these below.

### No-payload enums

```
enum NamedColor<ColorSpace> {
  case white, yellow, orange, red
  case magenta, purple, blue, cyan
  case green, darkGreen, brown, tan
  case lightGrey, mediumGrey, darkGrey, black
  // https://en.wikipedia.org/wiki/List_of_software_palettes#Apple_Macintosh_default_16-color_palette
}
```

A no-payload enum is like a C enum: its cases are just mutually-exclusive names. That means the compiler can just assign each case a numeric representation, and we’re done. There’s no run-time layout necessary.[2](#fn:evolution) Of course, a no-payload enum can still have generic parameters, which might get used in methods and such, but there’s nothing _stored_ in the enum values that’s generic, so nothing needs to be done beyond the existing logic in [`swift_allocate­Generic­ValueMetadata`](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata/).

There’s one other twist on no-payload enums compared to C enums: if you use Swift’s “raw value” support, the representation in memory might still be different from the raw value:

```
enum Multiplier: Int {
  case deca = 10
  case hecto = 100
  case kilo = 1_000
  case mega = 1_000_000
  case giga = 1_000_000_000

  case kibi = 0x400
  case mebi = 0x10_0000
  case gibi = 0x4000_0000
}
```

The current implementation of the compiler represents the value `Multiplier.kilo` as “2”, and also notes that it only takes one byte. When the user asks for `Multiplier.kilo.rawValue`, that’s calling a compiler-generated (and optimized) switch statement to get the raw value, _not_ just reinterpreting the value as an integer. This is good for saving space, as well as for raw values that are strings![3](#fn:objc)

That’s pretty much all there is to say about no-payload enums.

### Single-payload enums

If an enum only has one case that has a payload, the compiler and the runtime ~~conspire~~ collaborate to pick the most efficient layout based on the type of the payload and the number of non-payload cases. In the simplest case, this just ends up being “if this flag is set, there’s a valid value here, and otherwise there’s not”. Here’s an example for `Optional<Int32>`:

|  | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| `.some(0x11223344)` | `0x11223344` | `0` |  |  |  |
| `.none` |  | `1` |  |  |  |

(If you’re wondering why 0 is the “valid value” flag and not 1, consider that other enums may have more than one non-payload case.)

Let’s start by assuming this is the best we can do, and write some code. What operations do we need?

- Decide how much additional space to allocate for non-payload cases.
- Provide ways to get and set the “tag” of the enum, to record which case we’re in. (We don’t need to get or set the actual payload, because either it’s valid or it isn’t.)

These translate to some (mostly) pretty straightforward pseudocode, first for computing the layout of the enum type:

```
assert(numberOfCases <= UInt32.max)
let numTagBytes = (
  numberOfCases <= 1 ? 0 :
  numberOfCases <= UInt8.max ? 1 :
  numberOfCases <= UInt16.max ? 2 : 4)

var layout = payloadTypeLayout
layout._.size += numTagBytes
// Have to recompute these for the larger size.
layout.computeStride()
layout.computeInline()
```

And then for getting the tag:

```
let tagBytesAddr = enumValueRawAddr + payloadTypeLayout._.size
let numTagBytes = enumLayout._.size - payloadTypeLayout._.size
return tagBytesAddr.loadUnalignedBigEndianValue(size: numTagBytes)

extension UnsafeRawPointer {
  func loadUnalignedBigEndianValue(size: Int) -> UInt32 {
    var result: UInt32 = 0
    for i in 0..<size {
      result <<= 8
      result |= UInt32(self.load(fromByteOffset: i, as: UInt8.self))
    }
    return result
  }
}
```

(I’m leaving out setting because it’s pretty much the same as getting.)

In theory, that’s all it takes to make a discriminated union. We’ve even packed the tag in as tight as possible based on the number of cases, though because we haven’t made any alignment guarantees we have to assemble and disassemble it from scratch on a byte-by-byte basis. But we can do better for other types, and indeed we _have_ to do better for interoperability with C.

### “Extra inhabitants”

One of Swift’s biggest improvements over Objective-C (in my not-so-humble opinion) was following the lead of other languages in making nullability of pointers explicit using Optional: an `Optional<UIView>` can be `nil`, but a plain `UIView` reference cannot. However, in order to do that without some sort of conversion operation, we need a smarter representation of Optional: one that can use the same representation for `nil` that C uses for `NULL`. That is, for an `Optional<UnsafePointer<Int32>>` on PowerPC, we want the following layout:

|  | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| (a valid pointer) | (its address) |  |  |  |
| `nil` | `0x00000000` |  |  |  |

How do the compiler and runtime know that `0x00000000` isn’t a valid pointer? I mean, yeah, it’s going to be hardcoded somewhere, but hardcoding the standard library’s pointer structs wouldn’t be sufficient to satisfy one of Swift’s basic layout guarantees: **a struct containing a single stored property has the same layout as the property**. That is, if I write a wrapper struct FooPointer that contains a single four-byte UnsafePointer (remember, Classic Macs used 32-bit PowerPC CPUs), Swift should be smart enough to only use four bytes for `Optional<FooPointer>` as well. The purpose of this is to make sure that people can feel comfortable writing abstractions without worrying that they’ll use more memory than the raw types they’re built on—a worthy goal! So how do we do this?

The answer comes from something we’ve already seen, albeit in passing: the _extra inhabitant count_ in the [TypeLayout struct](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/#run-time-representation).

> As for the “extra inhabitant count”, that’s a count of memory representations that won’t ever be valid values of the type, meaning the runtime can use them to represent `nil` in Optionals. We’ll talk more about that when we talk about enums. For now, we can just talk about Swift’s strategy for computing the extra inhabitant count of structs and tuples: pick the element with the highest count and use that.
> 
> ```
> extraInhabitantCount = fieldTypes.lazy.map {
>   $0.extraInhabitantCount
> }.max() ?? 0
> ```

As quoted above, extra inhabitants are memory representations that are never used for a particular type. The most common of these is “0 will never be a valid pointer”, but there are a few others we can think of, like “100 does not represent a valid Multiplier value” from the enum above. The Swift compiler and runtime are smart enough to use these extra “bit patterns” to represent non-payload cases in a single-payload enum.

So, assuming we already have “extra inhabitant” information for types, we now need to modify our allocation and get/set logic to account for it.

### `swift_init­Enum­Metadata­SinglePayload`

Let’s get started with the real function:

```
@_cdecl("swift_initEnumMetadataSinglePayload")
func swift_initEnumMetadataSinglePayload(
  _ opaqueEnumType: TypeErasedMutablePointer<EnumMetadata>,
  _ rawLayoutFlags: UInt,
  _ opaquePayloadType: TypeErasedPointer<TypeLayout>,
  _ emptyCases: UInt32
) {
  let enumType = opaqueEnumType.assumingMemoryBound(to: EnumMetadata.self)
  let layoutFlags = EnumLayoutFlags(rawValue: rawLayoutFlags)
  let payloadTypeLayout =
    opaquePayloadType.assumingMemoryBound(to: TypeLayout.self)[]
```

In the best scenario, we’ll be able to use extra inhabitants for all the non-payload cases. If not, though, we’ll need extra space.

```
let unusedExtraInhabitants =
  Int(payloadType._.extraInhabitantCount) - Int(emptyCases)
let remainingEmptyCases = max(0, -unusedExtraInhabitants)

let extraTagBytes = getExtraTagBytes(
  payloadTypeLayout._.size,
  remainingEmptyCases,
  1)
```

We’ll come back to `getExtra­TagBytes` in a minute, but first let’s finish out the rest of this function. Most of it looks like the pseudocode from before, but with the addition of extra inhabitant information:

```
var layout = payloadTypeLayout
layout._.size += UInt(extraTagBytes)
layout._.flags.hasEnumWitnesses = true
layout._.extraInhabitantCount = UInt32(max(0, unusedExtraInhabitants))
layout.computeStride()
layout.computeInline()

let vwtable = enumType.getOrCreateMutableVWTableForInit(layoutFlags)
vwtable[]._.base.publishLayout(layout)
```

[We’ve seen `getOr­Create­Mutable­VWTable­ForInit` before for structs](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/#what-about-structs), and the version for enums is basically the same. However, value witness tables for enums have a few extra operations (“witnesses”) for getting the tag and the payload, which is more direct than calling a generic runtime function when the enum’s layout is statically known. It also allows the compiler to do custom packing for enums that _don’t_ use `swift_init­Enum­Metadata­SinglePayload`—nothing in Swift says that single-payload enums _have_ to use this layout as long no generated code tries to access the tag or payload directly.

I promise we’ll have a _whole blog post_ about value witness tables at some point, but for now let’s move on to that helper function, `getExtra­TagBytes`. It’s mostly just a smarter version of the measuring we did before.

```
func getExtraTagBytes(
  _ payloadSize: UInt,
  _ emptyCases: Int,
  _ payloadCases: Int
) -> Int {
  let numEmptyCasePayloadUnits: Int
  if emptyCases == 0 {
    numEmptyCasePayloadUnits = 0
  } else if payloadSize >= 4 {
    numEmptyCasePayloadUnits = 1
  } else {
    let bits = payloadSize &* 8
    let casesPerPayloadUnit = 1 &<< bits
    let emptyCasesRoundedUp =
      UInt(emptyCases).roundedUpToAlignMask(casesPerPayloadUnit &- 1)
    numEmptyCasePayloadUnits = Int(emptyCasesRoundedUp &>> bits)
  }

  let numTags = numEmptyCasePayloadUnits + payloadCases
  return (
    numTags <= 1 ? 0 :
    numTags <= UInt8.max ? 1 :
    numTags <= UInt16.max ? 2 : 4)
}
```

For our purposes, `payloadCases` is always 1, but this same logic can be used for laying out multi-payload enums as well. `emptyCases`, on the other hand, is going to be the number of non-payload cases that _can’t_ fit into the payload’s extra inhabitants—the ones we need extra space for. `getExtra­TagBytes` then has some special cases for common situations:

- If there are no remaining non-payload cases, we only need to discriminate between the different kinds of payload. For a single-payload enum, this means we don’t need any extra storage at all.
- If the payload is at least four bytes, then we can just put the number for a non-payload case in _there,_ and use a single tag bit to differentiate whether we’re in the “payload” or “non-payload” representation. Swift doesn’t support enums with more than 2³² cases (also known as 4 [gibicases](https://en.wikipedia.org/wiki/Binary_prefix)).

However, if we have a small payload, then we might not be able to fit all the remaining empty cases in that spot. In that situation, we measure the payload, round up the number of empty cases to the next number of “payload units” (using a variation of [`roundUp­To­AlignMask`](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/#show-me-some-code) that we saw earlier), and then figure out how many payload units it’ll take to represent all the empty cases. That becomes the number of tags we’ll need, and from there we can do the same “0, 1, 2, or 4” bytes check that we did originally.

### `swift_store­Enum­Tag­Single­PayloadGeneric`

We did the getter in our toy example before; this time, we’re going to look at the setter. (It’s actually a little easier to understand than the getter, the way it’s structured.)

```
@_silgen_name("swift_storeEnumTagSinglePayloadGeneric")
func swift_storeEnumTagSinglePayloadGeneric(
  _ enumAddr: UnsafeMutableRawPointer,
  _ whichCase: UInt32,
  _ numEmptyCases: UInt32,
  _ payloadType: UnsafePointer<TypeMetadata>,
  _ storeExtraInhabitantTag: storeExtraInhabitantTagFn?
) {
  let payloadLayout = payloadType.valueWitnessTable[]._.typeLayout
```

Yikes, there’s a bunch going on there! In particular, there’s already something unusual in that function signature: `storeExtraInhabitantTag`. What’s that do? Well, just because the payload type has extra inhabitants doesn’t mean that the runtime knows how to access them! That has to get passed in to this function, which, after all, is supposed to be a generic implementation for any single-payload enum and payload type. That callback looks like this:

```
typealias storeExtraInhabitantTagFn = @convention(thin) (
  _ enumAddr: UnsafeMutableRawPointer,
  _ whichCase: UInt32,
  _ numEmptyCases: UInt32,
  _ payloadType: UnsafePointer<TypeMetadata>
) -> Void
```

Chances are good you’ve never seen `@convention(thin)` anywhere. It’s the last of Swift’s custom callback conventions, alongside `@convention(c)` and `@convention(block)`, and it refers to a function that uses the Swift calling convention but has no captures. It doesn’t have any underscores in its name, but [it’s still not officially supported yet](https://forums.swift.org/t/use-of-convention-thin-to-avoid-allocating-closures/12087/6). Still, it’s the only way to be fully correct here, although in practice I don’t think any of Swift’s platforms would treat this particular callback any different if it were `@convention(c)` instead, including Swift-on-Classic.

All right, with that weirdness out of the way, let’s look into the body of the function. Like with allocation, we’ll start off by seeing if there are any tag bytes. Unlike in our toy example, we weren’t given the full size of the enum, so we’ll have to use `getExtra­TagBytes` again:

```
let numExtraTagBytes = getExtraTagBytes(
  payloadSize,
  max(0, Int(numEmptyCases &- payloadLayout._.numExtraInhabitants)),
  1)
```

Now we can get to work. The first thing we’ll try is using the payload’s extra inhabitants. (This also handles the payload itself, which is guaranteed to be represented by tag 0.)

```
let extraTagBitAddr = enumAddr + Int(payloadSize)
if whichCase <= payloadLayout._.numExtraInhabitants {
  extraTagBitAddr.storeUnalignedBigEndianValue(0, size: numExtraTagBytes)
  if whichCase != 0 {
    storeExtraInhabitantTag!(
      enumAddr,
      whichCase,
      payloadLayout._.numExtraInhabitants,
      payloadType)
  }
  return
}
```

Notice how we just defer to the callback we were given once we know the value is in range. We also pass the total number of extra inhabitants we expect, which is used in the case where the payload type is another single-payload enum! (Consider `Optional<Optional<Multiplier>>`, which should _still_ only take up one byte of memory.) This allows the implementation to differentiate `.none` from `.some(.none)` and not accidentally use the same tag for each, without requiring an additional wrapper function or checking the type specifically.

(You might also be wondering why we’re passing the number of extra inhabitants at all when we’re also passing the payload type. It took me a while to figure out, but the `StoreExtraInhabitantTag` functions are set up to work if you pass _more_ empty cases than there are empty inhabitants…in which case it will figure out how many extra tag bytes to use and zero them itself. I assume this is because the compiler sometimes calls these callback functions directly, but it’s too bad that we’ve now got two implementations of the same thing.)

If the case we’re storing doesn’t fit in the extra inhabitants, we move on to the non-payload representations. The first thing we’re going to do is subtract off the representations we already tried: the extra inhabitants and the payload case.

```
let caseIndexToStore = whichCase &- payloadLayout._.numExtraInhabitants &- 1
```

Next, we’re going to once again break up that index into the part that fits in the payload and the part that goes in the extra tag bytes.

```
let payloadIndex, extraTagIndex: UInt32
if payloadSize >= 4 {
  extraTagIndex = 1
  payloadIndex = caseIndexToStore
} else {
  let payloadBits = payloadSize &* 8
  extraTagIndex = 1 &+ (caseIndexToStore &>> payloadBits)
  payloadIndex = caseIndexToStore & ((1 &<< payloadBits) &- 1)
}
```

Like before, we just pass the index through for big payloads, and break it up by “payload units” for smaller ones. (Remember that masking by a power-of-two minus one is the same as taking the remainder.) The “extra tag” part always starts at 1 because 0 means “payload or extra inhabitant representation” already.

```
let payloadIndexSize = max(payloadSize, 4)
let payloadIndexAddr = enumAddr + Int(payloadSize &- payloadIndexSize)
payloadIndexAddr.storeUnalignedBigEndianValue(
  payloadIndex,
  size: Int(payloadIndexSize))
extraTagBitAddr.storeUnalignedBigEndianValue(
  extraTagIndex,
  size: numExtraTagBytes)
```

Finally, we store the two parts of the index in the payload and the extra bytes. But wait, why is the case index being stored in the _last_ four bytes of the payload instead of the first? It’s because the compiler treats the entire payload as one big integer…and on PowerPC running Classic, integers are stored [big-endian](https://en.wikipedia.org/wiki/Endianness#Classical_example). So storing a payload value that’s less than 2³² is never going to use anything but the last four bytes of the payload.[4](#fn:endian)

That’s it: we’ve stored our enum case tag! If there’s no payload involved, we’re done, and if there is, the code that called this function will do the rest.

(I’m not going to show the getter, but it’s the same thing in reverse.)

### Multi-payload enums

…were not something I needed for [ROSE-8](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/), and so I didn’t implement them. Sorry!

…for real, though, multi-payload enums are yet another discussion, and include a bunch of compile-time-only optimizations that it wouldn’t be right to leave out. So while they’re _not going to be covered in this series,_ I’d still like to talk about them someday. No promises, though!

### Wrap-up

We’ve now seen how Swift deals with both C-style enums and enums that only have one case with a payload, and how it goes beyond the simplest implementation to pack more information into fewer bytes (and stay compatible with C’s `NULL`). With that, we’ve talked about all of Swift’s “concrete” user-definable types: structs, classes, and enums.

Unfortunately, I’ve run out of buffer in writing these posts! So I’ll be taking a hiatus (for several weeks, most likely) before we get back to protocols, dynamic casts, and those repeatedly-teased _value witness tables._ For anyone who’s craving more content (and who didn’t see it at the time), I went on JP Simard and Jesse Squires’ _[Swift Unwrapped](https://spec.fm/podcasts/swift-unwrapped/1DMLbJg5)_ podcast to talk about this project and other things related to the Swift runtime.

1. In a language with enums, the most famous enum _ought_ to be Bool, with cases “false” and “true”. However, early versions of Swift didn’t generate very good code for checking which case an enum was in, which meant that _every `if` statement contributed to code bloat._ Because of this, Swift.Bool is defined as a struct around a 1-bit primitive value (1 byte when stored in memory), rather than as an enum. Oh well. [↩︎](#fnref:bool)
2. Remember that this blog series largely ignores support for [library evolution](https://swift.org/blog/library-evolution/), which would require that the numeric values for the enums are consistent for clients compiling against different versions of the library. This still doesn’t require any run-time support, however; the compiler just emits a global constant for each enum case that clients can use instead of a literal integer representation. [↩︎](#fnref:evolution)
3. The exception to this rule is enums tagged as `@objc`, which need to be able to interoperate with Objective-C. These follow the C rule of using the raw value as the representation, and use Objective-C’s “fixed underlying enum type” feature, [borrowed from C++](https://clang.llvm.org/docs/LanguageExtensions.html#enumerations-with-a-fixed-underlying-type), to make sure the size matches up in both languages. [↩︎](#fnref:objc)
4. Honestly, I suspect this behavior was an accident, something that fell out of the implementation for little-endian platforms. It wouldn’t be too hard to “fix” either, but you’d have to change both the compiler and the runtime. [↩︎](#fnref:endian)

This entry was posted on [October](https://belkadan.com/blog/2020/10) 20, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Swift runtime](https://belkadan.com/blog/tags/swift-runtime)
