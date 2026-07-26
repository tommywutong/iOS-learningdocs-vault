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
doc_path: /documentation/swiftui/nsviewcontrollerrepresentablecontext/environment
source_url: 'https://developer.apple.com/documentation/swiftui/nsviewcontrollerrepresentablecontext/environment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nsviewcontrollerrepresentablecontext/environment.json'
content_hash: 'sha256:1d6e887c1e13b1b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSViewControllerRepresentableContext](../nsviewcontrollerrepresentablecontext.md)

# environment

<sub>Instance Property</sub>

Environment data that describes the current state of the system.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency var environment: EnvironmentValues { get }
```

## Discussion

Use the environment values to configure the state of your view controller when creating or updating it.
