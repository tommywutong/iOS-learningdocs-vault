---
title: 'multiplying(byPowerOf10:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdecimalnumber/multiplying(bypowerof10:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/multiplying(bypowerof10:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/multiplying%28bypowerof10%3A%29.json'
content_hash: 'sha256:f722ece2c136abf9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDecimalNumber](../nsdecimalnumber.md)

# multiplying(byPowerOf10:)

<sub>Instance Method</sub>

Multiplies the number by 10 raised to the given power.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func multiplying(byPowerOf10 power: Int16) -> NSDecimalNumber
```

## Discussion

This method uses the default behavior when handling calculation errors and when rounding.

## See Also

### Related Documentation

- [defaultBehavior](defaultbehavior.md) — The way arithmetic methods round off and handle error conditions.

### Performing Arithmetic

- [- decimalNumberByAdding:](<adding(__).md>) — Adds this number to another given number.
- [- decimalNumberBySubtracting:](<subtracting(__).md>) — Subtracts another given number from this one.
- [- decimalNumberByMultiplyingBy:](<multiplying(by_).md>) — Multiplies the number by another given number.
- [- decimalNumberByDividingBy:](<dividing(by_).md>) — Divides the number by another given number.
- [- decimalNumberByRaisingToPower:](<raising(topower_).md>) — Raises the number to a given power.
- [- decimalNumberByAdding:withBehavior:](<adding(__withbehavior_).md>) — Adds this number to another given number using the specified behavior.
- [- decimalNumberBySubtracting:withBehavior:](<subtracting(__withbehavior_).md>) — Subtracts this a given number from this one using the specified behavior.
- [- decimalNumberByMultiplyingBy:withBehavior:](<multiplying(by_withbehavior_).md>) — Multiplies this number by another given number using the specified behavior.
- [- decimalNumberByDividingBy:withBehavior:](<dividing(by_withbehavior_).md>) — Divides this number by another given number using the specified behavior.
- [- decimalNumberByRaisingToPower:withBehavior:](<raising(topower_withbehavior_).md>) — Raises the number to a given power using the specified behavior.
- [- decimalNumberByMultiplyingByPowerOf10:withBehavior:](<multiplying(bypowerof10_withbehavior_).md>) — Multiplies the number by 10 raised to the given power using the specified behavior.
