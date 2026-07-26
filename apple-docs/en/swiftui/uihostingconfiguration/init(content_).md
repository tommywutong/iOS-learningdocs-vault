---
title: 'init(content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uihostingconfiguration/init(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingconfiguration/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingconfiguration/init%28content%3A%29.json'
content_hash: 'sha256:9c6233ee3552e09e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIHostingConfiguration](../uihostingconfiguration.md)

# init(content:)

<sub>Initializer</sub>

Creates a hosting configuration with the given contents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(@ContentBuilder content: () -> Content)
```

## Parameters

- `content` — The contents of the SwiftUI hierarchy to be shown inside the cell.
