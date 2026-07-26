---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/defaulttogglestyle/init()
source_url: 'https://developer.apple.com/documentation/swiftui/defaulttogglestyle/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/defaulttogglestyle/init%28%29.json'
content_hash: 'sha256:5948629a9f2b3c05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DefaultToggleStyle](../defaulttogglestyle.md)

# init()

<sub>Initializer</sub>

Creates a default toggle style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init()
```

## Discussion

Don’t call this initializer directly. Instead, use the [automatic](../togglestyle/automatic.md) static variable to create this style:

```swift
Toggle("Enhance Sound", isOn: $isEnhanced)
    .toggleStyle(.automatic)
```
