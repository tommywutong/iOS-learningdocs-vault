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
doc_path: /documentation/swiftui/uiviewcontrollerrepresentablecontext/environment
source_url: 'https://developer.apple.com/documentation/swiftui/uiviewcontrollerrepresentablecontext/environment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uiviewcontrollerrepresentablecontext/environment.json'
content_hash: 'sha256:40e9d16dc0b3b513'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIViewControllerRepresentableContext](../uiviewcontrollerrepresentablecontext.md)

# environment

<sub>Instance Property</sub>

Environment values that describe the current state of the system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var environment: EnvironmentValues { get }
```

## Discussion

Use the environment values to configure the state of your UIKit view controller when creating or updating it.
