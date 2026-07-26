---
title: '-(_:_:)'
framework: Foundation
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurement/-(_:_:)-2nnoy'
source_url: 'https://developer.apple.com/documentation/foundation/measurement/-(_:_:)-2nnoy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/-%28_%3A_%3A%29-2nnoy.json'
content_hash: 'sha256:cd73c1969bd92935'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Measurement](../measurement.md)

# -(_:_:)

<sub>Operator</sub>

Subtract two measurements of the same Unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func - (lhs: Measurement<UnitType>, rhs: Measurement<UnitType>) -> Measurement<UnitType>
```

## Return Value

A measurement of value `lhs.value - rhs.value` and unit `lhs.unit`.

## Discussion

> [!info] Precondition
> The `unit` of `lhs` and `rhs` must be `isEqual`.

## See Also

### Operating on a Measurement

- [*(_:_:)](<_(____)-1d26c.md>) — Multiply a scalar value by a measurement.
- [*(_:_:)](<_(____)-5tv8a.md>) — Multiply a measurement by a scalar value.
- [+(_:_:)](<+(____)-9lejn.md>) — Add two measurements.
- [+(_:_:)](<+(____)-4fsbl.md>) — Adds two measurements of the same dimension.
- [-(_:_:)](<-(____)-1a47h.md>) — Subtract two measurements of the same Dimension.
- [/(_:_:)](<_(____)-98s40.md>) — Divide a scalar value by a measurement.
- [/(_:_:)](<_(____)-71kwk.md>) — Divide a measurement by a scalar value.
