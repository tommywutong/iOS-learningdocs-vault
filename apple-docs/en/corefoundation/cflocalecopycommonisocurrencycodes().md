---
title: CFLocaleCopyCommonISOCurrencyCodes()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cflocalecopycommonisocurrencycodes()
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalecopycommonisocurrencycodes()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalecopycommonisocurrencycodes%28%29.json'
content_hash: 'sha256:bc8a5305f054ce67'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleCopyCommonISOCurrencyCodes()

<sub>Function</sub>

Returns an array of strings that represents ISO currency codes for currencies in common use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFLocaleCopyCommonISOCurrencyCodes() -> CFArray!
```

## Return Value

An array of CFString objects that represents ISO currency codes for currencies in common use. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Getting ISO Information

- [CFLocaleCopyISOCountryCodes](<cflocalecopyisocountrycodes().md>) — Returns an array of CFString objects that represents all known legal ISO country codes.
- [CFLocaleCopyISOLanguageCodes](<cflocalecopyisolanguagecodes().md>) — Returns an array of CFString objects that represents all known legal ISO language codes.
- [CFLocaleCopyISOCurrencyCodes](<cflocalecopyisocurrencycodes().md>) — Returns an array of CFString objects that represents all known legal ISO currency codes.
