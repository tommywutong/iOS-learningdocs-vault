---
title: 'init(_:systemImage:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/controlgroup/init(_:systemimage:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/controlgroup/init(_:systemimage:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlgroup/init%28_%3Asystemimage%3Acontent%3A%29.json'
content_hash: 'sha256:fa2dedb52acea0fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlGroup](../controlgroup.md)

# init(_:systemImage:content:)

<sub>Initializer</sub>

Creates a new control group with the specified content that generates its label from a string and image name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@export(implementation) nonisolated init<C, S>(_ title: S, systemImage: String, @ContentBuilder content: () -> C) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View, S : StringProtocol
```

## Parameters

- `title` — A string that describes the contents of the group.

- `systemImage` — The name of the image resource to lookup.

## See Also

### Creating a control group with an image

- [init(_:image:content:)](<init(__image_content_).md>) — Creates a new control group with the specified content that generates its label from a localized string resource and image resource.
