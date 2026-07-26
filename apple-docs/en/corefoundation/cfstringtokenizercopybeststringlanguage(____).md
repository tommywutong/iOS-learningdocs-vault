---
title: 'CFStringTokenizerCopyBestStringLanguage(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringtokenizercopybeststringlanguage(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringtokenizercopybeststringlanguage(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringtokenizercopybeststringlanguage%28_%3A_%3A%29.json'
content_hash: 'sha256:37905ed754755dc5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringTokenizerCopyBestStringLanguage(_:_:)

<sub>Function</sub>

Guesses a language of a given string and returns the guess as a BCP 47 string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringTokenizerCopyBestStringLanguage(_ string: CFString!, _ range: CFRange) -> CFString!
```

## Parameters

- `string` — The string to test to identify the language.

- `range` — The range of `string` to use for the test. If `NULL`, the first few hundred characters of the string are examined.

## Return Value

A language in BCP 47 form, or `NULL` if the language in `string` could not be identified. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The result is not guaranteed to be accurate. Typically, the function requires 200-400 characters to reliably guess the language of a string.

CFStringTokenizer recognizes the following languages:

ar (Arabic), bg (Bulgarian), cs (Czech), da (Danish), de (German), el (Greek), en (English), es (Spanish), fi (Finnish), fr (French), he (Hebrew), hr (Croatian), hu (Hungarian), is (Icelandic), it (Italian), ja (Japanese), ko (Korean), nb (Norwegian Bokmål), nl (Dutch), pl (Polish), pt (Portuguese), ro (Romanian), ru (Russian), sk (Slovak), sv (Swedish), th (Thai), tr (Turkish), uk (Ukrainian), zh-Hans (Simplified Chinese), zh-Hant (Traditional Chinese).
