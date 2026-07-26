---
title: estimatedPropertiesExpectingUpdates
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/estimatedpropertiesexpectingupdates
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/estimatedpropertiesexpectingupdates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/estimatedpropertiesexpectingupdates.json'
content_hash: 'sha256:c1deee1fb919983e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# estimatedPropertiesExpectingUpdates

<sub>Instance Property</sub>

The set of touch properties for which updated values are expected in the future.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var estimatedPropertiesExpectingUpdates: UITouch.Properties { get }
```

## Discussion

This property contains a bitmask of constants indicating which touch properties could not be reported immediately, and for which an update is expected later. When this property contains a non empty set, you can expect UIKit to call the [- touchesEstimatedPropertiesUpdated:](<../uiresponder/touchesestimatedpropertiesupdated(__).md>) method of your responder or gesture recognizer at a later time with the updated values for the given properties. Attach the value in the [estimationUpdateIndex](estimationupdateindex.md) property to your app’s copy of the touch data. When UIKit calls the [- touchesEstimatedPropertiesUpdated:](<../uiresponder/touchesestimatedpropertiesupdated(__).md>) method later, use the estimation update index of the new touch to locate and update your app’s copy of the touch data.

When this property contains an empty set, no more updates are expected. In that scenario, the estimated or updated value is the final value.

## See Also

### Managing estimated touch attributes

- [estimatedProperties](estimatedproperties.md) — A set of touch properties whose values contain only estimates.
- [Properties](properties.md) — A bit mask of touch properties that may get updated.
- [estimationUpdateIndex](estimationupdateindex.md) — An index number that lets you correlate an updated touch with the original touch.
