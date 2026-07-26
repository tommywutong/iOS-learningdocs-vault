---
title: 'pencilInteractionDidTap(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.1+（17.5 起废弃）, iPadOS 12.1+（17.5 起废弃）, Mac Catalyst 13.1+（17.5 起废弃）, visionOS 1.0+（1.2 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipencilinteractiondelegate/pencilinteractiondidtap(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipencilinteractiondelegate/pencilinteractiondidtap(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipencilinteractiondelegate/pencilinteractiondidtap%28_%3A%29.json'
content_hash: 'sha256:cb4159766bc7f45e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPencilInteractionDelegate](../uipencilinteractiondelegate.md)

# pencilInteractionDidTap(_:)

<sub>Instance Method</sub>

Tells the delegate that the user double-tapped Apple Pencil.

> [!warning] Deprecated
> Use [- pencilInteraction:didReceiveTap:](<pencilinteraction(__didreceivetap_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func pencilInteractionDidTap(_ interaction: UIPencilInteraction)
```

## Discussion

When handling the double tap, perform either:

- The action selected by the user in the Settings app, as specified by the [preferredTapAction](../uipencilinteraction/preferredtapaction.md) class property.
- An alternative behavior that gives the user the best experience for your app. Should you decide to support an alternative, provide an intuitive way for the user to learn about and enable that behavior.
