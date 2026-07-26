---
title: 'init(localizedSuggestion:localizedDescription:iconImage:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchsuggestionitem/init(localizedsuggestion:localizeddescription:iconimage:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchsuggestionitem/init(localizedsuggestion:localizeddescription:iconimage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchsuggestionitem/init%28localizedsuggestion%3Alocalizeddescription%3Aiconimage%3A%29.json'
content_hash: 'sha256:8cb158557af07853'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchSuggestionItem](../uisearchsuggestionitem.md)

# init(localizedSuggestion:localizedDescription:iconImage:)

<sub>Initializer</sub>

Creates a search suggestion with the specified text and image attributes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(localizedSuggestion suggestion: String, localizedDescription description: String?, iconImage: UIImage?)
```

## Parameters

- `suggestion` — A label for the suggestion, usually the search term the suggestion represents.

- `description` — A description of the suggestion. The system uses this description for accessibility.

- `iconImage` — An image for display on the suggestion.

## See Also

### Creating a search suggestion

- [- initWithLocalizedAttributedSuggestion:localizedDescription:iconImage:](<init(localizedattributedsuggestion_localizeddescription_iconimage_).md>) — Creates a search suggestion with the specified attributed label, accessibility description, and image.
- [- initWithLocalizedSuggestion:localizedDescription:](<init(localizedsuggestion_localizeddescription_).md>) — Creates a search suggestion with the specified label and accessibility description.
- [- initWithLocalizedAttributedSuggestion:localizedDescription:](<init(localizedattributedsuggestion_localizeddescription_).md>) — Creates a search suggestion with the specified attributed label and accessibility description.
- [- initWithLocalizedSuggestion:](<init(localizedsuggestion_).md>) — Creates a search suggestion with the specified label.
- [- initWithLocalizedAttributedSuggestion:](<init(localizedattributedsuggestion_).md>) — Creates a search suggestion with the specified attributed label.
