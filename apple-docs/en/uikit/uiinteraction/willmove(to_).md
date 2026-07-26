---
title: 'willMove(to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiinteraction/willmove(to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiinteraction/willmove(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinteraction/willmove%28to%3A%29.json'
content_hash: 'sha256:5e85db1ce2c41377'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInteraction](../uiinteraction.md)

# willMove(to:)

<sub>Instance Method</sub>

Tells the interaction that a view will add or remove it from the view’s interactions array.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func willMove(to view: UIView?)
```

## Parameters

- `view` — The view that will contain, and own, the interaction in its interactions array. If the view is `nil`, the interaction’s owner will remove the interaction from its interactions array.

## See Also

### Tracking the Movements

- [- didMoveToView:](<didmove(to_).md>) — Tells the interaction that a view added or removed it from the view’s interactions array.
