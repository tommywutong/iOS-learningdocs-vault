---
title: 'verticalGroup(with:repeatingSubitem:count:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+（16.0 起废弃）, iPadOS 16.0+（16.0 起废弃）, Mac Catalyst 16.0+（16.0 起废弃）, tvOS, visionOS]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/uikit/nscollectionlayoutgroup/verticalgroup(with:repeatingsubitem:count:)'
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutgroup/verticalgroup(with:repeatingsubitem:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutgroup/verticalgroup%28with%3Arepeatingsubitem%3Acount%3A%29.json'
content_hash: 'sha256:00d71f086e60b1b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSCollectionLayoutGroup](../nscollectionlayoutgroup.md)

# verticalGroup(with:repeatingSubitem:count:)

<sub>Type Method</sub>

Creates a group that repeats the specified subitem a certain number of times along the vertical axis.

> [!warning] Deprecated
> Use [+ verticalGroupWithLayoutSize:repeatingSubitem:count:](<vertical(layoutsize_repeatingsubitem_count_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency class func verticalGroup(with size: NSCollectionLayoutSize, repeatingSubitem subitem: NSCollectionLayoutItem, count: Int) -> NSCollectionLayoutGroup
```

## See Also

### Deprecated

- [+ horizontalGroupWithLayoutSize:subitem:count:](<horizontal(layoutsize_subitem_count_).md>) — Creates a group of the specified size, containing an array of equally sized items arranged in a horizontal line up to the number specified by count. _(deprecated)_
- [horizontalGroup(with:repeatingSubitem:count:)](<horizontalgroup(with_repeatingsubitem_count_).md>) — Creates a group that repeats the specified subitem a certain number of times along the horizontal axis. _(deprecated)_
- [+ verticalGroupWithLayoutSize:subitem:count:](<vertical(layoutsize_subitem_count_).md>) — Creates a group of the specified size, containing an array of equally sized items arranged in a vertical line up to the number specified by count. _(deprecated)_
