---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/formstyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/formstyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/formstyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:0f8af21027c275f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FormStyle](../formstyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view that represents the body of a form.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@ContentBuilder @MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

## Parameters

- `configuration` — The properties of the form.

## Return Value

A view that has behavior and appearance that enables it to function as a [Form](../form.md).

## See Also

### Creating custom form styles

- [Configuration](configuration.md) — The properties of a form instance.
- [Body](body.md) — A view that represents the appearance and interaction of a form.
