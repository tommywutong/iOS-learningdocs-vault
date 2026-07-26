---
title: 'textViewportLayoutController(_:retrieveCachedRenderingSurfaceFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:retrievecachedrenderingsurfacefor:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:retrievecachedrenderingsurfacefor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller%28_%3Aretrievecachedrenderingsurfacefor%3A%29.json'
content_hash: 'sha256:a52ec19c90886144'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextViewportLayoutControllerDelegate](../nstextviewportlayoutcontrollerdelegate.md)

# textViewportLayoutController(_:retrieveCachedRenderingSurfaceFor:)

<sub>Instance Method</sub>

Asks the delegate to return a previously cached rendering surface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textViewportLayoutController(_ textViewportLayoutController: NSTextViewportLayoutController, retrieveCachedRenderingSurfaceFor renderingSurfaceKey: any NSTextViewportRenderingSurfaceKey) -> any NSTextViewportRenderingSurface
```

## Parameters

- `textViewportLayoutController` — The viewport layout controller.

- `renderingSurfaceKey` — The key identifying the rendering surface.

## Return Value

The cached rendering surface, or `nil`.

## See Also

### Storing rendering surfaces

- [- textViewportLayoutController:cacheRenderingSurface:forKey:](<textviewportlayoutcontroller(__cacherenderingsurface_for_).md>) — Asks the delegate to cache a rendering surface for later retrieval.
