---
title: 'interactionDidEnd(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinteractiondelegate/interactiondidend(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinteractiondelegate/interactiondidend(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinteractiondelegate/interactiondidend%28_%3A%29.json'
content_hash: 'sha256:4896ca25fd019805'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInteractionDelegate](../uitextinteractiondelegate.md)

# interactionDidEnd(_:)

<sub>Instance Method</sub>

Tells the delegate that the text interaction ended.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func interactionDidEnd(_ interaction: UITextInteraction)
```

## Parameters

- `interaction` — The text interaction that called this method.

## See Also

### Handling text interaction events

- [- interactionShouldBegin:atPoint:](<interactionshouldbegin(__at_).md>) — Asks the delegate whether the text interaction should begin.
- [- interactionWillBegin:](<interactionwillbegin(__).md>) — Tells the delegate that the text interaction will begin.
