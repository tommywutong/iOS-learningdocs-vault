---
title: statusBar
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/toolbarplacement/statusbar
source_url: 'https://developer.apple.com/documentation/swiftui/toolbarplacement/statusbar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbarplacement/statusbar.json'
content_hash: 'sha256:d90511110ae1e319'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarPlacement](../toolbarplacement.md)

# statusBar

<sub>Type Property</sub>

The system status bar.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static var statusBar: ToolbarPlacement { get }
```

## Discussion

Use with [toolbarVisibility(_:for:)](<../view/toolbarvisibility(__for_).md>) to hide the status bar, or with [toolbarColorScheme(_:for:)](<../view/toolbarcolorscheme(__for_).md>) to specify the preferred status bar style.

```swift
content
    .toolbarVisibility(
        hideStatusBar ? .hidden : .automatic,
        for: .statusBar)
    // use light status bar on a dark background
    .toolbarColorScheme(.dark, for: .statusBar)
```

Using this placement with other toolbar customization APIs has no effect.
