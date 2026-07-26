---
title: GroupSectionsOfContent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/groupsectionsofcontent
source_url: 'https://developer.apple.com/documentation/swiftui/groupsectionsofcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/groupsectionsofcontent.json'
content_hash: 'sha256:c6d635156f7edd6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GroupSectionsOfContent

<sub>Structure</sub>

Transforms the sections of a given view into a resulting content view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct GroupSectionsOfContent<Sections, Content> where Sections : View, Content : View
```

## Overview

You don’t use this type directly. Instead SwiftUI creates this type on your behalf.

## Relationships

- **Conforms To**: [View](view.md)

## See Also

### Grouping views into a container

- [Creating custom container views](creating-custom-container-views.md) — Access individual subviews to compose flexible container views.
- [Group](group.md) — A type that collects multiple instances of a content type — like views, scenes, or commands — into a single unit.
- [GroupElementsOfContent](groupelementsofcontent.md) — Transforms the subviews of a given view into a resulting content view.
