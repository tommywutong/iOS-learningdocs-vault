---
title: 'subscript(_:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/environmentvalues/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/subscript%28_%3A%29.json'
content_hash: 'sha256:453c92a4b1ee1c9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the environment value associated with a custom key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<K>(key: K.Type) -> K.Value where K : EnvironmentKey { get set }
```

## Overview

Create a custom environment value by declaring a new property in an extension to the environment values structure and applying the [Entry()](<../entry().md>) macro to the variable declaration:

```swift
extension EnvironmentValues {
    @Entry var myCustomValue: String = "Default value"
}
```

You use custom environment values the same way you use system-provided values, setting a value with the [environment(_:_:)](<../view/environment(____).md>) view modifier, and reading values with the [Environment](../environment.md) property wrapper. You can also provide a dedicated view modifier as a convenience for setting the value:

```swift
extension View {
    func myCustomValue(_ myCustomValue: String) -> some View {
        environment(\.myCustomValue, myCustomValue)
    }
}
```

## See Also

### Creating and accessing values

- [init()](<init().md>) — Creates an environment values instance.
- [description](description.md) — A string that represents the contents of the environment values instance.
