---
title: ImmersiveSpaceViewContent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/immersivespaceviewcontent
source_url: 'https://developer.apple.com/documentation/swiftui/immersivespaceviewcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersivespaceviewcontent.json'
content_hash: 'sha256:94273c284b8da998'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ImmersiveSpaceViewContent

<sub>Structure</sub>

Immersive space content that uses a SwiftUI view hierarchy as the content.

<sub>visionOS</sub>

```swift
nonisolated struct ImmersiveSpaceViewContent<Content> where Content : View
```

## Overview

You don’t create this type directly. SwiftUI creates it when you construct an [ImmersiveSpace](immersivespace.md) with view-based content.

## Relationships

- **Conforms To**: [ImmersiveSpaceContent](immersivespacecontent.md)

## See Also

### Supporting types

- [ImmersiveSpaceContent](immersivespacecontent.md) — A type that you can use as the content of an immersive space.
