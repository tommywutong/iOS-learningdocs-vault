---
title: estimatedProperties
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/estimatedproperties
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/estimatedproperties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/estimatedproperties.json'
content_hash: 'sha256:9df16deb6a18665a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# estimatedProperties

<sub>Instance Property</sub>

A set of touch properties whose values contain only estimates.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var estimatedProperties: UITouch.Properties { get }
```

## Discussion

This property contains a bitmask of constants indicating which touch properties could not be reported immediately. For example, Apple Pencil records the force of a touch, but must transmit that information over the air to the underlying iPad. The delay incurred by transmitting the data may cause the information to be received after the touch has been reported to your app.

Values in this property are not guaranteed to be updated later. For a list of properties whose values are expected to be updated, see [estimatedPropertiesExpectingUpdates](estimatedpropertiesexpectingupdates.md).

## See Also

### Managing estimated touch attributes

- [estimatedPropertiesExpectingUpdates](estimatedpropertiesexpectingupdates.md) — The set of touch properties for which updated values are expected in the future.
- [Properties](properties.md) — A bit mask of touch properties that may get updated.
- [estimationUpdateIndex](estimationupdateindex.md) — An index number that lets you correlate an updated touch with the original touch.
