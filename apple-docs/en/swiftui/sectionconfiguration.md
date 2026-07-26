---
title: SectionConfiguration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/sectionconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionconfiguration.json'
content_hash: 'sha256:fc222c0be7e68b09'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SectionConfiguration

<sub>Structure</sub>

Specifies the contents of a section.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SectionConfiguration
```

## Overview

A `SectionConfiguration` includes the content of the section, as well as its header and footer.

A `SectionConfiguration` can represent either an explicit section, or groups of sibling views that are not explicitly wrapped in a section.

Notably, the `header`, `footer` and `content` properties of a `SectionConfiguration` are all `SubviewsCollection`s as they can be made up of multiple subviews. That means in most cases, the subviews collection should be treated as a collection (either indexed into, or used with a `ForEach`), or the subviews collection should be wrapped in a container view, like a layout, or other custom container:

```swift
PinboardSectionsLayout {
    ForEach(sections: content) { section in
        VStack {
            HStack { section.header }
            section.content
            HStack { section.footer }
        }
    }
}
```

Here, we want to create one view for `PinboardSectionsLayout` to place per section in content. To do that, we surround the `ForEach` body in another container, a `VStack` layout, ensuring the different subviews of section.content are treated as a single view by the surrounding layout. Additionally, surrounding the header and footer in an `HStack` layout avoids vertically stacking subviews of the header and footer which we want visually grouped together.

## Relationships

- **Conforms To**: [Identifiable](../swift/identifiable.md)

## Topics

### Structures

- [Actions](sectionconfiguration/actions-swift.struct.md) — The type-erased actions of a section.
- [ID](sectionconfiguration/id-swift.struct.md) — A unique identifier for a section.

### Instance Properties

- [actions](sectionconfiguration/actions-swift.property.md) — Custom actions associated with a section.
- [containerValues](sectionconfiguration/containervalues.md) — The container values associated with the given section.
- [content](sectionconfiguration/content.md) — The contents of the section body.
- [footer](sectionconfiguration/footer.md) — The contents of the section footer.
- [header](sectionconfiguration/header.md) — The contents of the section header.
- [id](sectionconfiguration/id-swift.property.md) — A unique identifier representing the section.

## See Also

### Organizing views into sections

- [Section](section.md) — A container view that you can use to add hierarchy within certain views.
- [SectionCollection](sectioncollection.md) — An opaque collection representing the sections of view.
