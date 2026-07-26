---
title: 'init(bitPattern:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float16/init(bitpattern:)'
source_url: 'https://developer.apple.com/documentation/swift/float16/init(bitpattern:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/init%28bitpattern%3A%29.json'
content_hash: 'sha256:e2ec66c29c2dc0c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# init(bitPattern:)

<sub>Initializer</sub>

Creates a new value with the given bit pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bitPattern: UInt16)
```

## Parameters

- `bitPattern` — The integer encoding of a `Float16` instance.

## Discussion

The value passed as `bitPattern` is interpreted in the binary interchange format defined by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).
