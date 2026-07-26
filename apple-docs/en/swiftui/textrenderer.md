---
title: TextRenderer
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textrenderer
source_url: 'https://developer.apple.com/documentation/swiftui/textrenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textrenderer.json'
content_hash: 'sha256:ee818fd08b430bfa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TextRenderer

<sub>Protocol</sub>

A value that can replace the default text view rendering behavior.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol TextRenderer : Animatable
```

## Relationships

- **Inherits From**: [Animatable](animatable.md)

## Topics

### Instance Properties

- [displayPadding](textrenderer/displaypadding.md) — Returns the size of the extra padding added to any drawing layer used to rasterize the text. For example when drawing the text with a shadow this may be used to extend the drawing bounds to avoid clipping the shadow.

### Instance Methods

- [draw(layout:in:)](<textrenderer/draw(layout_in_).md>) — Draws `layout` into `ctx`.
- [sizeThatFits(proposal:text:)](<textrenderer/sizethatfits(proposal_text_).md>) — Returns the size of the text in `proposal`. The provided `text` proxy value may be used to query the sizing behavior of the underlying text layout.

## See Also

### Rendering text

- [Creating visual effects with SwiftUI](creating-visual-effects-with-swiftui.md) — Add scroll effects, rich color treatments, custom transitions, and advanced effects using shaders and a text renderer.
- [TextAttribute](textattribute.md) — A value that you can attach to text views and that text renderers can query.
- [textRenderer(_:)](<view/textrenderer(__).md>) — Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [TextProxy](textproxy.md) — A proxy for a text view that custom text renderers use.
