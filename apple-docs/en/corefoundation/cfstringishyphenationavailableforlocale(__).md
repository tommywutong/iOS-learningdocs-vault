---
title: 'CFStringIsHyphenationAvailableForLocale(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringishyphenationavailableforlocale(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringishyphenationavailableforlocale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringishyphenationavailableforlocale%28_%3A%29.json'
content_hash: 'sha256:26d36dbd76da72aa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringIsHyphenationAvailableForLocale(_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether hyphenation data is available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringIsHyphenationAvailableForLocale(_ locale: CFLocale!) -> Bool
```

## Parameters

- `locale` — A valid locale that specifies which language’s hyphenation conventions to use. Hyphenation data is not available for all locales.

## See Also

### Working With Hyphenation

- [CFStringGetHyphenationLocationBeforeIndex](<cfstringgethyphenationlocationbeforeindex(____________).md>) — Retrieve the first potential hyphenation location found before the specified location.
