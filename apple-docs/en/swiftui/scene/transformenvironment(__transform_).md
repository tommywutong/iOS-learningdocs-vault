---
title: 'transformEnvironment(_:transform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/transformenvironment(_:transform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/transformenvironment(_:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/transformenvironment%28_%3Atransform%3A%29.json'
content_hash: 'sha256:07b0b423a9c001da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# transformEnvironment(_:transform:)

<sub>Instance Method</sub>

Transforms the environment value of the specified key path with the given function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func transformEnvironment<V>(_ keyPath: WritableKeyPath<EnvironmentValues, V>, transform: @escaping (inout V) -> Void) -> some Scene

```

## See Also

### Modifying the environment of a scene

- [environment(_:)](<environment(__).md>) — Places an observable object in the scene’s environment.
- [environment(_:_:)](<environment(____).md>) — Sets the environment value of the specified key path to the given value.
