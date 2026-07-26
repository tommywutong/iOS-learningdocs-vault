---
title: GraphicsContext.ClipOptions
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/clipoptions
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/clipoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/clipoptions.json'
content_hash: 'sha256:1fa10297307028f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# GraphicsContext.ClipOptions

<sub>Structure</sub>

Options that affect the use of clip shapes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct ClipOptions
```

## Overview

Use these options to affect how SwiftUI interprets a clip shape when you call [clip(to:style:options:)](<clip(to_style_options_).md>) to add a path to the array of clip shapes, or when you call [clipToLayer(opacity:options:content:)](<cliptolayer(opacity_options_content_).md>) to add a clipping layer.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Getting clip options

- [inverse](clipoptions/inverse.md) — An option to invert the shape or layer alpha as the clip mask.

## See Also

### Masking

- [clip(to:style:options:)](<clip(to_style_options_).md>) — Adds a path to the context’s array of clip shapes.
- [clipToLayer(opacity:options:content:)](<cliptolayer(opacity_options_content_).md>) — Adds a clip shape that you define in a new layer to the context’s array of clip shapes.
- [clipBoundingRect](clipboundingrect.md) — The bounding rectangle of the intersection of all current clip shapes in the current user space.
