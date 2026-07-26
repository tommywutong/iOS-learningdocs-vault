---
title: 'init(_:systemImage:value:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tab/init(_:systemimage:value:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tab/init(_:systemimage:value:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tab/init%28_%3Asystemimage%3Avalue%3Acontent%3A%29.json'
content_hash: 'sha256:924a48bdbdf577d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Tab](../tab.md)

# init(_:systemImage:value:content:)

<sub>Initializer</sub>

Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value using a system image for the tab’s tab item image, with a localized string key label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, value: Value, @ContentBuilder content: () -> Content) where Label == DefaultTabLabel
```

## Parameters

- `titleKey` — The localized string key label for the tab’s tab item.

- `systemImage` — The system image for the tab’s tab item.

- `value` — The `selection` value which selects this tab.

- `content` — The view content of the tab.

## See Also

### Creating a tab with system symbol

- [init(_:systemImage:content:)](<init(__systemimage_content_).md>) — Creates a new tab that you can use in a tab view using a system image for the tab item’s image, and a localized string key label.
- [init(_:systemImage:role:content:)](<init(__systemimage_role_content_).md>) — Creates a new tab that you can use in a tab view using a system image for the tab item’s image, and a localized string key label.
- [init(_:systemImage:value:role:content:)](<init(__systemimage_value_role_content_).md>) — Creates a tab that the tab view presents when the tab view’s selection matches the tab’s value using a system image for the tab’s tab item image, with a localized string key label.
