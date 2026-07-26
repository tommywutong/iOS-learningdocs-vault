---
title: 'sizeThatFits(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/windowlayoutroot/sizethatfits(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowlayoutroot/sizethatfits(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowlayoutroot/sizethatfits%28_%3A%29.json'
content_hash: 'sha256:f8bc0041aef23226'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowLayoutRoot](../windowlayoutroot.md)

# sizeThatFits(_:)

<sub>Instance Method</sub>

Asks the window’s content for its size.

<sub>macOS, visionOS</sub>

```swift
func sizeThatFits(_ proposal: ProposedViewSize) -> CGSize
```

## Parameters

- `proposal` — A proposed size for the subview. In SwiftUI, views choose their own size, but can take a size proposal from their parent view into account when doing so.

## Return Value

The size that the content chooses for itself, given the proposal from its container view.
