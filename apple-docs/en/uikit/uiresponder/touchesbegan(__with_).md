---
title: 'touchesBegan(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/touchesbegan(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/touchesbegan(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/touchesbegan%28_%3Awith%3A%29.json'
content_hash: 'sha256:882633cb0f34c395'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# touchesBegan(_:with:)

<sub>Instance Method</sub>

Tells this object that one or more new touches occurred in a view or window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?)
```

## Parameters

- `touches` — A set of [UITouch](../uitouch.md) instances that represent the touches for the starting phase of the event, which is represented by `event`. For touches in a view, this set contains only one touch by default. To receive multiple touches, you must set the view’s [multipleTouchEnabled](../uiview/ismultipletouchenabled.md) property to [true](../../swift/true.md).

- `event` — The event to which the touches belong.

## Discussion

UIKit calls this method when a new touch is detected in a view or window. Many UIKit classes override this method and use it to handle the corresponding touch events. The default implementation of this method forwards the message up the responder chain. When creating your own subclasses, call `super` to forward any events that you don’t handle yourself, like in the following code.

**Swift**

```swift
super.touchesBegan(touches, with: event)
```

**Objective-C**

```objc
[super touchesBegan:touches withEvent:event];
```

If you override this method without calling `super` (a common use pattern), you must also override the other methods for handling touch events, even if your implementations do nothing.

> [!note] Note
> In iOS 17, Messages allows you to interactively resize iMessage apps with a vertical pan gesture. Messages handles any conflicts between resize gestures and your custom gestures. If your app uses manual touch handling, override those methods in your app’s [UIView](../uiview.md). You can either change your manual touch handling code to use a gesture recognizer instead, or your [UIView](../uiview.md) can override [- gestureRecognizerShouldBegin:](<../uigesturerecognizerdelegate/gesturerecognizershouldbegin(__).md>) and return NO when your iMessage app doesn’t own the gesture.

## See Also

### Responding to touch events

- [- touchesMoved:withEvent:](<touchesmoved(__with_).md>) — Tells the responder when one or more touches associated with an event changed.
- [- touchesEnded:withEvent:](<touchesended(__with_).md>) — Tells the responder when one or more fingers are raised from a view or window.
- [- touchesCancelled:withEvent:](<touchescancelled(__with_).md>) — Tells the responder when a system event (such as a system alert) cancels a touch sequence.
- [- touchesEstimatedPropertiesUpdated:](<touchesestimatedpropertiesupdated(__).md>) — Tells the responder that updated values were received for previously estimated properties or that an update is no longer expected.
