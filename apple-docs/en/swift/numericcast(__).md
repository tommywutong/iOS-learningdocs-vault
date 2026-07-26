---
title: 'numericCast(_:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/numericcast(_:)'
source_url: 'https://developer.apple.com/documentation/swift/numericcast(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/numericcast%28_%3A%29.json'
content_hash: 'sha256:bf2069759daca35b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# numericCast(_:)

<sub>Function</sub>

Returns the given integer as the equivalent value in a different integer type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func numericCast<T, U>(_ x: T) -> U where T : BinaryInteger, U : BinaryInteger
```

## Parameters

- `x` — The integer to convert, an instance of type `T`.

## Return Value

The value of `x` converted to type `U`.

## Discussion

Calling the `numericCast(_:)` function is equivalent to calling an initializer for the destination type. `numericCast(_:)` traps on overflow in `-O` and `-Onone` builds.
