---
title: 'init(_:image:isOn:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/toggle/init(_:image:ison:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toggle/init(_:image:ison:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toggle/init%28_%3Aimage%3Aison%3A%29.json'
content_hash: 'sha256:81f9658b44d0227d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Toggle](../toggle.md)

# init(_:image:isOn:)

<sub>Initializer</sub>

Creates a toggle that generates its label from a localized string resource and image resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, isOn: Binding<Bool>)
```

## Parameters

- `titleResource` — Text resource for the toggle’s localized title, that describes the purpose of the toggle.

- `image` — The name of the image resource to lookup.

- `isOn` — A binding to a property that indicates whether the toggle is on or off.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf. See `Text` for more information about localizing strings.

## See Also

### Creating a toggle

- [init(_:isOn:)](<init(__ison_).md>) — Creates a toggle that generates its label from a localized string resource.
- [init(isOn:label:)](<init(ison_label_).md>) — Creates a toggle that displays a custom label.
- [init(_:systemImage:isOn:)](<init(__systemimage_ison_).md>) — Creates a toggle that generates its label from a localized string key and system image.
