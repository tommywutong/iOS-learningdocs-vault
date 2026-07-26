---
title: numberFormatter
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/lengthformatter/numberformatter
source_url: 'https://developer.apple.com/documentation/foundation/lengthformatter/numberformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/lengthformatter/numberformatter.json'
content_hash: 'sha256:28020fbe4b9fe4cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [LengthFormatter](../lengthformatter.md)

# numberFormatter

<sub>Instance Property</sub>

The number formatter used to format the numbers in length strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var numberFormatter: NumberFormatter! { get set }
```

## Discussion

This property defaults to a number formatter using the [NSNumberFormatterDecimalStyle](../numberformatter/style/decimal.md). You can provide a different number formatter to customize the length string’s appearance.

## See Also

### Formatting Length Strings

- [forPersonHeightUse](isforpersonheightuse.md) — A Boolean value that indicates whether the resulting string represents a person’s height.
- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — This method is not supported for the `NSLengthFormatter` class.
- [- stringFromMeters:](<string(frommeters_).md>) — Returns a length string for the provided value.
- [- stringFromValue:unit:](<string(fromvalue_unit_).md>) — Returns a properly formatted length string for the given value and unit.
- [- unitStringFromMeters:usedUnit:](<unitstring(frommeters_usedunit_).md>) — Returns the unit string for the provided value.
- [- unitStringFromValue:unit:](<unitstring(fromvalue_unit_).md>) — Returns the unit string based on the provided value and unit.
- [unitStyle](unitstyle.md) — The unit style used by this formatter.
