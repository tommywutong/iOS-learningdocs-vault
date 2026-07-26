---
title: abbreviated
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct/abbreviated
source_url: 'https://developer.apple.com/documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct/abbreviated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct/abbreviated.json'
content_hash: 'sha256:2523e2120b81053a'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Duration](../../../duration.md) · [UnitsFormatStyle](../../unitsformatstyle.md) · [UnitWidth](../unitwidth-swift.struct.md)

# abbreviated

<sub>Type Property</sub>

An abbreviated unit name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var abbreviated: Duration.UnitsFormatStyle.UnitWidth { get }
```

## Discussion

For example, `abbreviated` produces the unit label “3 hr” for a 3-hour duration in the `en_US` locale.

## See Also

### Duration unit widths

- [condensedAbbreviated](condensedabbreviated.md) — An abbreviated unit name, with condensed space between the value and name.
- [narrow](narrow.md) — The shortest possible unit name.
- [wide](wide.md) — The full unit name.
