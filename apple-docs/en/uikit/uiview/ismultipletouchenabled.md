---
title: isMultipleTouchEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/ismultipletouchenabled
source_url: 'https://developer.apple.com/documentation/uikit/uiview/ismultipletouchenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/ismultipletouchenabled.json'
content_hash: 'sha256:6555e77161fb9d8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# isMultipleTouchEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the view receives more than one touch at a time.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isMultipleTouchEnabled: Bool { get set }
```

## Discussion

When set to [true](../../swift/true.md), the view receives all touches associated with a multi-touch sequence and starting within the view’s bounds. When set to [false](../../swift/false.md), the view receives only the first touch event in a multi-touch sequence that start within the view’s bounds. The default value of this property is [false](../../swift/false.md).

> [!note] Note
> This property does not affect the gesture recognizers attached to the view. Gesture recognizers receive all touches that occur in the view.

Other views in the same window can still receive touch events when this property is [false](../../swift/false.md). If you want this view to handle multi-touch events exclusively, set the values of both this property and the [exclusiveTouch](isexclusivetouch.md) property to [true](../../swift/true.md). This property does not prevent a view from being asked to handle multiple touches. For example, two subviews may both forward their touches to a common parent, such as a window or the root view of a view controller. This property determines how many touches initially targeting the view are delivered to that view.

## See Also

### Configuring the event-related behavior

- [userInteractionEnabled](isuserinteractionenabled.md) — A Boolean value that determines whether user events are ignored and removed from the event queue.
- [exclusiveTouch](isexclusivetouch.md) — A Boolean value that indicates whether the receiver handles touch events exclusively.
