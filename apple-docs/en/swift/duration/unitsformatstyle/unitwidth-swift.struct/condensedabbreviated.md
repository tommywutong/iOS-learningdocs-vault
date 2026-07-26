---
title: condensedAbbreviated
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct/condensedabbreviated
source_url: 'https://developer.apple.com/documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct/condensedabbreviated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct/condensedabbreviated.json'
content_hash: 'sha256:9791b2d63e082820'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Duration](../../../duration.md) · [UnitsFormatStyle](../../unitsformatstyle.md) · [UnitWidth](../unitwidth-swift.struct.md)

# condensedAbbreviated

<sub>Type Property</sub>

An abbreviated unit name, with condensed space between the value and name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var condensedAbbreviated: Duration.UnitsFormatStyle.UnitWidth { get }
```

## Discussion

For example, `condensedAbbreviated` produces the unit label “3hr” for a 3-hour duration in the `en_US` locale.

## See Also

### Duration unit widths

- [abbreviated](abbreviated.md) — An abbreviated unit name.
- [narrow](narrow.md) — The shortest possible unit name.
- [wide](wide.md) — The full unit name.
