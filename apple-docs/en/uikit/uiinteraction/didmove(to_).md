---
title: 'didMove(to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiinteraction/didmove(to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiinteraction/didmove(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinteraction/didmove%28to%3A%29.json'
content_hash: 'sha256:9047f32b07060cae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInteraction](../uiinteraction.md)

# didMove(to:)

<sub>Instance Method</sub>

Tells the interaction that a view added or removed it from the view’s interactions array.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func didMove(to view: UIView?)
```

## Parameters

- `view` — The view that owns and contains the interaction in its interaction array. If the view is `nil`, the interaction’s owner removed the interaction from its interactions array.

## See Also

### Tracking the Movements

- [- willMoveToView:](<willmove(to_).md>) — Tells the interaction that a view will add or remove it from the view’s interactions array.
