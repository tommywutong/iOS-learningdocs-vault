---
title: UISearchSuggestionItem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchsuggestionitem
source_url: 'https://developer.apple.com/documentation/uikit/uisearchsuggestionitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchsuggestionitem.json'
content_hash: 'sha256:b17ec50cf64346b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISearchSuggestionItem

<sub>Class</sub>

A selectable search parameter.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UISearchSuggestionItem
```

## Overview

This class provides a basic implementation of the [UISearchSuggestion](uisearchsuggestion.md) protocol.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UISearchSuggestion](uisearchsuggestion.md)

## Topics

### Creating a search suggestion

- [- initWithLocalizedSuggestion:localizedDescription:iconImage:](<uisearchsuggestionitem/init(localizedsuggestion_localizeddescription_iconimage_).md>) — Creates a search suggestion with the specified text and image attributes.
- [- initWithLocalizedAttributedSuggestion:localizedDescription:iconImage:](<uisearchsuggestionitem/init(localizedattributedsuggestion_localizeddescription_iconimage_).md>) — Creates a search suggestion with the specified attributed label, accessibility description, and image.
- [- initWithLocalizedSuggestion:localizedDescription:](<uisearchsuggestionitem/init(localizedsuggestion_localizeddescription_).md>) — Creates a search suggestion with the specified label and accessibility description.
- [- initWithLocalizedAttributedSuggestion:localizedDescription:](<uisearchsuggestionitem/init(localizedattributedsuggestion_localizeddescription_).md>) — Creates a search suggestion with the specified attributed label and accessibility description.
- [- initWithLocalizedSuggestion:](<uisearchsuggestionitem/init(localizedsuggestion_).md>) — Creates a search suggestion with the specified label.
- [- initWithLocalizedAttributedSuggestion:](<uisearchsuggestionitem/init(localizedattributedsuggestion_).md>) — Creates a search suggestion with the specified attributed label.

### Describing a search suggestion

- [localizedSuggestion](uisearchsuggestionitem/localizedsuggestion.md) — A label for the suggestion, usually the search term the suggestion represents.
- [localizedAttributedSuggestion](uisearchsuggestionitem/localizedattributedsuggestion.md) — An attributed label for the suggestion, usually the search term the suggestion represents.
- [localizedDescription](uisearchsuggestionitem/localizeddescription.md) — A description of the suggestion.
- [iconImage](uisearchsuggestionitem/iconimage.md) — An image for display on the suggestion.
- [representedObject](uisearchsuggestionitem/representedobject.md) — An object for tracking supplementary information about the search suggestion.

## See Also

### Providing search suggestions

- [searchSuggestions](uisearchcontroller/searchsuggestions.md) — A list of suggestions to offer as shortcuts below the search field.
- [ignoresSearchSuggestionsForSearchBarPlacementStacked](uisearchcontroller/ignoressearchsuggestionsforsearchbarplacementstacked.md) — A Boolean value you use to specify whether the search controller prevents search suggestions from displaying for a stacked search bar.
- [UISearchSuggestion](uisearchsuggestion.md) — A set of attributes that a selectable search suggestion must provide.
