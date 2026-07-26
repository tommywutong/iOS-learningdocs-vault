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
doc_path: '/documentation/swift/uint16/init(bitpattern:)'
source_url: 'https://developer.apple.com/documentation/swift/uint16/init(bitpattern:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint16/init%28bitpattern%3A%29.json'
content_hash: 'sha256:9fa0f081654a0574'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt16](../uint16.md)

# init(bitPattern:)

<sub>Initializer</sub>

Creates a new instance with the same memory representation as the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bitPattern x: Int16)
```

## Parameters

- `x` — A value to use as the source of the new instance’s binary representation.

## Discussion

This initializer does not perform any range or overflow checking. The resulting instance may not have the same numeric value as `bitPattern`—it is only guaranteed to use the same pattern of bits in its binary representation.
