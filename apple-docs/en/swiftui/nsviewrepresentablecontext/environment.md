---
title: environment
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/nsviewrepresentablecontext/environment
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewrepresentablecontext/environment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewrepresentablecontext/environment.json'
content_hash: 'sha256:47810912d648e80b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewRepresentableContext](../nsviewrepresentablecontext.md)

# environment

<sub>Instance Property</sub>

Environment data that describes the current state of the system.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency var environment: EnvironmentValues { get }
```

## Discussion

Use the environment values to configure the state of your view when creating or updating it.
