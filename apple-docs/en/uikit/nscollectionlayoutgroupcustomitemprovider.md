---
title: NSCollectionLayoutGroupCustomItemProvider
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutgroupcustomitemprovider
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutgroupcustomitemprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutgroupcustomitemprovider.json'
content_hash: 'sha256:f59307003bccd6ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSCollectionLayoutGroupCustomItemProvider

<sub>Type Alias</sub>

A closure that creates and returns each of the custom group’s items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias NSCollectionLayoutGroupCustomItemProvider = (any NSCollectionLayoutEnvironment) -> [NSCollectionLayoutGroupCustomItem]
```

## Discussion

You use a custom item provider to supply the item arrangement when creating a group using the [+ customGroupWithLayoutSize:itemProvider:](<nscollectionlayoutgroup/custom(layoutsize_itemprovider_).md>) initializer.

## See Also

### Advanced layouts

- [NSCollectionLayoutGroupCustomItem](nscollectionlayoutgroupcustomitem.md) — An item used in a group with a custom layout arrangement.
