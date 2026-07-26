---
title: safeAreaAspectFitLayoutGuide
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindow/safeareaaspectfitlayoutguide
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/safeareaaspectfitlayoutguide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/safeareaaspectfitlayoutguide.json'
content_hash: 'sha256:2c9956bde09fc699'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# safeAreaAspectFitLayoutGuide

<sub>Instance Property</sub>

A layout guide for placing content of a particular aspect ratio.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var safeAreaAspectFitLayoutGuide: any UILayoutGuide & UILayoutGuideAspectFitting { get }
```

## Discussion

This layout guide provides a centered region in the window where you can place media content of a particular aspect ratio (width over height) to avoid obscuring the content.

> [!important] Important
> Use this layout guide for full-screen content. Avoid adding constraints to the guide through deeply nested view hierarchies.

## See Also

### Working with layout guides

- [UILayoutGuideAspectFitting](../uilayoutguideaspectfitting.md) — The interface for a layout guide that supports a particular aspect ratio.
