---
title: 'subtracting(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalnumber/subtracting(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/subtracting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/subtracting%28_%3A%29.json'
content_hash: 'sha256:e1c572f157e68636'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumber](../nsdecimalnumber.md)

# subtracting(_:)

<sub>Instance Method</sub>

Subtracts another given number from this one.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subtracting(_ decimalNumber: NSDecimalNumber) -> NSDecimalNumber
```

## Parameters

- `decimalNumber` — The number to subtract from the receiver.

## Return Value

A new `NSDecimalNumber` object whose value is `decimalNumber` subtracted from the receiver.

## Discussion

This method uses the default behavior when handling calculation errors and when rounding.

## See Also

### Related Documentation

- [defaultBehavior](defaultbehavior.md) — The way arithmetic methods round off and handle error conditions.

### Performing Arithmetic

- [- decimalNumberByAdding:](<adding(__).md>) — Adds this number to another given number.
- [- decimalNumberByMultiplyingBy:](<multiplying(by_).md>) — Multiplies the number by another given number.
- [- decimalNumberByDividingBy:](<dividing(by_).md>) — Divides the number by another given number.
- [- decimalNumberByRaisingToPower:](<raising(topower_).md>) — Raises the number to a given power.
- [- decimalNumberByMultiplyingByPowerOf10:](<multiplying(bypowerof10_).md>) — Multiplies the number by 10 raised to the given power.
- [- decimalNumberByAdding:withBehavior:](<adding(__withbehavior_).md>) — Adds this number to another given number using the specified behavior.
- [- decimalNumberBySubtracting:withBehavior:](<subtracting(__withbehavior_).md>) — Subtracts this a given number from this one using the specified behavior.
- [- decimalNumberByMultiplyingBy:withBehavior:](<multiplying(by_withbehavior_).md>) — Multiplies this number by another given number using the specified behavior.
- [- decimalNumberByDividingBy:withBehavior:](<dividing(by_withbehavior_).md>) — Divides this number by another given number using the specified behavior.
- [- decimalNumberByRaisingToPower:withBehavior:](<raising(topower_withbehavior_).md>) — Raises the number to a given power using the specified behavior.
- [- decimalNumberByMultiplyingByPowerOf10:withBehavior:](<multiplying(bypowerof10_withbehavior_).md>) — Multiplies the number by 10 raised to the given power using the specified behavior.
