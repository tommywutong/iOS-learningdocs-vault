---
title: 'init(exactly:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int8/init(exactly:)-6zkv6'
source_url: 'https://developer.apple.com/documentation/swift/int8/init(exactly:)-6zkv6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int8/init%28exactly%3A%29-6zkv6.json'
content_hash: 'sha256:e7e7e8fff07d05d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int8](../int8.md)

# init(exactly:)

<sub>Initializer</sub>

Creates an integer from the given floating-point value, if it can be represented exactly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(exactly source: Float)
```

## Parameters

- `source` — A floating-point value to convert to an integer.

## Discussion

If the value passed as `source` is not representable exactly, the result is `nil`. In the following example, the constant `x` is successfully created from a value of `21.0`, while the attempt to initialize the constant `y` from `21.5` fails:

```swift
let x = Int(exactly: 21.0)
// x == Optional(21)
let y = Int(exactly: 21.5)
// y == nil
```
