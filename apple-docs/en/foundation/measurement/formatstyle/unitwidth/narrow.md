---
title: narrow
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement/formatstyle/unitwidth/narrow
source_url: 'https://developer.apple.com/documentation/foundation/measurement/formatstyle/unitwidth/narrow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/formatstyle/unitwidth/narrow.json'
content_hash: 'sha256:20006e6ef9e8c569'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Measurement](../../../measurement.md) · [FormatStyle](../../formatstyle.md) · [UnitWidth](../unitwidth.md)

# narrow

<sub>Type Property</sub>

The shortest unit width.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var narrow: Measurement<UnitType>.FormatStyle.UnitWidth { get }
```

## Discussion

This width may condense the spacing between the value and the unit; for example, `37.20Cal` or `37,2L`.

## See Also

### Unit widths

- [wide](wide.md) — A unit width that shows the full unit name.
- [abbreviated](abbreviated.md) — An abbreviated unit width.
