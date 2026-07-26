---
title: 'replaceFoundTextInRange:inDocument:withText:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-53wjq/replacefoundtextinrange:indocument:withtext:'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/replacefoundtextinrange:indocument:withtext:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-53wjq/replacefoundtextinrange%3Aindocument%3Awithtext%3A.json'
content_hash: 'sha256:442f077086cff3b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-53wjq.md)

# replaceFoundTextInRange:inDocument:withText:

<sub>Instance Method</sub>

Informs the searchable object to replace the text range for the highlighted search result.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) replaceFoundTextInRange:(UITextRange *) range inDocument:(UITextSearchDocumentIdentifier) document withText:(NSString *) replacementText;
```

## Parameters

- `range` — The text range to replace.

- `document` — A string that uniquely identifies a document when searching multiple documents, or `nil` when searching a single document.

- `replacementText` — The string to replace the text with.

## Discussion

When [supportsTextReplacement](supportstextreplacement.md) returns `YES,` the system calls this method during a find session to request a text range to replace.

## See Also

### Handling replacements

- [supportsTextReplacement](supportstextreplacement.md) — A Boolean value that indicates whether the searchable object supports replacing text.
- [replaceAllOccurrencesOfQueryString:usingOptions:withText:](replacealloccurrencesofquerystring_usingoptions_withtext_.md) — Informs the searchable object to replace all matching text across all searchable documents.
- [shouldReplaceFoundTextInRange:inDocument:withText:](shouldreplacefoundtextinrange_indocument_withtext_.md) — Determines whether the searchable object allows replacement of the text range you provide.
