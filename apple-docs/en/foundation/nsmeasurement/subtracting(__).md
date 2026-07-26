---
title: 'subtracting(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmeasurement/subtracting(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmeasurement/subtracting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmeasurement/subtracting%28_%3A%29.json'
content_hash: 'sha256:964e384abae832d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMeasurement](../nsmeasurement.md)

# subtracting(_:)

<sub>Instance Method</sub>

Returns a new measurement by subtracting the specified measurement from the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subtracting(_ measurement: Measurement<Unit>) -> Measurement<Unit>
```

## Parameters

- `measurement` — The measurement to be subtracted.

## Return Value

A new measurement with a value equal to the receiver’s value minus the value of the specified measurement converted into the unit of the receiver.

## Discussion

This method raises an [NSInvalidArgumentException](../nsexceptionname/invalidargumentexception.md) if the receiver cannot be converted to unit.

You can use the [- canBeConvertedToUnit:](<canbeconverted(to_).md>) method, passing the unit of the specified measurement, to determine whether a measurement can be converted to a particular unit before calling this method.

## See Also

### Operating on Measurements

- [- measurementByAddingMeasurement:](<adding(__).md>) — Returns a new measurement by adding the receiver to the specified measurement.
