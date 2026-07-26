---
title: 'interactionShouldBegin(_:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinteractiondelegate/interactionshouldbegin(_:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinteractiondelegate/interactionshouldbegin(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinteractiondelegate/interactionshouldbegin%28_%3Aat%3A%29.json'
content_hash: 'sha256:8eae1c9b5d182e1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInteractionDelegate](../uitextinteractiondelegate.md)

# interactionShouldBegin(_:at:)

<sub>Instance Method</sub>

Asks the delegate whether the text interaction should begin.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func interactionShouldBegin(_ interaction: UITextInteraction, at point: CGPoint) -> Bool
```

## Parameters

- `interaction` — The text interaction that called this method.

- `point` — The position on the screen where the user is touching.

## Return Value

A Boolean value indicating whether the interaction should begin. Return [true](../../swift/true.md) to let the interaction begin; otherwise, return [false](../../swift/false.md) to prevent the interaction from beginning.

## See Also

### Handling text interaction events

- [- interactionWillBegin:](<interactionwillbegin(__).md>) — Tells the delegate that the text interaction will begin.
- [- interactionDidEnd:](<interactiondidend(__).md>) — Tells the delegate that the text interaction ended.
