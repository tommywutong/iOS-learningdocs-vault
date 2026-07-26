---
title: 'replaceAll(searchQuery:replacementString:options:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifindsession/replaceall(searchquery:replacementstring:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifindsession/replaceall(searchquery:replacementstring:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindsession/replaceall%28searchquery%3Areplacementstring%3Aoptions%3A%29.json'
content_hash: 'sha256:a0b728350d82d370'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFindSession](../uifindsession.md)

# replaceAll(searchQuery:replacementString:options:)

<sub>Instance Method</sub>

Replaces all matching instances of the query string with the replacement string you provide.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func replaceAll(searchQuery: String, replacementString: String, options: UITextSearchOptions?)
```

## Parameters

- `searchQuery` — The string to search for and replace, the user provides through the search text field of the system find panel.

- `replacementString` — The replacement string, the user provides through the replace text field of the system find panel.

- `options` — The object containing all the configurable options for the search.

## See Also

### Managing session interactions

- [- performSearchWithQuery:options:](<performsearch(query_options_).md>) — Initiates a search for the query string you provide.
- [- performSingleReplacementWithSearchQuery:replacementString:options:](<performsinglereplacement(query_replacementstring_options_).md>) — Replaces a single instance of the query string with the replacement string you provide.
- [- highlightNextResultInDirection:](<highlightnextresult(in_).md>) — Updates the highlighted result to the next or previous match.
- [- invalidateFoundResults](<invalidatefoundresults().md>) — Invalidates the found ranges and updates the system find panel.
