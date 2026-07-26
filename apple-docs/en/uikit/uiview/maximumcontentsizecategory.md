---
title: maximumContentSizeCategory
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/maximumcontentsizecategory
source_url: 'https://developer.apple.com/documentation/uikit/uiview/maximumcontentsizecategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/maximumcontentsizecategory.json'
content_hash: 'sha256:7336dfdc472d6f44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# maximumContentSizeCategory

<sub>Instance Property</sub>

The maximum content size category for the view and its subviews.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var maximumContentSizeCategory: UIContentSizeCategory? { get set }
```

## Discussion

Use this property to limit which content size categories your view hierarchy supports. The limit applies immediately after you set this value and when future content size category updates occur.

Set this property to `nil` to remove the maximum limit for the content size category.

## See Also

### Managing font-sizing preferences

- [minimumContentSizeCategory](minimumcontentsizecategory.md) — The minimum content size category for the view and its subviews.
- [appliedContentSizeCategoryLimitsDescription](appliedcontentsizecategorylimitsdescription.md) — A string that lists each of the view’s superviews, its content size category, and whether that view has content size category limits.
