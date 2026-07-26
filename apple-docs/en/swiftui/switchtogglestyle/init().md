---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 18.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/switchtogglestyle/init()
source_url: 'https://developer.apple.com/documentation/swiftui/switchtogglestyle/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/switchtogglestyle/init%28%29.json'
content_hash: 'sha256:6fceb702af5bb37a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SwitchToggleStyle](../switchtogglestyle.md)

# init()

<sub>Initializer</sub>

Creates a switch toggle style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init()
```

## Discussion

Don’t call this initializer directly. Instead, use the [switch](../togglestyle/switch.md) static variable to create this style:

```swift
Toggle("Enhance Sound", isOn: $isEnhanced)
    .toggleStyle(.switch)
```
