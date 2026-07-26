---
title: minimumContentSizeCategory
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/minimumcontentsizecategory
source_url: 'https://developer.apple.com/documentation/uikit/uiview/minimumcontentsizecategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/minimumcontentsizecategory.json'
content_hash: 'sha256:ed21bd9c59d54093'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# minimumContentSizeCategory

<sub>Instance Property</sub>

The minimum content size category for the view and its subviews.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var minimumContentSizeCategory: UIContentSizeCategory? { get set }
```

## Discussion

Use this property to limit which content size categories your view hierarchy supports. The limit applies immediately after you set this value and when future content size category updates occur.

Set this property to `nil` to remove the minimum limit for the content size category.

## See Also

### Managing font-sizing preferences

- [maximumContentSizeCategory](maximumcontentsizecategory.md) — The maximum content size category for the view and its subviews.
- [appliedContentSizeCategoryLimitsDescription](appliedcontentsizecategorylimitsdescription.md) — A string that lists each of the view’s superviews, its content size category, and whether that view has content size category limits.
