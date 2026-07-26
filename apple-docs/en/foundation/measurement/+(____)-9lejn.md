---
title: '+(_:_:)'
framework: Foundation
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurement/+(_:_:)-9lejn'
source_url: 'https://developer.apple.com/documentation/foundation/measurement/+(_:_:)-9lejn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/%2B%28_%3A_%3A%29-9lejn.json'
content_hash: 'sha256:43830dcf660e2c37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Measurement](../measurement.md)

# +(_:_:)

<sub>Operator</sub>

Add two measurements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func + (lhs: Measurement<UnitType>, rhs: Measurement<UnitType>) -> Measurement<UnitType>
```

## Parameters

- `lhs` — A measurement to add.

- `rhs` — Another measurement to add.

## Return Value

The result of adding the two measurements.

## See Also

### Operating on a Measurement

- [*(_:_:)](<_(____)-1d26c.md>) — Multiply a scalar value by a measurement.
- [*(_:_:)](<_(____)-5tv8a.md>) — Multiply a measurement by a scalar value.
- [+(_:_:)](<+(____)-4fsbl.md>) — Adds two measurements of the same dimension.
- [-(_:_:)](<-(____)-2nnoy.md>) — Subtract two measurements of the same Unit.
- [-(_:_:)](<-(____)-1a47h.md>) — Subtract two measurements of the same Dimension.
- [/(_:_:)](<_(____)-98s40.md>) — Divide a scalar value by a measurement.
- [/(_:_:)](<_(____)-71kwk.md>) — Divide a measurement by a scalar value.
