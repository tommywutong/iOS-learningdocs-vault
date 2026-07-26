---
title: 'suggestionWithLocalizedSuggestion:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchsuggestionitem/suggestionwithlocalizedsuggestion:'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchsuggestionitem/suggestionwithlocalizedsuggestion:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchsuggestionitem/suggestionwithlocalizedsuggestion%3A.json'
content_hash: 'sha256:8bb3a5a5b66f6fef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchSuggestionItem](../uisearchsuggestionitem.md)

# suggestionWithLocalizedSuggestion:

<sub>Type Method</sub>

Creates a search suggestion with the specified label.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) suggestionWithLocalizedSuggestion:(NSString *) suggestion;
```

## Parameters

- `suggestion` — The item’s label, usually the search term.

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
- [suggestionWithLocalizedSuggestion:descriptionString:](suggestionwithlocalizedsuggestion_descriptionstring_.md) — Creates a search suggestion with the specified label and accessibility description.
- [suggestionWithLocalizedAttributedSuggestion:descriptionString:](suggestionwithlocalizedattributedsuggestion_descriptionstring_.md) — Creates a search suggestion with the specified attributed label and accessibility description.
- [- initWithLocalizedSuggestion:](<init(localizedsuggestion_).md>) — Creates a search suggestion with the specified label.
- [- initWithLocalizedAttributedSuggestion:](<init(localizedattributedsuggestion_).md>) — Creates a search suggestion with the specified attributed label.
- [suggestionWithLocalizedAttributedSuggestion:](suggestionwithlocalizedattributedsuggestion_.md) — Creates a search suggestion with the specified attributed label.
