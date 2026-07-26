---
title: isForFoodEnergyUse
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/energyformatter/isforfoodenergyuse
source_url: 'https://developer.apple.com/documentation/foundation/energyformatter/isforfoodenergyuse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/energyformatter/isforfoodenergyuse.json'
content_hash: 'sha256:0eac8aed9f2e2dce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [EnergyFormatter](../energyformatter.md)

# isForFoodEnergyUse

<sub>Instance Property</sub>

A Boolean value that indicates whether the energy value is used to measure food energy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isForFoodEnergyUse: Bool { get set }
```

## Discussion

Returns [true](../../swift/true.md) if the energy is used to measure food energy; otherwise, [false](../../swift/false.md). If set to [true](../../swift/true.md), [NSEnergyFormatterUnitKilocalorie](unit/kilocalorie.md) may be represented using “C” instead of “kcal”. By default, this property returns [false](../../swift/false.md).

## See Also

### Formatting Energy Strings

- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — This method is not supported for the `NSEnergyFormatter` class.
- [numberFormatter](numberformatter.md) — The number formatter used to format the numbers in energy strings.
- [- stringFromJoules:](<string(fromjoules_).md>) — Returns an energy string for the provided value.
- [- stringFromValue:unit:](<string(fromvalue_unit_).md>) — Returns a properly formatted energy string for the given value and unit.
- [- unitStringFromJoules:usedUnit:](<unitstring(fromjoules_usedunit_).md>) — Returns the unit string for the provided value.
- [- unitStringFromValue:unit:](<unitstring(fromvalue_unit_).md>) — Returns the unit string based on the provided value and unit.
- [unitStyle](unitstyle.md) — The unit style used by this formatter.
