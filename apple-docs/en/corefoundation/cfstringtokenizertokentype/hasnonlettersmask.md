---
title: hasNonLettersMask
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstringtokenizertokentype/hasnonlettersmask
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype/hasnonlettersmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringtokenizertokentype/hasnonlettersmask.json'
content_hash: 'sha256:64909eb1a1bf9516'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFStringTokenizerTokenType](../cfstringtokenizertokentype.md)

# hasNonLettersMask

<sub>Type Property</sub>

Contains punctuation, symbols, and so on.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var hasNonLettersMask: CFStringTokenizerTokenType { get }
```

## Discussion

Given the way Unicode word break works, this means it is a standalone punctuation or symbol character, or a string of such.

## See Also

### Constants

- [kCFStringTokenizerTokenNormal](normal.md) — Has a normal token.
- [kCFStringTokenizerTokenHasSubTokensMask](hassubtokensmask.md) — Compound token which may contain subtokens but with no derived subtokens.
- [kCFStringTokenizerTokenHasDerivedSubTokensMask](hasderivedsubtokensmask.md) — Compound token which may contain derived subtokens.
- [kCFStringTokenizerTokenHasHasNumbersMask](hashasnumbersmask.md) — Appears to contain a number.
- [kCFStringTokenizerTokenIsCJWordMask](iscjwordmask.md) — Contains kana and/or ideographs.
