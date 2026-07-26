---
title: 'init(isOn:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/toggle/init(ison:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toggle/init(ison:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toggle/init%28ison%3Alabel%3A%29.json'
content_hash: 'sha256:8ab1c42c8498ac0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Toggle](../toggle.md)

# init(isOn:label:)

<sub>Initializer</sub>

Creates a toggle that displays a custom label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(isOn: Binding<Bool>, @ContentBuilder label: () -> Label)
```

## Parameters

- `isOn` — A binding to a property that determines whether the toggle is on or off.

- `label` — A view that describes the purpose of the toggle.

## See Also

### Creating a toggle

- [init(_:isOn:)](<init(__ison_).md>) — Creates a toggle that generates its label from a localized string resource.
- [init(_:image:isOn:)](<init(__image_ison_).md>) — Creates a toggle that generates its label from a localized string resource and image resource.
- [init(_:systemImage:isOn:)](<init(__systemimage_ison_).md>) — Creates a toggle that generates its label from a localized string key and system image.
