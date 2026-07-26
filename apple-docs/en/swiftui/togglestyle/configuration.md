---
title: ToggleStyle.Configuration
framework: SwiftUI
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/togglestyle/configuration
source_url: 'https://developer.apple.com/documentation/swiftui/togglestyle/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/togglestyle/configuration.json'
content_hash: 'sha256:df13107354172611'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToggleStyle](../togglestyle.md)

# ToggleStyle.Configuration

<sub>Type Alias</sub>

The properties of a toggle instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Configuration = ToggleStyleConfiguration
```

## Discussion

You receive a `configuration` parameter of this type — which is an alias for the [ToggleStyleConfiguration](../togglestyleconfiguration.md) type — when you implement the required [makeBody(configuration:)](<makebody(configuration_).md>) method in a custom toggle style implementation.

## See Also

### Creating custom toggle styles

- [makeBody(configuration:)](<makebody(configuration_).md>) — Creates a view that represents the body of a toggle.
- [ToggleStyleConfiguration](../togglestyleconfiguration.md) — The properties of a toggle instance.
- [Body](body.md) — A view that represents the appearance and interaction of a toggle.
