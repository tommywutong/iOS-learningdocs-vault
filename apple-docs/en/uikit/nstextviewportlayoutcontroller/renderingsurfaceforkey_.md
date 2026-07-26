---
title: 'renderingSurfaceForKey:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextviewportlayoutcontroller/renderingsurfaceforkey:'
source_url: 'https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontroller/renderingsurfaceforkey:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextviewportlayoutcontroller/renderingsurfaceforkey%3A.json'
content_hash: 'sha256:94eb18e66a1740f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextViewportLayoutController](../nstextviewportlayoutcontroller.md)

# renderingSurfaceForKey:

<sub>Instance Method</sub>

Returns a rendering surface corresponding to the specified key.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (id<NSTextViewportRenderingSurface>) renderingSurfaceForKey:(id<NSTextViewportRenderingSurfaceKey>) key;
```

## Parameters

- `key` — The key identifying the rendering surface.

## Return Value

The rendering surface, or `nil`.

## Discussion

The mapping is registered via the returned rendering surfaces from `textViewportLayoutController:renderingSurfaceForTextLayoutFragment:`. In addition, it can return auxiliary rendering surfaces registered through `addRenderingSurface:key:group:placement:`. The mappings are cleared at the beginning of each [- layoutViewport](<layoutviewport().md>).
