---
title: 'init(allowMove:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/dragconfiguration/init(allowmove:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dragconfiguration/init(allowmove:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dragconfiguration/init%28allowmove%3A%29.json'
content_hash: 'sha256:e2f2fbb76a329079'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DragConfiguration](../dragconfiguration.md)

# init(allowMove:)

<sub>Initializer</sub>

Creates a drag configuration that can support drag-to-move in addition to drag-to-copy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init(allowMove: Bool)
```

## Discussion

iOS supports drag-to-move operations only within an application. On macOS, an item can be dragged to move both within the app and to other apps.
