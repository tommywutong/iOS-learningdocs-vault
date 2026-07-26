---
title: clipBoundingRect
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/clipboundingrect
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/clipboundingrect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/clipboundingrect.json'
content_hash: 'sha256:938bb36c83fc5f12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# clipBoundingRect

<sub>Instance Property</sub>

The bounding rectangle of the intersection of all current clip shapes in the current user space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var clipBoundingRect: CGRect { get }
```

## See Also

### Masking

- [clip(to:style:options:)](<clip(to_style_options_).md>) — Adds a path to the context’s array of clip shapes.
- [clipToLayer(opacity:options:content:)](<cliptolayer(opacity_options_content_).md>) — Adds a clip shape that you define in a new layer to the context’s array of clip shapes.
- [ClipOptions](clipoptions.md) — Options that affect the use of clip shapes.
