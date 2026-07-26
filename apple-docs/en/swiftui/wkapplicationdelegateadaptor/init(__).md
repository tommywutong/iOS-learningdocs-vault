---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/wkapplicationdelegateadaptor/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/wkapplicationdelegateadaptor/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkapplicationdelegateadaptor/init%28_%3A%29.json'
content_hash: 'sha256:0618e35c78cb45b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WKApplicationDelegateAdaptor](../wkapplicationdelegateadaptor.md)

# init(_:)

<sub>Initializer</sub>

Creates an `WKApplicationDelegateAdaptor` using a WatchKit Application Delegate.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency init(_ delegateType: DelegateType.Type = DelegateType.self)
```

## Discussion

The framework will initialize the provided delegate and manage its lifetime, calling out to it when appropriate after performing its own work.

> [!note] Note
> The instantiated delegate will be placed in the Environment and may be accessed by using the `@Environment` property wrapper in the view hierarchy.
