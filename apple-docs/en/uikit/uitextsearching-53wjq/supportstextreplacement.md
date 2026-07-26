---
title: supportsTextReplacement
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearching-53wjq/supportstextreplacement
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/supportstextreplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-53wjq/supportstextreplacement.json'
content_hash: 'sha256:612e161d19979842'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-53wjq.md)

# supportsTextReplacement

<sub>Instance Property</sub>

A Boolean value that indicates whether the searchable object supports replacing text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) BOOL supportsTextReplacement;
```

## See Also

### Handling replacements

- [replaceFoundTextInRange:inDocument:withText:](replacefoundtextinrange_indocument_withtext_.md) — Informs the searchable object to replace the text range for the highlighted search result.
- [replaceAllOccurrencesOfQueryString:usingOptions:withText:](replacealloccurrencesofquerystring_usingoptions_withtext_.md) — Informs the searchable object to replace all matching text across all searchable documents.
- [shouldReplaceFoundTextInRange:inDocument:withText:](shouldreplacefoundtextinrange_indocument_withtext_.md) — Determines whether the searchable object allows replacement of the text range you provide.
