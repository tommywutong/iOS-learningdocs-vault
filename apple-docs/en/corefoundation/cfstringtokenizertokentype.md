---
title: CFStringTokenizerTokenType
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstringtokenizertokentype
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringtokenizertokentype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringtokenizertokentype.json'
content_hash: 'sha256:b60483e5c6b0ceb5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringTokenizerTokenType

<sub>Structure</sub>

Token types returned by [CFStringTokenizerGoToTokenAtIndex](<cfstringtokenizergototokenatindex(____).md>) and [CFStringTokenizerAdvanceToNextToken](<cfstringtokenizeradvancetonexttoken(__).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFStringTokenizerTokenType
```

## Overview

See [http://www.unicode.org/reports/tr29/#Word_Boundaries](http://www.unicode.org/reports/tr29/#Word_Boundaries) for a detailed description of word boundaries.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCFStringTokenizerTokenNormal](cfstringtokenizertokentype/normal.md) — Has a normal token.
- [kCFStringTokenizerTokenHasSubTokensMask](cfstringtokenizertokentype/hassubtokensmask.md) — Compound token which may contain subtokens but with no derived subtokens.
- [kCFStringTokenizerTokenHasDerivedSubTokensMask](cfstringtokenizertokentype/hasderivedsubtokensmask.md) — Compound token which may contain derived subtokens.
- [kCFStringTokenizerTokenHasHasNumbersMask](cfstringtokenizertokentype/hashasnumbersmask.md) — Appears to contain a number.
- [kCFStringTokenizerTokenHasNonLettersMask](cfstringtokenizertokentype/hasnonlettersmask.md) — Contains punctuation, symbols, and so on.
- [kCFStringTokenizerTokenIsCJWordMask](cfstringtokenizertokentype/iscjwordmask.md) — Contains kana and/or ideographs.

### Initializers

- [init(rawValue:)](<cfstringtokenizertokentype/init(rawvalue_).md>)

## See Also

### Constants

- [Tokenization Modifiers](1588024-tokenization-modifiers.md) — Tokenization options are used with [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>) to specify how the string should be tokenized
