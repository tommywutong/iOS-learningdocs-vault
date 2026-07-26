---
title: 'unsafeLoad(fromByteOffset:as:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rawspan/unsafeload(frombyteoffset:as:)'
source_url: 'https://developer.apple.com/documentation/swift/rawspan/unsafeload(frombyteoffset:as:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawspan/unsafeload%28frombyteoffset%3Aas%3A%29.json'
content_hash: 'sha256:46bcbbd9b467886d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RawSpan](../rawspan.md)

# unsafeLoad(fromByteOffset:as:)

<sub>Instance Method</sub>

Returns a new instance of the given type, constructed from the raw memory at the specified offset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func unsafeLoad<T>(fromByteOffset offset: Int = 0, as type: T.Type) -> T
```

## Parameters

- `offset` — The offset from this pointer, in bytes. `offset` must be nonnegative. The default is zero.

- `type` — The type of the instance to create.

## Return Value

A new instance of type `T`, read from the raw bytes at `offset`. The returned instance is memory-managed and unassociated with the value in the memory referenced by this pointer.

## Discussion

The memory at this pointer plus `offset` must be properly aligned for accessing `T` and initialized to `T` or another type that is layout compatible with `T`.

This is an unsafe operation. Failure to meet the preconditions above may produce an invalid value of `T`.
