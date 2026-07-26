---
title: hoverEffect
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 18.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contentshapekinds/hovereffect
source_url: 'https://developer.apple.com/documentation/swiftui/contentshapekinds/hovereffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contentshapekinds/hovereffect.json'
content_hash: 'sha256:ef9376ddb3f8ebf9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentShapeKinds](../contentshapekinds.md)

# hoverEffect

<sub>Type Property</sub>

The kind for hover effects.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let hoverEffect: ContentShapeKinds
```

## Discussion

When using this kind, only the preview shape is affected. To control the shape used to hit-test and start the effect, use the `interaction` kind.

On tvOS, this is used to define the shape of any hover effect applied to focusable and hoverable controls, for example button border or clipping shapes.

This kind does not affect the `onHover` modifier.

## See Also

### Getting shape kinds

- [interaction](interaction.md) — The kind for hit-testing and accessibility.
- [dragPreview](dragpreview.md) — The kind for drag and drop previews.
- [contextMenuPreview](contextmenupreview.md) — The kind for context menu previews.
- [focusEffect](focuseffect.md) — The kind for the focus effect.
- [accessibility](accessibility.md) — The kind for accessibility visuals and sorting.
