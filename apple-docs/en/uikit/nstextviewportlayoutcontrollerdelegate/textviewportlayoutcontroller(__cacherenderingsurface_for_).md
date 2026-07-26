---
title: 'textViewportLayoutController(_:cacheRenderingSurface:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:cacherenderingsurface:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:cacherenderingsurface:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller%28_%3Acacherenderingsurface%3Afor%3A%29.json'
content_hash: 'sha256:08fb1a4d6b49b219'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextViewportLayoutControllerDelegate](../nstextviewportlayoutcontrollerdelegate.md)

# textViewportLayoutController(_:cacheRenderingSurface:for:)

<sub>Instance Method</sub>

Asks the delegate to cache a rendering surface for later retrieval.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textViewportLayoutController(_ textViewportLayoutController: NSTextViewportLayoutController, cacheRenderingSurface renderingSurface: any NSTextViewportRenderingSurface, for renderingSurfaceKey: any NSTextViewportRenderingSurfaceKey)
```

## Parameters

- `textViewportLayoutController` — The viewport layout controller.

- `renderingSurface` — The rendering surface to cache.

- `renderingSurfaceKey` — The key identifying the rendering surface.

## See Also

### Storing rendering surfaces

- [- textViewportLayoutController:retrieveCachedRenderingSurfaceForKey:](<textviewportlayoutcontroller(__retrievecachedrenderingsurfacefor_).md>) — Asks the delegate to return a previously cached rendering surface.
