---
title: FormStyle.Configuration
framework: SwiftUI
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/formstyle/configuration
source_url: 'https://developer.apple.com/documentation/swiftui/formstyle/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/formstyle/configuration.json'
content_hash: 'sha256:5f8bb798d7705fe0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FormStyle](../formstyle.md)

# FormStyle.Configuration

<sub>Type Alias</sub>

The properties of a form instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Configuration = FormStyleConfiguration
```

## Discussion

You receive a `configuration` parameter of this type — which is an alias for the [FormStyleConfiguration](../formstyleconfiguration.md) type — when you implement the required [makeBody(configuration:)](<makebody(configuration_).md>) method in a custom form style implementation.

## See Also

### Creating custom form styles

- [makeBody(configuration:)](<makebody(configuration_).md>) — Creates a view that represents the body of a form.
- [Body](body.md) — A view that represents the appearance and interaction of a form.
