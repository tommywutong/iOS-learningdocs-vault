---
title: 'unitString(fromJoules:usedUnit:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/energyformatter/unitstring(fromjoules:usedunit:)'
source_url: 'https://developer.apple.com/documentation/foundation/energyformatter/unitstring(fromjoules:usedunit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/energyformatter/unitstring%28fromjoules%3Ausedunit%3A%29.json'
content_hash: 'sha256:1552edd60323c696'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [EnergyFormatter](../energyformatter.md)

# unitString(fromJoules:usedUnit:)

<sub>Instance Method</sub>

Returns the unit string for the provided value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func unitString(fromJoules numberInJoules: Double, usedUnit unitp: UnsafeMutablePointer<EnergyFormatter.Unit>?) -> String
```

## Parameters

- `numberInJoules` — The energy value in joules.

- `unitp` — An output parameter. This will hold the [Unit](unit.md) value that corresponds to the returned units.

## Return Value

A localized string representing the unit.

## Discussion

This method selects the correct unit based on the formatter’s locale, the magnitude of the value, and the [forFoodEnergyUse](isforfoodenergyuse.md) property.

## See Also

### Formatting Energy Strings

- [forFoodEnergyUse](isforfoodenergyuse.md) — A Boolean value that indicates whether the energy value is used to measure food energy.
- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — This method is not supported for the `NSEnergyFormatter` class.
- [numberFormatter](numberformatter.md) — The number formatter used to format the numbers in energy strings.
- [- stringFromJoules:](<string(fromjoules_).md>) — Returns an energy string for the provided value.
- [- stringFromValue:unit:](<string(fromvalue_unit_).md>) — Returns a properly formatted energy string for the given value and unit.
- [- unitStringFromValue:unit:](<unitstring(fromvalue_unit_).md>) — Returns the unit string based on the provided value and unit.
- [unitStyle](unitstyle.md) — The unit style used by this formatter.
