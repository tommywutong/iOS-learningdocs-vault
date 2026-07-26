---
title: TextProxy
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textproxy
source_url: 'https://developer.apple.com/documentation/swiftui/textproxy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textproxy.json'
content_hash: 'sha256:476726eed27fdce5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TextProxy

<sub>Structure</sub>

A proxy for a text view that custom text renderers use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TextProxy
```

## Topics

### Instance Methods

- [sizeThatFits(_:)](<textproxy/sizethatfits(__).md>) — Returns the space needed by the text view, for a proposed size.

## See Also

### Rendering text

- [Creating visual effects with SwiftUI](creating-visual-effects-with-swiftui.md) — Add scroll effects, rich color treatments, custom transitions, and advanced effects using shaders and a text renderer.
- [TextAttribute](textattribute.md) — A value that you can attach to text views and that text renderers can query.
- [textRenderer(_:)](<view/textrenderer(__).md>) — Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [TextRenderer](textrenderer.md) — A value that can replace the default text view rendering behavior.
