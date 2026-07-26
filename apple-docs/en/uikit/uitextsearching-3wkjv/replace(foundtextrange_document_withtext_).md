---
title: 'replace(foundTextRange:document:withText:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-3wkjv/replace(foundtextrange:document:withtext:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/replace(foundtextrange:document:withtext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-3wkjv/replace%28foundtextrange%3Adocument%3Awithtext%3A%29.json'
content_hash: 'sha256:d88012a7b8409521'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-3wkjv.md)

# replace(foundTextRange:document:withText:)

<sub>Instance Method</sub>

Informs the searchable object to replace the text range for the highlighted search result.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func replace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String)
```

## Parameters

- `foundTextRange` — The text range to replace.

- `document` — A string that uniquely identifies a document when searching multiple documents, or `nil` when searching a single document.

- `withText` — The string to replace the text with.

## Discussion

When [supportsTextReplacement](supportstextreplacement.md) returns `YES,` the system calls this method during a find session to request a text range to replace.

## Default Implementations

### UITextSearching Implementations

- [replace(foundTextRange:document:withText:)](<replace(foundtextrange_document_withtext_)-4psma.md>)

## See Also

### Handling replacements

- [supportsTextReplacement](supportstextreplacement.md) — A Boolean value that indicates whether the searchable object supports replacing text.
- [replaceAll(queryString:options:withText:)](<replaceall(querystring_options_withtext_).md>) — Informs the searchable object to replace all matching text across all searchable documents.
- [shouldReplace(foundTextRange:document:withText:)](<shouldreplace(foundtextrange_document_withtext_).md>) — Determines whether the searchable object allows replacement of the text range you provide.
