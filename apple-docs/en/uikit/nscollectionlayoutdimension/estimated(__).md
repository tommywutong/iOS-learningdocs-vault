---
title: 'estimated(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nscollectionlayoutdimension/estimated(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutdimension/estimated(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutdimension/estimated%28_%3A%29.json'
content_hash: 'sha256:c764196475c7998f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSCollectionLayoutDimension](../nscollectionlayoutdimension.md)

# estimated(_:)

<sub>Type Method</sub>

Creates a dimension with an estimated point value.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func estimated(_ estimatedDimension: CGFloat) -> Self
```

## Discussion

The final size of the dimension is determined when the content is rendered.

## See Also

### Creating a dimension

- [+ absoluteDimension:](<absolute(__).md>) — Creates a dimension with an absolute point value.
- [+ fractionalHeightDimension:](<fractionalheight(__).md>) — Creates a dimension that is computed as a fraction of the height of the containing group.
- [+ fractionalWidthDimension:](<fractionalwidth(__).md>) — Creates a dimension that is computed as a fraction of the width of the containing group.
- [+ uniformAcrossSiblingsWithEstimate:](<uniformacrosssiblings(estimate_).md>) — Creates a dimension in which each item receives as much room as it requires and grows to match the dimension of its largest sibling.
