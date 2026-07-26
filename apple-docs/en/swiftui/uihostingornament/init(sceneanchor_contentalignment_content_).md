---
title: 'init(sceneAnchor:contentAlignment:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uihostingornament/init(sceneanchor:contentalignment:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingornament/init(sceneanchor:contentalignment:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingornament/init%28sceneanchor%3Acontentalignment%3Acontent%3A%29.json'
content_hash: 'sha256:c72c71aae9851df8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIHostingOrnament](../uihostingornament.md)

# init(sceneAnchor:contentAlignment:content:)

<sub>Initializer</sub>

Creates an ornament with the specified alignment and content.

<sub>visionOS</sub>

```swift
init(sceneAnchor: UnitPoint, contentAlignment: Alignment = .center, @ContentBuilder content: () -> Content)
```

## Parameters

- `sceneAnchor` — The anchor point for aligning the ornament’s content (based on the `contentAlignment`) with the scene.

- `contentAlignment` — The alignment in the ornament used to position it.

- `content` — The content of the ornament.

## See Also

### Creating a hosting ornament

- [rootView](rootview.md) — The root view of the SwiftUI view hierarchy managed by this ornament.
