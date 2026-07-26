---
title: UITouch.Properties
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/properties
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/properties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/properties.json'
content_hash: 'sha256:22c972a48e3f28bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# UITouch.Properties

<sub>Structure</sub>

A bit mask of touch properties that may get updated.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct Properties
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [UITouchPropertyForce](properties/force.md) — A touch property, representing force, in a bit mask.
- [UITouchPropertyAzimuth](properties/azimuth.md) — A touch property, representing azimuth, in a bit mask.
- [UITouchPropertyAltitude](properties/altitude.md) — A touch property, representing altitude, in a bit mask.
- [UITouchPropertyLocation](properties/location.md) — A touch property, representing location, in a bit mask.
- [UITouchPropertyRoll](properties/roll.md) — A touch property, representing barrel-roll angle, in a bit mask.

### Initializers

- [init(rawValue:)](<properties/init(rawvalue_).md>) — Creates a structure that represents the properties of a touch object.

## See Also

### Managing estimated touch attributes

- [estimatedProperties](estimatedproperties.md) — A set of touch properties whose values contain only estimates.
- [estimatedPropertiesExpectingUpdates](estimatedpropertiesexpectingupdates.md) — The set of touch properties for which updated values are expected in the future.
- [estimationUpdateIndex](estimationupdateindex.md) — An index number that lets you correlate an updated touch with the original touch.
