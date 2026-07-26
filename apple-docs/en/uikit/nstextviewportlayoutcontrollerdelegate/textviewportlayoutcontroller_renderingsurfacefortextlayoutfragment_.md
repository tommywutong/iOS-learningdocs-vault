---
title: 'textViewportLayoutController:renderingSurfaceForTextLayoutFragment:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller:renderingsurfacefortextlayoutfragment:'
source_url: 'https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller:renderingsurfacefortextlayoutfragment:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller%3Arenderingsurfacefortextlayoutfragment%3A.json'
content_hash: 'sha256:9c3b6711be9e9c17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextViewportLayoutControllerDelegate](../nstextviewportlayoutcontrollerdelegate.md)

# textViewportLayoutController:renderingSurfaceForTextLayoutFragment:

<sub>Instance Method</sub>

Returns a rendering surface for the specified text layout fragment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (id<NSTextViewportRenderingSurface>) textViewportLayoutController:(NSTextViewportLayoutController *) textViewportLayoutController renderingSurfaceForTextLayoutFragment:(NSTextLayoutFragment *) textLayoutFragment;
```

## Parameters

- `textViewportLayoutController` — The viewport layout controller.

- `textLayoutFragment` — The layout fragment needing a rendering surface.

## Return Value

A rendering surface, or `nil`.

## Discussion

Invoked right before `textViewportLayoutController:configureRenderingSurfaceForTextLayoutFragment:`. The returned rendering surface is registered and mapped by `renderingSurfaceForKey:`.
