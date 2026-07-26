---
title: sourceFrame
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemprovider/sourceframe
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider/sourceframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider/sourceframe.json'
content_hash: 'sha256:792956f0959541de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProvider](../nsitemprovider.md)

# sourceFrame

<sub>Instance Property</sub>

The rectangle that the item occupies in the host app’s source window.

<sub>macOS</sub>

```swift
var sourceFrame: NSRect { get }
```

## Discussion

This property contains the rectangle, in screen coordinates, that encloses the item. This rectangle includes areas that might be clipped and not currently visible onscreen.

## See Also

### Getting the provider’s frame

- [containerFrame](containerframe.md) — The rectangle of the item’s visible content.
