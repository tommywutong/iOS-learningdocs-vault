---
title: 'suggestionWithLocalizedAttributedSuggestion:descriptionString:iconImage:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchsuggestionitem/suggestionwithlocalizedattributedsuggestion:descriptionstring:iconimage:'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchsuggestionitem/suggestionwithlocalizedattributedsuggestion:descriptionstring:iconimage:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchsuggestionitem/suggestionwithlocalizedattributedsuggestion%3Adescriptionstring%3Aiconimage%3A.json'
content_hash: 'sha256:996096a92e9edc56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchSuggestionItem](../uisearchsuggestionitem.md)

# suggestionWithLocalizedAttributedSuggestion:descriptionString:iconImage:

<sub>Type Method</sub>

Creates a search suggestion with the specified attributed label, accessibility description, and image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) suggestionWithLocalizedAttributedSuggestion:(NSAttributedString *) suggestion descriptionString:(NSString *) description iconImage:(UIImage *) iconImage;
```

## Parameters

- `suggestion` — An attributed label for the suggestion, usually the search term the suggestion represents.

- `description` — A description of the suggestion. The system uses this description for accessibility.

- `iconImage` — An image for display on the suggestion.

## See Also

### Creating a search suggestion

- [- initWithLocalizedSuggestion:localizedDescription:iconImage:](<init(localizedsuggestion_localizeddescription_iconimage_).md>) — Creates a search suggestion with the specified text and image attributes.
- [- initWithLocalizedAttributedSuggestion:localizedDescription:iconImage:](<init(localizedattributedsuggestion_localizeddescription_iconimage_).md>) — Creates a search suggestion with the specified attributed label, accessibility description, and image.
- [suggestionWithLocalizedSuggestion:descriptionString:iconImage:](suggestionwithlocalizedsuggestion_descriptionstring_iconimage_.md) — Creates a search suggestion with the specified text and image attributes.
- [- initWithLocalizedSuggestion:localizedDescription:](<init(localizedsuggestion_localizeddescription_).md>) — Creates a search suggestion with the specified label and accessibility description.
- [- initWithLocalizedAttributedSuggestion:localizedDescription:](<init(localizedattributedsuggestion_localizeddescription_).md>) — Creates a search suggestion with the specified attributed label and accessibility description.
- [suggestionWithLocalizedSuggestion:descriptionString:](suggestionwithlocalizedsuggestion_descriptionstring_.md) — Creates a search suggestion with the specified label and accessibility description.
- [suggestionWithLocalizedAttributedSuggestion:descriptionString:](suggestionwithlocalizedattributedsuggestion_descriptionstring_.md) — Creates a search suggestion with the specified attributed label and accessibility description.
- [- initWithLocalizedSuggestion:](<init(localizedsuggestion_).md>) — Creates a search suggestion with the specified label.
- [- initWithLocalizedAttributedSuggestion:](<init(localizedattributedsuggestion_).md>) — Creates a search suggestion with the specified attributed label.
- [suggestionWithLocalizedSuggestion:](suggestionwithlocalizedsuggestion_.md) — Creates a search suggestion with the specified label.
- [suggestionWithLocalizedAttributedSuggestion:](suggestionwithlocalizedattributedsuggestion_.md) — Creates a search suggestion with the specified attributed label.
