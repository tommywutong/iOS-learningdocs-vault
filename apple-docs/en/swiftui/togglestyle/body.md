---
title: Body
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/togglestyle/body
source_url: 'https://developer.apple.com/documentation/swiftui/togglestyle/body'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/togglestyle/body.json'
content_hash: 'sha256:eed5dd58fb54e2f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToggleStyle](../togglestyle.md)

# Body

<sub>Associated Type</sub>

A view that represents the appearance and interaction of a toggle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype Body : View
```

## Discussion

SwiftUI infers this type automatically based on the [View](../view.md) instance that you return from your implementation of the [makeBody(configuration:)](<makebody(configuration_).md>) method.

## See Also

### Creating custom toggle styles

- [makeBody(configuration:)](<makebody(configuration_).md>) — Creates a view that represents the body of a toggle.
- [ToggleStyleConfiguration](../togglestyleconfiguration.md) — The properties of a toggle instance.
- [Configuration](configuration.md) — The properties of a toggle instance.
