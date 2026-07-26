---
title: 'string(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurementformatter/string(from:)-4hwjz'
source_url: 'https://developer.apple.com/documentation/foundation/measurementformatter/string(from:)-4hwjz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurementformatter/string%28from%3A%29-4hwjz.json'
content_hash: 'sha256:b2b3cac0256efb87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MeasurementFormatter](../measurementformatter.md)

# string(from:)

<sub>Instance Method</sub>

Creates and returns a localized string representation of the provided unit of measure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(from unit: Unit) -> String
```

## Parameters

- `unit` — The unit of measure to be represented.

## Return Value

A user-readable string that represents the unit of measure. If the unit cannot be localized, the unit’s [symbol](../unit/symbol.md) value is used.

## See Also

### Converting Measurements

- [- stringFromMeasurement:](<string(from_)-wt9y.md>) — Creates and returns a localized string representation of the provided measurement.
- [string(from:)](<string(from_)-6rcb1.md>) — Creates and returns a localized string representation of the provided measurement.
