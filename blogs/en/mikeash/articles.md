---
title: articles
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-08-01-exploring-swift-memory-layout-part-ii.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3fe40ed3e1bcccb0'
translated: false
---

> 原文：[articles](https://www.mikeash.com/pyblog/friday-qa-2014-08-01-exploring-swift-memory-layout-part-ii.html)　·　mikeash.com Friday Q&A

Posted at 2014-08-01 14:22 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2014-08-15: Swift Name Mangling](https://www.mikeash.com/pyblog/friday-qa-2014-08-15-swift-name-mangling.html)  
Previous article: [Friday Q&A 2014-07-18: Exploring Swift Memory Layout](https://www.mikeash.com/pyblog/friday-qa-2014-07-18-exploring-swift-memory-layout.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2014-08-01: Exploring Swift Memory Layout, Part II

by [Mike Ash](https://www.mikeash.com/)

**Reminder: Subject to Change**  
Just as before, this is all internal details from a pre-release version of the language on a specific CPU/OS combination and may change at any time. Don't write code that relies on it. Specifically, these dumps are from x86-64 code running on 10.9. This is a little-endian architecture (as is everything Apple anymore) so all the numbers will be backwards.

**Generics**  
Generics are surprisingly simple. Everything just gets laid out and shifted around as necessary. Let's start with a simple generic `struct`:

```
    struct WrapperStruct<T> {
        let value: T
    }
```

Let's dump two versions of it:

```
    WrapperStruct(value: 42)
    WrapperStruct(value: (42, 43))
```

The result is:

```
    2a00000000000000
    2a00000000000000 2b00000000000000
```

Everything is laid out contiguously with no padding and no waste. Nice.

How about multiple generic values?

```
    struct WrapperStruct2<T, U> {
        let value1: T
        let value2: U
    }

    WrapperStruct2(value1: 42, value2: 43)
    WrapperStruct2(value1: (42, 43), value2: 44)
    WrapperStruct2(value1: 42, value2: (43, 44))
```

No surprises in the memory dump:

```
    2a00000000000000 2b00000000000000
    2a00000000000000 2b00000000000000 2c00000000000000
    2a00000000000000 2b00000000000000 2c00000000000000
```

In particular, note how the last two are identical. Although the compile-time types are different, that isn't evident in the memory dump. The type difference is all in how the values are accessed.

How about classes? You might expect this to be more complicated since classes have dynamic dispatch and are allocated on the heap. They're not:

```
    class WrapperClass<T> {
        let value: T

        init(_ value: T) {
            self.value = value
        }
    }

    dumpmem(WrapperClass(42))
    dumpmem(WrapperClass((42, 43)))
```

The result:

```
    c8033074807f0000 0800000001000000 2a00000000000000
    28093074807f0000 0800000001000000 2a00000000000000 2b00000000000000
```

We see the 16-byte object header discussed in the previous post, followed by the data. Note that the `isa` pointer of the two objects is not identical, even though both are an instance of `WrapperClass`. Evidently, a specialization of a generic class is a separate class at runtime.

It's also interesting to note that instances of generic classes can have different sizes. This is a natural consequence of the straightforward implementation of generics, but it's striking coming from Objective-C, where instances of any given class are always the same size, absent certain runtime shenanigans.

**Optionals**  
Let's start off with an easy one: optional object pointers.

A quick refresher: in Swift, unlike Objective-C, a straight object reference cannot be `nil`:

```
    let ptr: NSObject
```

This variable is guaranteed (as far as a compiler can guarantee things) to always point to an object. If we want to allow `nil`, we have to explicitly declare an optional by specifying the type as `NSObject?` or `NSObject!`.

Plain object pointers just contain the address of the object they point to, just like Objective-C. When Objective-C APIs are bridged to Swift, the object pointers get translated to optionals, so we'd expect that, for object pointers, Swift optionals are represented just like Objective-C: a plain address when pointing to an object, and all zeroes for `nil`. Let's see:

```
    let obj: NSObject? = NSObject()
    let nilobj: NSObject? = nil
    let explicitobj: NSObject! = NSObject()
    let explicitnilobj: NSObject! = nil
```

These variables contain:

```
    806040c1957f0000
    0000000000000000
    70e440c1957f0000
    0000000000000000
```

It's just as we expected. They either contain an object address or all zeroes. Further, explicit and implicit optionals contain the same sort of stuff, which makes sense as explicit/implicit is just syntactic sugar.

Let's move on to integers. Unlike pointers, there's no underlying machine value that doesn't correspond to a valid integer, so something else must be at work. Let's see what we get:

```
    let x = 42
    let y: Int? = 42
    let z: Int? = nil
```

This produces:

```
    2a00000000000000
    2a00000000000000 00
    0000000000000000 01
```

A plain `Int` stores the raw value in eight bytes of memory, as expected. The optional type adds an extra byte at the end to signal whether or not a value is present. If that trailing byte is zero, a value is present. If that trailing byte is `1`, the optional contains `nil`. Thus, optional `Int`s take up nine bytes rather than eight.

How about `struct`s? If you guessed they'd be the same, you'd be right:

```
    let rect: NSRect? = NSMakeRect(1, 2, 3, 4)
    let nilrect: NSRect? = nil

    000000000000f03f 0000000000000040 0000000000000840 0000000000001040 00
    0000000000000000 0000000000000000 0000000000000000 0000000000000000 01
```

We can see that optionals for value types are implemented by adding an extra byte to the end, where zero means the optional contains a value, and one means the optional is `nil`. Reference types are implemented by storing the address when the optional contains a value, and storing zero when the optional contains `nil`.

**Protocols**  
Protocols are pretty straightforward for the most part. Any conforming class or `struct` implements the methods or properties specified by the protocol, and you can call those. However, there's one interesting aspect of protocols, namely that it's possible to declare a variable that's a protocol type. This is nothing special in Objective-C, since it's just another kind of static type on top of an object pointer. Swift is different, because protocols can apply to `struct`s as well as classes. A `struct` is a value type, but a class is a reference type, so how can you combine them?

Let's start with a simple example protocol:

```
    protocol P {
        func p()
    }
```

Let's make `NSObject` conform to `P` in an extension:

```
    extension NSObject: P {
        func p() {}
    }
```

Then let's stuff an `NSObject` instance into a variable of type `P`:

```
    let pobj: P = NSObject()
```

Here's what `pobj` contains:

```
    4000201b9c7f0000 2200000000000080 0000050701000000 40e3401a9c7f0000 a8ebb90601000000
```

The first chunk is the object pointer. `0x00007f9c1b200040` (remember, it's backwards) points to an `NSObject` instance in memory. The next two chunks are just garbage, used for padding here. The last 16 bytes contain two pointers to metadata tables. The first one, at offset 24, contains a pointer to the "direct type metadata" for the underlying type. This in turn contains pointers to structures containing things like the type name and fields. The last one, at offset 32 is a "protocol witness table" for the underlying type and the protocol, which contains pointers to the type's implementations of the protocol methods. This is how the compiler is able to invoke methods, such as `p()`, on a value of protocol type without knowing the underlying type at runtime.

Let's check out a simple `struct`. In this case, we'll start with `Int`, which is ultimately a `struct` in Swift:

```
    extension Int: P {
        func p() {}
    }

    let pint: P = 42
```

The dump is much the same:

```
    2a00000000000000 0a00000000000080 c0014a0201000000 98912d0201000000 d00b050201000000
```

It contains the underlying value, some garbage-filled padding, then the two metadata pointers at the end.

Let's try a bigger struct. It starts to get interesting:

```
    struct S: P {
        let x: Int
        let y: Int

        func p() {}
    }

    let s: P = S(x: 42, y: 43)
```

This produces:

```
    2a00000000000000 2b00000000000000 e001540201000000 2815050201000000 d80b050201000000
```

It looks like that padding is available for use if the underlying value needs the storage. Is the same true of the third chunk?

```
    struct T: P {
        let x: Int
        let y: Int
        let z: Int

        func p() {}
    }

    let t: P = T(x: 42, y: 43, z: 44)

    2a00000000000000 2b00000000000000 2c00000000000000 38c61d0401000000 e0bb1d0401000000
```

Indeed so. What happens if the `struct` requires more storage than that?

```
    struct U: P {
        let a: Int
        let b: Int
        let c: Int
        let d: Int

        func p() {}
    }

    let u: P = U(a: 42, b: 43, c: 44, d: 45)
```

Dumping the memory of `u` produces:

```
    801f600401000000 1500000000000080 10046c0401000000 58c71d0401000000 e8bb1d0401000000
```

There's nothing recognizable anymore. None of the `struct` elements are present. The first chunk is a pointer to `malloc` memory, and dumping that produces:

```
    2a00000000000000 2b00000000000000 2c00000000000000 2d00000000000000
```

There's the `struct` storage. It seems that protocol values provide 24 bytes of storage. If the underlying value fits within 24 bytes, it's stored inline, otherwise it's automatically spilled to the heap.

**Conclusion**  
Swift memory layout for generics is completely straightforward. The values are laid out just as they are with non-generic types, even if it means that class instances change size. Optionals of reference types represent `nil` as all zeroes, just like we're used to in Objective-C. Optionals of value types append a byte to the end of the value to indicate whether or not a value is present. Protocol types take up 40 bytes of storage, with the last two pointers containing references to type metadata tables, and the rest available for storying the underlying value. If more than 24 bytes of storage is needed, the value is automatically placed on the heap, and a pointer to the allocation is stored instead.

That's it for today. Come back next time for more exciting Swift adventures!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2014-08-01-exploring-swift-memory-layout-part-ii.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
