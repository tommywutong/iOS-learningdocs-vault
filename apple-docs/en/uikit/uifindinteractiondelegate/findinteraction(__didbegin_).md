---
title: 'findInteraction(_:didBegin:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifindinteractiondelegate/findinteraction(_:didbegin:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifindinteractiondelegate/findinteraction(_:didbegin:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindinteractiondelegate/findinteraction%28_%3Adidbegin%3A%29.json'
content_hash: 'sha256:38ea60f8b1e0d56a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFindInteractionDelegate](../uifindinteractiondelegate.md)

# findInteraction(_:didBegin:)

<sub>Instance Method</sub>

Informs the delegate when the interaction is about to present the find panel.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func findInteraction(_ interaction: UIFindInteraction, didBegin session: UIFindSession)
```

## Parameters

- `interaction` — The interaction object triggering the find panel.

- `session` — The session object you provided for the interaction.

## Discussion

Use this method to decorate your view to indicate that a search operation is about to occur. For example, apply a dimming view around the unhighlighted search results.

## See Also

### Decorating the searched content

- [- findInteraction:didEndFindSession:](<findinteraction(__didend_).md>) — Informs the delegate when the interaction is about to dismiss the find panel.
