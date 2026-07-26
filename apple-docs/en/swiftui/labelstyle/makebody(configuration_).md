---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/labelstyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/labelstyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/labelstyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:d8b2ee46df6ab829'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LabelStyle](../labelstyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view that represents the body of a label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@ContentBuilder @MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

## Parameters

- `configuration` — The properties of the label.

## Discussion

The system calls this method for each [Label](../label.md) instance in a view hierarchy where this style is the current label style.

## See Also

### Creating custom label styles

- [Configuration](configuration.md) — The properties of a label.
- [Body](body.md) — A view that represents the body of a label.
