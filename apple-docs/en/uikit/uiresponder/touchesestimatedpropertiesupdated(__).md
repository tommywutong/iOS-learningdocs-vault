---
title: 'touchesEstimatedPropertiesUpdated(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/touchesestimatedpropertiesupdated(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/touchesestimatedpropertiesupdated(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/touchesestimatedpropertiesupdated%28_%3A%29.json'
content_hash: 'sha256:d530c6fce95c91fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# touchesEstimatedPropertiesUpdated(_:)

<sub>Instance Method</sub>

Tells the responder that updated values were received for previously estimated properties or that an update is no longer expected.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func touchesEstimatedPropertiesUpdated(_ touches: Set<UITouch>)
```

## Parameters

- `touches` — The array of [UITouch](../uitouch.md) objects containing the updated properties. In each touch object, UIKit updates the [estimatedPropertiesExpectingUpdates](../uitouch/estimatedpropertiesexpectingupdates.md) property by removing the bit flag for each property that was updated.

## Discussion

When UIKit is unable to report actual values for a touch, it delivers estimates for the values and sets the appropriate bits in the [estimatedProperties](../uitouch/estimatedproperties.md) and [estimatedPropertiesExpectingUpdates](../uitouch/estimatedpropertiesexpectingupdates.md) properties of the [UITouch](../uitouch.md) object. When updates are received for items in the [estimatedPropertiesExpectingUpdates](../uitouch/estimatedpropertiesexpectingupdates.md) property, UIKit calls this method to deliver those updates. UIKit also calls this method if one or more updates are no longer expected. You use this method to update your app’s internal data structures with the new values provided by UIKit.

In your implementation of this method, use the [estimationUpdateIndex](../uitouch/estimationupdateindex.md) property of a [UITouch](../uitouch.md) object in the `touches` parameter to locate the original data in your app. Upon locating the data, apply the new values from the touch object to it. You can determine which touch properties were updated by checking the [estimatedPropertiesExpectingUpdates](../uitouch/estimatedpropertiesexpectingupdates.md) bit mask of the touch object; updated properties are no longer included in the bit mask.

Touch-related properties may remain estimated because of hardware considerations. For example, sensors may not be able to ascertain the exact altitude or azimuth of Apple Pencil when it’s near the edges of the screen. In those cases, the [estimatedProperties](../uitouch/estimatedproperties.md) property continues to store the list of properties whose values are only estimates.

## See Also

### Responding to touch events

- [- touchesBegan:withEvent:](<touchesbegan(__with_).md>) — Tells this object that one or more new touches occurred in a view or window.
- [- touchesMoved:withEvent:](<touchesmoved(__with_).md>) — Tells the responder when one or more touches associated with an event changed.
- [- touchesEnded:withEvent:](<touchesended(__with_).md>) — Tells the responder when one or more fingers are raised from a view or window.
- [- touchesCancelled:withEvent:](<touchescancelled(__with_).md>) — Tells the responder when a system event (such as a system alert) cancels a touch sequence.
