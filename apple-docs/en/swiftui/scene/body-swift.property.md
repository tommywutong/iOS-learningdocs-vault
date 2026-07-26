---
title: body
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scene/body-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/scene/body-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/body-swift.property.json'
content_hash: 'sha256:b0c72f643baf4782'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# body

<sub>Instance Property</sub>

The content and behavior of the scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@SceneBuilder @MainActor @preconcurrency var body: Self.Body { get }
```

## Discussion

For any scene that you create, provide a computed `body` property that defines the scene as a composition of other scenes. You can assemble a scene from built-in scenes that SwiftUI provides, as well as other scenes that you’ve defined.

Swift infers the scene’s [Body](body-swift.associatedtype.md) associated type based on the contents of the `body` property.

## See Also

### Creating a scene

- [Body](body-swift.associatedtype.md) — The type of scene that represents the body of this scene.
