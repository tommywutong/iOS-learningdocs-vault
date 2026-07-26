---
title: 'string(fromValue:unit:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/massformatter/string(fromvalue:unit:)'
source_url: 'https://developer.apple.com/documentation/foundation/massformatter/string(fromvalue:unit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/massformatter/string%28fromvalue%3Aunit%3A%29.json'
content_hash: 'sha256:d42cd2f25d1e24be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MassFormatter](../massformatter.md)

# string(fromValue:unit:)

<sub>Instance Method</sub>

Returns a properly formatted mass string for the given value and unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(fromValue value: Double, unit: MassFormatter.Unit) -> String
```

## Parameters

- `value` — The mass’s value in the given unit.

- `unit` — The unit used in the resulting mass string.

## Return Value

A localized string that combines the provided value and unit.

## See Also

### Formatting Mass Strings

- [forPersonMassUse](isforpersonmassuse.md) — A Boolean value that indicates whether the resulting string represents a person’s mass.
- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — This method is not supported for the `NSMassFormatter` class.
- [numberFormatter](numberformatter.md) — The number formatter used to format the numbers in a mass strings.
- [- stringFromKilograms:](<string(fromkilograms_).md>) — Returns a mass string for the provided value.
- [- unitStringFromKilograms:usedUnit:](<unitstring(fromkilograms_usedunit_).md>) — Returns the unit string for the provided value.
- [- unitStringFromValue:unit:](<unitstring(fromvalue_unit_).md>) — Returns the unit string based on the provided value and unit.
- [unitStyle](unitstyle.md) — The unit style used by this formatter.
