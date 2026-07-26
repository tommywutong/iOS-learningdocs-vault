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
doc_path: '/documentation/swift/float80/init(exactly:)-6kkqt'
source_url: 'https://developer.apple.com/documentation/swift/float80/init(exactly:)-6kkqt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/init%28exactly%3A%29-6kkqt.json'
content_hash: 'sha256:fcf4946db065ea88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# init(exactly:)

<sub>Initializer</sub>

Creates a new instance initialized to the given value, if it can be represented without rounding.

<sub>macOS</sub>

```swift
init?(exactly other: Float)
```

## Parameters

- `other` — The value to use for the new instance.

## Discussion

If `other` can’t be represented as an instance of `Float80` without rounding, the result of this initializer is `nil`. In particular, passing NaN as `other` always results in `nil`.

```swift
let x: Float = 21.25
let y = Float80(exactly: x)
// y == Optional.some(21.25)

let z = Float80(exactly: Float.nan)
// z == nil
```
