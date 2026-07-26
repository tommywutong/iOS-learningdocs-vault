---
title: 'init(rootScene:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nshostingscenerepresentation/init(rootscene:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingscenerepresentation/init(rootscene:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingscenerepresentation/init%28rootscene%3A%29.json'
content_hash: 'sha256:976651f33c80c0c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingSceneRepresentation](../nshostingscenerepresentation.md)

# init(rootScene:)

<sub>Initializer</sub>

Creates a new hosting scene representation for the specified scene(s).

<sub>macOS</sub>

```swift
@MainActor init(@SceneBuilder rootScene: () -> Content)
```

## Parameters

- `rootScene` — The SwiftUI scene(s) to be represented.
