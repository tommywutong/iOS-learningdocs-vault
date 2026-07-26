---
title: 'appRefresh(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/backgroundtask/apprefresh(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/backgroundtask/apprefresh(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/backgroundtask/apprefresh%28_%3A%29.json'
content_hash: 'sha256:88df64ef245e635d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [BackgroundTask](../backgroundtask.md)

# appRefresh(_:)

<sub>Type Method</sub>

A task that updates your app’s state in the background for a matching identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static func appRefresh(_ identifier: String) -> BackgroundTask<Void, Void>
```

## Return Value

A background task that you can handle with your app or extension.
