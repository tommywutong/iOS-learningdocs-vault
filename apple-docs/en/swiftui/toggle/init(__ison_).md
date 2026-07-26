---
title: 'init(_:isOn:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/toggle/init(_:ison:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toggle/init(_:ison:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toggle/init%28_%3Aison%3A%29.json'
content_hash: 'sha256:9528bfc911deaa24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Toggle](../toggle.md)

# init(_:isOn:)

<sub>Initializer</sub>

Creates a toggle that generates its label from a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, isOn: Binding<Bool>)
```

## Parameters

- `titleResource` — Text resource for the toggle’s localized title, that describes the purpose of the toggle.

- `isOn` — A binding to a property that indicates whether the toggle is on or off.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf. See `Text` for more information about localizing strings.

## See Also

### Creating a toggle

- [init(isOn:label:)](<init(ison_label_).md>) — Creates a toggle that displays a custom label.
- [init(_:image:isOn:)](<init(__image_ison_).md>) — Creates a toggle that generates its label from a localized string resource and image resource.
- [init(_:systemImage:isOn:)](<init(__systemimage_ison_).md>) — Creates a toggle that generates its label from a localized string key and system image.
