---
title: visible
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowtoolbarfullscreenvisibility/visible
source_url: 'https://developer.apple.com/documentation/swiftui/windowtoolbarfullscreenvisibility/visible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowtoolbarfullscreenvisibility/visible.json'
content_hash: 'sha256:49fd5d122e52684d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowToolbarFullScreenVisibility](../windowtoolbarfullscreenvisibility.md)

# visible

<sub>Type Property</sub>

Prefer to show window toolbar when the window is in full screen mode.

<sub>macOS</sub>

```swift
static let visible: WindowToolbarFullScreenVisibility
```

## Discussion

This has no effect if the toolbar is completely hidden, i.e. setting the visibility to `hidden` for `windowToolbar` placements using [toolbarVisibility(_:for:)](<../view/toolbarvisibility(__for_).md>) will cause the toolbar to remain completely hidden, even in full screen.
