---
title: TextAttribute
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textattribute
source_url: 'https://developer.apple.com/documentation/swiftui/textattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textattribute.json'
content_hash: 'sha256:5fd02fbd0576973e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TextAttribute

<sub>Protocol</sub>

A value that you can attach to text views and that text renderers can query.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol TextAttribute : Hashable
```

## Relationships

- **Inherits From**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## See Also

### Rendering text

- [Creating visual effects with SwiftUI](creating-visual-effects-with-swiftui.md) — Add scroll effects, rich color treatments, custom transitions, and advanced effects using shaders and a text renderer.
- [textRenderer(_:)](<view/textrenderer(__).md>) — Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [TextRenderer](textrenderer.md) — A value that can replace the default text view rendering behavior.
- [TextProxy](textproxy.md) — A proxy for a text view that custom text renderers use.
