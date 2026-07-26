---
title: globalFrameDidChangeNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+（10.14 起废弃）]
languages: [swift, swift, occ]
beta: false
deprecated: true
doc_path: /documentation/appkit/nsview/globalframedidchangenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsview/globalframedidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsview/globalframedidchangenotification.json'
content_hash: 'sha256:2b587c746d4d85c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSView](../nsview.md)

# globalFrameDidChangeNotification

<sub>Type Property</sub>

Posted whenever an `NSView` object that has attached surfaces (that is, `NSOpenGLContext` objects) moves to a different screen, or other cases where the `NSOpenGLContext` object needs to be updated.

> [!warning] Deprecated
> Use NSOpenGLView instead.

<sub>macOS</sub>

```swift
class let globalFrameDidChangeNotification: NSNotification.Name
```

## Discussion

The notification object is the surface’s view. This notification does not contain a `userInfo` dictionary.
