---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/menustyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/menustyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menustyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:06b61ac59ba09b81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MenuStyle](../menustyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view that represents the body of a menu.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@ContentBuilder @MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

## Parameters

- `configuration` — The properties of the menu.

## Discussion

The system calls this method for each [Menu](../menu.md) instance in a view hierarchy where this style is the current menu style.

## See Also

### Creating custom menu styles

- [Configuration](configuration.md) — The properties of a menu.
- [Body](body.md) — A view that represents the body of a menu.
