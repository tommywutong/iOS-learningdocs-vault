---
title: 'round(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float/round(_:)'
source_url: 'https://developer.apple.com/documentation/swift/float/round(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/round%28_%3A%29.json'
content_hash: 'sha256:fb8b35d2efd6c410'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# round(_:)

<sub>Instance Method</sub>

Rounds the value to an integral value using the specified rounding rule.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func round(_ rule: FloatingPointRoundingRule)
```

## Parameters

- `rule` — The rounding rule to use.

## Discussion

The following example rounds a value using four different rounding rules:

```swift
// Equivalent to the C 'round' function:
var w = 6.5
w.round(.toNearestOrAwayFromZero)
// w == 7.0

// Equivalent to the C 'trunc' function:
var x = 6.5
x.round(.towardZero)
// x == 6.0

// Equivalent to the C 'ceil' function:
var y = 6.5
y.round(.up)
// y == 7.0

// Equivalent to the C 'floor' function:
var z = 6.5
z.round(.down)
// z == 6.0
```

For more information about the available rounding rules, see the `FloatingPointRoundingRule` enumeration. To round a value using the default “schoolbook rounding” of `.toNearestOrAwayFromZero`, you can use the shorter `round()` method instead.

```swift
var w1 = 6.5
w1.round()
// w1 == 7.0
```

## See Also

### Rounding Values

- [rounded()](<rounded().md>)
- [rounded(_:)](<rounded(__).md>) — Returns this value rounded to an integral value using the specified rounding rule.
- [round()](<round().md>)
