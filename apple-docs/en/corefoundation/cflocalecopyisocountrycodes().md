---
title: CFLocaleCopyISOCountryCodes()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cflocalecopyisocountrycodes()
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalecopyisocountrycodes()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalecopyisocountrycodes%28%29.json'
content_hash: 'sha256:a02367bac2469c20'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleCopyISOCountryCodes()

<sub>Function</sub>

Returns an array of CFString objects that represents all known legal ISO country codes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFLocaleCopyISOCountryCodes() -> CFArray!
```

## Return Value

An array of CFString objects that represents all known legal ISO country codes. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Note: many of these will not have any supporting locale data in macOS.

## See Also

### Getting ISO Information

- [CFLocaleCopyISOLanguageCodes](<cflocalecopyisolanguagecodes().md>) — Returns an array of CFString objects that represents all known legal ISO language codes.
- [CFLocaleCopyISOCurrencyCodes](<cflocalecopyisocurrencycodes().md>) — Returns an array of CFString objects that represents all known legal ISO currency codes.
- [CFLocaleCopyCommonISOCurrencyCodes](<cflocalecopycommonisocurrencycodes().md>) — Returns an array of strings that represents ISO currency codes for currencies in common use.
