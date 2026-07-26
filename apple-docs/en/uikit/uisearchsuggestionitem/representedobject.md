---
title: representedObject
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchsuggestionitem/representedobject
source_url: 'https://developer.apple.com/documentation/uikit/uisearchsuggestionitem/representedobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchsuggestionitem/representedobject.json'
content_hash: 'sha256:9f3238c76133e0d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchSuggestionItem](../uisearchsuggestionitem.md)

# representedObject

<sub>Instance Property</sub>

An object for tracking supplementary information about the search suggestion.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var representedObject: Any? { get set }
```

## Discussion

Use this property to associate the search suggestion with a corresponding object.

## See Also

### Describing a search suggestion

- [localizedSuggestion](localizedsuggestion.md) — A label for the suggestion, usually the search term the suggestion represents.
- [localizedAttributedSuggestion](localizedattributedsuggestion.md) — An attributed label for the suggestion, usually the search term the suggestion represents.
- [localizedDescription](localizeddescription.md) — A description of the suggestion.
- [iconImage](iconimage.md) — An image for display on the suggestion.
