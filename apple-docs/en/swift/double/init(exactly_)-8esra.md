---
title: 'init(exactly:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/double/init(exactly:)-8esra'
source_url: 'https://developer.apple.com/documentation/swift/double/init(exactly:)-8esra'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/init%28exactly%3A%29-8esra.json'
content_hash: 'sha256:9131a23c982b9f06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# init(exactly:)

<sub>Initializer</sub>

Creates a new instance from the given value, if it can be represented exactly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?<Source>(exactly value: Source) where Source : BinaryFloatingPoint
```

## Parameters

- `value` — A floating-point value to be converted.

## Discussion

If the given floating-point value cannot be represented exactly, the result is `nil`.

## See Also

### Converting with No Loss of Precision

- [init(exactly:)](<init(exactly_)-1h1oc.md>) — Creates a new value, if the given integer can be represented exactly.
- [init(exactly:)](<init(exactly_)-2uexo.md>) — Creates a new value, if the given integer can be represented exactly.
- [init(exactly:)](<init(exactly_)-2l6p1.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-7cl0t.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-50ofc.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-63925.md>) — Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init(exactly:)](<init(exactly_)-8e00y.md>)
