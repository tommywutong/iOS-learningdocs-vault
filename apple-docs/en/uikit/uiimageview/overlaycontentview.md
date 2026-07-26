---
title: overlayContentView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageview/overlaycontentview
source_url: 'https://developer.apple.com/documentation/uikit/uiimageview/overlaycontentview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageview/overlaycontentview.json'
content_hash: 'sha256:bd0508c4dd226453'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImageView](../uiimageview.md)

# overlayContentView

<sub>Instance Property</sub>

A view for hosting layered content on top of the image view.

<sub>tvOS</sub>

```swift
var overlayContentView: UIView { get }
```

## Discussion

Use this view to host content that you want layered on top of the image view. This view is managed by the image view itself and is automatically sized to fill the image view’s frame rectangle. Add your subviews and use layout constraints to position them within the view. When the [adjustsImageWhenAncestorFocused](adjustsimagewhenancestorfocused.md) property is [true](../../swift/true.md), the overlay view receives the same floating effects as the image view when it’s focused.

The view in this property clips its subviews to its bounds rectangle by default, but you can change that behavior using the [clipsToBounds](../uiview/clipstobounds.md) property.
