---
title: contextMenuPreview
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contentshapekinds/contextmenupreview
source_url: 'https://developer.apple.com/documentation/swiftui/contentshapekinds/contextmenupreview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contentshapekinds/contextmenupreview.json'
content_hash: 'sha256:b00af9ce4646463e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentShapeKinds](../contentshapekinds.md)

# contextMenuPreview

<sub>Type Property</sub>

The kind for context menu previews.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let contextMenuPreview: ContentShapeKinds
```

## Discussion

When using this kind, only the preview shape will be affected. To control the shape used to hit-test and start the context menu presentation, use the `.interaction` kind.

## See Also

### Getting shape kinds

- [interaction](interaction.md) — The kind for hit-testing and accessibility.
- [dragPreview](dragpreview.md) — The kind for drag and drop previews.
- [focusEffect](focuseffect.md) — The kind for the focus effect.
- [hoverEffect](hovereffect.md) — The kind for hover effects.
- [accessibility](accessibility.md) — The kind for accessibility visuals and sorting.
