---
title: 'codeBlockIntentWithIdentity:languageHint:nestedInsideIntent:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspresentationintent/codeblockintentwithidentity:languagehint:nestedinsideintent:'
source_url: 'https://developer.apple.com/documentation/foundation/nspresentationintent/codeblockintentwithidentity:languagehint:nestedinsideintent:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspresentationintent/codeblockintentwithidentity%3Alanguagehint%3Anestedinsideintent%3A.json'
content_hash: 'sha256:d055e5b69715ec4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPresentationIntent](../nspresentationintent.md)

# codeBlockIntentWithIdentity:languageHint:nestedInsideIntent:

<sub>Type Method</sub>

Creates an code-block intent with the provided information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSPresentationIntent *) codeBlockIntentWithIdentity:(NSInteger) identity languageHint:(NSString *) languageHint nestedInsideIntent:(NSPresentationIntent *) parent;
```

## Parameters

- `identity` — The unique identifier for the intent.

- `languageHint` — The programming language for the code listing.

- `parent` — The parent intent of the code block.

## Return Value

A new intent with the kind set to [NSPresentationIntentKindCodeBlock](../nspresentationintentkind/nspresentationintentkindcodeblock.md).

## See Also

### Creating a presentation intent

- [paragraphIntentWithIdentity:nestedInsideIntent:](paragraphintentwithidentity_nestedinsideintent_.md) — Creates a  paragraph intent with the provided information.
- [headerIntentWithIdentity:level:nestedInsideIntent:](headerintentwithidentity_level_nestedinsideintent_.md) — Creates a header intent with the provided information.
- [orderedListIntentWithIdentity:nestedInsideIntent:](orderedlistintentwithidentity_nestedinsideintent_.md) — Creates an ordered-list intent with the provided information.
- [unorderedListIntentWithIdentity:nestedInsideIntent:](unorderedlistintentwithidentity_nestedinsideintent_.md) — Creates an unordered-list intent with the provided information.
- [listItemIntentWithIdentity:ordinal:nestedInsideIntent:](listitemintentwithidentity_ordinal_nestedinsideintent_.md) — Creates an item for an ordered list with the provided information.
- [blockQuoteIntentWithIdentity:nestedInsideIntent:](blockquoteintentwithidentity_nestedinsideintent_.md) — Creates a block-quote intent with the provided information.
- [thematicBreakIntentWithIdentity:nestedInsideIntent:](thematicbreakintentwithidentity_nestedinsideintent_.md) — Creates a thematic break intent with the provided information.
- [tableIntentWithIdentity:columnCount:alignments:nestedInsideIntent:](tableintentwithidentity_columncount_alignments_nestedinsideintent_.md) — Creates a table intent with the provided information.
- [tableHeaderRowIntentWithIdentity:nestedInsideIntent:](tableheaderrowintentwithidentity_nestedinsideintent_.md) — Creates a table header intent with the provided information.
- [tableRowIntentWithIdentity:row:nestedInsideIntent:](tablerowintentwithidentity_row_nestedinsideintent_.md) — Creates a table row intent with the provided information.
- [tableCellIntentWithIdentity:column:nestedInsideIntent:](tablecellintentwithidentity_column_nestedinsideintent_.md) — Creates a table cell intent with the provided information.
