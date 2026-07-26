---
title: 'init(_:isExpanded:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/disclosuregroup/init(_:isexpanded:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/disclosuregroup/init(_:isexpanded:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/disclosuregroup/init%28_%3Aisexpanded%3Acontent%3A%29.json'
content_hash: 'sha256:95c45e5a838da3a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DisclosureGroup](../disclosuregroup.md)

# init(_:isExpanded:content:)

<sub>Initializer</sub>

Creates a disclosure group, using a provided localized string resource to create a text view for the label, and a binding to the expansion state (expanded or collapsed).

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, isExpanded: Binding<Bool>, @ContentBuilder content: @escaping () -> Content)
```

## Parameters

- `titleResource` — The localized label of `self` that describes the content of the disclosure group.

- `isExpanded` — A binding to a Boolean value that determines the group’s expansion state (expanded or collapsed).

- `content` — The content shown when the disclosure group expands.

## See Also

### Creating a disclosure group

- [init(_:content:)](<init(__content_).md>) — Creates a disclosure group, using a provided localized string resource to create a text view for the label.
- [init(content:label:)](<init(content_label_).md>) — Creates a disclosure group with the given label and content views.
- [init(isExpanded:content:label:)](<init(isexpanded_content_label_).md>) — Creates a disclosure group with the given label and content views, and a binding to the expansion state (expanded or collapsed).
