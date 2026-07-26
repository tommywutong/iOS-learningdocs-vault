---
title: 'motionBegan(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/motionbegan(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/motionbegan(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/motionbegan%28_%3Awith%3A%29.json'
content_hash: 'sha256:2d9f29c28163670b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# motionBegan(_:with:)

<sub>Instance Method</sub>

Tells the responder that a motion event has begun.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func motionBegan(_ motion: UIEvent.EventSubtype, with event: UIEvent?)
```

## Parameters

- `motion` — An event-subtype constant indicating the kind of motion. A common motion is shaking, which is indicated by [UIEventSubtypeMotionShake](../uievent/eventsubtype/motionshake.md).

- `event` — An object representing the event associated with the motion.

## Discussion

UIKit informs the responder only when a motion event starts and ends. It doesn’t report intermediate shakes. Motion events are delivered initially to the first responder and are forwarded up the responder chain as appropriate.

The default implementation of this method forwards the message up the responder chain.

## See Also

### Responding to motion events

- [- motionEnded:withEvent:](<motionended(__with_).md>) — Tells the responder that a motion event has ended.
- [- motionCancelled:withEvent:](<motioncancelled(__with_).md>) — Tells the responder that a motion event has been canceled.
