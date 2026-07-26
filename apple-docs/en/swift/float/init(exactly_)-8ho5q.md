---
title: 'init(exactly:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float/init(exactly:)-8ho5q'
source_url: 'https://developer.apple.com/documentation/swift/float/init(exactly:)-8ho5q'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/init%28exactly%3A%29-8ho5q.json'
content_hash: 'sha256:aa154f39418dd27b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# init(exactly:)

<sub>Initializer</sub>

Creates a new instance initialized to the given value, if it can be represented without rounding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(exactly other: Float16)
```

## Parameters

- `other` — The value to use for the new instance.

## Discussion

If `other` can’t be represented as an instance of `Float` without rounding, the result of this initializer is `nil`. In particular, passing NaN as `other` always results in `nil`.

```swift
let x: Float16 = 21.25
let y = Float(exactly: x)
// y == Optional.some(21.25)

let z = Float(exactly: Float16.nan)
// z == nil
```

## See Also

### Converting with No Loss of Precision

- [init(exactly:)](<init(exactly_)-8esr8.md>) — Creates a new instance from the given value, if it can be represented exactly.
- [init(exactly:)](<init(exactly_)-89na7.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-89pn7.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-6l5fa.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-zknq.md>)
- [init(exactly:)](<init(exactly_)-1h1oe.md>) — Creates a new value, if the given integer can be represented exactly.
