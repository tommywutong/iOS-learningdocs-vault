---
title: wide
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct/wide
source_url: 'https://developer.apple.com/documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct/wide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct/wide.json'
content_hash: 'sha256:eff7b6b4e3787b82'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Duration](../../../duration.md) · [UnitsFormatStyle](../../unitsformatstyle.md) · [UnitWidth](../unitwidth-swift.struct.md)

# wide

<sub>Type Property</sub>

The full unit name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var wide: Duration.UnitsFormatStyle.UnitWidth { get }
```

## Discussion

For example, `wide` produces the unit label “3 hours” for a 3-hour duration in the `en_US` locale.

## See Also

### Duration unit widths

- [abbreviated](abbreviated.md) — An abbreviated unit name.
- [condensedAbbreviated](condensedabbreviated.md) — An abbreviated unit name, with condensed space between the value and name.
- [narrow](narrow.md) — The shortest possible unit name.
