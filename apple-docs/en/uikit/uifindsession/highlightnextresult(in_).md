---
title: 'highlightNextResult(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifindsession/highlightnextresult(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifindsession/highlightnextresult(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindsession/highlightnextresult%28in%3A%29.json'
content_hash: 'sha256:8ff0a3a6927525bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFindSession](../uifindsession.md)

# highlightNextResult(in:)

<sub>Instance Method</sub>

Updates the highlighted result to the next or previous match.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func highlightNextResult(in direction: UITextStorageDirection)
```

## Parameters

- `direction` — The direction, either forward or backward, to move through the search results.

## Discussion

The system calls this method when a person taps the next or previous button, or enters `Return` or `Shift+Return` on a hardware keyboard while the search field has focus.

## See Also

### Managing session interactions

- [- performSearchWithQuery:options:](<performsearch(query_options_).md>) — Initiates a search for the query string you provide.
- [- performSingleReplacementWithSearchQuery:replacementString:options:](<performsinglereplacement(query_replacementstring_options_).md>) — Replaces a single instance of the query string with the replacement string you provide.
- [- replaceAllInstancesOfSearchQuery:withReplacementString:options:](<replaceall(searchquery_replacementstring_options_).md>) — Replaces all matching instances of the query string with the replacement string you provide.
- [- invalidateFoundResults](<invalidatefoundresults().md>) — Invalidates the found ranges and updates the system find panel.
