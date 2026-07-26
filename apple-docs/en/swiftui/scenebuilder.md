---
title: SceneBuilder
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scenebuilder
source_url: 'https://developer.apple.com/documentation/swiftui/scenebuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scenebuilder.json'
content_hash: 'sha256:d1db7f90d323df1d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SceneBuilder

<sub>Structure</sub>

A result builder for composing a collection of scenes into a single composite scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@resultBuilder struct SceneBuilder
```

## Topics

### Building content

- [buildBlock(_:)](<scenebuilder/buildblock(__).md>)
- [buildExpression(_:)](<scenebuilder/buildexpression(__).md>) — Builds an expression within the builder.
- [buildLimitedAvailability(_:)](<scenebuilder/buildlimitedavailability(__).md>) — Processes scene content for a conditional compiler-control statement that performs an availability check.
- [buildOptional(_:)](<scenebuilder/buildoptional(__).md>) — Produces an optional scene for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.

## See Also

### Creating scenes

- [Scene](scene.md) — A part of an app’s user interface with a life cycle managed by the system.
