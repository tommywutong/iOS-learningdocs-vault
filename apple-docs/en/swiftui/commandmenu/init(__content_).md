---
title: 'init(_:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/commandmenu/init(_:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/commandmenu/init(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commandmenu/init%28_%3Acontent%3A%29.json'
content_hash: 'sha256:4da2ebd6821d9d4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CommandMenu](../commandmenu.md)

# init(_:content:)

<sub>Initializer</sub>

Creates a new menu with a localized name for a collection of app- specific commands, inserted in the standard location for app menus (after the View menu, in order with other menus declared without an explicit location).

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ name: LocalizedStringResource, @ContentBuilder content: () -> Content)
```
