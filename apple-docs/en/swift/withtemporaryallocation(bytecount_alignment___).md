---
title: 'withTemporaryAllocation(byteCount:alignment:_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/withtemporaryallocation(bytecount:alignment:_:)'
source_url: 'https://developer.apple.com/documentation/swift/withtemporaryallocation(bytecount:alignment:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/withtemporaryallocation%28bytecount%3Aalignment%3A_%3A%29.json'
content_hash: 'sha256:9ac8885adb404bb4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# withTemporaryAllocation(byteCount:alignment:_:)

<sub>Function</sub>

Provides scoped access to an output raw span with the specified byte count and alignment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withTemporaryAllocation<R, E>(byteCount: Int, alignment: Int, _ body: @_lifetime(0: copy 0) (inout OutputRawSpan) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

## Parameters

- `byteCount` — The number of bytes to temporarily allocate. `byteCount` must not be negative.

- `alignment` — The alignment of the new, temporary region of allocated memory, in bytes. `alignment` must be a whole power of 2.

- `body` — A closure to invoke and to which the allocated output raw span should be passed.

## Return Value

Whatever is returned by `body`.

## Discussion

This function is useful for cheaply allocating raw storage for a brief duration. Storage may be allocated on the heap or on the stack, depending on the required size and alignment.

When `body` is called, it is passed an empty `OutputRawSpan`. `body` may append bytes to the output raw span. After `body` returns, deallocation is automatic.

> [!danger] Throws
> Whatever is thrown by `body`.

## See Also

### Memory Access

- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-9fjn6.md>) — Invokes the given closure with a pointer to the given argument.
- [withUnsafePointer(to:_:)](<withunsafepointer(to___)-35wrn.md>) — Invokes the given closure with a pointer to the given argument.
- [withUnsafeMutablePointer(to:_:)](<withunsafemutablepointer(to___).md>) — Calls the given closure with a mutable pointer to the given argument.
- [withUnsafeBytes(of:_:)](<withunsafebytes(of___)-3ywhh.md>) — Invokes the given closure with a buffer pointer covering the raw bytes of the given argument.
- [withUnsafeMutableBytes(of:_:)](<withunsafemutablebytes(of___).md>) — Invokes the given closure with a mutable buffer pointer covering the raw bytes of the given argument.
- [withTemporaryAllocation(of:capacity:_:)](<withtemporaryallocation(of_capacity___).md>) — Provides scoped access to an output span of the specified type and capacity.
- [withUnsafeTemporaryAllocation(of:capacity:_:)](<withunsafetemporaryallocation(of_capacity___).md>) — Provides scoped access to a buffer pointer to memory of the specified type and with the specified capacity.
- [withUnsafeTemporaryAllocation(byteCount:alignment:_:)](<withunsafetemporaryallocation(bytecount_alignment___).md>) — Provides scoped access to a raw buffer pointer with the specified byte count and alignment.
- [swap(_:_:)](<swap(____).md>) — Exchanges the values of the two arguments.
- [exchange(_:with:)](<exchange(__with_).md>) — Replaces the value of a mutable value with the supplied new value, returning the original.
