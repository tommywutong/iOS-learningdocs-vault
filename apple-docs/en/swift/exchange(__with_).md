---
title: 'exchange(_:with:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/exchange(_:with:)'
source_url: 'https://developer.apple.com/documentation/swift/exchange(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/exchange%28_%3Awith%3A%29.json'
content_hash: 'sha256:ce7547d231bd7cfc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# exchange(_:with:)

<sub>Function</sub>

Replaces the value of a mutable value with the supplied new value, returning the original.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func exchange<T>(_ item: inout T, with newValue: consuming T) -> T where T : ~Copyable
```

## Parameters

- `item` — A mutable binding.

- `newValue` — The new value of `item`.

## Return Value

The original value of `item`.

## See Also

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
