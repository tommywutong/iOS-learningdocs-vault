---
title: adjustsFontForContentSizeCategory
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentsizecategoryadjusting/adjustsfontforcontentsizecategory
source_url: 'https://developer.apple.com/documentation/uikit/uicontentsizecategoryadjusting/adjustsfontforcontentsizecategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentsizecategoryadjusting/adjustsfontforcontentsizecategory.json'
content_hash: 'sha256:3eb9f88b654573e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentSizeCategoryAdjusting](../uicontentsizecategoryadjusting.md)

# adjustsFontForContentSizeCategory

<sub>Instance Property</sub>

A Boolean that indicates whether the object automatically updates its font when the device’s content size category changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var adjustsFontForContentSizeCategory: Bool { get set }
```

## Discussion

Set the value of this property to [true](../../swift/true.md) to allow the element to update its font when the size category changes. Set the value to [false](../../swift/false.md) to ignore the size category changes.

For this property to take effect, the element’s font must be vended one of the following ways:

- It must be vended using the [+ preferredFontForTextStyle:](<../uifont/preferredfont(fortextstyle_).md>) or [+ preferredFontForTextStyle:compatibleWithTraitCollection:](<../uifont/preferredfont(fortextstyle_compatiblewith_).md>) method with a valid text style.
- It must be vended using one of the scaling methods from [UIFontMetrics](../uifontmetrics.md).

Because fonts are immutable, any element that adjusts for an updated content size category doesn’t modify the font itself. Instead, the element replaces the assigned font with a new instance based on the original settings.

If you set this property to [true](../../swift/true.md), the element adjusts for a new content size category on a [UIContentSizeCategoryDidChangeNotification](../uicontentsizecategory/didchangenotification.md).
