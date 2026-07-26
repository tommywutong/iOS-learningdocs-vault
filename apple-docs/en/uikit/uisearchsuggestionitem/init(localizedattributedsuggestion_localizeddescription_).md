---
title: 'init(localizedAttributedSuggestion:localizedDescription:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchsuggestionitem/init(localizedattributedsuggestion:localizeddescription:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchsuggestionitem/init(localizedattributedsuggestion:localizeddescription:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchsuggestionitem/init%28localizedattributedsuggestion%3Alocalizeddescription%3A%29.json'
content_hash: 'sha256:eee804b115af8f84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchSuggestionItem](../uisearchsuggestionitem.md)

# init(localizedAttributedSuggestion:localizedDescription:)

<sub>Initializer</sub>

Creates a search suggestion with the specified attributed label and accessibility description.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(localizedAttributedSuggestion suggestion: NSAttributedString, localizedDescription description: String?)
```

## Parameters

- `suggestion` — An attributed label for the suggestion, usually the search term the suggestion represents.

- `description` — A description of the suggestion. The system uses this description for accessibility.

## See Also

### Creating a search suggestion

- [- initWithLocalizedSuggestion:localizedDescription:iconImage:](<init(localizedsuggestion_localizeddescription_iconimage_).md>) — Creates a search suggestion with the specified text and image attributes.
- [- initWithLocalizedAttributedSuggestion:localizedDescription:iconImage:](<init(localizedattributedsuggestion_localizeddescription_iconimage_).md>) — Creates a search suggestion with the specified attributed label, accessibility description, and image.
- [- initWithLocalizedSuggestion:localizedDescription:](<init(localizedsuggestion_localizeddescription_).md>) — Creates a search suggestion with the specified label and accessibility description.
- [- initWithLocalizedSuggestion:](<init(localizedsuggestion_).md>) — Creates a search suggestion with the specified label.
- [- initWithLocalizedAttributedSuggestion:](<init(localizedattributedsuggestion_).md>) — Creates a search suggestion with the specified attributed label.
