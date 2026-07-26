---
title: 'horizontal(layoutSize:repeatingSubitem:count:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nscollectionlayoutgroup/horizontal(layoutsize:repeatingsubitem:count:)'
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutgroup/horizontal(layoutsize:repeatingsubitem:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutgroup/horizontal%28layoutsize%3Arepeatingsubitem%3Acount%3A%29.json'
content_hash: 'sha256:574552f40e97f458'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSCollectionLayoutGroup](../nscollectionlayoutgroup.md)

# horizontal(layoutSize:repeatingSubitem:count:)

<sub>Type Method</sub>

Creates a group that repeats the specified subitem a certain number of times along the horizontal axis.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func horizontal(layoutSize: NSCollectionLayoutSize, repeatingSubitem subitem: NSCollectionLayoutItem, count: Int) -> Self
```

## Parameters

- `layoutSize` — The group’s size.

- `subitem` — The subitem to repeat. It’s your responsibility to ensure that the group’s `layoutSize` can fit `count` repetitions of this item.

- `count` — The number of times to repeat the subitem.

## See Also

### Creating a horizontal group

- [+ horizontalGroupWithLayoutSize:subitems:](<horizontal(layoutsize_subitems_).md>) — Creates a group of the specified size, containing an array of items arranged in a horizontal line.
