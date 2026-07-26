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
doc_path: '/documentation/swiftui/progressviewstyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/progressviewstyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressviewstyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:47f67b4f0cfdeeff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProgressViewStyle](../progressviewstyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view representing the body of a progress view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@ContentBuilder @MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

## Parameters

- `configuration` — The properties of the progress view being created.

## Discussion

The view hierarchy calls this method for each progress view where this style is the current progress view style.

## See Also

### Creating custom progress view styles

- [Configuration](configuration.md) — A type alias for the properties of a progress view instance.
- [Body](body.md) — A view representing the body of a progress view.
