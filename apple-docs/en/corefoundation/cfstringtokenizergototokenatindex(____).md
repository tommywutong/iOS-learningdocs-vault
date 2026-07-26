---
title: 'CFStringTokenizerGoToTokenAtIndex(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringtokenizergototokenatindex(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringtokenizergototokenatindex(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringtokenizergototokenatindex%28_%3A_%3A%29.json'
content_hash: 'sha256:b5057d69d5d0cf76'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringTokenizerGoToTokenAtIndex(_:_:)

<sub>Function</sub>

Finds a token that includes the character at a given index, and set it as the current token.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringTokenizerGoToTokenAtIndex(_ tokenizer: CFStringTokenizer!, _ index: CFIndex) -> CFStringTokenizerTokenType
```

## Parameters

- `tokenizer` — A CFStringTokenizer object.

- `index` — The index of a character in the string for `tokenizer`.

## Return Value

The type of the token if the tokenizer succeeded in finding a token and setting it as the current token. Returns `kCFStringTokenizerTokenNone` if the tokenizer failed to find a token. For possible values, see [CFStringTokenizerTokenType](cfstringtokenizertokentype.md).

## Discussion

You can obtain the range and attribute of the token calling [CFStringTokenizerGetCurrentTokenRange](<cfstringtokenizergetcurrenttokenrange(__).md>) and [CFStringTokenizerCopyCurrentTokenAttribute](<cfstringtokenizercopycurrenttokenattribute(____).md>). If the token is a compound (with type `kCFStringTokenizerTokenHasSubTokensMask` or `kCFStringTokenizerTokenHasDerivedSubTokensMask`), you can obtain its subtokens and (or) derived subtokens by calling [CFStringTokenizerGetCurrentSubTokens](<cfstringtokenizergetcurrentsubtokens(________).md>).

## See Also

### Changing the Location

- [CFStringTokenizerAdvanceToNextToken](<cfstringtokenizeradvancetonexttoken(__).md>) — Advances the tokenizer to the next token and sets that as the current token.
