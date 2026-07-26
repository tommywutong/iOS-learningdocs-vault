---
title: coexist
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/immersiveenvironmentbehavior/coexist
source_url: 'https://developer.apple.com/documentation/swiftui/immersiveenvironmentbehavior/coexist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersiveenvironmentbehavior/coexist.json'
content_hash: 'sha256:71befa341fbd5cc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersiveEnvironmentBehavior](../immersiveenvironmentbehavior.md)

# coexist

<sub>Type Property</sub>

A behavior that keeps the system’s immersive environment as is when opening a scene.

<sub>visionOS</sub>

```swift
static var coexist: ImmersiveEnvironmentBehavior { get }
```

## Discussion

Use this value with the [immersiveEnvironmentBehavior(_:)](<../scene/immersiveenvironmentbehavior(__).md>) scene modifier to define that the system should allow the system’s immersive environment to co-exist with the scene.
