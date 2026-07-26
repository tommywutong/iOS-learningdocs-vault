---
title: 'performSingleReplacement(query:replacementString:options:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifindsession/performsinglereplacement(query:replacementstring:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifindsession/performsinglereplacement(query:replacementstring:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindsession/performsinglereplacement%28query%3Areplacementstring%3Aoptions%3A%29.json'
content_hash: 'sha256:2b231da7224de15b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFindSession](../uifindsession.md)

# performSingleReplacement(query:replacementString:options:)

<sub>Instance Method</sub>

Replaces a single instance of the query string with the replacement string you provide.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func performSingleReplacement(query searchQuery: String, replacementString: String, options: UITextSearchOptions?)
```

## Parameters

- `searchQuery` — The string to search for and replace, the user provides through the search text field of the system find panel.

- `replacementString` — The replacement string, the user provides through the replace text field of the system find panel.

- `options` — The object containing all the configurable options for the search.

## Discussion

The system calls this method when the user initiates the replacement the text for a single match of a string in your app’s text content with the replacement string.

## See Also

### Managing session interactions

- [- performSearchWithQuery:options:](<performsearch(query_options_).md>) — Initiates a search for the query string you provide.
- [- replaceAllInstancesOfSearchQuery:withReplacementString:options:](<replaceall(searchquery_replacementstring_options_).md>) — Replaces all matching instances of the query string with the replacement string you provide.
- [- highlightNextResultInDirection:](<highlightnextresult(in_).md>) — Updates the highlighted result to the next or previous match.
- [- invalidateFoundResults](<invalidatefoundresults().md>) — Invalidates the found ranges and updates the system find panel.
