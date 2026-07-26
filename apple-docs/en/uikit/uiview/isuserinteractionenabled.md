---
title: isUserInteractionEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/isuserinteractionenabled
source_url: 'https://developer.apple.com/documentation/uikit/uiview/isuserinteractionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/isuserinteractionenabled.json'
content_hash: 'sha256:f58d97b3d7278bf4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# isUserInteractionEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether user events are ignored and removed from the event queue.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isUserInteractionEnabled: Bool { get set }
```

## Discussion

When set to [false](../../swift/false.md), touch, press, keyboard, and focus events intended for the view are ignored and removed from the event queue. When set to [true](../../swift/true.md), events are delivered to the view normally. The default value of this property is [true](../../swift/true.md).

During an animation, user interactions are temporarily disabled for all views involved in the animation, regardless of the value in this property. You can disable this behavior by specifying the [UIViewAnimationOptionAllowUserInteraction](animationoptions/allowuserinteraction.md) option when configuring the animation.

> [!note] Note
> Some UIKit subclasses override this property and return a different default value. See the documentation for that class to determine if it returns a different value.

## See Also

### Configuring the event-related behavior

- [multipleTouchEnabled](ismultipletouchenabled.md) — A Boolean value that indicates whether the view receives more than one touch at a time.
- [exclusiveTouch](isexclusivetouch.md) — A Boolean value that indicates whether the receiver handles touch events exclusively.
