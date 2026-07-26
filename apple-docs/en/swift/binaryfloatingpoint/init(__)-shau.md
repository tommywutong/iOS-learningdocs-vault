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
doc_path: '/documentation/swift/binaryfloatingpoint/init(_:)-shau'
source_url: 'https://developer.apple.com/documentation/swift/binaryfloatingpoint/init(_:)-shau'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryfloatingpoint/init%28_%3A%29-shau.json'
content_hash: 'sha256:fd0f85403e069d96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryFloatingPoint](../binaryfloatingpoint.md)

# init(_:)

<sub>Initializer</sub>

Creates a new instance from the given value, rounded to the closest possible representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Source>(_ value: Source) where Source : BinaryFloatingPoint
```

## Parameters

- `value` — A floating-point value to be converted.

## Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.

## Default Implementations

### BinaryFloatingPoint Implementations

- [init(_:)](<init(__)-17tah.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](<init(__)-5p0og.md>) — Creates a new value, rounded to the closest possible representation.

## See Also

### Converting Floating-Point Values

- [init(_:)](<init(__)-57jx7.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](<init(__)-7ft14.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
- [init(_:)](<init(__)-1nijh.md>) — Creates a new instance from the given value, rounded to the closest possible representation.
