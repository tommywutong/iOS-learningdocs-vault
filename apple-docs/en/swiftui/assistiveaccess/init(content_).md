---
title: 'init(content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/assistiveaccess/init(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/assistiveaccess/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/assistiveaccess/init%28content%3A%29.json'
content_hash: 'sha256:150c12e721950193'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AssistiveAccess](../assistiveaccess.md)

# init(content:)

<sub>Initializer</sub>

Creates an Assistive Access scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(@ContentBuilder content: () -> Content)
```

## Parameters

- `content` — A closure that creates the content for the app when Assistive Access is enabled.

## Discussion

When Assistive Access is enabled, the given view is used as the root view of the app.
