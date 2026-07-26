---
title: valueLengthLimits
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/unitsformatstyle/valuelengthlimits
source_url: 'https://developer.apple.com/documentation/swift/duration/unitsformatstyle/valuelengthlimits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/unitsformatstyle/valuelengthlimits.json'
content_hash: 'sha256:90e3b5be8d85f89e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Duration](../../duration.md) · [UnitsFormatStyle](../unitsformatstyle.md)

# valueLengthLimits

<sub>Instance Property</sub>

The padding or truncating behavior of the unit value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var valueLengthLimits: Range<Int>?
```

## Discussion

For example, set this to `2...` to force 2-digit padding on all units.

## See Also

### Working with units

- [allowedUnits](allowedunits.md) — The units that may be included in the output string.
- [Unit](unit.md) — A unit to use in formatting a duration.
- [maximumUnitCount](maximumunitcount.md) — The maximum number of time units to include in the output string.
