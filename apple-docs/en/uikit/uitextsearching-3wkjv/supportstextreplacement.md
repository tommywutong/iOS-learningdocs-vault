---
title: supportsTextReplacement
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearching-3wkjv/supportstextreplacement
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/supportstextreplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-3wkjv/supportstextreplacement.json'
content_hash: 'sha256:e86d7c39ae67e7c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-3wkjv.md)

# supportsTextReplacement

<sub>Instance Property</sub>

A Boolean value that indicates whether the searchable object supports replacing text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var supportsTextReplacement: Bool { get }
```

## Default Implementations

### UITextSearching Implementations

- [supportsTextReplacement](supportstextreplacement-68rh6.md)

## See Also

### Handling replacements

- [replace(foundTextRange:document:withText:)](<replace(foundtextrange_document_withtext_).md>) — Informs the searchable object to replace the text range for the highlighted search result.
- [replaceAll(queryString:options:withText:)](<replaceall(querystring_options_withtext_).md>) — Informs the searchable object to replace all matching text across all searchable documents.
- [shouldReplace(foundTextRange:document:withText:)](<shouldreplace(foundtextrange_document_withtext_).md>) — Determines whether the searchable object allows replacement of the text range you provide.
