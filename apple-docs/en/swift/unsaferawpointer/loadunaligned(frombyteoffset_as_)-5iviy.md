---
title: 'loadUnaligned(fromByteOffset:as:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsaferawpointer/loadunaligned(frombyteoffset:as:)-5iviy'
source_url: 'https://developer.apple.com/documentation/swift/unsaferawpointer/loadunaligned(frombyteoffset:as:)-5iviy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawpointer/loadunaligned%28frombyteoffset%3Aas%3A%29-5iviy.json'
content_hash: 'sha256:7b549af5deb03934'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeRawPointer](../unsaferawpointer.md)

# loadUnaligned(fromByteOffset:as:)

<sub>Instance Method</sub>

Returns a new instance of the given type, constructed from the raw memory at the specified offset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func loadUnaligned<T>(fromByteOffset offset: Int = 0, as type: T.Type) -> T where T : BitwiseCopyable, T : ~Escapable
```

## Parameters

- `offset` — The offset from this pointer, in bytes. `offset` must be nonnegative. The default is zero.

- `type` — The type of the instance to create.

## Return Value

A new instance of type `T`, read from the raw bytes at `offset`. The returned instance isn’t associated with the value in the range of memory referenced by this pointer.

## Discussion

This function only supports loading trivial types, and will trap if this precondition is not met. A trivial type does not contain any reference-counted property within its in-memory representation. The memory at this pointer plus `offset` must be laid out identically to the in-memory representation of `T`.

> [!note] Note
> A trivial type can be copied with just a bit-for-bit copy without any indirection or reference-counting operations. Generally, native Swift types that do not contain strong or weak references or other forms of indirection are trivial, as are imported C structs and enums.
