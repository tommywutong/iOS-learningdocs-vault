---
title: hasSubTokensMask
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstringtokenizertokentype/hassubtokensmask
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype/hassubtokensmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringtokenizertokentype/hassubtokensmask.json'
content_hash: 'sha256:14742577636282e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFStringTokenizerTokenType](../cfstringtokenizertokentype.md)

# hasSubTokensMask

<sub>Type Property</sub>

Compound token which may contain subtokens but with no derived subtokens.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var hasSubTokensMask: CFStringTokenizerTokenType { get }
```

## Discussion

You can obtain subtokens by calling [CFStringTokenizerGetCurrentSubTokens](<../cfstringtokenizergetcurrentsubtokens(________).md>).

## See Also

### Constants

- [kCFStringTokenizerTokenNormal](normal.md) — Has a normal token.
- [kCFStringTokenizerTokenHasDerivedSubTokensMask](hasderivedsubtokensmask.md) — Compound token which may contain derived subtokens.
- [kCFStringTokenizerTokenHasHasNumbersMask](hashasnumbersmask.md) — Appears to contain a number.
- [kCFStringTokenizerTokenHasNonLettersMask](hasnonlettersmask.md) — Contains punctuation, symbols, and so on.
- [kCFStringTokenizerTokenIsCJWordMask](iscjwordmask.md) — Contains kana and/or ideographs.
