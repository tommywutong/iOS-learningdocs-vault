---
title: Body
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scene/body-swift.associatedtype
source_url: 'https://developer.apple.com/documentation/swiftui/scene/body-swift.associatedtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/body-swift.associatedtype.json'
content_hash: 'sha256:9ef2673f29e94b68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# Body

<sub>Associated Type</sub>

The type of scene that represents the body of this scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Body : Scene
```

## Discussion

When you create a custom scene, Swift infers this type from your implementation of the required [body](body-swift.property.md) property.

## See Also

### Creating a scene

- [body](body-swift.property.md) — The content and behavior of the scene.
