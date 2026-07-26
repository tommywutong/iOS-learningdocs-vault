---
title: interaction
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contentshapekinds/interaction
source_url: 'https://developer.apple.com/documentation/swiftui/contentshapekinds/interaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contentshapekinds/interaction.json'
content_hash: 'sha256:f00a00e7905b5454'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentShapeKinds](../contentshapekinds.md)

# interaction

<sub>Type Property</sub>

The kind for hit-testing and accessibility.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let interaction: ContentShapeKinds
```

## Discussion

Setting a content shape with this kind causes the view to hit-test using the specified shape.

## See Also

### Getting shape kinds

- [dragPreview](dragpreview.md) — The kind for drag and drop previews.
- [contextMenuPreview](contextmenupreview.md) — The kind for context menu previews.
- [focusEffect](focuseffect.md) — The kind for the focus effect.
- [hoverEffect](hovereffect.md) — The kind for hover effects.
- [accessibility](accessibility.md) — The kind for accessibility visuals and sorting.
