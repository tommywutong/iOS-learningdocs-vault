---
title: 'raising(toPower:withBehavior:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalnumber/raising(topower:withbehavior:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/raising(topower:withbehavior:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/raising%28topower%3Awithbehavior%3A%29.json'
content_hash: 'sha256:1eb6288372a9d4be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumber](../nsdecimalnumber.md)

# raising(toPower:withBehavior:)

<sub>Instance Method</sub>

Raises the number to a given power using the specified behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func raising(toPower power: Int, withBehavior behavior: (any NSDecimalNumberBehaviors)?) -> NSDecimalNumber
```

## Discussion

`behavior` specifies the handling of calculation errors and rounding.

## See Also

### Performing Arithmetic

- [- decimalNumberByAdding:](<adding(__).md>) — Adds this number to another given number.
- [- decimalNumberBySubtracting:](<subtracting(__).md>) — Subtracts another given number from this one.
- [- decimalNumberByMultiplyingBy:](<multiplying(by_).md>) — Multiplies the number by another given number.
- [- decimalNumberByDividingBy:](<dividing(by_).md>) — Divides the number by another given number.
- [- decimalNumberByRaisingToPower:](<raising(topower_).md>) — Raises the number to a given power.
- [- decimalNumberByMultiplyingByPowerOf10:](<multiplying(bypowerof10_).md>) — Multiplies the number by 10 raised to the given power.
- [- decimalNumberByAdding:withBehavior:](<adding(__withbehavior_).md>) — Adds this number to another given number using the specified behavior.
- [- decimalNumberBySubtracting:withBehavior:](<subtracting(__withbehavior_).md>) — Subtracts this a given number from this one using the specified behavior.
- [- decimalNumberByMultiplyingBy:withBehavior:](<multiplying(by_withbehavior_).md>) — Multiplies this number by another given number using the specified behavior.
- [- decimalNumberByDividingBy:withBehavior:](<dividing(by_withbehavior_).md>) — Divides this number by another given number using the specified behavior.
- [- decimalNumberByMultiplyingByPowerOf10:withBehavior:](<multiplying(bypowerof10_withbehavior_).md>) — Multiplies the number by 10 raised to the given power using the specified behavior.
