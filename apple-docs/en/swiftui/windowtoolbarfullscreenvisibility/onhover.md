---
title: onHover
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowtoolbarfullscreenvisibility/onhover
source_url: 'https://developer.apple.com/documentation/swiftui/windowtoolbarfullscreenvisibility/onhover'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowtoolbarfullscreenvisibility/onhover.json'
content_hash: 'sha256:5e0df190dea1e967'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowToolbarFullScreenVisibility](../windowtoolbarfullscreenvisibility.md)

# onHover

<sub>Type Property</sub>

Hide the window toolbar in full screen mode by default. It will reveal itself when the mouse moves into the area occupied by the menu bar.

<sub>macOS</sub>

```swift
static let onHover: WindowToolbarFullScreenVisibility
```

## Discussion

This has no effect if the toolbar is completely hidden, i.e. setting the visibility to `hidden` for `windowToolbar` placements using [toolbarVisibility(_:for:)](<../view/toolbarvisibility(__for_).md>) will cause the toolbar to remain completely hidden, even in full screen.
