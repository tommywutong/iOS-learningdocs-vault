---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/floatingpoint/init(_:)-2xwlo'
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/init(_:)-2xwlo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/init%28_%3A%29-2xwlo.json'
content_hash: 'sha256:d682ff4e8cf023b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# init(_:)

<sub>Initializer</sub>

Creates a new value, rounded to the closest possible representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ value: Int)
```

## Parameters

- `value` — The integer to convert to a floating-point value.

## Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.

## Default Implementations

### BinaryFloatingPoint Implementations

- [init(_:)](<../binaryfloatingpoint/init(__)-17tah.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](<../binaryfloatingpoint/init(__)-5p0og.md>) — Creates a new value, rounded to the closest possible representation.
