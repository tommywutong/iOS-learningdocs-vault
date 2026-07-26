---
title: 'unsafeLoadUnaligned(fromByteOffset:as:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rawspan/unsafeloadunaligned(frombyteoffset:as:)'
source_url: 'https://developer.apple.com/documentation/swift/rawspan/unsafeloadunaligned(frombyteoffset:as:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rawspan/unsafeloadunaligned%28frombyteoffset%3Aas%3A%29.json'
content_hash: 'sha256:02a40cd37e7e73c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RawSpan](../rawspan.md)

# unsafeLoadUnaligned(fromByteOffset:as:)

<sub>Instance Method</sub>

Returns a new instance of the given type, constructed from the raw memory at the specified offset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func unsafeLoadUnaligned<T>(fromByteOffset offset: Int = 0, as type: T.Type) -> T where T : BitwiseCopyable
```

## Parameters

- `offset` — The offset from this pointer, in bytes. `offset` must be nonnegative. The default is zero.

- `type` — The type of the instance to create.

## Return Value

A new instance of type `T`, read from the raw bytes at `offset`. The returned instance isn’t associated with the value in the range of memory referenced by this pointer.

## Discussion

The memory at this pointer plus `offset` must be initialized to `T` or another type that is layout compatible with `T`.

This is an unsafe operation. Failure to meet the preconditions above may produce an invalid value of `T`.
