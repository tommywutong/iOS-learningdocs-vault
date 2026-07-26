---
title: preferredContentSizeCategory
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitcollection/preferredcontentsizecategory
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/preferredcontentsizecategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/preferredcontentsizecategory.json'
content_hash: 'sha256:a14d58b28e3c1475'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# preferredContentSizeCategory

<sub>Instance Property</sub>

The font sizing option preferred by the user.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredContentSizeCategory: UIContentSizeCategory { get }
```

## Discussion

With Dynamic Type, users can ask that apps display text using fonts that are larger or smaller than the normal font size defined by the system. For example, a user with a visual impairment might request a larger default font size to make it easier to read text. Use the value of this property to request a [UIFont](../uifont.md) object that matches the user’s requested size.

## See Also

### Retrieving content size category information

- [UIContentSizeCategory](../uicontentsizecategory.md) — Constants that indicate the preferred size of your content.
