---
title: TabPlacement
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabplacement
source_url: 'https://developer.apple.com/documentation/swiftui/tabplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabplacement.json'
content_hash: 'sha256:e288de71974a7e23'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TabPlacement

<sub>Structure</sub>

A place that a tab can appear.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TabPlacement
```

## Overview

Not all `TabView` styles support all placements.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Type Properties

- [automatic](tabplacement/automatic.md) — The default tab location.
- [pinned](tabplacement/pinned.md) — The pinned tab placement location.
- [sidebarOnly](tabplacement/sidebaronly.md) — The sidebar tab placement location.

## See Also

### Configuring a tab

- [sectionActions(content:)](<view/sectionactions(content_).md>) — Adds custom actions to a section.
- [TabContentBuilder](tabcontentbuilder.md) — A result builder that constructs tabs for a tab view that supports programmatic selection. This builder requires that all tabs in the tab view have the same selection type.
- [TabContent](tabcontent.md) — A type that provides content for programmatically selectable tabs in a tab view.
- [AnyTabContent](anytabcontent.md) — Type erased tab content.
