---
title: 'init(_:image:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/controlgroup/init(_:image:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/controlgroup/init(_:image:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlgroup/init%28_%3Aimage%3Acontent%3A%29.json'
content_hash: 'sha256:af8d581c101a9860'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlGroup](../controlgroup.md)

# init(_:image:content:)

<sub>Initializer</sub>

Creates a new control group with the specified content that generates its label from a localized string resource and image resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@export(implementation) nonisolated init<C>(_ titleResource: LocalizedStringResource, image: ImageResource, @ContentBuilder content: () -> C) where Content == LabeledControlGroupContent<C, Label<Text, Image>>, C : View
```

## Parameters

- `titleResource` — Text resource for the group’s localized title, that describes the contents of the group.

## See Also

### Creating a control group with an image

- [init(_:systemImage:content:)](<init(__systemimage_content_).md>) — Creates a new control group with the specified content that generates its label from a string and image name.
