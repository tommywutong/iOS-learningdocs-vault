---
title: 'buildBlock(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scenebuilder/buildblock(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scenebuilder/buildblock(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenebuilder/buildblock%28_%3A%29.json'
content_hash: 'sha256:163122be95f26af8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SceneBuilder](../scenebuilder.md)

# buildBlock(_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildBlock<each Content>(_ content: repeat each Content) -> some Scene where repeat each Content : Scene

```

## See Also

### Building content

- [buildExpression(_:)](<buildexpression(__).md>) — Builds an expression within the builder.
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>) — Processes scene content for a conditional compiler-control statement that performs an availability check.
- [buildOptional(_:)](<buildoptional(__).md>) — Produces an optional scene for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
