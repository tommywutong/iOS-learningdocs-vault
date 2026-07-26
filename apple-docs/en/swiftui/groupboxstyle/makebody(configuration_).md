---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/groupboxstyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/groupboxstyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/groupboxstyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:44896c6992ca498d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GroupBoxStyle](../groupboxstyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view representing the body of a group box.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@ContentBuilder @MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

## Parameters

- `configuration` — The properties of the group box instance being created.

## Discussion

SwiftUI calls this method for each instance of [GroupBox](../groupbox.md) created within a view hierarchy where this style is the current group box style.

## See Also

### Creating custom group box styles

- [Configuration](configuration.md) — The properties of a group box instance.
- [Body](body.md) — A view that represents the body of a group box.
