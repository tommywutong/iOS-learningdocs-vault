---
title: 'headerIntentWithIdentity:level:nestedInsideIntent:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nspresentationintent/headerintentwithidentity:level:nestedinsideintent:'
source_url: 'https://developer.apple.com/documentation/foundation/nspresentationintent/headerintentwithidentity:level:nestedinsideintent:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspresentationintent/headerintentwithidentity%3Alevel%3Anestedinsideintent%3A.json'
content_hash: 'sha256:9ccb8df6a6137ca2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSPresentationIntent](../nspresentationintent.md)

# headerIntentWithIdentity:level:nestedInsideIntent:

<sub>Type Method</sub>

Creates a header intent with the provided information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSPresentationIntent *) headerIntentWithIdentity:(NSInteger) identity level:(NSInteger) level nestedInsideIntent:(NSPresentationIntent *) parent;
```

## Parameters

- `identity` — The unique identifier for the intent.

- `level` — The level for the header section. Specify `1` or greater for this parameter. Don’t specify `0`.

- `parent` — The parent intent of the header.

## Return Value

A new intent with the kind set to [NSPresentationIntentKindHeader](../nspresentationintentkind/nspresentationintentkindheader.md).

## See Also

### Creating a presentation intent

- [paragraphIntentWithIdentity:nestedInsideIntent:](paragraphintentwithidentity_nestedinsideintent_.md) — Creates a  paragraph intent with the provided information.
- [orderedListIntentWithIdentity:nestedInsideIntent:](orderedlistintentwithidentity_nestedinsideintent_.md) — Creates an ordered-list intent with the provided information.
- [unorderedListIntentWithIdentity:nestedInsideIntent:](unorderedlistintentwithidentity_nestedinsideintent_.md) — Creates an unordered-list intent with the provided information.
- [listItemIntentWithIdentity:ordinal:nestedInsideIntent:](listitemintentwithidentity_ordinal_nestedinsideintent_.md) — Creates an item for an ordered list with the provided information.
- [codeBlockIntentWithIdentity:languageHint:nestedInsideIntent:](codeblockintentwithidentity_languagehint_nestedinsideintent_.md) — Creates an code-block intent with the provided information.
- [blockQuoteIntentWithIdentity:nestedInsideIntent:](blockquoteintentwithidentity_nestedinsideintent_.md) — Creates a block-quote intent with the provided information.
- [thematicBreakIntentWithIdentity:nestedInsideIntent:](thematicbreakintentwithidentity_nestedinsideintent_.md) — Creates a thematic break intent with the provided information.
- [tableIntentWithIdentity:columnCount:alignments:nestedInsideIntent:](tableintentwithidentity_columncount_alignments_nestedinsideintent_.md) — Creates a table intent with the provided information.
- [tableHeaderRowIntentWithIdentity:nestedInsideIntent:](tableheaderrowintentwithidentity_nestedinsideintent_.md) — Creates a table header intent with the provided information.
- [tableRowIntentWithIdentity:row:nestedInsideIntent:](tablerowintentwithidentity_row_nestedinsideintent_.md) — Creates a table row intent with the provided information.
- [tableCellIntentWithIdentity:column:nestedInsideIntent:](tablecellintentwithidentity_column_nestedinsideintent_.md) — Creates a table cell intent with the provided information.
