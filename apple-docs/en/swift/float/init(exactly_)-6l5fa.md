---
title: 'init(exactly:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float/init(exactly:)-6l5fa'
source_url: 'https://developer.apple.com/documentation/swift/float/init(exactly:)-6l5fa'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/init%28exactly%3A%29-6l5fa.json'
content_hash: 'sha256:a8433e4a892b659e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

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

If `other` can’t be represented as an instance of `Float` without rounding, the result of this initializer is `nil`. In particular, passing NaN as `other` always results in `nil`.

```swift
let x: Float80 = 21.25
let y = Float(exactly: x)
// y == Optional.some(21.25)

let z = Float(exactly: Float80.nan)
// z == nil
```

## See Also

### Converting with No Loss of Precision

- [init(exactly:)](<init(exactly_)-8esr8.md>) — Creates a new instance from the given value, if it can be represented exactly.
- [init(exactly:)](<init(exactly_)-89na7.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-89pn7.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-zknq.md>)
- [init(exactly:)](<init(exactly_)-1h1oe.md>) — Creates a new value, if the given integer can be represented exactly.
- [init(exactly:)](<init(exactly_)-8ho5q.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
