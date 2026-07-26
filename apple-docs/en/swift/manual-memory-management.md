---
title: Manual Memory Management
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/manual-memory-management
source_url: 'https://developer.apple.com/documentation/swift/manual-memory-management'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/manual-memory-management.json'
content_hash: 'sha256:44ed74dcb790ce43'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md)

# Manual Memory Management

<sub>API Collection</sub>

Allocate and manage memory manually.

## Topics

### First Steps

- [Calling Functions With Pointer Parameters](calling-functions-with-pointer-parameters.md) — Use implicit pointer casting or bridging when calling functions that takes pointers as parameters.

### Safe Memory Access

- [Span](span.md) — `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [RawSpan](rawspan.md) — `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [OutputSpan](outputspan.md) — `OutputSpan` is a reference to a contiguous region of memory that starts with some number of initialized `Element` instances followed by uninitialized memory. It provides operations to access the items it stores, as well as to add new elements and to remove existing ones.
- [OutputRawSpan](outputrawspan.md) — `OutputRawSpan` is a reference to a contiguous region of memory which starts with some number of initialized bytes, followed by uninitialized memory. It provides operations to access the bytes it stores, as well as to append and to remove bytes.
- [UTF8Span](utf8span.md) — A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.
- [MutableSpan](mutablespan.md) — `MutableSpan<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [MutableRawSpan](mutablerawspan.md) — `MutableRawSpan` represents a contiguous region of memory which contains initialized bytes.
- [SpanIterator](spaniterator.md) _(beta)_

### Safe Access to Raw Bytes

- [FullyInhabited](fullyinhabited.md) — A protocol for types whose memory can safely be written as or read from raw bytes.
- [ConvertibleFromBytes](convertiblefrombytes.md) — A protocol for types whose memory can safely be populated from raw bytes, resulting in a valid instance.
- [ConvertibleToBytes](convertibletobytes.md) — A protocol for types whose memory can safely be read as individual raw bytes.
- [ByteOrder](byteorder.md) — A byte ordering in memory. _(beta)_
- [bitCast(_:to:)](<bitcast(__to_).md>) — Returns the bits of the given instance, interpreted as having the specified type.

### Typed Pointers

- [UnsafePointer](unsafepointer.md) — A pointer for accessing data of a specific type.
- [UnsafeMutablePointer](unsafemutablepointer.md) — A pointer for accessing and manipulating data of a specific type.
- [UnsafeBufferPointer](unsafebufferpointer.md) — A nonowning collection interface to a buffer of elements stored contiguously in memory.
- [UnsafeMutableBufferPointer](unsafemutablebufferpointer.md) — A nonowning collection interface to a buffer of mutable elements stored contiguously in memory.

### Raw Pointers

- [UnsafeRawPointer](unsaferawpointer.md) — A raw pointer for accessing untyped data.
- [UnsafeMutableRawPointer](unsafemutablerawpointer.md) — A raw pointer for accessing and manipulating untyped data.
- [UnsafeRawBufferPointer](unsaferawbufferpointer.md) — A  nonowning collection interface to the bytes in a region of memory.
- [UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md) — A mutable nonowning collection interface to the bytes in a region of memory.

### Memory Access

- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-9fjn6.md>) — Invokes the given closure with a pointer to the given argument.
- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-35wrn.md>) — Invokes the given closure with a pointer to the given argument.
- [withUnsafeMutablePointer(to:_:)](<withunsafemutablepointer(to___).md>) — Calls the given closure with a mutable pointer to the given argument.
- [withUnsafeBytes(of:_:)](<withunsafebytes(of___)-3ywhh.md>) — Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [withUnsafeMutableBytes(of:_:)](<withunsafemutablebytes(of___).md>) — Invokes the given closure with a mutable buffer pointer covering the raw bytes of the given argument.
- [withTemporaryAllocation(byteCount:alignment:_:)](<withtemporaryallocation(bytecount_alignment___).md>) — Provides scoped access to an output raw span with the specified byte count and alignment.
- [withTemporaryAllocation(of:capacity:_:)](<withtemporaryallocation(of_capacity___).md>) — Provides scoped access to an output span of the specified type and capacity.
- [withUnsafeTemporaryAllocation(of:capacity:_:)](<withunsafetemporaryallocation(of_capacity___).md>) — Provides scoped access to a buffer pointer to memory of the specified type and with the specified capacity.
- [withUnsafeTemporaryAllocation(byteCount:alignment:_:)](<withunsafetemporaryallocation(bytecount_alignment___).md>) — Provides scoped access to a raw buffer pointer with the specified byte count and alignment.
- [swap(_:_:)](<swap(____).md>) — Exchanges the values of the two arguments.
- [exchange(_:with:)](<exchange(__with_).md>) — Replaces the value of a mutable value with the supplied new value, returning the original.

### Memory Layout

- [MemoryLayout](memorylayout.md) — The memory layout of a type, describing its size, stride, and alignment.

### Heap Storage

- [UniqueArray](uniquearray.md) — A dynamically self-resizing, heap allocated, noncopyable array of potentially noncopyable elements. _(beta)_
- [UniqueBox](uniquebox.md) — A smart pointer type that uniquely owns an instance of `Value` on the heap. _(beta)_

### Reference Counting

- [Unmanaged](unmanaged.md) — A type for propagating an unmanaged object reference.
- [withExtendedLifetime(_:_:)](<withextendedlifetime(____)-4mmpv.md>) — Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.
- [withExtendedLifetime(_:_:)](<withextendedlifetime(____)-59dz3.md>) — Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.
- [extendLifetime(_:)](<extendlifetime(__).md>) — Extends the lifetime of the given instance.

## See Also

### Programming Tasks

- [Input and Output](input-and-output.md) — Print values to the console, read from and write to text streams, and use command line arguments.
- [Debugging and Reflection](debugging-and-reflection.md) — Fortify your code with runtime checks, and examine your values’ runtime representation.
- [Macros](macros.md) — Generate boilerplate code and perform other compile-time operations.
- [Concurrency](concurrency.md) — Perform asynchronous and parallel operations.
- [Key-Path Expressions](key-path-expressions.md) — Use key-path expressions to access properties dynamically.
- [Type Casting and Existential Types](type-casting-and-existential-types.md) — Perform casts between types or represent values of any type.
- [C Interoperability](c-interoperability.md) — Use imported C types or call C variadic functions.
- [Operator Declarations](operator-declarations.md) — Work with prefix, postfix, and infix operators.
