---
title: 'touchesCancelled(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/touchescancelled(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/touchescancelled(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/touchescancelled%28_%3Awith%3A%29.json'
content_hash: 'sha256:b6b718f883b387cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# touchesCancelled(_:with:)

<sub>Instance Method</sub>

Tells the responder when a system event (such as a system alert) cancels a touch sequence.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?)
```

## Parameters

- `touches` — A set of [UITouch](../uitouch.md) instances that represent the touches for the ending phase of the event represented by `event`. For touches in a view, this set contains only one touch by default. To receive multiple touches, you must set the view’s [multipleTouchEnabled](../uiview/ismultipletouchenabled.md) property to [true](../../swift/true.md).

- `event` — The event to which the touches belong.

## Discussion

UIKit calls this method when it receives a system interruption requiring cancellation of the touch sequence. An interruption is anything that causes the application to become inactive or causes the view handling the touch events to be removed from its window. Your implementation of this method should clean up any state associated with handling the touch sequence. The default implementation of this method forwards the message up the responder chain. When creating your own subclasses, call `super` to forward any events that you don’t handle yourself, like in the following code.

**Swift**

```swift
super.touchesCancelled(touches, with: event)
```

**Objective-C**

```objc
[super touchesCancelled:touches withEvent:event];
```

If you override this method without calling `super` (a common use pattern), you must also override the other methods for handling touch events, if only as stub (empty) implementations.

## See Also

### Responding to touch events

- [- touchesBegan:withEvent:](<touchesbegan(__with_).md>) — Tells this object that one or more new touches occurred in a view or window.
- [- touchesMoved:withEvent:](<touchesmoved(__with_).md>) — Tells the responder when one or more touches associated with an event changed.
- [- touchesEnded:withEvent:](<touchesended(__with_).md>) — Tells the responder when one or more fingers are raised from a view or window.
- [- touchesEstimatedPropertiesUpdated:](<touchesestimatedpropertiesupdated(__).md>) — Tells the responder that updated values were received for previously estimated properties or that an update is no longer expected.
