---
title: 'replaceAllOccurrencesOfQueryString:usingOptions:withText:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-53wjq/replacealloccurrencesofquerystring:usingoptions:withtext:'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/replacealloccurrencesofquerystring:usingoptions:withtext:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-53wjq/replacealloccurrencesofquerystring%3Ausingoptions%3Awithtext%3A.json'
content_hash: 'sha256:7ce354fe925e7310'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-53wjq.md)

# replaceAllOccurrencesOfQueryString:usingOptions:withText:

<sub>Instance Method</sub>

Informs the searchable object to replace all matching text across all searchable documents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) replaceAllOccurrencesOfQueryString:(NSString *) queryString usingOptions:(UITextSearchOptions *) options withText:(NSString *) replacementText;
```

## Parameters

- `queryString` — The string to search for and replace.

- `options` — The configurable options to use for matching words and comparing strings.

- `replacementText` — The string to replace the text with.

## Discussion

When [supportsTextReplacement](supportstextreplacement.md) returns `YES,` the system calls this method during a find session to request the replacement of all text matching the query string.

## See Also

### Handling replacements

- [supportsTextReplacement](supportstextreplacement.md) — A Boolean value that indicates whether the searchable object supports replacing text.
- [replaceFoundTextInRange:inDocument:withText:](replacefoundtextinrange_indocument_withtext_.md) — Informs the searchable object to replace the text range for the highlighted search result.
- [shouldReplaceFoundTextInRange:inDocument:withText:](shouldreplacefoundtextinrange_indocument_withtext_.md) — Determines whether the searchable object allows replacement of the text range you provide.
