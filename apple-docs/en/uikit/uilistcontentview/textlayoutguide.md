---
title: textLayoutGuide
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentview/textlayoutguide
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentview/textlayoutguide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentview/textlayoutguide.json'
content_hash: 'sha256:738f23a7177d7a95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentView](../uilistcontentview.md)

# textLayoutGuide

<sub>Instance Property</sub>

A guide for positioning the primary text in the content view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var textLayoutGuide: UILayoutGuide? { get }
```

## Discussion

If the configuration doesn’t specify primary text, the value of this property is `nil`.

If you apply a new configuration without primary text to the content view, the system removes this layout guide from the view and deactivates any constraints associated with it.

## See Also

### Managing the content layout

- [secondaryTextLayoutGuide](secondarytextlayoutguide.md) — A guide for positioning the secondary text in the content view.
- [imageLayoutGuide](imagelayoutguide.md) — A guide for positioning the image in the content view.
