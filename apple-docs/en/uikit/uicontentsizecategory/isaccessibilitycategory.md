---
title: isAccessibilityCategory
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, tvOS 11.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentsizecategory/isaccessibilitycategory
source_url: 'https://developer.apple.com/documentation/uikit/uicontentsizecategory/isaccessibilitycategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentsizecategory/isaccessibilitycategory.json'
content_hash: 'sha256:fba95a6e7898868f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentSizeCategory](../uicontentsizecategory.md)

# isAccessibilityCategory

<sub>Instance Property</sub>

A Boolean value that indicates whether the content size category is associated with accessibility.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isAccessibilityCategory: Bool { get }
```

## Discussion

This property is [true](../../swift/true.md) for [UIContentSizeCategoryAccessibilityMedium](accessibilitymedium.md), [UIContentSizeCategoryAccessibilityLarge](accessibilitylarge.md), [UIContentSizeCategoryAccessibilityExtraLarge](accessibilityextralarge.md), [UIContentSizeCategoryAccessibilityExtraExtraLarge](accessibilityextraextralarge.md), and [UIContentSizeCategoryAccessibilityExtraExtraExtraLarge](accessibilityextraextraextralarge.md). It is [false](../../swift/false.md) for other values.

## See Also

### Accessibility sizes

- [UIContentSizeCategoryAccessibilityMedium](accessibilitymedium.md) — A medium font size that reflects the current accessibility settings.
- [UIContentSizeCategoryAccessibilityLarge](accessibilitylarge.md) — A large font size that reflects the current accessibility settings.
- [UIContentSizeCategoryAccessibilityExtraLarge](accessibilityextralarge.md) — An extra-large font size that reflects the current accessibility settings.
- [UIContentSizeCategoryAccessibilityExtraExtraLarge](accessibilityextraextralarge.md) — A font that is larger than the extra-large font but not the largest available, reflecting the current accessibility settings.
- [UIContentSizeCategoryAccessibilityExtraExtraExtraLarge](accessibilityextraextraextralarge.md) — The largest font size that reflects the current accessibility settings.
