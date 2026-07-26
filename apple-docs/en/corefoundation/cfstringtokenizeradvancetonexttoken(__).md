---
title: 'CFStringTokenizerAdvanceToNextToken(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringtokenizeradvancetonexttoken(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringtokenizeradvancetonexttoken(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringtokenizeradvancetonexttoken%28_%3A%29.json'
content_hash: 'sha256:9d3c54567f8d2f64'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringTokenizerAdvanceToNextToken(_:)

<sub>Function</sub>

Advances the tokenizer to the next token and sets that as the current token.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringTokenizerAdvanceToNextToken(_ tokenizer: CFStringTokenizer!) -> CFStringTokenizerTokenType
```

## Parameters

- `tokenizer` — A CFStringTokenizer object.

## Return Value

The type of the token if the tokenizer succeeded in finding a token and setting it as current token. Returns `kCFStringTokenizerTokenNone` if the tokenizer failed to find a token. For possible values, see [CFStringTokenizerTokenType](cfstringtokenizertokentype.md).

## Discussion

If there is no preceding call to [CFStringTokenizerGoToTokenAtIndex](<cfstringtokenizergototokenatindex(____).md>) or [CFStringTokenizerAdvanceToNextToken](<cfstringtokenizeradvancetonexttoken(__).md>), the function finds the first token in the range specified by the [CFStringTokenizerCreate](<cfstringtokenizercreate(__________).md>). If there is a preceding, successful, call to [CFStringTokenizerGoToTokenAtIndex](<cfstringtokenizergototokenatindex(____).md>) or [CFStringTokenizerAdvanceToNextToken](<cfstringtokenizeradvancetonexttoken(__).md>) and there is a current token, proceeds to the next token. If a token is found, it is set as the current token and the function returns `true`; otherwise the current token is invalidated and the function returns `false`.

You can obtain the range and attribute of the token calling [CFStringTokenizerGetCurrentTokenRange](<cfstringtokenizergetcurrenttokenrange(__).md>) and [CFStringTokenizerCopyCurrentTokenAttribute](<cfstringtokenizercopycurrenttokenattribute(____).md>). If the token is a compound (with type `kCFStringTokenizerTokenHasSubTokensMask` or `kCFStringTokenizerTokenHasDerivedSubTokensMask`), you can obtain its subtokens and (or) derived subtokens by calling [CFStringTokenizerGetCurrentSubTokens](<cfstringtokenizergetcurrentsubtokens(________).md>).

## See Also

### Changing the Location

- [CFStringTokenizerGoToTokenAtIndex](<cfstringtokenizergototokenatindex(____).md>) — Finds a token that includes the character at a given index, and set it as the current token.
