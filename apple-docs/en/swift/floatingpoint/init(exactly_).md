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
doc_path: '/documentation/swift/floatingpoint/init(exactly:)'
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/init(exactly:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/init%28exactly%3A%29.json'
content_hash: 'sha256:74a0a39632a18c93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

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

## Default Implementations

### BinaryFloatingPoint Implementations

- [init(exactly:)](<../binaryfloatingpoint/init(exactly_)-6fobm.md>) — Creates a new instance from the given value, if it can be represented exactly.
- [init(exactly:)](<../binaryfloatingpoint/init(exactly_)-9lyid.md>) — Creates a new value, if the given integer can be represented exactly.
