---
title: accessibility
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contentshapekinds/accessibility
source_url: 'https://developer.apple.com/documentation/swiftui/contentshapekinds/accessibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contentshapekinds/accessibility.json'
content_hash: 'sha256:feccc3fa93fc5987'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ContentShapeKinds](../contentshapekinds.md)

# accessibility

<sub>Type Property</sub>

The kind for accessibility visuals and sorting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let accessibility: ContentShapeKinds
```

## Discussion

Setting a content shape with this kind causes the accessibility frame and path of the view’s underlying accessibility element to match the shape without adjusting the hit-testing shape, updating the visual focus ring that assistive apps, such as VoiceOver, draw, as well as how the element is sorted. Updating the accessibility shape is only required if the shape or size used to hit-test significantly diverges from the visual shape of the view.

To control the shape for accessibility and hit-testing, use the `interaction` kind.

## See Also

### Getting shape kinds

- [interaction](interaction.md) — The kind for hit-testing and accessibility.
- [dragPreview](dragpreview.md) — The kind for drag and drop previews.
- [contextMenuPreview](contextmenupreview.md) — The kind for context menu previews.
- [focusEffect](focuseffect.md) — The kind for the focus effect.
- [hoverEffect](hovereffect.md) — The kind for hover effects.
