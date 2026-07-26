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
doc_path: '/documentation/foundation/lengthformatter/string(fromvalue:unit:)'
source_url: 'https://developer.apple.com/documentation/foundation/lengthformatter/string(fromvalue:unit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/lengthformatter/string%28fromvalue%3Aunit%3A%29.json'
content_hash: 'sha256:4f700d6aa21ae54f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [LengthFormatter](../lengthformatter.md)

# string(fromValue:unit:)

<sub>Instance Method</sub>

Returns a properly formatted length string for the given value and unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(fromValue value: Double, unit: LengthFormatter.Unit) -> String
```

## Parameters

- `value` — The length’s value in the given unit.

- `unit` — The unit used in the resulting length string.

## Return Value

A localized string that combines the provided value and unit.

## See Also

### Formatting Length Strings

- [forPersonHeightUse](isforpersonheightuse.md) — A Boolean value that indicates whether the resulting string represents a person’s height.
- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — This method is not supported for the `NSLengthFormatter` class.
- [numberFormatter](numberformatter.md) — The number formatter used to format the numbers in length strings.
- [- stringFromMeters:](<string(frommeters_).md>) — Returns a length string for the provided value.
- [- unitStringFromMeters:usedUnit:](<unitstring(frommeters_usedunit_).md>) — Returns the unit string for the provided value.
- [- unitStringFromValue:unit:](<unitstring(fromvalue_unit_).md>) — Returns the unit string based on the provided value and unit.
- [unitStyle](unitstyle.md) — The unit style used by this formatter.
