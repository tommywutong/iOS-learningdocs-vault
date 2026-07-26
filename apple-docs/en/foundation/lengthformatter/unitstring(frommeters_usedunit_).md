---
title: 'unitString(fromMeters:usedUnit:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/lengthformatter/unitstring(frommeters:usedunit:)'
source_url: 'https://developer.apple.com/documentation/foundation/lengthformatter/unitstring(frommeters:usedunit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/lengthformatter/unitstring%28frommeters%3Ausedunit%3A%29.json'
content_hash: 'sha256:a170471033214a1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [LengthFormatter](../lengthformatter.md)

# unitString(fromMeters:usedUnit:)

<sub>Instance Method</sub>

Returns the unit string for the provided value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func unitString(fromMeters numberInMeters: Double, usedUnit unitp: UnsafeMutablePointer<LengthFormatter.Unit>?) -> String
```

## Parameters

- `numberInMeters` — The length’s value in meters.

- `unitp` — An output parameter. This will hold the [Unit](unit.md) value that corresponds to the returned units.

## Return Value

A localized string representing the unit.

## Discussion

This method selects the correct unit based on the formatter’s locale, the magnitude of the value, and the [forPersonHeightUse](isforpersonheightuse.md) property.

## See Also

### Formatting Length Strings

- [forPersonHeightUse](isforpersonheightuse.md) — A Boolean value that indicates whether the resulting string represents a person’s height.
- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — This method is not supported for the `NSLengthFormatter` class.
- [numberFormatter](numberformatter.md) — The number formatter used to format the numbers in length strings.
- [- stringFromMeters:](<string(frommeters_).md>) — Returns a length string for the provided value.
- [- stringFromValue:unit:](<string(fromvalue_unit_).md>) — Returns a properly formatted length string for the given value and unit.
- [- unitStringFromValue:unit:](<unitstring(fromvalue_unit_).md>) — Returns the unit string based on the provided value and unit.
- [unitStyle](unitstyle.md) — The unit style used by this formatter.
