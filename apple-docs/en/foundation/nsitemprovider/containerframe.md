---
title: containerFrame
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemprovider/containerframe
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/containerframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/containerframe.json'
content_hash: 'sha256:f877231a5bbe816b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# containerFrame

<sub>Instance Property</sub>

The rectangle of the item’s visible content.

<sub>macOS</sub>

```swift
var containerFrame: NSRect { get }
```

## Discussion

The rectangle in this property corresponds to the onscreen frame rectangle of the item. This rectangle may or may not intersect the [sourceFrame](sourceframe.md) rectangle of the item. An intersection of the rectangles means that at least part of the item is visible onscreen.

The rectangle in this property may be a clipped version of the source frame or it might be [NSZeroRect](../nszerorect.md) if the item is offscreen or the system can’t determine the clipping rectangle. The system treats a value of [NSZeroRect](../nszerorect.md) as meaning the item is fully visible.

## See Also

### Getting the provider’s frame

- [sourceFrame](sourceframe.md) — The rectangle that the item occupies in the host app’s source window.
