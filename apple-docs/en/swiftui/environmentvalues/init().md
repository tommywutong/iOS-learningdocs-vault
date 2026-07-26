---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/init()
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/init%28%29.json'
content_hash: 'sha256:426e18afef9281a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# init()

<sub>Initializer</sub>

Creates an environment values instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Discussion

You don’t typically create an instance of [EnvironmentValues](../environmentvalues.md) directly. Doing so would provide access only to default values that don’t update based on system settings or device characteristics. Instead, you rely on an environment values’ instance that SwiftUI manages for you when you use the [Environment](../environment.md) property wrapper and the [environment(_:_:)](<../view/environment(____).md>) view modifier.

## See Also

### Creating and accessing values

- [subscript(_:)](<subscript(__).md>) — Accesses the environment value associated with a custom key.
- [description](description.md) — A string that represents the contents of the environment values instance.
