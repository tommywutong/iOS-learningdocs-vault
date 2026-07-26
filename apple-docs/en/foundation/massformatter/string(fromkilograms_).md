---
title: 'string(fromKilograms:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/massformatter/string(fromkilograms:)'
source_url: 'https://developer.apple.com/documentation/foundation/massformatter/string(fromkilograms:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/massformatter/string%28fromkilograms%3A%29.json'
content_hash: 'sha256:44a9f2fff4c6fc64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MassFormatter](../massformatter.md)

# string(fromKilograms:)

<sub>Instance Method</sub>

Returns a mass string for the provided value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(fromKilograms numberInKilograms: Double) -> String
```

## Parameters

- `numberInKilograms` — The mass’s value in kilograms.

## Return Value

A string that combines a value and a unit string appropriate for the formatter’s locale.

## Discussion

This method converts the provided mass in kilograms into units appropriate for the formatter’s locale.

## See Also

### Formatting Mass Strings

- [forPersonMassUse](isforpersonmassuse.md) — A Boolean value that indicates whether the resulting string represents a person’s mass.
- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — This method is not supported for the `NSMassFormatter` class.
- [numberFormatter](numberformatter.md) — The number formatter used to format the numbers in a mass strings.
- [- stringFromValue:unit:](<string(fromvalue_unit_).md>) — Returns a properly formatted mass string for the given value and unit.
- [- unitStringFromKilograms:usedUnit:](<unitstring(fromkilograms_usedunit_).md>) — Returns the unit string for the provided value.
- [- unitStringFromValue:unit:](<unitstring(fromvalue_unit_).md>) — Returns the unit string based on the provided value and unit.
- [unitStyle](unitstyle.md) — The unit style used by this formatter.
