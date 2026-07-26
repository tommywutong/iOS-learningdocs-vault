---
title: 'quotientAndRemainder(dividingBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint16/quotientandremainder(dividingby:)'
source_url: 'https://developer.apple.com/documentation/swift/uint16/quotientandremainder(dividingby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint16/quotientandremainder%28dividingby%3A%29.json'
content_hash: 'sha256:3b84d5771b0c7be5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt16](../uint16.md)

# quotientAndRemainder(dividingBy:)

<sub>Instance Method</sub>

Returns the quotient and remainder of this value divided by the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func quotientAndRemainder(dividingBy rhs: Self) -> (quotient: Self, remainder: Self)
```

## Parameters

- `rhs` — The value to divide this value by.

## Return Value

A tuple containing the quotient and remainder of this value divided by `rhs`. The remainder has the same sign as `lhs`.

## Discussion

Use this method to calculate the quotient and remainder of a division at the same time.

```swift
let x = 1_000_000
let (q, r) = x.quotientAndRemainder(dividingBy: 933)
// q == 1071
// r == 757
```
