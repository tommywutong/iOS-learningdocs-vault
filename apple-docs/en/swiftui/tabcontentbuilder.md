---
title: TabContentBuilder
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabcontentbuilder
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontentbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontentbuilder.json'
content_hash: 'sha256:383269588730d533'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TabContentBuilder

<sub>Structure</sub>

A result builder that constructs tabs for a tab view that supports programmatic selection. This builder requires that all tabs in the tab view have the same selection type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@resultBuilder struct TabContentBuilder<TabValue> where TabValue : Hashable
```

## Topics

### Structures

- [Content](tabcontentbuilder/content.md) — A view representation of the content of a builder-based tab view with selection.

### Type Methods

- [buildBlock(_:)](<tabcontentbuilder/buildblock(__).md>)
- [buildBlock(_:_:)](<tabcontentbuilder/buildblock(____).md>)
- [buildBlock(_:_:_:)](<tabcontentbuilder/buildblock(______).md>)
- [buildBlock(_:_:_:_:)](<tabcontentbuilder/buildblock(________).md>)
- [buildBlock(_:_:_:_:_:)](<tabcontentbuilder/buildblock(__________).md>)
- [buildBlock(_:_:_:_:_:_:)](<tabcontentbuilder/buildblock(____________).md>)
- [buildBlock(_:_:_:_:_:_:_:)](<tabcontentbuilder/buildblock(______________).md>)
- [buildBlock(_:_:_:_:_:_:_:_:)](<tabcontentbuilder/buildblock(________________).md>)
- [buildBlock(_:_:_:_:_:_:_:_:_:)](<tabcontentbuilder/buildblock(__________________).md>)
- [buildBlock(_:_:_:_:_:_:_:_:_:_:)](<tabcontentbuilder/buildblock(____________________).md>)
- [buildEither(first:)](<tabcontentbuilder/buildeither(first_).md>)
- [buildEither(second:)](<tabcontentbuilder/buildeither(second_).md>)
- [buildExpression(_:)](<tabcontentbuilder/buildexpression(__).md>)
- [buildIf(_:)](<tabcontentbuilder/buildif(__).md>)
- [buildLimitedAvailability(_:)](<tabcontentbuilder/buildlimitedavailability(__).md>)

## See Also

### Configuring a tab

- [sectionActions(content:)](<view/sectionactions(content_).md>) — Adds custom actions to a section.
- [TabPlacement](tabplacement.md) — A place that a tab can appear.
- [TabContent](tabcontent.md) — A type that provides content for programmatically selectable tabs in a tab view.
- [AnyTabContent](anytabcontent.md) — Type erased tab content.
