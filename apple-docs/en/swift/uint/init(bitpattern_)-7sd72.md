---
title: 'init(bitPattern:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint/init(bitpattern:)-7sd72'
source_url: 'https://developer.apple.com/documentation/swift/uint/init(bitpattern:)-7sd72'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint/init%28bitpattern%3A%29-7sd72.json'
content_hash: 'sha256:3c4a0ae4c64d4411'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt](../uint.md)

# init(bitPattern:)

<sub>Initializer</sub>

Creates a new value with the bit pattern of the given pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bitPattern pointer: OpaquePointer?)
```

## Parameters

- `pointer` — The pointer to use as the source for the new integer.

## Discussion

The new value represents the address of the pointer passed as `pointer`. If `pointer` is `nil`, the result is `0`.
