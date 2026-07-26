---
title: 'withTemporaryAllocation(of:capacity:_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/withtemporaryallocation(of:capacity:_:)'
source_url: 'https://developer.apple.com/documentation/swift/withtemporaryallocation(of:capacity:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withtemporaryallocation%28of%3Acapacity%3A_%3A%29.json'
content_hash: 'sha256:69a0e4e0bf49057d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withTemporaryAllocation(of:capacity:_:)

<sub>Function</sub>

Provides scoped access to an output span of the specified type and capacity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withTemporaryAllocation<T, R, E>(of type: T.Type, capacity: Int, _ body: @_lifetime(0: copy 0) (inout OutputSpan<T>) throws(E) -> R) throws(E) -> R where E : Error, T : ~Copyable, R : ~Copyable
```

## Parameters

- `type` — The type of the elements in the buffer being temporarily allocated.

- `capacity` — The capacity of the output span being temporarily allocated.

- `body` — A closure to invoke and to which the allocated output span should be passed.

## Return Value

Whatever is returned by `body`.

## Discussion

This function is useful for cheaply allocating storage for a sequence of values for a brief duration. Storage may be allocated on the heap or on the stack, depending on the required size and alignment.

When `body` is called, it is passed an empty `OutputSpan`. `body` may append or initialize elements in the output span. Any elements that have been initialized when `body` returns are deinitialized automatically, and deallocation is also automatic.

> [!danger] Throws
> Whatever is thrown by `body`.

## See Also

### Memory Access

- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-9fjn6.md>) — Invokes the given closure with a pointer to the given argument.
- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-35wrn.md>) — Invokes the given closure with a pointer to the given argument.
- [withUnsafeMutablePointer(to:_:)](<withunsafemutablepointer(to___).md>) — Calls the given closure with a mutable pointer to the given argument.
- [withUnsafeBytes(of:_:)](<withunsafebytes(of___)-3ywhh.md>) — Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [withUnsafeMutableBytes(of:_:)](<withunsafemutablebytes(of___).md>) — Invokes the given closure with a mutable buffer pointer covering the raw bytes of the given argument.
- [withTemporaryAllocation(byteCount:alignment:_:)](<withtemporaryallocation(bytecount_alignment___).md>) — Provides scoped access to an output raw span with the specified byte count and alignment.
- [withUnsafeTemporaryAllocation(of:capacity:_:)](<withunsafetemporaryallocation(of_capacity___).md>) — Provides scoped access to a buffer pointer to memory of the specified type and with the specified capacity.
- [withUnsafeTemporaryAllocation(byteCount:alignment:_:)](<withunsafetemporaryallocation(bytecount_alignment___).md>) — Provides scoped access to a raw buffer pointer with the specified byte count and alignment.
- [swap(_:_:)](<swap(____).md>) — Exchanges the values of the two arguments.
- [exchange(_:with:)](<exchange(__with_).md>) — Replaces the value of a mutable value with the supplied new value, returning the original.
