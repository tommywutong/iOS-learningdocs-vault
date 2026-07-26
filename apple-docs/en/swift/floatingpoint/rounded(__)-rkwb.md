---
title: 'rounded(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/floatingpoint/rounded(_:)-rkwb'
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/rounded(_:)-rkwb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/rounded%28_%3A%29-rkwb.json'
content_hash: 'sha256:9037fc31cf6e09b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# rounded(_:)

<sub>Instance Method</sub>

Returns this value rounded to an integral value using the specified rounding rule.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func rounded(_ rule: FloatingPointRoundingRule) -> Self
```

## Parameters

- `rule` — The rounding rule to use.

## Return Value

The integral value found by rounding using `rule`.

## Discussion

The following example rounds a value using four different rounding rules:

```swift
let x = 6.5

// Equivalent to the C 'round' function:
print(x.rounded(.toNearestOrAwayFromZero))
// Prints "7.0"

// Equivalent to the C 'trunc' function:
print(x.rounded(.towardZero))
// Prints "6.0"

// Equivalent to the C 'ceil' function:
print(x.rounded(.up))
// Prints "7.0"

// Equivalent to the C 'floor' function:
print(x.rounded(.down))
// Prints "6.0"
```

For more information about the available rounding rules, see the `FloatingPointRoundingRule` enumeration. To round a value using the default “schoolbook rounding” of `.toNearestOrAwayFromZero`, you can use the shorter `rounded()` method instead.

```swift
print(x.rounded())
// Prints "7.0"
```
