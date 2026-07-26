---
title: UnsafeRawPointer
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsaferawpointer
source_url: 'https://developer.apple.com/documentation/swift/unsaferawpointer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawpointer.json'
content_hash: 'sha256:75b7f1383c31b51d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UnsafeRawPointer

<sub>Structure</sub>

A raw pointer for accessing untyped data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UnsafeRawPointer
```

## Overview

The `UnsafeRawPointer` type provides no automated memory management, no type safety, and no alignment guarantees. You are responsible for handling the life cycle of any memory you work with through unsafe pointers, to avoid leaks or undefined behavior.

Memory that you manually manage can be either _untyped_ or _bound_ to a specific type. You use the `UnsafeRawPointer` type to access and manage raw bytes in memory, whether or not that memory has been bound to a specific type.

## Understanding a Pointer’s Memory State

The memory referenced by an `UnsafeRawPointer` instance can be in one of several states. Many pointer operations must only be applied to pointers with memory in a specific state—you must keep track of the state of the memory you are working with and understand the changes to that state that different operations perform. Memory can be untyped and uninitialized, bound to a type and uninitialized, or bound to a type and initialized to a value. Finally, memory that was allocated previously may have been deallocated, leaving existing pointers referencing unallocated memory.

## Raw, Uninitialized Memory

Raw memory that has just been allocated is in an _uninitialized, untyped_ state. Uninitialized memory must be initialized with values of a type before it can be used with any typed operations.

To bind uninitialized memory to a type without initializing it, use the `bindMemory(to:count:)` method. This method returns a typed pointer for further typed access to the memory.

## Typed Memory

Memory that has been bound to a type, whether it is initialized or uninitialized, is typically accessed using typed pointers—instances of `UnsafePointer` and `UnsafeMutablePointer`. Initialization, assignment, and deinitialization can be performed using `UnsafeMutablePointer` methods.

Memory that has been bound to a type can be rebound to a different type only after it has been deinitialized or if the bound type is a _trivial type_. Deinitializing typed memory does not unbind that memory’s type. The deinitialized memory can be reinitialized with values of the same type, bound to a new type, or deallocated.

> [!note] Note
> A trivial type can be copied bit for bit with no indirection or reference-counting operations. Generally, native Swift types that do not contain strong or weak references or other forms of indirection are trivial, as are imported C structs and enumerations.

When reading from  memory as raw bytes when that memory is bound to a type, you must ensure that you satisfy any alignment requirements.

## Raw Pointer Arithmetic

Pointer arithmetic with raw pointers is performed at the byte level. When you add to or subtract from a raw pointer, the result is a new raw pointer offset by that number of bytes. The following example allocates four bytes of memory and stores `0xFF` in all four bytes:

```swift
let bytesPointer = UnsafeMutableRawPointer.allocate(byteCount: 4, alignment: 4)
bytesPointer.storeBytes(of: 0xFFFF_FFFF, as: UInt32.self)

// Load a value from the memory referenced by 'bytesPointer'
let x = bytesPointer.load(as: UInt8.self)       // 255

// Load a value from the last two allocated bytes
let offsetPointer = bytesPointer + 2
let y = offsetPointer.load(as: UInt16.self)     // 65535
```

The code above stores the value `0xFFFF_FFFF` into the four newly allocated bytes, and then loads the first byte as a `UInt8` instance and the third and fourth bytes as a `UInt16` instance.

Always remember to deallocate any memory that you allocate yourself.

```swift
bytesPointer.deallocate()
```

## Implicit Casting and Bridging

When calling a function or method with an `UnsafeRawPointer` parameter, you can pass an instance of that specific pointer type, pass an instance of a compatible pointer type, or use Swift’s implicit bridging to pass a compatible pointer.

For example, the `print(address:as:)` function in the following code sample takes an `UnsafeRawPointer` instance as its first parameter:

```swift
func print<T>(address p: UnsafeRawPointer, as type: T.Type) {
    let value = p.load(as: type)
    print(value)
}
```

As is typical in Swift, you can call the `print(address:as:)` function with an `UnsafeRawPointer` instance. This example passes `rawPointer` as the initial parameter.

```swift
// 'rawPointer' points to memory initialized with `Int` values.
let rawPointer: UnsafeRawPointer = ...
print(address: rawPointer, as: Int.self)
// Prints "42"
```

Because typed pointers can be implicitly cast to raw pointers when passed as a parameter, you can also call `print(address:as:)` with any mutable or immutable typed pointer instance.

```swift
let intPointer: UnsafePointer<Int> = ...
print(address: intPointer, as: Int.self)
// Prints "42"

let mutableIntPointer = UnsafeMutablePointer(mutating: intPointer)
print(address: mutableIntPointer, as: Int.self)
// Prints "42"
```

Alternatively, you can use Swift’s _implicit bridging_ to pass a pointer to an instance or to the elements of an array. Use inout syntax to implicitly create a pointer to an instance of any type. The following example uses implicit bridging to pass a pointer to `value` when calling `print(address:as:)`:

```swift
var value: Int = 23
print(address: &value, as: Int.self)
// Prints "23"
```

An immutable pointer to the elements of an array is implicitly created when you pass the array as an argument. This example uses implicit bridging to pass a pointer to the elements of `numbers` when calling `print(address:as:)`.

```swift
let numbers = [5, 10, 15, 20]
print(address: numbers, as: Int.self)
// Prints "5"
```

You can also use inout syntax to pass a mutable pointer to the elements of an array. Because `print(address:as:)` requires an immutable pointer, although this is syntactically valid, it isn’t necessary.

```swift
var mutableNumbers = numbers
print(address: &mutableNumbers, as: Int.self)
```

> [!important] Important
> The pointer created through implicit bridging of an instance or of an array’s elements is only valid during the execution of the called function. Escaping the pointer to use after the execution of the function is undefined behavior. In particular, do not use implicit bridging when calling an `UnsafeRawPointer` initializer.
>
> ```swift
> var number = 5
> let numberPointer = UnsafeRawPointer(&number)
> // Accessing 'numberPointer' is undefined behavior.
> ```

## Relationships

- **Conforms To**: [AtomicOptionalRepresentable](../synchronization/atomicoptionalrepresentable.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BitwiseCopyable](bitwisecopyable.md), [Comparable](comparable.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [CustomReflectable](customreflectable.md), [Equatable](equatable.md), [Escapable](escapable.md), [Hashable](hashable.md), [Strideable](strideable.md)

## Topics

### Initializers

- [init(_:)](<unsaferawpointer/init(__)-1z2cc.md>) — Creates a new raw pointer from an `AutoreleasingUnsafeMutablePointer` instance.
- [init(_:)](<unsaferawpointer/init(__)-1z902.md>) — Creates a new raw pointer from the given typed pointer.
- [init(_:)](<unsaferawpointer/init(__)-2kyf.md>) — Creates a new raw pointer from an `AutoreleasingUnsafeMutablePointer` instance.
- [init(_:)](<unsaferawpointer/init(__)-4dxzd.md>) — Creates a new raw pointer from the given mutable raw pointer.
- [init(_:)](<unsaferawpointer/init(__)-76a4f.md>) — Creates a new raw pointer from the given typed pointer.
- [init(_:)](<unsaferawpointer/init(__)-84kry.md>) — Creates a new raw pointer from the given typed pointer.
- [init(_:)](<unsaferawpointer/init(__)-8tlvz.md>) — Creates a new raw pointer from the given mutable raw pointer.
- [init(_:)](<unsaferawpointer/init(__)-9t67o.md>) — Creates a new raw pointer from the given typed pointer.

### Instance Properties

- [customPlaygroundQuickLook](unsaferawpointer/customplaygroundquicklook.md) — A custom playground Quick Look for this instance.
- [hashValue](unsaferawpointer/hashvalue.md) — The hash value.

### Instance Methods

- [alignedDown(for:)](<unsaferawpointer/aligneddown(for_).md>) — Obtain the preceding pointer properly aligned to store a value of type `T`.
- [alignedDown(toMultipleOf:)](<unsaferawpointer/aligneddown(tomultipleof_).md>) — Obtain the preceding pointer whose bit pattern is a multiple of `alignment`.
- [alignedUp(for:)](<unsaferawpointer/alignedup(for_).md>) — Obtain the next pointer properly aligned to store a value of type `T`.
- [alignedUp(toMultipleOf:)](<unsaferawpointer/alignedup(tomultipleof_).md>) — Obtain the next pointer whose bit pattern is a multiple of `alignment`.
- [assumingMemoryBound(to:)](<unsaferawpointer/assumingmemorybound(to_).md>) — Returns a typed pointer to the memory referenced by this pointer, assuming that the memory is already bound to the specified type.
- [bindMemory(to:capacity:)](<unsaferawpointer/bindmemory(to_capacity_).md>) — Binds the memory to the specified type and returns a typed pointer to the bound memory.
- [deallocate()](<unsaferawpointer/deallocate().md>) — Deallocates the previously allocated memory block referenced by this pointer.
- [load(fromByteOffset:as:)](<unsaferawpointer/load(frombyteoffset_as_).md>) — Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [loadUnaligned(fromByteOffset:as:)](<unsaferawpointer/loadunaligned(frombyteoffset_as_)-5iviy.md>) — Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [loadUnaligned(fromByteOffset:as:)](<unsaferawpointer/loadunaligned(frombyteoffset_as_)-5wi7f.md>) — Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [withMemoryRebound(to:capacity:_:)](<unsaferawpointer/withmemoryrebound(to_capacity___).md>) — Executes the given closure while temporarily binding memory to the specified number of instances of type `T`.

### Type Aliases

- [Pointee](unsaferawpointer/pointee.md)

### Default Implementations

- [AtomicOptionalRepresentable Implementations](unsaferawpointer/atomicoptionalrepresentable-implementations.md)
- [AtomicRepresentable Implementations](unsaferawpointer/atomicrepresentable-implementations.md)
- [Comparable Implementations](unsaferawpointer/comparable-implementations.md)
- [CustomReflectable Implementations](unsaferawpointer/customreflectable-implementations.md)
- [Equatable Implementations](unsaferawpointer/equatable-implementations.md)
- [Hashable Implementations](unsaferawpointer/hashable-implementations.md)
- [Strideable Implementations](unsaferawpointer/strideable-implementations.md)

## See Also

### Raw Pointers

- [UnsafeMutableRawPointer](unsafemutablerawpointer.md) — A raw pointer for accessing and manipulating untyped data.
- [UnsafeRawBufferPointer](unsaferawbufferpointer.md) — A  nonowning collection interface to the bytes in a region of memory.
- [UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md) — A mutable nonowning collection interface to the bytes in a region of memory.
