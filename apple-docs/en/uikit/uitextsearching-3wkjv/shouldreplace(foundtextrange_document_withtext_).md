---
title: 'shouldReplace(foundTextRange:document:withText:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-3wkjv/shouldreplace(foundtextrange:document:withtext:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/shouldreplace(foundtextrange:document:withtext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-3wkjv/shouldreplace%28foundtextrange%3Adocument%3Awithtext%3A%29.json'
content_hash: 'sha256:1f80689a01811596'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-3wkjv.md)

# shouldReplace(foundTextRange:document:withText:)

<sub>Instance Method</sub>

Determines whether the searchable object allows replacement of the text range you provide.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func shouldReplace(foundTextRange: UITextRange, document: Self.DocumentIdentifier?, withText: String) -> Bool
```

## Parameters

- `foundTextRange` — The range of characters in a text container to consider a replacement for.

- `document` — A string that uniquely identifies the document containing the text range.

- `withText` — The string to replace the text with.

## Return Value

Return `No` to prevent the replacement of a particular text range.

## Discussion

Returning `NO` from this method disables the “replace” button in the find panel. If you don’t implement this method, the system assumes all results are replacable.

## Default Implementations

### UITextSearching Implementations

- [shouldReplace(foundTextRange:document:withText:)](<shouldreplace(foundtextrange_document_withtext_)-58mw8.md>)

## See Also

### Handling replacements

- [supportsTextReplacement](supportstextreplacement.md) — A Boolean value that indicates whether the searchable object supports replacing text.
- [replace(foundTextRange:document:withText:)](<replace(foundtextrange_document_withtext_).md>) — Informs the searchable object to replace the text range for the highlighted search result.
- [replaceAll(queryString:options:withText:)](<replaceall(querystring_options_withtext_).md>) — Informs the searchable object to replace all matching text across all searchable documents.
