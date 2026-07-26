---
title: MeasurementFormatUnitUsage
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurementformatunitusage
source_url: 'https://developer.apple.com/documentation/foundation/measurementformatunitusage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurementformatunitusage.json'
content_hash: 'sha256:dc0f23807543b2ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# MeasurementFormatUnitUsage

<sub>Structure</sub>

A type that provides the generalized usage for a formatted measurement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MeasurementFormatUnitUsage<UnitType> where UnitType : Dimension
```

## Relationships

- **Conforms To**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Selecting a General Format for a Measurement Unit

- [general](measurementformatunitusage/general.md) — A general usage of the formatted measurement.
- [asProvided](measurementformatunitusage/asprovided.md) — A usage of the formatted measurement that reflects the units that you used to create the measurement.

### Selecting a Format for an Energy Measurement

- [food](measurementformatunitusage/food.md) — A usage of an energy measurement related to food.
- [workout](measurementformatunitusage/workout.md) — A usage of a energy measurement related to a workout.

### Selecting a Format for a Length Measurement

- [person](measurementformatunitusage/person-8bfxd.md) — A format usage of a length measurement for displaying a distance as it relates to people.
- [personHeight](measurementformatunitusage/personheight.md) — A usage of a length measurement related to a person’s height.
- [road](measurementformatunitusage/road.md) — A usage of a length measurement related to a road.

### Selecting a Format for a Mass Measurement

- [personWeight](measurementformatunitusage/personweight.md) — A usage of a mass measurement related to a person’s weight.

### Selecting a Format for a Temperature Measurement

- [person](measurementformatunitusage/person-4ifk7.md) — A format usage of a temperature measurement for displaying a temperature as it relates to people.
- [weather](measurementformatunitusage/weather.md) — A usage of a temperature measurement related to the weather.

### Type Properties

- [barometric](measurementformatunitusage/barometric.md) — Describes the unit for barometric pressure
- [focalLength](measurementformatunitusage/focallength.md) — Used to format the focal length of an optical system, such as that of camera lenses
- [liquid](measurementformatunitusage/liquid.md) — Used to format the amount of liquid
- [rainfall](measurementformatunitusage/rainfall.md) — Used to format the rainfall amount
- [snowfall](measurementformatunitusage/snowfall.md) — Used to format the snowfall amount
- [visibility](measurementformatunitusage/visibility.md) — Describes the distance of visibility
- [wind](measurementformatunitusage/wind.md) — Describes the unit for wind speed
