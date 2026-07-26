---
title: 'init(isExpanded:content:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/disclosuregroup/init(isexpanded:content:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/disclosuregroup/init(isexpanded:content:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/disclosuregroup/init%28isexpanded%3Acontent%3Alabel%3A%29.json'
content_hash: 'sha256:d40f2fad3f48a50f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DisclosureGroup](../disclosuregroup.md)

# init(isExpanded:content:label:)

<sub>Initializer</sub>

Creates a disclosure group with the given label and content views, and a binding to the expansion state (expanded or collapsed).

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(isExpanded: Binding<Bool>, @ContentBuilder content: @escaping () -> Content, @ContentBuilder label: () -> Label)
```

## Parameters

- `isExpanded` — A binding to a Boolean value that determines the group’s expansion state (expanded or collapsed).

- `content` — The content shown when the disclosure group expands.

- `label` — A view that describes the content of the disclosure group.

## See Also

### Creating a disclosure group

- [init(_:content:)](<init(__content_).md>) — Creates a disclosure group, using a provided localized string resource to create a text view for the label.
- [init(content:label:)](<init(content_label_).md>) — Creates a disclosure group with the given label and content views.
- [init(_:isExpanded:content:)](<init(__isexpanded_content_).md>) — Creates a disclosure group, using a provided localized string resource to create a text view for the label, and a binding to the expansion state (expanded or collapsed).
