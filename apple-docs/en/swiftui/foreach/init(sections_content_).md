---
title: 'init(sections:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/foreach/init(sections:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/foreach/init(sections:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/foreach/init%28sections%3Acontent%3A%29.json'
content_hash: 'sha256:ae5786ed089fa724'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ForEach](../foreach.md)

# init(sections:content:)

<sub>Initializer</sub>

Creates an instance that uniquely identifies and creates views across updates based on the sections of a given view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<V>(sections view: V, @ContentBuilder content: @escaping (SectionConfiguration) -> Content) where Data == ForEachSectionCollection<Content>, ID == SectionConfiguration.ID, Content : View, V : View
```

## Parameters

- `view` — The view to extract the sections of.

- `content` — The content builder that creates views from sections

## See Also

### Creating a collection

- [init(_:)](<init(__).md>) — Creates an instance that uniquely identifies and creates table rows across updates based on the identity of the underlying data.
- [init(_:content:)](<init(__content_).md>) — Creates an instance that uniquely identifies and creates map content across updates based on the identity of the underlying data.
- [init(_:id:content:)](<init(__id_content_).md>) — Creates an instance that uniquely identifies and creates map content across updates based on the provided key path to the underlying data’s identifier.
- [init(subviews:content:)](<init(subviews_content_).md>) — Creates an instance that uniquely identifies and creates views across updates based on the subviews of a given view.
