---
title: '/(_:_:)'
framework: Foundation
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurement/_(_:_:)-71kwk'
source_url: 'https://developer.apple.com/documentation/foundation/measurement/_(_:_:)-71kwk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/_%28_%3A_%3A%29-71kwk.json'
content_hash: 'sha256:60eec32d5b282718'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Measurement](../measurement.md)

# /(_:_:)

<sub>Operator</sub>

Divide a measurement by a scalar value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func / (lhs: Measurement<UnitType>, rhs: Double) -> Measurement<UnitType>
```

## Parameters

- `lhs` — A measurement to divide.

- `rhs` — A double-precision floating-point number to divide by.

## Return Value

A measurement of value `lhs.value / rhs` with the same unit as `lhs`.

## See Also

### Operating on a Measurement

- [*(_:_:)](<_(____)-1d26c.md>) — Multiply a scalar value by a measurement.
- [*(_:_:)](<_(____)-5tv8a.md>) — Multiply a measurement by a scalar value.
- [+(_:_:)](<+(____)-9lejn.md>) — Add two measurements.
- [+(_:_:)](<+(____)-4fsbl.md>) — Adds two measurements of the same dimension.
- [-(_:_:)](<-(____)-2nnoy.md>) — Subtract two measurements of the same Unit.
- [-(_:_:)](<-(____)-1a47h.md>) — Subtract two measurements of the same Dimension.
- [/(_:_:)](<_(____)-98s40.md>) — Divide a scalar value by a measurement.
