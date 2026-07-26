---
title: 'buildOptional(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scenebuilder/buildoptional(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scenebuilder/buildoptional(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenebuilder/buildoptional%28_%3A%29.json'
content_hash: 'sha256:205439cd0168fc27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SceneBuilder](../scenebuilder.md)

# buildOptional(_:)

<sub>Type Method</sub>

Produces an optional scene for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static func buildOptional(_ scene: (any Scene & _LimitedAvailabilitySceneMarker)?) -> some Scene

```

## Discussion

Conditional statements in a [SceneBuilder](../scenebuilder.md) can contain an `if` statement but not an `else` statement, and the condition can only perform a compiler check for availability, like in the following code:

```swift
var body: some Scene {
    if #available(iOS 16, *) {
        WindowGroup {
            ContentView()
        }
    }
}
```

## See Also

### Building content

- [buildBlock(_:)](<buildblock(__).md>)
- [buildExpression(_:)](<buildexpression(__).md>) — Builds an expression within the builder.
- [buildLimitedAvailability(_:)](<buildlimitedavailability(__).md>) — Processes scene content for a conditional compiler-control statement that performs an availability check.
