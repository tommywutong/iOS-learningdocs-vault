---
title: 'The Swift Runtime: Class Metadata Initialization'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/'
original_language: en
published: 2020-10-06
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:f2b0a87cd23b336a'
translated: false
---

> 原文：[The Swift Runtime: Class Metadata Initialization](https://belkadan.com/blog/2020/10/Swift-Runtime-Class-Metadata-Initialization/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [The Swift Runtime: Class Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/)

[The Swift Runtime: Enums](https://belkadan.com/blog/2020/10/Swift-Runtime-Enums/) »

« [The Swift Runtime: Class Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/?tag=swift)

[The Swift Runtime: Enums](https://belkadan.com/blog/2020/10/Swift-Runtime-Enums/?tag=swift) »

« [The Swift Runtime: Class Metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Class-Metadata/?tag=swift-runtime)

[The Swift Runtime: Enums](https://belkadan.com/blog/2020/10/Swift-Runtime-Enums/?tag=swift-runtime) »

## [The Swift Runtime: Class Metadata Initialization](#)

Welcome to the sixth in a series of posts on the [Swift runtime](https://belkadan.com/blog/tags/swift-runtime). The goal is to go over the functions of the Swift runtime, using what I learned in my [Swift on Mac OS 9 project](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/) as a reference. Last time we went through the fields of class metadata; today we’re going to finish initializing them.more

As mentioned previously, I implemented my stripped-down runtime in Swift as much as possible, though I had to use a few undocumented Swift features to do so. I’ll be showing excerpts of my runtime code throughout these posts, and you can check out the full thing [in the ppc-swift repository](https://belkadan.com/source/ppc-swift-project/tree/refs/heads/dev:/stdlib/_Runtime).

## `swift_init­ClassMetadata2`

Just like struct metadata had both `swift_allocate­Generic­ValueMetadata` and `swift_init­StructMetadata`, class metadata has `swift_allocate­Generic­ClassMetadata` and `swift_init­ClassMetadata2`. Wait, why “2”? Because the original `swift_init­ClassMetadata` didn’t handle cycles in metadata initialization, which was [one of the oldest public issues in the Swift project](https://bugs.swift.org/browse/SR-263). But [as mentioned previously](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/) my runtime doesn’t handle cycles in metadata initialization either, so I’m just going to ignore all that.

The high-level algorithm fits in a few lines:

```
@_silgen_name("swift_initClassMetadata2")
func swift_initClassMetadata2(
  _ metadata: UnsafeMutablePointer<ClassMetadata>,
  _ flags: ClassLayoutFlags,
  _ numFields: UInt,
  _ fieldTypes: UnsafePointer<UnsafePointer<TypeLayout>>,
  _ fieldOffsets: UnsafeMutablePointer<UInt>
) -> MetadataDependency {
  metadata[]._.superclass = getSuperclassMetadata(forSubclass: metadata)
  copySuperclassMetadataToSubclass(metadata, flags)
  if !flags.hasStaticVTable {
    fatalError("This should never happen without library evolution.")
  }
  initClassFieldOffsetVector(metadata, numFields, fieldTypes, fieldOffsets)
  
  return MetadataDependency() // for handling cycles, not implemented
}
```

First we get the superclass. Then we copy down relevant parts of the metadata. Then we handle the “field offset vector”, whatever that is. And…that’s it, though admittedly it’s a lot more complicated in a runtime that supports Objective-C interoperability. (Also all vtable layout—methods and such—should have offsets determined statically, since I’m not supporting [library evolution](https://swift.org/blog/swift-5-1-released/#module-stability) in my project.) So the rest of this post will just be walking through each of those helpers.

## `getSuperclassMetadata(forSubclass:)`

This helper function also looks tiny, but that’s because it hides its complexity elsewhere:

```
private func getSuperclassMetadata(
  forSubclass metadata: UnsafePointer<ClassMetadata>
) -> UnsafePointer<ClassMetadata>? {
  return metadata[]._.description.superclassMangledName.map {
    let genericArgs = metadata.upcast(to: \._.base).genericArgs
    let metadata = metadataFromMangledName($0, genericArgs)
    return metadata.downcast(from: \ClassMetadata._.base)
  }
}
```

The superclass’s mangled name is stored in the class type description. It’s an Optional (because of root classes), so we use [`map`](https://developer.apple.com/documentation/swift/optional/1539476-map) to only decode that metadata if it’s non-`nil`. The generic args of _this_ class may be necessary to correctly set up the superclass—consider `class Child<Foo> : Parent<[String: Foo]>`. And then we’ve got these `upcast(to:)` and `downcast(from:)` helpers, plus whatever’s in `metadataFrom­MangledName(_:_:)`. Let’s take those separately.

Remember back in the third post I talked about [embedding structs inside other structs as a form of subclassing](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Metadata#filling-in-the-fields)? Because those structs are (nearly) always embedded with the “base” type being the first element, both the “base” and the “subclass” have the same address. That makes it possible to convert between them by going through UnsafeRawPointer. But nothing stops me from writing the _wrong_ type in that case, which is where these helpers come in:

```
extension UnsafePointer {
  func upcast<Base>(
    to keyPath: KeyPath<Pointee, Base>
  ) -> UnsafePointer<Base> {
    // Ideally we'd enforce that Base is at a 0 offset from Pointee,
    // but that's not implemented.
    return UnsafeRawPointer(self).assumingMemoryBound(to: Base.self)
  }

  func downcast<Subtype>(
    from keyPath: KeyPath<Subtype, Pointee>
  ) -> UnsafePointer<Subtype> {
    return UnsafeRawPointer(self).assumingMemoryBound(to: Subtype.self)
  }
}
```

The use of key paths enforces that the “cast” is actually to a “base class” or “subclass” in the embedding hierarchy, which is a lot safer than going to UnsafeRawPointer and back explicitly (which is what I was doing before I added these). I didn’t actually implement any of the runtime support for key paths, but they can still be used in static ways, which in this case is purely for enforcing types. (You’ll notice the `keyPath` argument isn’t used at all in the body of the function.)

I feel a lot better about my runtime implementation thanks to these helpers, and you’ll see them pop up more in further samples.

`metadataFrom­MangledName(_:_:)`, on the other hand, has enough going on that it deserves its own section.

## Mangled name type encoding

By the time `swift_init­ClassMetadata2` completes the `superclass` field has to be a valid ClassMetadata pointer, but if the superclass is generic it’s not (necessarily) possible for that pointer to be available at compile time! The simplest way to address this would be to put in an “accessor function” that takes generic arguments and returns the appropriate superclass (probably by calling [`swift_get­GenericMetadata`](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/) somewhere in its implementation), and have subclasses reference that. And indeed, that is a valid approach, but it has one major downside: code size. It’s not going to be _that_ big a function, since a huge chunk of the work is handled by `swift_get­GenericMetadata`, but it’s still significant enough that the Swift team at Apple wanted to do something better. What they[1](#fn:they) needed was a compact, structured format that could uniquely refer to a type, and, well, turns out they already had one: mangled names. (I’m not going to explain what mangled names are here; [Gwynne Raskind has a good explainer on Mike Ash’s blog](https://mikeash.com/pyblog/friday-qa-2014-08-15-swift-name-mangling.html). Note that the [details of Swift name mangling](https://github.com/apple/swift/blob/release/5.3/docs/ABI/Mangling.rst) have changed a fair amount from 2014, but the principles are still there.)

Now, mangled names are normally only used as symbol names, or for referring to a declaration when indexing a codebase (for refactoring, jump-to-definition, looking up docs for an API, etc). But to use them to describe type metadata at run time, they have to be able to handle things that can’t be looked up by symbol name, like types declared in a function. So the Swift team added the ability to embed relative and absolute pointers _inside_ a “mangled name”, which code like `metadataFrom­MangledName` would know how to resolve. This means that a “mangled name” in the runtime sense may not be a valid printable “name” anymore.

In the real Swift codebase, the _demangler_—the code to take a mangled name and reconstruct its structure[2](#fn:structure)—is written in C++, which allows it to be used in the runtime, the compiler, the `swift-demangle` command-line tool, and the out-of-process inspection library used by the debugger. Implementing that in Swift would have been a long and mostly boring exercise, but I didn’t want to try to get that C++ to run on Mac OS 9 either. (I didn’t check, but it’s very likely it depends on having a newer C++ standard library than would have been available in 2001.)

Fortunately, the name mangling scheme used by the compiler had an escape hatch: a way to embed a pointer to the simple “accessor function” that I mentioned at the beginning of this section. So this is one of the few places where I changed the Swift compiler to support this project: it _always_ uses accessor functions when emitting mangled-name-style type references. (In theory I could remove this extra bit of indirection by pointing directly to the accessor function, since it’s no longer serving a purpose, but in practice that would probably mean changing a lot more in the compiler, and that wasn’t worth the effort.)

All of this is to say my `metadataFrom­MangledName(_:_:)` is a lot simpler than the real one:

```
func metadataFromMangledName(
  _ mangledRef: UnsafePointer<UInt8>,
  _ genericArgs: UnsafePointer<UnsafeRawPointer?>?
) -> UnsafePointer<TypeMetadata> {
  guard mangledRef[0] == 255 && mangledRef[1] == 9 else {
    fatalError()
  }

  typealias MetadataAccessFn = @convention(c) (
    UnsafePointer<UnsafeRawPointer?>?
  ) -> TypeErasedPointer<TypeMetadata>

  let offset = RelativePointerOffset<MetadataAccessFn>(
    fromUnalignedBytes: mangledRef + 2)
  let accessFn = mangledRef.applying(offset, additionalOffset: 2)!
  return accessFn[](genericArgs).assumingMemoryBound(to: TypeMetadata.self)
}
```

We check that the first two bytes of the mangled name have the signature of an accessor function. Then we load the relative pointer stored in the “mangled name”, resolve it to an absolute pointer-to-function, and then call that function and assume the result is what we want. (`init(fromUnalignedBytes:)` is a helper to deal with reconstructing a 32-bit signed offset from an `UnsafePointer<UInt8>`.) That’s all the “mangled name handling” you’re going to get from me. Sorry!

## `copySuperclass­Metadata­ToSubclass(_:_:)`

What information does a class need from its superclass? The most obvious thing is the methods, but without library evolution support, that can actually be resolved at compile time. Instead, there’s two things that depend on the _particular_ concrete superclass: the generic arguments, and the _field offset vector._

- Why do the _superclass’s_ generic arguments need to be present in the _subclass?_ Because we’re going to call methods inherited from the superclass, and they expect the superclass’s generic arguments to be located at a particular offset in the class metadata.
- What’s the “field offset vector”? It’s come up before, actually, in the initialization of [struct metadata](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/#what-about-structs). That’s what’s going to store the offsets of each field in the struct/class, so that when you access the `second` field of a class like this:

  ```
  class Pair<First, Second> {
    var first: First
    var second: Second
  }
  ```

  …the offset doesn’t have to be recomputed every time. And again, the field offsets for superclass fields need to be copied into subclass metadata so that superclass _methods_ can directly access stored properties.
- Can we get all that information from the superclass? Turns out no, we can’t! We _only_ want the generic arguments and the field offsets; if we copy _everything_ in the superclass, we’ll stomp on any entries for methods this class has overridden. Of course, we could have some way to copy those _back_ afterwards, but then we’re back to either adding code size for a dedicated function, or something more involved than just a bunch of range copies. So the Swift runtime chooses to iterate through the entire superclass chain to decide what bits it needs to copy. (It still gets those bits from the immediate superclass, though, to avoid accessing more memory and more cache lines than it needs to.)

```
private func copySuperclassMetadataToSubclass(
  _ metadata: UnsafeMutablePointer<ClassMetadata>,
  _ flags: ClassLayoutFlags
) {
  guard let superclass = metadata[]._.superclass else { return }

  let rawMetadata = UnsafeMutableRawPointer(metadata)
  let rawSuperclass = UnsafeRawPointer(superclass)

  for ancestor in sequence(first: superclass, next: { $0[]._.superclass }) {
    let description = ancestor[]._.description

    if let generics = description.upcast(to: \._.base).fullGenericContextHeader {
      let offset = description[].metadataBounds.immediateMembersOffset
      let superclassGenericArgs =
        (rawSuperclass + offset).assumingMemoryBound(to: UnsafeRawPointer.self)
      (rawMetadata + offset).initializeMemory(
        as: UnsafeRawPointer.self,
        from: superclassGenericArgs,
        count: generics[]._.base.totalArgumentCount)
    }

    if !flags.hasStaticVTable {
      fatalError("This should never happen without library evolution.")
    }

    if description[]._.fieldOffsetVectorOffset != 0 {
      let offset = Int(description[]._.fieldOffsetVectorOffset) &*
        MemoryLayout<UInt>.size
      let superclassFieldOffsets =
        (rawSuperclass + offset).assumingMemoryBound(to: UInt.self)
      (rawMetadata + offset).initializeMemory(
        as: UInt.self,
        from: superclassFieldOffsets,
        count: Int(description[]._.numFields))
    }
  }
}
```

There’s actually one optimization the compiler and runtime _could_ make but don’t, which is to not duplicate generic arguments when they’re exactly the same as the superclass’s.

```
class ChildWrapper<Value> : ParentWrapper<Value>
```

But this would only work when they’re _exactly_ the same as the superclass’s, including all constraints.[3](#fn:key) Otherwise, we’d have to store the extra information elsewhere, and then logic that asks for “a type’s generic arguments” will be missing important information about how to use the type! (There’s logic elsewhere in the runtime that assumes generic arguments are contiguous in memory.) It would also mean storing an additional field on the class for where the generic arguments live, instead of just assuming they’re at the start of the “immediate members” region. So maybe it’s not worth it.

## `initClass­Field­OffsetVector(_:_:_:_:)`

After all that about superclasses, this last bit should look comfortingly familiar—it’s basically the same as what [`swift_init­StructMetadata`](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/#what-about-structs) does.

```
private func initClassFieldOffsetVector(
  _ metadata: UnsafeMutablePointer<ClassMetadata>,
  _ numFields: UInt,
  _ fieldTypes: UnsafePointer<UnsafePointer<TypeLayout>>,
  _ fieldOffsets: UnsafeMutablePointer<UInt>
) {
  let size: UInt
  let alignMask: UInt32

  if let superclass = metadata[]._.superclass {
    size = UInt(superclass[]._.instanceSize)
    alignMask = UInt32(superclass[]._.instanceAlignMask)
  } else {
    size = 2 &* UInt(MemoryLayout<UInt>.size)
    alignMask = UInt32(MemoryLayout<UInt>.alignment) &- 1
  }
  
  var layout = TypeLayout((
    size: size,
    stride: size,
    flags: ValueWitnessFlags(rawValue: alignMask),
    extraInhabitantCount: 0))

  let fields = UnsafeBufferPointer(start: fieldTypes, count: Int(numFields))
  performBasicLayout(&layout, fields.lazy.map { $0[] }) {
    fieldOffsets[$0] = UInt($1)
  }
  metadata[]._.instanceSize = UInt32(layout._.size)
  metadata[]._.instanceAlignMask = UInt16(layout._.flags.alignMask)
}
```

We’re starting with the size and alignment of our superclass, or of the [heap object header](https://belkadan.com/blog/2020/08/Swift-Runtime-Heap-Objects/) if we don’t have a superclass. For classes, we don’t care about stride or extra inhabitants, so we don’t bother setting those fields to their precise values, just something that won’t break [`performBasic­Layout‍(_‍:_‍:setOffset‍:‍)`](https://belkadan.com/blog/2020/09/Swift-Runtime-Type-Layout/#all-together-now). (It’s great that we can just keep reusing `performBasic­Layout‍(_‍:_‍:setOffset‍:‍)`!)

## Wrap-up

With this, we’ve now seen the entire process of creating and initializing class metadata, just like we did with structs. Of course, in many cases the compiler will be able to do much of this work at compile time, but in case it can’t, the Swift runtime is powerful enough to do it all itself.

We’ve talked about structs and classes; [next time we’ll finally get to enums](https://belkadan.com/blog/2020/10/Swift-Runtime-Enums/).

1. I was at Apple working on Swift at the time, but I had very little to do with this feature, so I’m not including myself. [↩︎](#fnref:they)
2. The term “demangler” is often used for a tool that takes a mangled name and prints a flat human-readable form of the name, and these tools may not even bother to construct a structured representation of the name if it’s not needed. But because Swift does a lot more with “demangle trees” than just show them to humans, the human-readable printing is just another consumer. You can see the structure of those trees by passing the `-expand` option to `swift-demangle`. [↩︎](#fnref:structure)
3. Technically, the only constraints that matter are [the ones that count as “key” or “extra” arguments](https://belkadan.com/blog/2020/09/Swift-Runtime-Uniquing-Caches/#choosing-our-cache-key); same-type constraints don’t actually add any run-time information to a generic type. [↩︎](#fnref:key)

This entry was posted on [October](https://belkadan.com/blog/2020/10) 06, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Swift runtime](https://belkadan.com/blog/tags/swift-runtime)
