---
title: items
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitoolbar/items
source_url: 'https://developer.apple.com/documentation/uikit/uitoolbar/items'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitoolbar/items.json'
content_hash: 'sha256:92402c257d0cd391'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIToolbar](../uitoolbar.md)

# items

<sub>Instance Property</sub>

The items displayed on the toolbar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var items: [UIBarButtonItem]? { get set }
```

## Discussion

The items, instances of [UIBarButtonItem](../uibarbuttonitem.md), that are visible on the toolbar in the order they appear in this array. Any changes to this property aren’t animated. Use the [- setItems:animated:](<setitems(__animated_).md>) method to animate changes.

The default value is `nil`.

## See Also

### Configuring toolbar items

- [- setItems:animated:](<setitems(__animated_).md>) — Sets the items on the toolbar by animating the changes.
