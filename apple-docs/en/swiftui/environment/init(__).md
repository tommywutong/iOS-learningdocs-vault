---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/environment/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/environment/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environment/init%28_%3A%29.json'
content_hash: 'sha256:bdcb4047810a3d41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Environment](../environment.md)

# init(_:)

<sub>Initializer</sub>

Creates an environment property to read the specified key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ keyPath: KeyPath<EnvironmentValues, Value>)
```

## Parameters

- `keyPath` — A key path to a specific resulting value.

## Discussion

Don’t call this initializer directly. Instead, declare a property with the [Environment](../environment.md) property wrapper, and provide the key path of the environment value that the property should reflect:

```swift
struct MyView: View {
    @Environment(\.colorScheme) var colorScheme: ColorScheme

    // ...
}
```

SwiftUI automatically updates any parts of `MyView` that depend on the property when the associated environment value changes. You can’t modify the environment value using a property like this. Instead, use the [environment(_:_:)](<../view/environment(____).md>) view modifier on a view to set a value for a view hierarchy.
