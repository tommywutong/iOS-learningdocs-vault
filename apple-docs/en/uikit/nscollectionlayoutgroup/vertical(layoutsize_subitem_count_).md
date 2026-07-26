---
title: 'vertical(layoutSize:subitem:count:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+（16.0 起废弃）, iPadOS 13.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, tvOS 13.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/nscollectionlayoutgroup/vertical(layoutsize:subitem:count:)'
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutgroup/vertical(layoutsize:subitem:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutgroup/vertical%28layoutsize%3Asubitem%3Acount%3A%29.json'
content_hash: 'sha256:5d9c5b27ab583b67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSCollectionLayoutGroup](../nscollectionlayoutgroup.md)

# vertical(layoutSize:subitem:count:)

<sub>Type Method</sub>

Creates a group of the specified size, containing an array of equally sized items arranged in a vertical line up to the number specified by count.

> [!warning] Deprecated
> Use [+ verticalGroupWithLayoutSize:repeatingSubitem:count:](<vertical(layoutsize_repeatingsubitem_count_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func vertical(layoutSize: NSCollectionLayoutSize, subitem: NSCollectionLayoutItem, count: Int) -> Self
```

## Discussion

When you set a value for the [interItemSpacing](interitemspacing.md) property after using this initializer, the group keeps the same number of items and automatically resizes them to add the extra specified spacing between them.

## See Also

### Deprecated

- [+ horizontalGroupWithLayoutSize:subitem:count:](<horizontal(layoutsize_subitem_count_).md>) — Creates a group of the specified size, containing an array of equally sized items arranged in a horizontal line up to the number specified by count. _(deprecated)_
- [horizontalGroup(with:repeatingSubitem:count:)](<horizontalgroup(with_repeatingsubitem_count_).md>) — Creates a group that repeats the specified subitem a certain number of times along the horizontal axis. _(deprecated)_
- [verticalGroup(with:repeatingSubitem:count:)](<verticalgroup(with_repeatingsubitem_count_).md>) — Creates a group that repeats the specified subitem a certain number of times along the vertical axis. _(deprecated)_
