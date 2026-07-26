---
title: 'pressesChanged(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/presseschanged(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/presseschanged(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/presseschanged%28_%3Awith%3A%29.json'
content_hash: 'sha256:9b0698ce7b5cfc76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# pressesChanged(_:with:)

<sub>Instance Method</sub>

Tells this object when a value associated with a press has changed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func pressesChanged(_ presses: Set<UIPress>, with event: UIPressesEvent?)
```

## Parameters

- `presses` — A set of [UIPress](../uipress.md) instances containing changed values.

- `event` — The event to which the presses belong.

## Discussion

UIKit calls this method when an analog value associated with a button or thumbstick changes. For example, it calls this method when the analog force value of a push button changes. Use this method to take any needed actions in response to the change.

The default implementation of this method forwards the message up the responder chain. When creating your own subclasses, call `super` to forward any events that you don’t handle yourself.

## See Also

### Responding to press events

- [- pressesBegan:withEvent:](<pressesbegan(__with_).md>) — Tells this object when a physical button is first pressed.
- [- pressesEnded:withEvent:](<pressesended(__with_).md>) — Tells the object when a button is released.
- [- pressesCancelled:withEvent:](<pressescancelled(__with_).md>) — Tells this object when a system event (such as a low-memory warning) cancels a press event.
