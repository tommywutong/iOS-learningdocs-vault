---
title: 'replaceAll(queryString:options:withText:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-3wkjv/replaceall(querystring:options:withtext:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/replaceall(querystring:options:withtext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-3wkjv/replaceall%28querystring%3Aoptions%3Awithtext%3A%29.json'
content_hash: 'sha256:f5d727b52f380f77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-3wkjv.md)

# replaceAll(queryString:options:withText:)

<sub>Instance Method</sub>

Informs the searchable object to replace all matching text across all searchable documents.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func replaceAll(queryString: String, options: UITextSearchOptions, withText: String)
```

## Parameters

- `queryString` — The string to search for and replace.

- `options` — The configurable options to use for matching words and comparing strings.

- `withText` — The string to replace the text with.

## Discussion

When [supportsTextReplacement](supportstextreplacement.md) returns `YES,` the system calls this method during a find session to request the replacement of all text matching the query string.

## Default Implementations

### UITextSearching Implementations

- [replaceAll(queryString:options:withText:)](<replaceall(querystring_options_withtext_)-72c3k.md>)

## See Also

### Handling replacements

- [supportsTextReplacement](supportstextreplacement.md) — A Boolean value that indicates whether the searchable object supports replacing text.
- [replace(foundTextRange:document:withText:)](<replace(foundtextrange_document_withtext_).md>) — Informs the searchable object to replace the text range for the highlighted search result.
- [shouldReplace(foundTextRange:document:withText:)](<shouldreplace(foundtextrange_document_withtext_).md>) — Determines whether the searchable object allows replacement of the text range you provide.
