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
doc_path: '/documentation/swift/binaryinteger/init(_:)-2ln0u'
source_url: 'https://developer.apple.com/documentation/swift/binaryinteger/init(_:)-2ln0u'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryinteger/init%28_%3A%29-2ln0u.json'
content_hash: 'sha256:cf8c072f6b82c0c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryInteger](../binaryinteger.md)

# init(_:)

<sub>Initializer</sub>

Creates an integer from the given floating-point value, rounding toward zero.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T>(_ source: T) where T : BinaryFloatingPoint
```

## Parameters

- `source` — A floating-point value to convert to an integer. `source` must be representable in this type after rounding toward zero.

## Discussion

Any fractional part of the value passed as `source` is removed, rounding the value toward zero.

```swift
let x = Int(21.5)
// x == 21
let y = Int(-21.5)
// y == -21
```

If `source` is outside the bounds of this type after rounding toward zero, a runtime error may occur.

```swift
let z = UInt(-21.5)
// Error: ...the result would be less than UInt.min
```

## Default Implementations

### BinaryInteger Implementations

- [init(_:)](<init(__)-3cx61.md>) — Creates a new integer value from the given string.
- [init(_:)](<init(__)-5yrn0.md>) — Creates a new instance from the given integer.
- [init(_:)](<init(__)-62cdc.md>)
- [init(_:)](<init(__)-6u4mr.md>) — Creates a new instance from the given integer.

### FixedWidthInteger Implementations

- [init(_:)](<../fixedwidthinteger/init(__).md>) — Convert from an Backtrace.Address.
