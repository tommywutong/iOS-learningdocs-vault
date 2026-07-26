---
title: replace
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/immersiveenvironmentbehavior/replace
source_url: 'https://developer.apple.com/documentation/swiftui/immersiveenvironmentbehavior/replace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersiveenvironmentbehavior/replace.json'
content_hash: 'sha256:71111cee4eaca061'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersiveEnvironmentBehavior](../immersiveenvironmentbehavior.md)

# replace

<sub>Type Property</sub>

A behavior that replaces any currently opened immersive environment with the new scene.

<sub>visionOS</sub>

```swift
static var replace: ImmersiveEnvironmentBehavior { get }
```

## Discussion

Use this value with the [immersiveEnvironmentBehavior(_:)](<../scene/immersiveenvironmentbehavior(__).md>) scene modifier to define that the system should hide the system’s immersive environment before opening the scene.
