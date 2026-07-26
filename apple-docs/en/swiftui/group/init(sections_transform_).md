---
title: 'init(sections:transform:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/group/init(sections:transform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/group/init(sections:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/group/init%28sections%3Atransform%3A%29.json'
content_hash: 'sha256:3363b054db93a379'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Group](../group.md)

# init(sections:transform:)

<sub>Initializer</sub>

Constructs a group from the sections of the given view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Base, Result>(sections view: Base, @ContentBuilder transform: @escaping (SectionCollection) -> Result) where Content == GroupSectionsOfContent<Base, Result>, Base : View, Result : View
```

## Parameters

- `view` — The view to extract the sections of.

## Discussion

Sections are constructed lazily, on demand, so access only as much of this collection as is necessary to create the resulting content.

```swift
struct SectionedStack<Content: View>: View {
    var content: Content

    init(@ContentBuilder content: () -> Content) {
        self.content = content()
    }

    var body: some View {
        VStack {
            Group(sections: content) { sections in
                ForEach(sections) { section in
                    SectionChrome {
                        section.content
                    } header: {
                        section.header
                    } footer: {
                        section.footer
                    }
                }
            }
        }
    }
}
```

This can then be used by creating a `SectionedStack` with it’s content builder-based initializer.

```swift
SectionedStack {
    Section("Header A") {
        Text("Hello")
        Text("World")
    } footer: {
        Text("Footer A")
    }
    Section("Header B") {
        Text("Foo")
        Text("Bar")
    } footer: {
        Text("Footer B")
    }
}
```

Any content of the given view which is not explicitly specified as a section is grouped with its sibling content to form implicit sections, meaning the minimum number of sections in a `SectionCollection` is one. For example in the following `SectionedStack`, there is one explicit section, and two implicit sections containing the content before, and after the explicit section:

```swift
SectionedStack {
    Text("First implicit section")
    Section("Explicit section") {
        Text("Content")
    }
    Text("Second implicit section")
}
```

## See Also

### Creating a group

- [init(content:)](<init(content_).md>) — Creates a group of content.
- [init(subviews:transform:)](<init(subviews_transform_).md>) — Constructs a group from the subviews of the given view.
