---
title: isForPersonMassUse
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/massformatter/isforpersonmassuse
source_url: 'https://developer.apple.com/documentation/foundation/massformatter/isforpersonmassuse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/massformatter/isforpersonmassuse.json'
content_hash: 'sha256:9efe550b1462043c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MassFormatter](../massformatter.md)

# isForPersonMassUse

<sub>Instance Property</sub>

A Boolean value that indicates whether the resulting string represents a person’s mass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isForPersonMassUse: Bool { get set }
```

## Discussion

Returns [true](../../swift/true.md) if the value passed to [- stringFromKilograms:](<string(fromkilograms_).md>) or [- unitStringFromKilograms:usedUnit:](<unitstring(fromkilograms_usedunit_).md>) is a person’s mass; otherwise, [false](../../swift/false.md). By default, this property returns [false](../../swift/false.md).

The mass formatter uses this property when determining the best unit for a given locale (for example, in the [- stringFromKilograms:](<string(fromkilograms_).md>) method).

## See Also

### Formatting Mass Strings

- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — This method is not supported for the `NSMassFormatter` class.
- [numberFormatter](numberformatter.md) — The number formatter used to format the numbers in a mass strings.
- [- stringFromKilograms:](<string(fromkilograms_).md>) — Returns a mass string for the provided value.
- [- stringFromValue:unit:](<string(fromvalue_unit_).md>) — Returns a properly formatted mass string for the given value and unit.
- [- unitStringFromKilograms:usedUnit:](<unitstring(fromkilograms_usedunit_).md>) — Returns the unit string for the provided value.
- [- unitStringFromValue:unit:](<unitstring(fromvalue_unit_).md>) — Returns the unit string based on the provided value and unit.
- [unitStyle](unitstyle.md) — The unit style used by this formatter.
