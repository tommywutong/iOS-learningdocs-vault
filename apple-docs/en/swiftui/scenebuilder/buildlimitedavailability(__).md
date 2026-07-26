---
title: 'buildLimitedAvailability(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.1+, iPadOS 16.1+, Mac Catalyst 16.1+, macOS 13.0+, tvOS 16.1+, visionOS 1.0+, watchOS 9.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scenebuilder/buildlimitedavailability(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scenebuilder/buildlimitedavailability(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenebuilder/buildlimitedavailability%28_%3A%29.json'
content_hash: 'sha256:93e36c5f252355ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SceneBuilder](../scenebuilder.md)

# buildLimitedAvailability(_:)

<sub>Type Method</sub>

Processes scene content for a conditional compiler-control statement that performs an availability check.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildLimitedAvailability(_ scene: some Scene) -> any Scene & _LimitedAvailabilitySceneMarker
```

## See Also

### Building content

- [buildBlock(_:)](<buildblock(__).md>)
- [buildExpression(_:)](<buildexpression(__).md>) — Builds an expression within the builder.
- [buildOptional(_:)](<buildoptional(__).md>) — Produces an optional scene for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.
