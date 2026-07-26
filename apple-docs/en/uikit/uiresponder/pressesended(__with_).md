---
title: 'pressesEnded(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/pressesended(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/pressesended(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/pressesended%28_%3Awith%3A%29.json'
content_hash: 'sha256:a8c5d310fcc9a092'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# pressesEnded(_:with:)

<sub>Instance Method</sub>

Tells the object when a button is released.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func pressesEnded(_ presses: Set<UIPress>, with event: UIPressesEvent?)
```

## Parameters

- `presses` — A set of [UIPress](../uipress.md) instances that represent the buttons that the user is no longer pressing. The phase of each press is set to [UIPressPhaseEnded](../uipress/phase-swift.enum/ended.md).

- `event` — The event to which the presses belong.

## Discussion

UIKit calls this method when the user stops pressing one or more buttons. Use this method to take any needed actions in response to the end of the press.The default implementation of this method forwards the message up the responder chain. When creating your own subclasses, call `super` to forward any events that you don’t handle yourself.

## See Also

### Responding to press events

- [- pressesBegan:withEvent:](<pressesbegan(__with_).md>) — Tells this object when a physical button is first pressed.
- [- pressesChanged:withEvent:](<presseschanged(__with_).md>) — Tells this object when a value associated with a press has changed.
- [- pressesCancelled:withEvent:](<pressescancelled(__with_).md>) — Tells this object when a system event (such as a low-memory warning) cancels a press event.
