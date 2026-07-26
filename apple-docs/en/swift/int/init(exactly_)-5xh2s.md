---
title: 'init(exactly:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int/init(exactly:)-5xh2s'
source_url: 'https://developer.apple.com/documentation/swift/int/init(exactly:)-5xh2s'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/init%28exactly%3A%29-5xh2s.json'
content_hash: 'sha256:cf47768b8cc73b1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# init(exactly:)

<sub>Initializer</sub>

Creates an integer from the given floating-point value, if it can be represented exactly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(exactly source: Float16)
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

## See Also

### Converting with No Loss of Precision

- [init(exactly:)](<init(exactly_)-7yhn6.md>)
- [init(exactly:)](<init(exactly_)-77kq8.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<init(exactly_)-7qdwf.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(exactly:)](<init(exactly_)-5kot1.md>) — Creates an integer from the given floating-point value, if it can be represented exactly.
