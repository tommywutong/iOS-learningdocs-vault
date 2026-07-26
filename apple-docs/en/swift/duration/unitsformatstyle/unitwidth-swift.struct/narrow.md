---
title: narrow
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct/narrow
source_url: 'https://developer.apple.com/documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct/narrow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct/narrow.json'
content_hash: 'sha256:b6fa23fd5642c2de'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Duration](../../../duration.md) · [UnitsFormatStyle](../../unitsformatstyle.md) · [UnitWidth](../unitwidth-swift.struct.md)

# narrow

<sub>Type Property</sub>

The shortest possible unit name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var narrow: Duration.UnitsFormatStyle.UnitWidth { get }
```

## Discussion

For example, `narrow` produces the unit label “3h” for a 3-hour duration in the `en_US` locale.

## See Also

### Duration unit widths

- [abbreviated](abbreviated.md) — An abbreviated unit name.
- [condensedAbbreviated](condensedabbreviated.md) — An abbreviated unit name, with condensed space between the value and name.
- [wide](wide.md) — The full unit name.
