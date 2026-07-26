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
doc_path: '/documentation/foundation/measurementformatter/string(from:)-wt9y'
source_url: 'https://developer.apple.com/documentation/foundation/measurementformatter/string(from:)-wt9y'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurementformatter/string%28from%3A%29-wt9y.json'
content_hash: 'sha256:de4d5b175bdccf8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [MeasurementFormatter](../measurementformatter.md)

# string(from:)

<sub>Instance Method</sub>

Creates and returns a localized string representation of the provided measurement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(from measurement: Measurement<Unit>) -> String
```

## Parameters

- `measurement` — The measurement to be represented.

## Return Value

A user-readable string that represents the measurement.

## See Also

### Converting Measurements

- [string(from:)](<string(from_)-6rcb1.md>) — Creates and returns a localized string representation of the provided measurement.
- [- stringFromUnit:](<string(from_)-4hwjz.md>) — Creates and returns a localized string representation of the provided unit of measure.
