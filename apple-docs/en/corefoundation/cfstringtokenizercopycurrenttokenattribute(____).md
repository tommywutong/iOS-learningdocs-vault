---
title: 'CFStringTokenizerCopyCurrentTokenAttribute(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringtokenizercopycurrenttokenattribute(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringtokenizercopycurrenttokenattribute(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringtokenizercopycurrenttokenattribute%28_%3A_%3A%29.json'
content_hash: 'sha256:4898693d1af5d2d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringTokenizerCopyCurrentTokenAttribute(_:_:)

<sub>Function</sub>

Returns a given attribute of the current token.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringTokenizerCopyCurrentTokenAttribute(_ tokenizer: CFStringTokenizer!, _ attribute: CFOptionFlags) -> CFTypeRef!
```

## Parameters

- `tokenizer` — A CFStringTokenizer object.

- `attribute` — The token attribute to obtain. The value must be `kCFStringTokenizerAttributeLatinTranscription`, or `kCFStringTokenizerAttributeLanguage`.

## Return Value

The attribute specified by `attribute` of the current token, or `NULL` if the current token does not have the specified attribute or there is no current token. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Getting Information About the Current Token

- [CFStringTokenizerGetCurrentTokenRange](<cfstringtokenizergetcurrenttokenrange(__).md>) — Returns the range of the current token.
- [CFStringTokenizerGetCurrentSubTokens](<cfstringtokenizergetcurrentsubtokens(________).md>) — Retrieves the subtokens or derived subtokens contained in the compound token.
