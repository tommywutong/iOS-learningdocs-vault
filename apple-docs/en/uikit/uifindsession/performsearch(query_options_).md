---
title: 'performSearch(query:options:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifindsession/performsearch(query:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifindsession/performsearch(query:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindsession/performsearch%28query%3Aoptions%3A%29.json'
content_hash: 'sha256:9b081a607d49c6c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFindSession](../uifindsession.md)

# performSearch(query:options:)

<sub>Instance Method</sub>

Initiates a search for the query string you provide.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func performSearch(query: String, options: UITextSearchOptions?)
```

## Parameters

- `query` — The string to search, the user provides through the search text field of the system find panel.

- `options` — The object containing all the configurable options for the search.

## Discussion

The system calls this method when the user initiates a search for a string in your app’s text content.

## See Also

### Managing session interactions

- [- performSingleReplacementWithSearchQuery:replacementString:options:](<performsinglereplacement(query_replacementstring_options_).md>) — Replaces a single instance of the query string with the replacement string you provide.
- [- replaceAllInstancesOfSearchQuery:withReplacementString:options:](<replaceall(searchquery_replacementstring_options_).md>) — Replaces all matching instances of the query string with the replacement string you provide.
- [- highlightNextResultInDirection:](<highlightnextresult(in_).md>) — Updates the highlighted result to the next or previous match.
- [- invalidateFoundResults](<invalidatefoundresults().md>) — Invalidates the found ranges and updates the system find panel.
