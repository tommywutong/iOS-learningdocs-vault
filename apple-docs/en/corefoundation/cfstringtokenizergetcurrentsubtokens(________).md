---
title: 'CFStringTokenizerGetCurrentSubTokens(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringtokenizergetcurrentsubtokens(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringtokenizergetcurrentsubtokens(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringtokenizergetcurrentsubtokens%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:bf5317431ea919b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringTokenizerGetCurrentSubTokens(_:_:_:_:)

<sub>Function</sub>

Retrieves the subtokens or derived subtokens contained in the compound token.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringTokenizerGetCurrentSubTokens(_ tokenizer: CFStringTokenizer!, _ ranges: UnsafeMutablePointer<CFRange>!, _ maxRangeLength: CFIndex, _ derivedSubTokens: CFMutableArray!) -> CFIndex
```

## Parameters

- `tokenizer` — A CFStringTokenizer object.

- `ranges` — Upon return, an array of CFRanges containing the ranges of subtokens. The ranges are relative to the string specified to CFStringTokenizerCreate. This parameter can be `NULL`.

- `maxRangeLength` — The maximum number of ranges to return.

- `derivedSubTokens` — A CFMutableArray to which the derived subtokens are to be added. This parameter can be `NULL`.

## Return Value

The number of ranges returned.

## Discussion

If token type is `kCFStringTokenizerTokenNone`, the `ranges` array and `derivedSubTokens` array are untouched and the return value is `0`.

If token type is `kCFStringTokenizerTokenNormal`, the `ranges` array has one item filled in with the entire range of the token (if `maxRangeLength` \>= 1) and a string taken from the entire token range is added to the `derivedSubTokens` array and the return value is `1`.

If token type is `kCFStringTokenizerTokenHasSubTokensMask` or `kCFStringTokenizerTokenHasDerivedSubTokensMask`, the ranges array is filled in with as many items as there are subtokens (up to a limit of `maxRangeLength`).

The `derivedSubTokens` array will have sub tokens added even when the sub token is a substring of the token. If token type is `kCFStringTokenizerTokenHasSubTokensMask`, the ordinary non-derived subtokens are added to the `derivedSubTokens` array.

## See Also

### Getting Information About the Current Token

- [CFStringTokenizerCopyCurrentTokenAttribute](<cfstringtokenizercopycurrenttokenattribute(____).md>) — Returns a given attribute of the current token.
- [CFStringTokenizerGetCurrentTokenRange](<cfstringtokenizergetcurrenttokenrange(__).md>) — Returns the range of the current token.
