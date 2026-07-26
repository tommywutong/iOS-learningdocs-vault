---
title: Swift imports fixed-size C arrays as tuples
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/12/swift-imports-fixed-size-c-arrays-as-tuples/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:8dc3277a4bffd92d'
translated: false
---

> 原文：[Swift imports fixed-size C arrays as tuples](https://oleb.net/blog/2017/12/swift-imports-fixed-size-c-arrays-as-tuples/)　·　Ole Begemann

# Swift imports fixed-size C arrays as tuples

_This is a follow-up on [yesterday’s article about using a tuple to mimic a stack-allocated array](https://oleb.net/blog/2017/12/fixed-size-arrays/). Please read that one first if you haven’t already._

Yesterday, we saw how you can obtain a pointer to a tuple’s underlying memory and treat it as a collection. Today, I’d like to discuss how we can use the same approach when interfacing with C APIs that work with fixed-size arrays.

# Swift imports fixed-size C arrays as tuples

The Swift equivalent of the C type `float[4]` would be `(Float, Float, Float, Float)`. This has the benefit of incurring no bridging overhead because the Swift compiler can lay out tuples in a C-compatible way.

A tuple often isn’t a convenient type for the user of the API, though — as we’ve seen, you can’t iterate over a tuple’s elements or access one via subscripting.

# Example: `char[256]`

Let’s look at an example. The [`uname`](https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man3/uname.3.html) function returns some strings identifying the current platform. You call `uname` by passing it a pointer to a struct which `uname` then fills with values. The struct is defined like this in C:

```
struct utsname {
  char sysname[256];  /* [XSI] Name of OS */
  char nodename[256]; /* [XSI] Name of this network node */
  char release[256];  /* [XSI] Release level */
  char version[256];  /* [XSI] Version level */
  char machine[256];  /* [XSI] Hardware type */
};
```

You know what’s coming next, right? Swift’s [Clang importer](https://swift.org/compiler-stdlib/#compiler-architecture) sees the `char[256]` declarations and turns them into 256-tuples(!). This is how the same type appears in Swift (feel free to count the number of elements):

```
public struct utsname {
    public var sysname:  (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8) /* [XSI] Name of OS */
    public var nodename: (Int8, /* ... 254 more ... */, Int8) /* [XSI] Name of this network node */
    public var release:  (Int8, /* ... 254 more ... */, Int8) /* [XSI] Release level */
    public var version:  (Int8, /* ... 254 more ... */, Int8) /* [XSI] Version level */
    public var machine:  (Int8, /* ... 254 more ... */, Int8) /* [XSI] Hardware type */
}
```

Calling `uname` on macOS is as simple as this:

```
import Darwin
var utsInfo = utsname()
uname(&utsInfo)
```

But how do you then proceed to extract the information in the `utsInfo` struct? `utsInfo.machine` is a 256-tuple of integers, so it’s unusable in its current form:

```
print(utsInfo.machine)
// → (120, 56, 54, 95, 54, 52, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
```

## Using `_FixedArray256`

One approach is to generate a `_FixedArray256` type as I showed yesterday. You can then pass one of the fields in `utsInfo` directly to the `_FixedArray256` initializer. From then on, you have the full [`Collection`](https://developer.apple.com/documentation/swift/collection) API at your disposal to work with the data:

```
// Assuming we have generated a _FixedArray256 type
let machine = _FixedArray256(storage: utsInfo.machine)
```

This is probably the way to go if you’re dealing with smaller arrays of numbers etc., but in this particular case there are two significant downsides to this approach:

1. **256 elements is a pretty big tuple, and the impact on code size and compile times is not negligible.** I did a quick test: my version of `_FixedArray256` (approximately 1,600 lines of generated Swift code) takes about 8 seconds to compile and adds nearly 750 KB to the compiled binary (with optimizations enabled). The convenience doesn’t come for free.
2. The second problem only applies to APIs that return strings. The strings the `uname` functions writes into the struct are actually null-terminated — the length of 256 bytes is just an upper limit. As a result, most of the elements in our “array” would contain garbage data and we’d have to process the data further (i.e. strip everything after the first null byte).

**`_FixedArray256` takes about 8 seconds to compile and adds nearly 750 KB to the compiled binary.**

## Using `withUnsafeBytes(of:)` directly

A better approach is to not use `_FixedArray256` at all. Instead, let’s just take the idea of obtaining a pointer to the tuple’s storage and using that to initialize a string. Since [`String`](https://developer.apple.com/documentation/swift/string) already has [a matching initializer for a null-terminated C string](https://developer.apple.com/documentation/swift/string/1641523-init), this can be done in very little code:

```
let machine = withUnsafeBytes(of: &utsInfo.machine) { (rawPtr) -> String in
    let ptr = rawPtr.baseAddress!.assumingMemoryBound(to: CChar.self)
    return String(cString: ptr)
}
print(machine) // → x86_64
```

This compiles much faster and doesn’t have a significant impact on code size.
