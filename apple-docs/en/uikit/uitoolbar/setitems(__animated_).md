---
title: 'setItems(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitoolbar/setitems(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbar/setitems(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbar/setitems%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:3d0b1acd6dc93fe7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolbar](../uitoolbar.md)

# setItems(_:animated:)

<sub>Instance Method</sub>

Sets the items on the toolbar by animating the changes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setItems(_ items: [UIBarButtonItem]?, animated: Bool)
```

## Parameters

- `items` — The items to display on the toolbar.

- `animated` — A Boolean value if set to [true](../../swift/true.md) animates the transition to the items; otherwise, does not.

## Discussion

If `animated` is [true](../../swift/true.md), the changes are dissolved or the reordering is animated—for example, removed items fade out and new items fade in. This method also adjusts the spacing between items.

## See Also

### Configuring toolbar items

- [items](items.md) — The items displayed on the toolbar.
