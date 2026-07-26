---
title: 'init(sign:exponentBitPattern:significandBitPattern:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/init(sign:exponentbitpattern:significandbitpattern:)'
source_url: 'https://developer.apple.com/documentation/swift/float80/init(sign:exponentbitpattern:significandbitpattern:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/init%28sign%3Aexponentbitpattern%3Asignificandbitpattern%3A%29.json'
content_hash: 'sha256:f360cf9a6e94a545'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# init(sign:exponentBitPattern:significandBitPattern:)

<sub>Initializer</sub>

Creates a new instance from the specified sign and bit patterns.

<sub>macOS</sub>

```swift
init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt64)
```

## Parameters

- `sign` — The sign of the new value.

- `exponentBitPattern` — The bit pattern to use for the exponent field of the new value.

- `significandBitPattern` — The bit pattern to use for the significand field of the new value.

## Discussion

The values passed as `exponentBitPattern` and `significandBitPattern` are interpreted in the binary interchange format defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).
