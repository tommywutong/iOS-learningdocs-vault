---
title: 'init(exactly:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/double/init(exactly:)-2l6p1'
source_url: 'https://developer.apple.com/documentation/swift/double/init(exactly:)-2l6p1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/init%28exactly%3A%29-2l6p1.json'
content_hash: 'sha256:769ac79d77b7c6b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# init(exactly:)

<sub>Initializer</sub>

Creates a new instance initialized to the given value, if it can be represented without rounding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(exactly other: Double)
```

## Parameters

- `other` — The value to use for the new instance.

## Discussion

If `other` can’t be represented as an instance of `Double` without rounding, the result of this initializer is `nil`. In particular, passing NaN as `other` always results in `nil`.

```swift
let x: Double = 21.25
let y = Double(exactly: x)
// y == Optional.some(21.25)

let z = Double(exactly: Double.nan)
// z == nil
```

## See Also

### Converting with No Loss of Precision

- [init(exactly:)](<init(exactly_)-8esra.md>) — Creates a new instance from the given value, if it can be represented exactly.
- [init(exactly:)](<init(exactly_)-1h1oc.md>) — Creates a new value, if the given integer can be represented exactly.
- [init(exactly:)](<init(exactly_)-2uexo.md>) — Creates a new value, if the given integer can be represented exactly.
- [init(exactly:)](<init(exactly_)-7cl0t.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-50ofc.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-63925.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-8e00y.md>)
