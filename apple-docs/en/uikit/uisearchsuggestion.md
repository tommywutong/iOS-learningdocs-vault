---
title: UISearchSuggestion
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchsuggestion
source_url: 'https://developer.apple.com/documentation/uikit/uisearchsuggestion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchsuggestion.json'
content_hash: 'sha256:6f124b303419cdaf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISearchSuggestion

<sub>Protocol</sub>

A set of attributes that a selectable search suggestion must provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UISearchSuggestion : NSObjectProtocol
```

## Overview

Provide common or predicted search queries to save the user the time of typing their entire query in a [UISearchController](uisearchcontroller.md) field. [UISearchSuggestionItem](uisearchsuggestionitem.md) provides a simple implementation of this protocol. You may also define and use your own type that conforms to [UISearchSuggestion](uisearchsuggestion.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UISearchSuggestionItem](uisearchsuggestionitem.md)

## Topics

### Describing a search suggestion

- [localizedSuggestion](uisearchsuggestion/localizedsuggestion.md) — A label for the suggestion, usually the search term the suggestion represents.
- [localizedDescription](uisearchsuggestion/localizeddescription.md) — A description of the suggestion.
- [localizedAttributedSuggestion](uisearchsuggestion/localizedattributedsuggestion.md) — An attributed label for the suggestion, usually the search term the suggestion represents.
- [iconImage](uisearchsuggestion/iconimage.md) — An image for display on the suggestion.
- [representedObject](uisearchsuggestion/representedobject.md) — An object for tracking supplementary information about the search suggestion.

## See Also

### Providing search suggestions

- [searchSuggestions](uisearchcontroller/searchsuggestions.md) — A list of suggestions to offer as shortcuts below the search field.
- [ignoresSearchSuggestionsForSearchBarPlacementStacked](uisearchcontroller/ignoressearchsuggestionsforsearchbarplacementstacked.md) — A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [UISearchSuggestionItem](uisearchsuggestionitem.md) — A selectable search parameter.
