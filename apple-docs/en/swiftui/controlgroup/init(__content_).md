---
title: 'init(_:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/controlgroup/init(_:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/controlgroup/init(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlgroup/init%28_%3Acontent%3A%29.json'
content_hash: 'sha256:0e023467d2aa80a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlGroup](../controlgroup.md)

# init(_:content:)

<sub>Initializer</sub>

Creates a new control group with the specified content that generates its label from a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@export(implementation) nonisolated init<C, S>(_ title: S, @ContentBuilder content: () -> C) where Content == LabeledControlGroupContent<C, Text>, C : View, S : StringProtocol
```

## Parameters

- `title` — A string that describes the contents of the group.

## See Also

### Creating a control group

- [init(content:)](<init(content_).md>) — Creates a new ControlGroup with the specified children
- [init(content:label:)](<init(content_label_).md>) — Creates a new control group with the specified content and a label.
