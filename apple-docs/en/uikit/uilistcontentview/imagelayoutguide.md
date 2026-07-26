---
title: imageLayoutGuide
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentview/imagelayoutguide
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentview/imagelayoutguide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentview/imagelayoutguide.json'
content_hash: 'sha256:cf3b22f360144893'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentView](../uilistcontentview.md)

# imageLayoutGuide

<sub>Instance Property</sub>

A guide for positioning the image in the content view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var imageLayoutGuide: UILayoutGuide? { get }
```

## Discussion

If the configuration doesn’t specify an image, the value of this property is `nil`.

If you apply a new configuration without secondary text to the content view, the system removes this layout guide from the view and deactivates any constraints associated with it.

## See Also

### Managing the content layout

- [textLayoutGuide](textlayoutguide.md) — A guide for positioning the primary text in the content view.
- [secondaryTextLayoutGuide](secondarytextlayoutguide.md) — A guide for positioning the secondary text in the content view.
