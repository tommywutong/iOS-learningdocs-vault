---
title: unitStyle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/lengthformatter/unitstyle
source_url: 'https://developer.apple.com/documentation/foundation/lengthformatter/unitstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/lengthformatter/unitstyle.json'
content_hash: 'sha256:99d5629fed6c6b4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [LengthFormatter](../lengthformatter.md)

# unitStyle

<sub>Instance Property</sub>

The unit style used by this formatter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var unitStyle: Formatter.UnitStyle { get set }
```

## Discussion

This property defaults to [NSFormattingUnitStyleMedium](../formatter/unitstyle/medium.md). For a complete list of unit styles, see [UnitStyle](../formatter/unitstyle.md).

## See Also

### Formatting Length Strings

- [forPersonHeightUse](isforpersonheightuse.md) — A Boolean value that indicates whether the resulting string represents a person’s height.
- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — This method is not supported for the `NSLengthFormatter` class.
- [numberFormatter](numberformatter.md) — The number formatter used to format the numbers in length strings.
- [- stringFromMeters:](<string(frommeters_).md>) — Returns a length string for the provided value.
- [- stringFromValue:unit:](<string(fromvalue_unit_).md>) — Returns a properly formatted length string for the given value and unit.
- [- unitStringFromMeters:usedUnit:](<unitstring(frommeters_usedunit_).md>) — Returns the unit string for the provided value.
- [- unitStringFromValue:unit:](<unitstring(fromvalue_unit_).md>) — Returns the unit string based on the provided value and unit.
