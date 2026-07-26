---
title: 'shouldReplaceFoundTextInRange:inDocument:withText:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-53wjq/shouldreplacefoundtextinrange:indocument:withtext:'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/shouldreplacefoundtextinrange:indocument:withtext:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-53wjq/shouldreplacefoundtextinrange%3Aindocument%3Awithtext%3A.json'
content_hash: 'sha256:0578fa8d3f72c4de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-53wjq.md)

# shouldReplaceFoundTextInRange:inDocument:withText:

<sub>Instance Method</sub>

Determines whether the searchable object allows replacement of the text range you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (BOOL) shouldReplaceFoundTextInRange:(UITextRange *) range inDocument:(UITextSearchDocumentIdentifier) document withText:(NSString *) replacementText;
```

## Parameters

- `range` — The range of characters in a text container to consider a replacement for.

- `document` — A string that uniquely identifies the document containing the text range.

- `replacementText` — The string to replace the text with.

## Return Value

Return `No` to prevent the replacement of a particular text range.

## Discussion

Returning `NO` from this method disables the “replace” button in the find panel. If you don’t implement this method, the system assumes all results are replacable.

## See Also

### Handling replacements

- [supportsTextReplacement](supportstextreplacement.md) — A Boolean value that indicates whether the searchable object supports replacing text.
- [replaceFoundTextInRange:inDocument:withText:](replacefoundtextinrange_indocument_withtext_.md) — Informs the searchable object to replace the text range for the highlighted search result.
- [replaceAllOccurrencesOfQueryString:usingOptions:withText:](replacealloccurrencesofquerystring_usingoptions_withtext_.md) — Informs the searchable object to replace all matching text across all searchable documents.
