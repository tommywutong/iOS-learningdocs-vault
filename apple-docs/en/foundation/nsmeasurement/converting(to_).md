---
title: 'converting(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmeasurement/converting(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmeasurement/converting(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmeasurement/converting%28to%3A%29.json'
content_hash: 'sha256:38f416668ea677c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMeasurement](../nsmeasurement.md)

# converting(to:)

<sub>Instance Method</sub>

Returns a measurement created by converting the receiver to the specified unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func converting(to unit: Unit) -> Measurement<Unit>
```

## Parameters

- `unit` — The unit to convert the measurement into.

## Return Value

A new measurement with a value calculated by converting into the new unit.

## Discussion

This method raises an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md) if the receiver cannot be converted to unit.

## See Also

### Converting to Other Units

- [- canBeConvertedToUnit:](<canbeconverted(to_).md>) — Indicates whether the measurement can be converted to the given unit.
