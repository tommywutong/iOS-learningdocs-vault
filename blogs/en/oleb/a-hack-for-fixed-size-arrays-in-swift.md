---
title: A hack for fixed-size arrays in Swift
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/12/fixed-size-arrays/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:fd6b611ac9331726'
translated: false
---

> 原文：[A hack for fixed-size arrays in Swift](https://oleb.net/blog/2017/12/fixed-size-arrays/)　·　Ole Begemann

# A hack for fixed-size arrays in Swift

Swift 4 doesn’t have a built-in type for fixed-size, stack-allocated arrays. And as far as I know, implementing such a type in a generic way (for arbitrary array lengths) is currently impossible — it would require either special compiler support or more advanced generics features, such as variadic generic parameters.

# Mimicking a fixed-size array with a tuple

I came across an interesting workaround for this in the standard library source code. The file [`FixedArray.swift.gyb`](https://github.com/apple/swift/blob/master/stdlib/public/core/FixedArray.swift.gyb) contains a template for a fixed-size array struct. The struct, named `_FixedArrayN<T>` (where `T` is the generic element type and _N_ is the number of array elements), is **a wrapper around a tuple of _N_ elements.**

Swift doesn’t guarantee stack allocation for local variables, but it’s highly likely that a local variable declared like this will be placed on the stack:

```
var eightInts = _FixedArray8<Int>(allZeros: ())
```

Contrast this with a regular `Array`, which is essentially a wrapper around a reference to a separate, heap-allocated buffer. This has many advantages, such as the ability to dynamically grow and shrink the buffer, to outlive the current scope, and to implement copy-on-write (multiple arrays can share the same buffer, as long as no one mutates the buffer). But it comes with some overhead that a simple tuple of `N` elements doesn’t have.

# Think twice before using this

Before I continue, a disclaimer. Here’s what Michael Ilseman, who added this type to the standard library, has to say:

> [@olebegeman](https://twitter.com/olebegemann/status/939903265751425025) I knew I’d live to regret adding that!
> 
> Exercise caution in using it. If mishandled it can balloon code size and the tuple’s metadata is not cheap.

I’m writing about this because I think it’s an interesting workaround for a real problem, and looking at the implementation is instructive even if you don’t end up using it in production. Eventually, Swift will hopefully gain a native fixed-size array type (or a low-level function to allocate arbitrary memory on the stack, which would allow you to build the type described here without resorting to code generation).

# Collection interface

An array type should adopt Swift’s standard [`Collection`](https://developer.apple.com/documentation/swift/collection) protocol. This isn’t trivial for `_FixedArrayN` because tuples don’t support subscripting, i.e. it’s not straightforward to write code that accesses the _n_-th element of a tuple (where _n_ is a variable).

The implementation in the standard library solves this with pointer arithmetic on the tuple’s underlying raw memory. It obtains a pointer to the tuple, computes the byte offset for the _n_-th element and copies the value from/to that location. Here’s how [the `subscript` implementation looks like](https://github.com/apple/swift/blob/d2dc653420cc5d58e2b0fd3c7e8930613ab515ac/stdlib/public/core/FixedArray.swift.gyb#L63-L93) (I simplified the code a little):

```
internal subscript(i: Int) -> T {
  get {
    var copy = storage
    let res: T = withUnsafeBytes(of: &copy) {
      (rawPtr : UnsafeRawBufferPointer) -> T in
      let stride = MemoryLayout<T>.stride
      assert(rawPtr.count == ${N}*stride, "layout mismatch?")
      let bufPtr = UnsafeBufferPointer(
        start: rawPtr.baseAddress!.assumingMemoryBound(to: T.self),
        count: count)
      return bufPtr[i]
    }
    return res
  }
  set { /* looks similar */ }
}
```

The `${N}` is a placeholder for the actual element count that is replaced in the code generation step (see below).

With the subscript in place, it’s easy to conform the struct to [`RandomAccessCollection`](https://developer.apple.com/documentation/swift/randomaccesscollection). This means you can use it pretty much like a regular array. `for` loops, `map`, `filter`, `index(of:)`, etc. all work as expected.

## Is it safe?

You might ask, is operating on the raw memory in this way safe? If you read the code in [`FixedArray.swift.gyb`](https://github.com/apple/swift/blob/d2dc653420cc5d58e2b0fd3c7e8930613ab515ac/stdlib/public/core/FixedArray.swift.gyb#L27-L28), you’ll notice this scary comment:

```
// ABI TODO: The [type] has assumptions about tuple layout in the ABI, namely that
// they are laid out contiguously and individually addressable (i.e. strided).
```

This sounds like the implementation could break with new compiler versions until the ABI is finalized. The person who wrote that comment probably knows this better than I do, but I don’t think that’s actually the case. In April 2017, [John McCall wrote](https://forums.swift.org/t/guarantees-of-tuples-as-fixed-sized-stack-allocated-arrays/5800/3):

> **Tuples are guaranteed to use a standard C-style layout wherever that layout is ABI-observable, e.g. when you construct an `UnsafePointer` to one.**
> 
> Note that that layout isn’t ABI-observable when the tuple is, say, just stored in a struct. The compiler is allowed to break up the tuple and store its components however it likes. Of course, if the compiler does that, and you turn around and construct an `UnsafePointer` to that property, then the compiler has to reconstitute the tuple into an ABI-compliant temporary that it can give you a pointer to; this is yet another reason why you can’t maintain permanent unsafe pointers to components of a struct.

If I interpret this correctly, the call to [`withUnsafeBytes`](https://developer.apple.com/documentation/swift/2635826-withunsafebytes) guarantees that the argument (`&copy`) is laid out contiguously in a way that’s compatible with a C array of the same size and element type. What _isn’t_ guaranteed is that this is free of overhead. If the compiler decided to store the tuple in an different layout, it has to make a temporary copy for the duration of the `withUsafeBytes` call. Depending on the size of the tuple, this might destroy the performance gains we hoped to get from using a stack-allocated value in the first place.

By the way, if you’re wondering why the subscript getter creates a copy of the tuple first: `inout` arguments must be mutable, and `storage` isn’t (the getter would have to be marked `mutating` for that).

# Code generation

Swift doesn’t support generically-sized tuples, so you’d need to write a separate type for each array size you need in your code (and these sizes must all be known at compile time). For example, `_FixedArray8<T>` and `_FixedArray16<T>` would allow you to use fixed arrays with either 8 or 16 elements (but the element type `T` can be anything).

Obviously you wouldn’t want to write these definitions by hand, especially since declaring tuples of the form `(T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T)` is no fun. The good news is that the code can be generated. The Swift team uses GYB for this, which is a relatively simple preprocessor they’ve written to keep the standard library source free from excessive repetition (e.g [they use GYB to generate the code for the various integer types](https://github.com/apple/swift/blob/master/stdlib/public/core/Integers.swift.gyb)).

If you check out [`FixedArray.swift.gyb`](https://github.com/apple/swift/blob/d2dc653420cc5d58e2b0fd3c7e8930613ab515ac/stdlib/public/core/FixedArray.swift.gyb), you’ll notice this at the top:

```
%{
  # The sizes to generate code for.
  sizes = [16]
}%
```

GYB will generate a `_FixedArrayN` struct for any size you put in the `sizes` array here. As you can see, the standard library currently only uses a `_FixedArray16`.

# Usage

`_FixedArrayN` is an internal type that the standard library uses in its implementation; it’s not part of the official standard library API. If you want to use it in your own project, you’ll have to copy the code from the Swift repository:

1. `FixedArray.swift.gyb`

  and the

  `gyb.py`

  script from the Swift repository. Alternatively, clone the entire repository.
2. to add your desired sizes to the

  array.
3. Run this command in Terminal:

  ```
  > python gyb.py FixedArray.swift.gyb -o FixedArray.swift
  ```

  This will generate a `FixedArray.swift` file that you can add to your project.

# Initializing a fixed-size array

Swift’s [strict initialization rules](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/Initialization.html) are probably the biggest hurdle when working with `_FixedArrayN`. A variable must be fully initialized before it can be used; you can’t create an “empty” fixed-size array with the goal of filling it with data later — the compiler won’t allow it.

Like all structs, `_FixedArrayN` has a memberwise initializer for its properties, but using that means we’re back to filling tuples manually — exactly the thing we want to avoid.

The standard library implementation also comes with an `init(allZeros:)` initializer that allows you to set all elements to zero. Here’s an example:

```
var eightInts = _FixedArray8<Int>(allZeros: ())
eightInts[3] = 42
print(eightInts)
// → _FixedArray8<Int>(storage: (0, 0, 0, 42, 0, 0, 0, 0))
```

(Note that the initializer takes an empty tuple, or `Void`, as its argument. The only purpose of the `allZeros:` parameter is to create a unique name for this initializer — the passed-in value isn’t used.)

This only works with number types, though. If you want to use other types, you’ll need to add one or more other initializers to the GYB file. Here’s one, `init(repeating: T)`, that sets all array elements to a value the caller can pass in:

```
extension _FixedArray${N} {
  internal init(repeating v: T) {
    self.storage = (
% for i in range(0, N-1):
    v,
% end
    v
    )
  }
}
```

(Check out the GYB syntax for a simple loop: `% for i in range(0, N-1):`.)

And here’s how you can use it:

```
var fourStrings = _FixedArray4(repeating: "")
fourStrings[1] = "🤔"
print(fourStrings)
// → _FixedArray4<String>(storage: ("", "🤔", "", ""))

var fourBools = _FixedArray4(repeating: false)
print(fourBools)
// → _FixedArray4<Bool>(storage: (false, false, false, false))
```

With a little more GYB-fu it should also be possible to write an initializer that takes an array (or an array literal) and copies the elements into the storage tuple one by one.
