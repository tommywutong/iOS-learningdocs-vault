---
title: 'CFStringTokenizerGetCurrentTokenRange(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringtokenizergetcurrenttokenrange(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringtokenizergetcurrenttokenrange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringtokenizergetcurrenttokenrange%28_%3A%29.json'
content_hash: 'sha256:72b1ad67bbf1033d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringTokenizerGetCurrentTokenRange(_:)

<sub>Function</sub>

Returns the range of the current token.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringTokenizerGetCurrentTokenRange(_ tokenizer: CFStringTokenizer!) -> CFRange
```

## Parameters

- `tokenizer` — A CFStringTokenizer object.

## Return Value

The range of the current token, or `{``kCFNotFound`, `0}` if there is no current token.

## See Also

### Getting Information About the Current Token

- [CFStringTokenizerCopyCurrentTokenAttribute](<cfstringtokenizercopycurrenttokenattribute(____).md>) — Returns a given attribute of the current token.
- [CFStringTokenizerGetCurrentSubTokens](<cfstringtokenizergetcurrentsubtokens(________).md>) — Retrieves the subtokens or derived subtokens contained in the compound token.
