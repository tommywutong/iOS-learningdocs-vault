---
title: nan
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/nan
source_url: 'https://developer.apple.com/documentation/swift/float16/nan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/nan.json'
content_hash: 'sha256:a71100aa13e3a90f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# nan

<sub>Type Property</sub>

A quiet NaN (“not a number”).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var nan: Float16 { get }
```

## Discussion

A NaN compares not equal, not greater than, and not less than every value, including itself. Passing a NaN to an operation generally results in NaN.

```swift
let x = 1.21
// x > Double.nan == false
// x < Double.nan == false
// x == Double.nan == false
```

Because a NaN always compares not equal to itself, to test whether a floating-point value is NaN, use its `isNaN` property instead of the equal-to operator (`==`). In the following example, `y` is NaN.

```swift
let y = x + Double.nan
print(y == Double.nan)
// Prints "false"
print(y.isNaN)
// Prints "true"
```
