---
title: adjustsImageSizeForAccessibilityContentSizeCategory
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycontentsizecategoryimageadjusting/adjustsimagesizeforaccessibilitycontentsizecategory
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycontentsizecategoryimageadjusting/adjustsimagesizeforaccessibilitycontentsizecategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycontentsizecategoryimageadjusting/adjustsimagesizeforaccessibilitycontentsizecategory.json'
content_hash: 'sha256:c6ca387a62ab656d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityContentSizeCategoryImageAdjusting](../uiaccessibilitycontentsizecategoryimageadjusting.md)

# adjustsImageSizeForAccessibilityContentSizeCategory

<sub>Instance Property</sub>

A Boolean value that indicates whether the image size increases to support accessibility content size categories.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor var adjustsImageSizeForAccessibilityContentSizeCategory: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), the current object scales its image to an appropriate accessibility content size category. When the value of this property is [false](../../swift/false.md), the current object displays its image at the regular content sizes.
