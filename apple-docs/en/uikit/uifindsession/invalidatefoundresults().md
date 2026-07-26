---
title: invalidateFoundResults()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifindsession/invalidatefoundresults()
source_url: 'https://developer.apple.com/documentation/uikit/uifindsession/invalidatefoundresults()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindsession/invalidatefoundresults%28%29.json'
content_hash: 'sha256:85f32931e4b3e24d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFindSession](../uifindsession.md)

# invalidateFoundResults()

<sub>Instance Method</sub>

Invalidates the found ranges and updates the system find panel.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func invalidateFoundResults()
```

## Discussion

If the [searchText](../uifindinteraction/searchtext.md) for the find interaction is non-empty, a call to this method this triggers a call to [- performSearchWithQuery:options:](<performsearch(query_options_).md>) immediately after to begin a new search.

## See Also

### Managing session interactions

- [- performSearchWithQuery:options:](<performsearch(query_options_).md>) — Initiates a search for the query string you provide.
- [- performSingleReplacementWithSearchQuery:replacementString:options:](<performsinglereplacement(query_replacementstring_options_).md>) — Replaces a single instance of the query string with the replacement string you provide.
- [- replaceAllInstancesOfSearchQuery:withReplacementString:options:](<replaceall(searchquery_replacementstring_options_).md>) — Replaces all matching instances of the query string with the replacement string you provide.
- [- highlightNextResultInDirection:](<highlightnextresult(in_).md>) — Updates the highlighted result to the next or previous match.
