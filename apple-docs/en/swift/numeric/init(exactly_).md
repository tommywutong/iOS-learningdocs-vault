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
doc_path: '/documentation/swift/numeric/init(exactly:)'
source_url: 'https://developer.apple.com/documentation/swift/numeric/init(exactly:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/numeric/init%28exactly%3A%29.json'
content_hash: 'sha256:2b30a9bf61a8d30d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Numeric](../numeric.md)

# init(exactly:)

<sub>Initializer</sub>

Creates a new instance from the given integer, if it can be represented exactly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?<T>(exactly source: T) where T : BinaryInteger
```

## Parameters

- `source` — A value to convert to this type.

## Discussion

If the value passed as `source` is not representable exactly, the result is `nil`. In the following example, the constant `x` is successfully created from a value of `100`, while the attempt to initialize the constant `y` from `1_000` fails because the `Int8` type can represent `127` at maximum:

```swift
let x = Int8(exactly: 100)
// x == Optional(100)
let y = Int8(exactly: 1_000)
// y == nil
```

## Default Implementations

### BinaryFloatingPoint Implementations

- [init(exactly:)](<../binaryfloatingpoint/init(exactly_)-6fobm.md>) — Creates a new instance from the given value, if it can be represented exactly.
- [init(exactly:)](<../binaryfloatingpoint/init(exactly_)-9lyid.md>) — Creates a new value, if the given integer can be represented exactly.

### Numeric Implementations

- [init(exactly:)](<init(exactly_)-1dg3p.md>)
- [init(exactly:)](<init(exactly_)-8briw.md>)
- [init(exactly:)](<init(exactly_)-uz93.md>)
