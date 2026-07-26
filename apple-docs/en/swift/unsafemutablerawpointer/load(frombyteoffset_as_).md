---
title: 'load(fromByteOffset:as:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablerawpointer/load(frombyteoffset:as:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawpointer/load(frombyteoffset:as:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawpointer/load%28frombyteoffset%3Aas%3A%29.json'
content_hash: 'sha256:bebc564dcbfabacd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawPointer](../unsafemutablerawpointer.md)

# load(fromByteOffset:as:)

<sub>Instance Method</sub>

Returns a new instance of the given type, constructed from the raw memory at the specified offset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func load<T>(fromByteOffset offset: Int = 0, as type: T.Type) -> T where T : ~Escapable
```

## Parameters

- `offset` — The offset from this pointer, in bytes. `offset` must be nonnegative. The default is zero.

- `type` — The type of the instance to create.

## Return Value

A new instance of type `T`, read from the raw bytes at `offset`. The returned instance is memory-managed and unassociated with the value in the memory referenced by this pointer.

## Discussion

The memory at this pointer plus `offset` must be properly aligned for accessing `T` and initialized to `T` or another type that is layout compatible with `T`.
