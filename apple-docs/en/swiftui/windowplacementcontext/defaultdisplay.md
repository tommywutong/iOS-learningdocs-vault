---
title: defaultDisplay
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowplacementcontext/defaultdisplay
source_url: 'https://developer.apple.com/documentation/swiftui/windowplacementcontext/defaultdisplay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowplacementcontext/defaultdisplay.json'
content_hash: 'sha256:49d4b162af81471b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowPlacementContext](../windowplacementcontext.md)

# defaultDisplay

<sub>Instance Property</sub>

The display on which new windows will be presented by default.

<sub>macOS</sub>

```swift
var defaultDisplay: DisplayProxy { get }
```

## Discussion

On macOS, this is typically the display which currently has focus.
