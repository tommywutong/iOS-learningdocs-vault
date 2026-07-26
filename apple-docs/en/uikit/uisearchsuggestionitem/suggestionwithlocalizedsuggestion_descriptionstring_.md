---
title: 'suggestionWithLocalizedSuggestion:descriptionString:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchsuggestionitem/suggestionwithlocalizedsuggestion:descriptionstring:'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchsuggestionitem/suggestionwithlocalizedsuggestion:descriptionstring:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchsuggestionitem/suggestionwithlocalizedsuggestion%3Adescriptionstring%3A.json'
content_hash: 'sha256:c8eb8a52b5df9b1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchSuggestionItem](../uisearchsuggestionitem.md)

# suggestionWithLocalizedSuggestion:descriptionString:

<sub>Type Method</sub>

Creates a search suggestion with the specified label and accessibility description.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) suggestionWithLocalizedSuggestion:(NSString *) suggestion descriptionString:(NSString *) description;
```

## Parameters

- `suggestion` — A label for the suggestion, usually the search term the suggestion represents.

- `description` — A description of the suggestion. The system uses this description for accessibility.

## Return Value

A new search suggestion.

## See Also

### Creating a search suggestion

- [- initWithLocalizedSuggestion:localizedDescription:iconImage:](<init(localizedsuggestion_localizeddescription_iconimage_).md>) — Creates a search suggestion with the specified text and image attributes.
- [- initWithLocalizedAttributedSuggestion:localizedDescription:iconImage:](<init(localizedattributedsuggestion_localizeddescription_iconimage_).md>) — Creates a search suggestion with the specified attributed label, accessibility description, and image.
- [suggestionWithLocalizedSuggestion:descriptionString:iconImage:](suggestionwithlocalizedsuggestion_descriptionstring_iconimage_.md) — Creates a search suggestion with the specified text and image attributes.
- [suggestionWithLocalizedAttributedSuggestion:descriptionString:iconImage:](suggestionwithlocalizedattributedsuggestion_descriptionstring_iconimage_.md) — Creates a search suggestion with the specified attributed label, accessibility description, and image.
- [- initWithLocalizedSuggestion:localizedDescription:](<init(localizedsuggestion_localizeddescription_).md>) — Creates a search suggestion with the specified label and accessibility description.
- [- initWithLocalizedAttributedSuggestion:localizedDescription:](<init(localizedattributedsuggestion_localizeddescription_).md>) — Creates a search suggestion with the specified attributed label and accessibility description.
- [suggestionWithLocalizedAttributedSuggestion:descriptionString:](suggestionwithlocalizedattributedsuggestion_descriptionstring_.md) — Creates a search suggestion with the specified attributed label and accessibility description.
- [- initWithLocalizedSuggestion:](<init(localizedsuggestion_).md>) — Creates a search suggestion with the specified label.
- [- initWithLocalizedAttributedSuggestion:](<init(localizedattributedsuggestion_).md>) — Creates a search suggestion with the specified attributed label.
- [suggestionWithLocalizedSuggestion:](suggestionwithlocalizedsuggestion_.md) — Creates a search suggestion with the specified label.
- [suggestionWithLocalizedAttributedSuggestion:](suggestionwithlocalizedattributedsuggestion_.md) — Creates a search suggestion with the specified attributed label.
