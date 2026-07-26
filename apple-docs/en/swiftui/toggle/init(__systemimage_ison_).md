---
title: 'init(_:systemImage:isOn:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/toggle/init(_:systemimage:ison:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toggle/init(_:systemimage:ison:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toggle/init%28_%3Asystemimage%3Aison%3A%29.json'
content_hash: 'sha256:9ae0e372bf2faa34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Toggle](../toggle.md)

# init(_:systemImage:isOn:)

<sub>Initializer</sub>

Creates a toggle that generates its label from a localized string key and system image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, isOn: Binding<Bool>)
```

## Parameters

- `titleKey` — The key for the toggle’s localized title, that describes the purpose of the toggle.

- `systemImage` — The name of the image resource to lookup.

- `isOn` — A binding to a property that indicates whether the toggle is on or off.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf, and treats the localized key similar to [init(_:tableName:bundle:comment:)](<../text/init(__tablename_bundle_comment_).md>). See `Text` for more information about localizing strings.

## See Also

### Creating a toggle

- [init(_:isOn:)](<init(__ison_).md>) — Creates a toggle that generates its label from a localized string resource.
- [init(isOn:label:)](<init(ison_label_).md>) — Creates a toggle that displays a custom label.
- [init(_:image:isOn:)](<init(__image_ison_).md>) — Creates a toggle that generates its label from a localized string resource and image resource.
