---
title: frame()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/view/frame()
source_url: 'https://developer.apple.com/documentation/swiftui/view/frame()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/frame%28%29.json'
content_hash: 'sha256:6feef7ac1f368196'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# frame()

<sub>Instance Method</sub>

Positions this view within an invisible frame.

> [!warning] Deprecated
> Use [frame(width:height:alignment:)](<frame(width_height_alignment_).md>) or [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](<frame(minwidth_idealwidth_maxwidth_minheight_idealheight_maxheight_alignment_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func frame() -> some View

```

## See Also

### Layout modifiers

- [edgesIgnoringSafeArea(_:)](<edgesignoringsafearea(__).md>) — Changes the view’s proposed area to extend outside the screen’s safe areas. _(deprecated)_
- [coordinateSpace(name:)](<coordinatespace(name_).md>) — Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space. _(deprecated)_
