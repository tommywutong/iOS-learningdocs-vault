---
title: 'transformEnvironment(_:transform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/transformenvironment(_:transform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/transformenvironment(_:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/transformenvironment%28_%3Atransform%3A%29.json'
content_hash: 'sha256:0b0df35f8f40d5ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# transformEnvironment(_:transform:)

<sub>Instance Method</sub>

Transforms the environment value of the specified key path with the given function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func transformEnvironment<V>(_ keyPath: WritableKeyPath<EnvironmentValues, V>, transform: @escaping (inout V) -> Void) -> some View

```

## See Also

### Modifying the environment of a view

- [environment(_:)](<environment(__).md>) — Places an observable object in the view’s environment.
- [environment(_:_:)](<environment(____).md>) — Sets the environment value of the specified key path to the given value.
