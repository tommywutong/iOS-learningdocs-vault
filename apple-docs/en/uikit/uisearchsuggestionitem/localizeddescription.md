---
title: localizedDescription
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchsuggestionitem/localizeddescription
source_url: 'https://developer.apple.com/documentation/uikit/uisearchsuggestionitem/localizeddescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchsuggestionitem/localizeddescription.json'
content_hash: 'sha256:b08e49a79636c092'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchSuggestionItem](../uisearchsuggestionitem.md)

# localizedDescription

<sub>Instance Property</sub>

A description of the suggestion.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var localizedDescription: String? { get }
```

## Discussion

The system uses this description for accessibility.

## See Also

### Describing a search suggestion

- [localizedSuggestion](localizedsuggestion.md) — A label for the suggestion, usually the search term the suggestion represents.
- [localizedAttributedSuggestion](localizedattributedsuggestion.md) — An attributed label for the suggestion, usually the search term the suggestion represents.
- [iconImage](iconimage.md) — An image for display on the suggestion.
- [representedObject](representedobject.md) — An object for tracking supplementary information about the search suggestion.
