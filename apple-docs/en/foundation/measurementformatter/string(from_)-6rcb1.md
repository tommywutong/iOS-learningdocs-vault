---
title: 'string(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurementformatter/string(from:)-6rcb1'
source_url: 'https://developer.apple.com/documentation/foundation/measurementformatter/string(from:)-6rcb1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurementformatter/string%28from%3A%29-6rcb1.json'
content_hash: 'sha256:bfcdfd24d69a5b3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MeasurementFormatter](../measurementformatter.md)

# string(from:)

<sub>Instance Method</sub>

Creates and returns a localized string representation of the provided measurement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string<UnitType>(from measurement: Measurement<UnitType>) -> String where UnitType : Unit
```

## Parameters

- `measurement` — The measurement to be represented.

## Return Value

A user-readable string that represents the measurement.

## See Also

### Converting Measurements

- [- stringFromMeasurement:](<string(from_)-wt9y.md>) — Creates and returns a localized string representation of the provided measurement.
- [- stringFromUnit:](<string(from_)-4hwjz.md>) — Creates and returns a localized string representation of the provided unit of measure.
