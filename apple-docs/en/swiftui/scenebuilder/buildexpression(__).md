---
title: 'buildExpression(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scenebuilder/buildexpression(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scenebuilder/buildexpression(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenebuilder/buildexpression%28_%3A%29.json'
content_hash: 'sha256:d0cca16cb67dfc98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SceneBuilder](../scenebuilder.md)

# buildExpression(_:)

<sub>Type Method</sub>

Builds an expression within the builder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildExpression<Content>(_ content: Content) -> Content where Content : Scene
```

## See Also

### Building content

- [buildBlock(_:)](<buildblock(__).md>)
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>) — Processes scene content for a conditional compiler-control statement that performs an availability check.
- [buildOptional(_:)](<buildoptional(__).md>) — Produces an optional scene for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
