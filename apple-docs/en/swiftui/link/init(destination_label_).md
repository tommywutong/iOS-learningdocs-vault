---
title: 'init(destination:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/link/init(destination:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/link/init(destination:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/link/init%28destination%3Alabel%3A%29.json'
content_hash: 'sha256:012e06fbd3885ad2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Link](../link.md)

# init(destination:label:)

<sub>Initializer</sub>

Creates a control, consisting of a URL and a label, used to navigate to the given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(destination: URL, @ContentBuilder label: () -> Label)
```

## Parameters

- `destination` — The URL for the link.

- `label` — A view that describes the destination of URL.

## See Also

### Creating a link

- [init(_:destination:)](<init(__destination_).md>) — Creates a control, consisting of a URL and a title resource, used to navigate to a URL.
