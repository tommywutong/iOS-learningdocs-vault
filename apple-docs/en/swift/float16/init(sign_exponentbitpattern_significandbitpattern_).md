---
title: 'init(sign:exponentBitPattern:significandBitPattern:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float16/init(sign:exponentbitpattern:significandbitpattern:)'
source_url: 'https://developer.apple.com/documentation/swift/float16/init(sign:exponentbitpattern:significandbitpattern:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/init%28sign%3Aexponentbitpattern%3Asignificandbitpattern%3A%29.json'
content_hash: 'sha256:0c66d12d28d251c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# init(sign:exponentBitPattern:significandBitPattern:)

<sub>Initializer</sub>

Creates a new instance from the specified sign and bit patterns.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt16)
```

## Parameters

- `sign` — The sign of the new value.

- `exponentBitPattern` — The bit pattern to use for the exponent field of the new value.

- `significandBitPattern` — The bit pattern to use for the significand field of the new value.

## Discussion

The values passed as `exponentBitPattern` and `significandBitPattern` are interpreted in the binary interchange format defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).
