---
title: 'unitString(fromKilograms:usedUnit:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/massformatter/unitstring(fromkilograms:usedunit:)'
source_url: 'https://developer.apple.com/documentation/foundation/massformatter/unitstring(fromkilograms:usedunit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/massformatter/unitstring%28fromkilograms%3Ausedunit%3A%29.json'
content_hash: 'sha256:dc8c626664af7f55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MassFormatter](../massformatter.md)

# unitString(fromKilograms:usedUnit:)

<sub>Instance Method</sub>

Returns the unit string for the provided value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func unitString(fromKilograms numberInKilograms: Double, usedUnit unitp: UnsafeMutablePointer<MassFormatter.Unit>?) -> String
```

## Parameters

- `numberInKilograms` — The mass’s value in kilograms.

- `unitp` — An output parameter. This will hold the [Unit](unit.md) value that corresponds to the returned units.

## Return Value

A localized string representing the unit.

## Discussion

This method selects the correct unit based on the formatter’s locale, the magnitude of the value, and the [forPersonMassUse](isforpersonmassuse.md) property. The value, once converted into the appropriate unit, determines whether the unit string is plural or singular.

## See Also

### Formatting Mass Strings

- [forPersonMassUse](isforpersonmassuse.md) — A Boolean value that indicates whether the resulting string represents a person’s mass.
- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — This method is not supported for the `NSMassFormatter` class.
- [numberFormatter](numberformatter.md) — The number formatter used to format the numbers in a mass strings.
- [- stringFromKilograms:](<string(fromkilograms_).md>) — Returns a mass string for the provided value.
- [- stringFromValue:unit:](<string(fromvalue_unit_).md>) — Returns a properly formatted mass string for the given value and unit.
- [- unitStringFromValue:unit:](<unitstring(fromvalue_unit_).md>) — Returns the unit string based on the provided value and unit.
- [unitStyle](unitstyle.md) — The unit style used by this formatter.
