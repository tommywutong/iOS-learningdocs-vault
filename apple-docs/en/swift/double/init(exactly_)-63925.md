---
title: 'init(exactly:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/double/init(exactly:)-63925'
source_url: 'https://developer.apple.com/documentation/swift/double/init(exactly:)-63925'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/init%28exactly%3A%29-63925.json'
content_hash: 'sha256:f179f740576a4fbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# init(exactly:)

<sub>Initializer</sub>

Creates a new instance initialized to the given value, if it can be represented without rounding.

<sub>macOS</sub>

```swift
init?(exactly other: Float80)
```

## Parameters

- `other` — The value to use for the new instance.

## Discussion

If `other` can’t be represented as an instance of `Double` without rounding, the result of this initializer is `nil`. In particular, passing NaN as `other` always results in `nil`.

```swift
let x: Float80 = 21.25
let y = Double(exactly: x)
// y == Optional.some(21.25)

let z = Double(exactly: Float80.nan)
// z == nil
```

## See Also

### Converting with No Loss of Precision

- [init(exactly:)](<init(exactly_)-8esra.md>) — Creates a new instance from the given value, if it can be represented exactly.
- [init(exactly:)](<init(exactly_)-1h1oc.md>) — Creates a new value, if the given integer can be represented exactly.
- [init(exactly:)](<init(exactly_)-2uexo.md>) — Creates a new value, if the given integer can be represented exactly.
- [init(exactly:)](<init(exactly_)-2l6p1.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-7cl0t.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-50ofc.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-8e00y.md>)
