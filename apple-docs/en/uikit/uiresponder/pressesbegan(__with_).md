---
title: 'pressesBegan(_:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/pressesbegan(_:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/pressesbegan(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/pressesbegan%28_%3Awith%3A%29.json'
content_hash: 'sha256:d93693f3049626c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# pressesBegan(_:with:)

<sub>Instance Method</sub>

Tells this object when a physical button is first pressed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func pressesBegan(_ presses: Set<UIPress>, with event: UIPressesEvent?)
```

## Parameters

- `presses` — A set of [UIPress](../uipress.md) instances that represent the new presses that occurred. The phase of each press is set to [UIPressPhaseBegan](../uipress/phase-swift.enum/began.md).

- `event` — The event to which the presses belong.

## Discussion

UIKit calls this method when a new button is pressed by the user. Use this method to determine which button was pressed and to take any needed actions.

The default implementation of this method forwards the message up the responder chain. When creating your own subclasses, call `super` to forward any events that you don’t handle yourself.

## See Also

### Responding to press events

- [- pressesChanged:withEvent:](<presseschanged(__with_).md>) — Tells this object when a value associated with a press has changed.
- [- pressesEnded:withEvent:](<pressesended(__with_).md>) — Tells the object when a button is released.
- [- pressesCancelled:withEvent:](<pressescancelled(__with_).md>) — Tells this object when a system event (such as a low-memory warning) cancels a press event.
