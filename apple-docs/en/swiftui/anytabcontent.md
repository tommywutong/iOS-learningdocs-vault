---
title: AnyTabContent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/anytabcontent
source_url: 'https://developer.apple.com/documentation/swiftui/anytabcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anytabcontent.json'
content_hash: 'sha256:eacdc7123b998c76'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AnyTabContent

<sub>Structure</sub>

Type erased tab content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct AnyTabContent<SelectionValue> where SelectionValue : Hashable
```

## Relationships

- **Conforms To**: [TabContent](tabcontent.md)

## Topics

### Initializers

- [init(_:)](<anytabcontent/init(__).md>) — Create an instance that type-erases `tabContent`.

## See Also

### Configuring a tab

- [sectionActions(content:)](<view/sectionactions(content_).md>) — Adds custom actions to a section.
- [TabPlacement](tabplacement.md) — A place that a tab can appear.
- [TabContentBuilder](tabcontentbuilder.md) — A result builder that constructs tabs for a tab view that supports programmatic selection. This builder requires that all tabs in the tab view have the same selection type.
- [TabContent](tabcontent.md) — A type that provides content for programmatically selectable tabs in a tab view.
