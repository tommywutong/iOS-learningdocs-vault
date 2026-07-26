---
title: 'motionCancelled(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/motioncancelled(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/motioncancelled(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/motioncancelled%28_%3Awith%3A%29.json'
content_hash: 'sha256:d21f5f15be548473'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# motionCancelled(_:with:)

<sub>Instance Method</sub>

Tells the responder that a motion event has been canceled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func motionCancelled(_ motion: UIEvent.EventSubtype, with event: UIEvent?)
```

## Parameters

- `motion` — An event-subtype constant indicating the kind of motion associated with `event`. A common motion is shaking, which is indicated by [UIEventSubtypeMotionShake](../uievent/eventsubtype/motionshake.md).

- `event` — An object representing the event associated with the motion.

## Discussion

UIKit calls this method when it receives an interruption requiring cancellation of the motion event. An interruption is anything that causes the application to become inactive or causes the view handling the motion events to be removed from its window. UIKit might also call this method if the shaking goes on too long. All responders that handle motion events should implement this method. In your implementation, clean up any state information associated with handling the motion events.

The default implementation of this method forwards the message up the responder chain.

## See Also

### Responding to motion events

- [- motionBegan:withEvent:](<motionbegan(__with_).md>) — Tells the responder that a motion event has begun.
- [- motionEnded:withEvent:](<motionended(__with_).md>) — Tells the responder that a motion event has ended.
