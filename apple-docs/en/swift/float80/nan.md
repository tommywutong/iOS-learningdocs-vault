---
title: nan
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/nan
source_url: 'https://developer.apple.com/documentation/swift/float80/nan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/nan.json'
content_hash: 'sha256:87d0c8173ffec22d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# nan

<sub>Type Property</sub>

A quiet NaN (“not a number”).

<sub>macOS</sub>

```swift
static var nan: Float80 { get }
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
