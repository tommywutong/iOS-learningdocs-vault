---
title: isForPersonHeightUse
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/lengthformatter/isforpersonheightuse
source_url: 'https://developer.apple.com/documentation/foundation/lengthformatter/isforpersonheightuse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/lengthformatter/isforpersonheightuse.json'
content_hash: 'sha256:f90375b921fd7cf2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [LengthFormatter](../lengthformatter.md)

# isForPersonHeightUse

<sub>Instance Property</sub>

A Boolean value that indicates whether the resulting string represents a person’s height.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isForPersonHeightUse: Bool { get set }
```

## Discussion

Returns [true](../../swift/true.md) if the value passed to [- stringFromMeters:](<string(frommeters_).md>) or [- unitStringFromMeters:usedUnit:](<unitstring(frommeters_usedunit_).md>) is a person’s height; otherwise, [false](../../swift/false.md). By default, this property returns [false](../../swift/false.md).

The length formatter uses this property when determining the best unit for a given locale (for example, in the [- stringFromMeters:](<string(frommeters_).md>) method).

## See Also

### Formatting Length Strings

- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — This method is not supported for the `NSLengthFormatter` class.
- [numberFormatter](numberformatter.md) — The number formatter used to format the numbers in length strings.
- [- stringFromMeters:](<string(frommeters_).md>) — Returns a length string for the provided value.
- [- stringFromValue:unit:](<string(fromvalue_unit_).md>) — Returns a properly formatted length string for the given value and unit.
- [- unitStringFromMeters:usedUnit:](<unitstring(frommeters_usedunit_).md>) — Returns the unit string for the provided value.
- [- unitStringFromValue:unit:](<unitstring(fromvalue_unit_).md>) — Returns the unit string based on the provided value and unit.
- [unitStyle](unitstyle.md) — The unit style used by this formatter.
