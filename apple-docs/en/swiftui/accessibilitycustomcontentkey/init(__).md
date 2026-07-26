---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/accessibilitycustomcontentkey/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilitycustomcontentkey/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilitycustomcontentkey/init%28_%3A%29.json'
content_hash: 'sha256:1f0b1cd2151cf31c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityCustomContentKey](../accessibilitycustomcontentkey.md)

# init(_:)

<sub>Initializer</sub>

Create an `AccessibilityCustomContentKey` with the specified label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ label: LocalizedStringResource)
```

## Parameters

- `label` — Localized text describing to the user what is contained in this additional information entry. For example: “orientation”. This will also be used as the identifier.

## See Also

### Creating a key

- [init(_:id:)](<init(__id_).md>) — Create an `AccessibilityCustomContentKey` with the specified label and identifier.
