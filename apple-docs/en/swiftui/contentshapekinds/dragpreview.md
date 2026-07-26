---
title: dragPreview
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contentshapekinds/dragpreview
source_url: 'https://developer.apple.com/documentation/swiftui/contentshapekinds/dragpreview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contentshapekinds/dragpreview.json'
content_hash: 'sha256:38ea79f7bd85ba77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentShapeKinds](../contentshapekinds.md)

# dragPreview

<sub>Type Property</sub>

The kind for drag and drop previews.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let dragPreview: ContentShapeKinds
```

## Discussion

When using this kind, only the preview shape is affected. To control the shape used to hit-test and start the drag preview, use the `interaction` kind.

## See Also

### Getting shape kinds

- [interaction](interaction.md) — The kind for hit-testing and accessibility.
- [contextMenuPreview](contextmenupreview.md) — The kind for context menu previews.
- [focusEffect](focuseffect.md) — The kind for the focus effect.
- [hoverEffect](hovereffect.md) — The kind for hover effects.
- [accessibility](accessibility.md) — The kind for accessibility visuals and sorting.
