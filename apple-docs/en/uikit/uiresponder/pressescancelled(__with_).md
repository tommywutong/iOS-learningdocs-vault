---
title: 'pressesCancelled(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/pressescancelled(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/pressescancelled(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/pressescancelled%28_%3Awith%3A%29.json'
content_hash: 'sha256:832d9f92905166c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# pressesCancelled(_:with:)

<sub>Instance Method</sub>

Tells this object when a system event (such as a low-memory warning) cancels a press event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func pressesCancelled(_ presses: Set<UIPress>, with event: UIPressesEvent?)
```

## Parameters

- `presses` — A set of [UIPress](../uipress.md) instances that represent the presses associated with the event. The phase of each press is set to [UIPressPhaseCancelled](../uipress/phase-swift.enum/cancelled.md).

- `event` — The event to which the presses belong.

## Discussion

UIKit calls this method when it receives a system interruption requiring cancellation of the press sequence. An interruption is anything that causes the application to become inactive or causes the view handling the press events to be removed from its window. Your implementation of this method should clean up any state associated with handling the press sequence. Failure to handle cancellation is likely to lead to incorrect behavior or crashes.

The default implementation of this method forwards the message up the responder chain. When creating your own subclasses, call `super` to forward any events that you don’t handle yourself.

## See Also

### Responding to press events

- [- pressesBegan:withEvent:](<pressesbegan(__with_).md>) — Tells this object when a physical button is first pressed.
- [- pressesChanged:withEvent:](<presseschanged(__with_).md>) — Tells this object when a value associated with a press has changed.
- [- pressesEnded:withEvent:](<pressesended(__with_).md>) — Tells the object when a button is released.
