---
title: SearchSuggestionsPlacement.Set
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/searchsuggestionsplacement/set
source_url: 'https://developer.apple.com/documentation/swiftui/searchsuggestionsplacement/set'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/searchsuggestionsplacement/set.json'
content_hash: 'sha256:6f2bb78c105241a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SearchSuggestionsPlacement](../searchsuggestionsplacement.md)

# SearchSuggestionsPlacement.Set

<sub>Structure</sub>

An efficient set of search suggestion display modes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Set
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Getting placement sets

- [content](set/content.md) — A set containing placements with the apps main content, excluding the menu placement.
- [menu](set/menu.md) — A set containing the menu display mode.

### Creating a set

- [init(rawValue:)](<set/init(rawvalue_).md>) — Creates a set of search suggestions from an integer.
- [rawValue](set/rawvalue.md) — The raw value that records the search suggestion display modes.

### Supporting types

- [Element](set/element.md) — A type for the elements of the set.
