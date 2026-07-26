---
title: GroupElementsOfContent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/groupelementsofcontent
source_url: 'https://developer.apple.com/documentation/swiftui/groupelementsofcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/groupelementsofcontent.json'
content_hash: 'sha256:1e52b31da9734664'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GroupElementsOfContent

<sub>Structure</sub>

Transforms the subviews of a given view into a resulting content view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct GroupElementsOfContent<Subviews, Content> where Subviews : View, Content : View
```

## Overview

You don’t use this type directly. Instead SwiftUI creates this type on your behalf.

## Relationships

- **Conforms To**: [View](view.md)

## See Also

### Grouping views into a container

- [Creating custom container views](creating-custom-container-views.md) — Access individual subviews to compose flexible container views.
- [Group](group.md) — A type that collects multiple instances of a content type — like views, scenes, or commands — into a single unit.
- [GroupSectionsOfContent](groupsectionsofcontent.md) — Transforms the sections of a given view into a resulting content view.
