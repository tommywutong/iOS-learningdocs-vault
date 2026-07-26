---
title: 'init(_:sources:isOn:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/toggle/init(_:sources:ison:)'
source_url: 'https://developer.apple.com/documentation/swiftui/toggle/init(_:sources:ison:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toggle/init%28_%3Asources%3Aison%3A%29.json'
content_hash: 'sha256:1536e16fafa8c186'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Toggle](../toggle.md)

# init(_:sources:isOn:)

<sub>Initializer</sub>

Creates a toggle representing a collection of values that generates its label from a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init<C>(_ titleResource: LocalizedStringResource, sources: C, isOn: KeyPath<C.Element, Binding<Bool>>) where C : RandomAccessCollection
```

## Parameters

- `titleResource` — Text resource for the toggle’s localized title, that describes the purpose of the toggle.

- `sources` — A collection of values used as the source for rendering the Toggle’s state.

- `isOn` — The key path of the values that determines whether the toggle is on, mixed or off.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf. See `Text` for more information about localizing strings.

The following example creates a single toggle that represents the state of multiple alarms:

```swift
struct Alarm: Hashable, Identifiable {
    var id = UUID()
    var isOn = false
    var name = ""
}

@State private var alarms = [
    Alarm(isOn: true, name: "Morning"),
    Alarm(isOn: false, name: "Evening")
]

Toggle("Enable all alarms", sources: $alarms, isOn: \.isOn)
```

## See Also

### Creating a toggle for a collection

- [init(sources:isOn:label:)](<init(sources_ison_label_).md>) — Creates a toggle representing a collection of values with a custom label.
- [init(_:image:sources:isOn:)](<init(__image_sources_ison_).md>) — Creates a toggle representing a collection of values that generates its label from a localized string resource and image resource.
- [init(_:systemImage:sources:isOn:)](<init(__systemimage_sources_ison_).md>) — Creates a toggle representing a collection of values that generates its label from a localized string key and system image.
