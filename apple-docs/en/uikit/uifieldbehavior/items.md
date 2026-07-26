---
title: items
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifieldbehavior/items
source_url: 'https://developer.apple.com/documentation/uikit/uifieldbehavior/items'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifieldbehavior/items.json'
content_hash: 'sha256:8ea3ac12b399af85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFieldBehavior](../uifieldbehavior.md)

# items

<sub>Instance Property</sub>

The dynamic items associated with the current field behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var items: [any UIDynamicItem] { get }
```

## Discussion

When it is enabled, the current field applies its behavior to all of the items in the array.

## See Also

### Managing the associated dynamic items

- [- addItem:](<additem(__).md>) — Associates the field behavior with the specified dynamic item.
- [- removeItem:](<removeitem(__).md>) — Removes the field behavior from the specified dynamic item.
