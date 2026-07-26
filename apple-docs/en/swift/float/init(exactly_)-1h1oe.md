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
doc_path: '/documentation/swift/float/init(exactly:)-1h1oe'
source_url: 'https://developer.apple.com/documentation/swift/float/init(exactly:)-1h1oe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/init%28exactly%3A%29-1h1oe.json'
content_hash: 'sha256:e9938fa5c1bcb214'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# init(exactly:)

<sub>Initializer</sub>

Creates a new value, if the given integer can be represented exactly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?<Source>(exactly value: Source) where Source : BinaryInteger
```

## Parameters

- `value` — The integer to convert to a floating-point value.

## Discussion

If the given integer cannot be represented exactly, the result is `nil`.

## See Also

### Converting with No Loss of Precision

- [init(exactly:)](<init(exactly_)-8esr8.md>) — Creates a new instance from the given value, if it can be represented exactly.
- [init(exactly:)](<init(exactly_)-89na7.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-89pn7.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-6l5fa.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-zknq.md>)
- [init(exactly:)](<init(exactly_)-8ho5q.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
