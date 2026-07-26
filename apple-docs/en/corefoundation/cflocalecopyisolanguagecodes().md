---
title: CFLocaleCopyISOLanguageCodes()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cflocalecopyisolanguagecodes()
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalecopyisolanguagecodes()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalecopyisolanguagecodes%28%29.json'
content_hash: 'sha256:2b854b6aef263cc2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleCopyISOLanguageCodes()

<sub>Function</sub>

Returns an array of CFString objects that represents all known legal ISO language codes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFLocaleCopyISOLanguageCodes() -> CFArray!
```

## Return Value

An array of CFString objects that represents all known legal ISO language codes. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Note: many of these will not have any supporting locale data in macOS.

## See Also

### Getting ISO Information

- [CFLocaleCopyISOCountryCodes](<cflocalecopyisocountrycodes().md>) — Returns an array of CFString objects that represents all known legal ISO country codes.
- [CFLocaleCopyISOCurrencyCodes](<cflocalecopyisocurrencycodes().md>) — Returns an array of CFString objects that represents all known legal ISO currency codes.
- [CFLocaleCopyCommonISOCurrencyCodes](<cflocalecopycommonisocurrencycodes().md>) — Returns an array of strings that represents ISO currency codes for currencies in common use.
