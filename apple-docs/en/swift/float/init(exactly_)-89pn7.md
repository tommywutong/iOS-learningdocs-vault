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
doc_path: '/documentation/swift/float/init(exactly:)-89pn7'
source_url: 'https://developer.apple.com/documentation/swift/float/init(exactly:)-89pn7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/init%28exactly%3A%29-89pn7.json'
content_hash: 'sha256:c8c89c48a77dbe40'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# init(exactly:)

<sub>Initializer</sub>

Creates a new instance initialized to the given value, if it can be represented without rounding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(exactly other: Float)
```

## Parameters

- `other` — The value to use for the new instance.

## Discussion

If `other` can’t be represented as an instance of `Float` without rounding, the result of this initializer is `nil`. In particular, passing NaN as `other` always results in `nil`.

```swift
let x: Float = 21.25
let y = Float(exactly: x)
// y == Optional.some(21.25)

let z = Float(exactly: Float.nan)
// z == nil
```

## See Also

### Converting with No Loss of Precision

- [init(exactly:)](<init(exactly_)-8esr8.md>) — Creates a new instance from the given value, if it can be represented exactly.
- [init(exactly:)](<init(exactly_)-89na7.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-6l5fa.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-zknq.md>)
- [init(exactly:)](<init(exactly_)-1h1oe.md>) — Creates a new value, if the given integer can be represented exactly.
- [init(exactly:)](<init(exactly_)-8ho5q.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
