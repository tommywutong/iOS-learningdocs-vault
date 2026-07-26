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
doc_path: '/documentation/swift/float16/init(exactly:)-27ijx'
source_url: 'https://developer.apple.com/documentation/swift/float16/init(exactly:)-27ijx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/init%28exactly%3A%29-27ijx.json'
content_hash: 'sha256:a6032566bddbe83d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

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

If `other` can’t be represented as an instance of `Float16` without rounding, the result of this initializer is `nil`. In particular, passing NaN as `other` always results in `nil`.

```swift
let x: Float16 = 21.25
let y = Float16(exactly: x)
// y == Optional.some(21.25)

let z = Float16(exactly: Float16.nan)
// z == nil
```
