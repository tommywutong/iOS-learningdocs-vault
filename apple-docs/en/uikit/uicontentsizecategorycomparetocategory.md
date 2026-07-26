---
title: UIContentSizeCategoryCompareToCategory
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentsizecategorycomparetocategory
source_url: 'https://developer.apple.com/documentation/uikit/uicontentsizecategorycomparetocategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentsizecategorycomparetocategory.json'
content_hash: 'sha256:6b19fb0d98d52337'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContentSizeCategoryCompareToCategory

<sub>Function</sub>

Compares two content size category values to determine whether they are equal or whether one is larger than the other.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSComparisonResult UIContentSizeCategoryCompareToCategory(UIContentSizeCategory lhs, UIContentSizeCategory rhs);
```

## See Also

### Retrieving content size category information

- [preferredContentSizeCategory](uitraitcollection/preferredcontentsizecategory.md) — The font sizing option preferred by the user.
- [UIContentSizeCategory](uicontentsizecategory.md) — Constants that indicate the preferred size of your content.
- [UIContentSizeCategoryIsAccessibilityCategory](uicontentsizecategoryisaccessibilitycategory.md) — Returns a Boolean value that indicates whether the content size category belongs to the group of accessibility-related sizes.
