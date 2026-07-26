---
title: environment
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uiviewrepresentablecontext/environment
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewrepresentablecontext/environment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewrepresentablecontext/environment.json'
content_hash: 'sha256:809810bf7bc7cfc5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIViewRepresentableContext](../uiviewrepresentablecontext.md)

# environment

<sub>Instance Property</sub>

The current environment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var environment: EnvironmentValues { get }
```

## Discussion

Use the environment values to configure the state of your view when creating or updating it.
