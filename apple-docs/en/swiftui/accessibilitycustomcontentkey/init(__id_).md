---
title: 'init(_:id:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/accessibilitycustomcontentkey/init(_:id:)'
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilitycustomcontentkey/init(_:id:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilitycustomcontentkey/init%28_%3Aid%3A%29.json'
content_hash: 'sha256:1250516ecbdceee0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityCustomContentKey](../accessibilitycustomcontentkey.md)

# init(_:id:)

<sub>Initializer</sub>

Create an `AccessibilityCustomContentKey` with the specified label and identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) init(_ label: LocalizedStringResource, id: String)
```

## Parameters

- `label` — Localized text describing to the user what is contained in this additional information entry. For example: “orientation”.

- `id` — String used to identify the additional information entry to SwiftUI. Adding an entry will replace any previous value with the same identifier.

## See Also

### Creating a key

- [init(_:)](<init(__).md>) — Create an `AccessibilityCustomContentKey` with the specified label.
