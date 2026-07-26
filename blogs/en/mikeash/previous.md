---
title: previous
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-07-18-exploring-swift-memory-layout.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4645cb12ee92d746'
translated: false
---

> 原文：[previous](https://www.mikeash.com/pyblog/friday-qa-2014-07-18-exploring-swift-memory-layout.html)　·　mikeash.com Friday Q&A

Posted at 2014-07-18 13:57 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2014-08-01: Exploring Swift Memory Layout, Part II](https://www.mikeash.com/pyblog/friday-qa-2014-08-01-exploring-swift-memory-layout-part-ii.html)  
Previous article: [Friday Q&A 2014-07-04: Secrets of Swift's Speed](https://www.mikeash.com/pyblog/friday-qa-2014-07-04-secrets-of-swifts-speed.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2014-07-18: Exploring Swift Memory Layout

by [Mike Ash](https://www.mikeash.com/)

**Subject to Change**  
Everything about Swift is subject to change, but internal implementation details like these are even more so. This stuff can be handy to know and potentially useful for debugging, but don't write production code that relies on it, Or Else.

These dumps are from Swift code compiled for `x86-64` running on 10.9. In addition to potential variations in future compiler releases, everything may be different on different CPU architectures or OS versions. When reading the dumps, keep in mind that this is a little-endian architecture, so all the numbers will be backwards.

If you're wondering where the data came from, I'm reading Objective-C runtime structures with the standard runtime APIs, and using `mach_vm_read_overwrite` to read raw memory by chasing pointers recursively, using a custom Swift program that I hope to discuss in a future article.

**Structs**  
Let's start out with a simple `struct`:

```
    struct TestStruct {
        let a: UInt64 = 0xaaaaaaaaaaaaaaaa
        let b: UInt64 = 0xbbbbbbbbbbbbbbbb
    }
```

Dumping the contents of an instance reveals this mundane chunk of memory:

```
    aaaaaaaaaaaaaaaa bbbbbbbbbbbbbbbb
```

Let's try a `struct` with more complicated contents:

```
    struct PaddingTestStruct {
        let a: UInt8 = 0xaa
        let b: UInt16 = 0xbbbb
        let c: UInt64 = 0xcccccccccccccccc
    }
```

This produces:

```
    aaa0bbbbff7f0000 cccccccccccccccc
```

We can see that `b` and `c` are both aligned to their size, with some garbage-filled padding in between.

Let's try adding some functions:

```
    struct FuncTestStruct {
        let a: UInt64 = 0xaaaaaaaaaaaaaaaa

        func dummy1() {}
        func dummy2() {}
        func dummy3() {}
    }
```

This produces:

```
    aaaaaaaaaaaaaaaa
```

The functions, although conceptually associated with the `struct`, don't actually show up in the memory contents. Since `struct`s in Swift don't allow inheritance, there's no need for anything besides the variables.

We can see that Swift `struct`s behave a lot like C `struct`s. They store their variables as declared in memory without any annotation or metadata. Although Swift allows `struct`s to contain functions, at runtime they aren't associated with instances of the `struct`.

**Objects**  
Let's check out a simple class with an instance variable and a couple of methods:

```
    class TestClass {
        let a: UInt64 = 0xaaaaaaaaaaaaaaaa

        func method1() {}
        func method2() {}
    }
```

Instantiating the class and dumping the contents of the instance produces the following memory dump:

```
    00393b0701000000 0c00000001000000 aaaaaaaaaaaaaaaa
```

It looks similar to an Objective-C object, but there's 16 bytes of metadata instead of just 8 as is the case for Objective-C. It turns out that it _is_ an Objective-C object that can be inspected using the APIs in `objc/runtime.h`. Here's what it produces:

```
    Objective-C class _TtC6memory9TestClass:
        Ivar: a 
    Objective-C class SwiftObject:
        Ivar: magic {SwiftObject_s="isa"^v"refCount"q}
        Property: hash TQ,R
        Property: superclass T#,R
        Property: description T@"NSString",R,C
        Property: debugDescription T@"NSString",R,C
        Method: __usesNativeSwiftReferenceCounting B16@0:8
        Method: .cxx_construct @16@0:8
        Method: release v16@0:8
        Method: autorelease @16@0:8
        Method: dealloc v16@0:8
        Method: class @16@0:8
        Method: retain @16@0:8
        Method: isEqual: c24@0:8@16
        Method: hash Q16@0:8
        Method: superclass #16@0:8
        Method: self @16@0:8
        Method: zone ^{_NSZone=}16@0:8
        Method: performSelector: @24@0:8:16
        Method: performSelector:withObject: @32@0:8:16@24
        Method: performSelector:withObject:withObject: @40@0:8:16@24@32
        Method: isProxy c16@0:8
        Method: isKindOfClass: c24@0:8#16
        Method: isMemberOfClass: c24@0:8#16
        Method: conformsToProtocol: c24@0:8@16
        Method: respondsToSelector: c24@0:8:16
        Method: retainCount Q16@0:8
        Method: description @16@0:8
        Method: debugDescription @16@0:8
        Method: doesNotRecognizeSelector: v24@0:8:16
```

There are several interesting things about this:

1. 's name gets mangled to produce an Objective-C class name that contains not only the Swift name, but also the Swift module (in this case, "memory") and some other stuff.
2. gets an Objective-C instance variable, but its methods don't show up. The instance variable has no type annotation, just a name.
3. , which is a new root class. Plain Swift classes are not subclasses (directly or indirectly) of

  .

  does implement the

  protocol, so it can play the part of

  to an extent.
4. contains a single instance variable called

  . Cute.
5. is actually a

  containing two members. The first is the familiar

  , while the second is a

  called

  .
6. also contains a method called

  . This tells us that there's such a thing as native Swift reference counting. I'm not sure why it's necessary to check for native Swift reference counting at runtime, but apparently it's done with this method.

Let's take a closer look at that `refCount` field. Here's what the object looks like originally, and then when retained five times:

```
    00393b0701000000 0800000001000000 aaaaaaaaaaaaaaaa
    00393b0701000000 0c00000001000000 aaaaaaaaaaaaaaaa
    00393b0701000000 1000000001000000 aaaaaaaaaaaaaaaa
    00393b0701000000 1400000001000000 aaaaaaaaaaaaaaaa
    00393b0701000000 1800000001000000 aaaaaaaaaaaaaaaa
    00393b0701000000 1c00000001000000 aaaaaaaaaaaaaaaa
```

It looks like the bottom two bits are reserved, and each retain increments the `refCount` field by `4`. (Remember, these are little-endian numbers, so they're backwards.) The `1` farther up the number looks like some sort of flag, but its meaning is unknown.

Let's subclass the test class and see what it produces:

```
    class TestSubclass : TestClass {
        let b: UInt64 = 0xbbbbbbbbbbbbbbbb

        override func method2() {}
        func method3() {}
        func method4() {}
    }
```

The memory contents are what we'd expect to find:

```
    b0393b0701000000 0c00000001000000 aaaaaaaaaaaaaaaa bbbbbbbbbbbbbbbb
```

It looks the same as `TestClass`, with an extra instance variable and a different `isa` pointer. The Objective-C side just contains one instance variable:

```
    Objective-C class _TtC6memory12TestSubclass:
        Ivar: b
```

Let's try an `NSObject` subclass:

```
    class TestNSClass: NSObject {
        let a: UInt64 = 0xaaaaaaaaaaaaaaaa

        func method1() {}
        func method2() {}
    }
```

The instance contains:

```
    50333b0701000000 0000000000000000 aaaaaaaaaaaaaaaa 0000000000000000
```

It looks like it makes room for the extra `magic` storage from `SwiftObject`, but the second chunk of memory goes unused. Inspecting the class with the Objective-C runtime produces some actual methods in addition to the instance variable:

```
    Objective-C class _TtC6memory11TestNSClass:
        Ivar: a 
        Method: method1 v16@0:8
        Method: method2 v16@0:8
        Method: a Q16@0:8
        Method: init @16@0:8
```

The instance variable still doesn't have a type annotation, but the methods are just as we'd expect. Both methods are present, as well as a getter for the instance variable and an `init` method.

Let's subclass this and see how it looks:

```
    class TestNSSubclass : TestNSClass {
        let b: UInt64 = 0xbbbbbbbbbbbbbbbb

        override func method2() {}
        func method3() {}
        func method4() {}
    }
```

An instance of this one contains:

```
    d0333b0701000000 0000000000000000 aaaaaaaaaaaaaaaa bbbbbbbbbbbbbbbb
```

As we'd expect, it maintains the same layout as the superclass, with the additional ivar at the end. The Objective-C class also contains what we'd expect, with a new ivar, entries for the new methods, as well as an entry for the overridden `method2`:

```
    Objective-C class _TtC6memory14TestNSSubclass:
        Ivar: b 
        Method: method2 v16@0:8
        Method: method3 v16@0:8
        Method: method4 v16@0:8
        Method: b Q16@0:8
        Method: init @16@0:8
```

**Classes**  
Let's dive into the actual class structures a bit more. They're Objective-C classes, but what else do they contain? Dumping the raw data for `TestClass` produces this:

```
    c0383b0701000000 2002610701000000 10bac588ff7f0000 0000000000000000 f14a4099e97f0000 1800000007000000 7800000010000000 70223b0701000000 30443a0701000000 d0433a0701000000 e0433a0701000000 50443a0701000000 1000000000000000 0000000000000000 4802610701000000 c0383b0701000000
```

What is all that junk? We know it's an Objective-C class, and the structure for that can be found in [Apple's runtime sources](http://www.opensource.apple.com/source/objc4/objc4-551.1/runtime/objc-runtime-new.h):

```
    struct objc_class : objc_object {
        // Class ISA;
        Class superclass;
        cache_t cache;
        uintptr_t data_NEVER_USE;  // class_rw_t * plus custom rr/alloc flags
```

The first chunk is the `isa`, or the class of the class. And indeed, that first pointer points to the metaclass of `TestClass`:

```
    0x00000001073b38c0: Symbol _TMmC6memory9TestClass
```

Then comes the superclass:

```
    0x0000000107610220: Symbol OBJC_CLASS_$_SwiftObject ObjC class SwiftObject
```

The cache and `data_NEVER_USE` follow, and then there's more stuff beyond the basic Objective-C class data. Some of it is mysterious and doesn't appear to point to anything, but there are some interesting tidbits a bit further down, starting at offset 56 (the 8th-pointer-sized chunk above) within the class:

```
    0x00000001073b2270: Symbol _TMnC6memory9TestClass
    0x00000001073a4430: Symbol _TFC6memory9TestClassg1aVSs6UInt64
    0x00000001073a43d0: Symbol _TFC6memory9TestClass7method1fS0_FT_T_
    0x00000001073a43e0: Symbol _TFC6memory9TestClass7method2fS0_FT_T_
    0x00000001073a4450: Symbol _TFC6memory9TestClasscfMS0_FT_S0_
```

That first one is a bit mysterious, but it looks like a Swift-level metaclass. Apple's `swift-demangle` tool describes it as "nominal type descriptor for `memory.TestClass`". The others are method implementations. There's the getter for `a`, implementations for `method1` and `method2`, and finally the init method. This is presumably the vtable used for method dispatch in Swift code.

`TestSubclass` looks similar:

```
    70393b0701000000 00393b0701000000 e0e54099e97f0000 0300000002000000 714b4099e97f0000 2000000007000000 9800000010000000 a0223b0701000000 30443a0701000000 d0433a0701000000 c0443a0701000000 50453a0701000000 1000000000000000 30453a0701000000 d0443a0701000000 e0443a0701000000
```

It starts with Objective-C class data, and then has the same sort of extra stuff:

```
    0x00000001073b22a0: Symbol _TMnC6memory12TestSubclass
    0x00000001073a4430: Symbol _TFC6memory9TestClassg1aVSs6UInt64
    0x00000001073a43d0: Symbol _TFC6memory9TestClass7method1fS0_FT_T_
    0x00000001073a44c0: Symbol _TFC6memory12TestSubclass7method2fS0_FT_T_
    0x00000001073a4550: Symbol _TFC6memory12TestSubclasscfMS0_FT_S0_
    0x00000001073a4530: Symbol _TFC6memory12TestSubclassg1bVSs6UInt64
    0x00000001073a44d0: Symbol _TFC6memory12TestSubclass7method3fS0_FT_T_
    0x00000001073a44e0: Symbol _TFC6memory12TestSubclass7method4fS0_FT_T_
```

Once again, we have the type descriptor entry followed by the vtable. It maintains the same layout and has some of the same entries. We can clearly see how `method1` comes from `TestClass` but `method2` is overridden. The new methods added in `TestSubclass` are added to the end.

This illustrates how vtable dispatch works. For an instance of `TestClass`, looking up the slot for `method2` will produce `_TFC6memory9TestClass7method2fS0_FT_T_`, which is `TestClass`'s implementation. For an instance of `TestSubclass`, that same slot contains `_TFC6memory12TestSubclass7method2fS0_FT_T_`, so a simple array indexing operation is enough to locate the function to invoke.

`TestNSClass` and `TestNSSubclass` show the same structure, including the vtable. Although their methods are made available in the Objective-C runtime, they're still made available to Swift's vtable dispatch mechanism as well. I'm not sure if the vtable actually gets used in that case, but that investigation will have to wait for another day.

**Conclusion**  
There's some interesting stuff going on with variables holding protocol types, since they can hold both objects and `struct`s. There's also interesting stuff to be seen in the layout of arrays and dictionaries. However, I have too many words and not enough time, so that will have to wait for the next article. So far, we've seen that `struct`s and objects are laid out mostly like we'd expect, with objects containing some extra data for reference counting. Swift classes are Objective-C classes, even when they don't subclass `NSObject`. In that case, they subclass `SwiftObject` which is a new root class that conforms to the `NSObject` protocol. In addition to the normal Objective-C class structure, Swift classes also contain a vtable for all of their methods inline in the class.

That's it for today, but we'll return soon with more exploration of Swift's runtime memory structures.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
