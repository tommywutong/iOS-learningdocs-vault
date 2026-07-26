---
title: UIAccessibilityContentSizeCategoryImageAdjusting
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycontentsizecategoryimageadjusting
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycontentsizecategoryimageadjusting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycontentsizecategoryimageadjusting.json'
content_hash: 'sha256:6e4b4834110c67cc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityContentSizeCategoryImageAdjusting

<sub>Protocol</sub>

Methods to determine when to adjust images for different content size categories.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol UIAccessibilityContentSizeCategoryImageAdjusting : NSObjectProtocol
```

## Overview

Objects adopt this protocol when they support scaling image assets to the size required by the accessibility content size categories. Typically, an object sets the [adjustsImageSizeForAccessibilityContentSizeCategory](uiaccessibilitycontentsizecategoryimageadjusting/adjustsimagesizeforaccessibilitycontentsizecategory.md) property to [true](../swift/true.md) only when its image contains vector data that can scale well to the larger sizes required for accessibility.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [NSTextAttachment](nstextattachment.md), [UIButton](uibutton.md), [UIImageView](uiimageview.md)

## Topics

### Preferring accessibility-specific images

- [adjustsImageSizeForAccessibilityContentSizeCategory](uiaccessibilitycontentsizecategoryimageadjusting/adjustsimagesizeforaccessibilitycontentsizecategory.md) — A Boolean value that indicates whether the image size increases to support accessibility content size categories.

## See Also

### Behaviors

- [UIAccessibilityFocus](../objectivec/uiaccessibilityfocus.md) — An informal protocol that provides a way to determine whether an assistive app, such as VoiceOver, has focus on an accessible element.
- [UIAccessibilityIdentification](uiaccessibilityidentification.md) — Methods that associate a unique identifier with elements in your user interface.
- [UIAccessibilityReadingContent](uiaccessibilityreadingcontent.md) — Methods to implement for an object that represents content that users read, such as a book or an article.
- [UIAccessibilityTextualContext](uiaccessibilitytextualcontext.md) — Constants that describe a named context that helps identify and classify the type of text inside an element.
