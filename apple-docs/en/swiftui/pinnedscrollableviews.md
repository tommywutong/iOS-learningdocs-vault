---
title: PinnedScrollableViews
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pinnedscrollableviews
source_url: 'https://developer.apple.com/documentation/swiftui/pinnedscrollableviews'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pinnedscrollableviews.json'
content_hash: 'sha256:8d69f64fbfd734e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PinnedScrollableViews

<sub>Structure</sub>

A set of view types that may be pinned to the bounds of a scroll view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PinnedScrollableViews
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting scrollable view types

- [sectionHeaders](pinnedscrollableviews/sectionheaders.md) — The header view of each `Section` will be pinned.
- [sectionFooters](pinnedscrollableviews/sectionfooters.md) — The footer view of each `Section` will be pinned.

## See Also

### Dynamically arranging views in one dimension

- [Grouping data with lazy stack views](grouping-data-with-lazy-stack-views.md) — Split content into logical sections inside lazy stack views.
- [Creating performant scrollable stacks](creating-performant-scrollable-stacks.md) — Display large numbers of repeated views efficiently with scroll views, stack views, and lazy stacks.
- [LazyHStack](lazyhstack.md) — A view that arranges its children in a line that grows horizontally, creating items only as needed.
- [LazyVStack](lazyvstack.md) — A view that arranges its children in a line that grows vertically, creating items only as needed.
