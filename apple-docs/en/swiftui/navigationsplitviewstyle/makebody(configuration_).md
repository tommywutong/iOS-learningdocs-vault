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
doc_path: '/documentation/swiftui/navigationsplitviewstyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/navigationsplitviewstyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationsplitviewstyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:ed623ef162b21d98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationSplitViewStyle](../navigationsplitviewstyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view that represents the body of a navigation split view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@ContentBuilder @MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

## Parameters

- `configuration` — The properties of the instance to create.

## Discussion

SwiftUI calls this method for each instance of [NavigationSplitView](../navigationsplitview.md), where this style is the current [NavigationSplitViewStyle](../navigationsplitviewstyle.md).

## See Also

### Creating custom styles

- [Configuration](configuration.md) — The properties of a navigation split view instance.
- [Body](body.md) — A view that represents the body of a navigation split view.
