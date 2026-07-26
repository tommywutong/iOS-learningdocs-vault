---
title: 'interactionDidFinish(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uispringloadedinteractionbehavior/interactiondidfinish(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uispringloadedinteractionbehavior/interactiondidfinish(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uispringloadedinteractionbehavior/interactiondidfinish%28_%3A%29.json'
content_hash: 'sha256:a089edfd7cd7e579'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISpringLoadedInteractionBehavior](../uispringloadedinteractionbehavior.md)

# interactionDidFinish(_:)

<sub>Instance Method</sub>

Tells the behavior object when the spring-loading interaction is finished, either because it was canceled or because spring loading was activated.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func interactionDidFinish(_ interaction: UISpringLoadedInteraction)
```

## Parameters

- `interaction` — The spring-loaded interaction requesting the information.
