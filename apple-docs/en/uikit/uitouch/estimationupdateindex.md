---
title: estimationUpdateIndex
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/estimationupdateindex
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/estimationupdateindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/estimationupdateindex.json'
content_hash: 'sha256:c8f8c3b80d68dae7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# estimationUpdateIndex

<sub>Instance Property</sub>

An index number that lets you correlate an updated touch with the original touch.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var estimationUpdateIndex: NSNumber? { get }
```

## Discussion

This property contains a unique marker for the current touch data. When the touch contains estimated properties, save this index along with the rest of the touch data to your app’s data structures. When the system reports the actual touch values later, use this index to locate the original data in your app’s data structures and replace the estimated values you stored previously. For example, when a touch contains estimated properties, you might use this property as a key in a dictionary whose value is the object you use to store the touch data.

The value of this property increases monotonically for each touch that contains estimated properties. The value of this property is `nil` when the touch object does not contain either estimated or updated properties.

## See Also

### Managing estimated touch attributes

- [estimatedProperties](estimatedproperties.md) — A set of touch properties whose values contain only estimates.
- [estimatedPropertiesExpectingUpdates](estimatedpropertiesexpectingupdates.md) — The set of touch properties for which updated values are expected in the future.
- [Properties](properties.md) — A bit mask of touch properties that may get updated.
