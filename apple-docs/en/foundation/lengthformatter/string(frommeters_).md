---
title: 'string(fromMeters:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/lengthformatter/string(frommeters:)'
source_url: 'https://developer.apple.com/documentation/foundation/lengthformatter/string(frommeters:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/lengthformatter/string%28frommeters%3A%29.json'
content_hash: 'sha256:0dd1dea27d7d99c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [LengthFormatter](../lengthformatter.md)

# string(fromMeters:)

<sub>Instance Method</sub>

Returns a length string for the provided value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(fromMeters numberInMeters: Double) -> String
```

## Parameters

- `numberInMeters` — The length’s value in meters.

## Return Value

A string that combines a value and a unit string appropriate for the formatter’s locale.

## Discussion

This method converts the provided length into units appropriate for the formatter’s locale.

## See Also

### Formatting Length Strings

- [forPersonHeightUse](isforpersonheightuse.md) — A Boolean value that indicates whether the resulting string represents a person’s height.
- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — This method is not supported for the `NSLengthFormatter` class.
- [numberFormatter](numberformatter.md) — The number formatter used to format the numbers in length strings.
- [- stringFromValue:unit:](<string(fromvalue_unit_).md>) — Returns a properly formatted length string for the given value and unit.
- [- unitStringFromMeters:usedUnit:](<unitstring(frommeters_usedunit_).md>) — Returns the unit string for the provided value.
- [- unitStringFromValue:unit:](<unitstring(fromvalue_unit_).md>) — Returns the unit string based on the provided value and unit.
- [unitStyle](unitstyle.md) — The unit style used by this formatter.
