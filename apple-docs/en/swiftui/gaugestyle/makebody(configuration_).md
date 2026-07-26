---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gaugestyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gaugestyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gaugestyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:2765e5e71527d423'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GaugeStyle](../gaugestyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view representing the body of a gauge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@ContentBuilder @MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

## Parameters

- `configuration` — The properties to apply to the gauge instance.

## Discussion

The system calls this modifier on each instance of gauge within a view hierarchy where this style is the current gauge style.

## See Also

### Creating custom gauge styles

- [Configuration](configuration.md) — The properties of a gauge instance.
- [Body](body.md) — A view representing the body of a gauge.
