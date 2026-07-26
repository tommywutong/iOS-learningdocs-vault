---
title: CFLocaleCopyAvailableLocaleIdentifiers()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cflocalecopyavailablelocaleidentifiers()
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalecopyavailablelocaleidentifiers()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalecopyavailablelocaleidentifiers%28%29.json'
content_hash: 'sha256:14e98e040a6b0d65'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleCopyAvailableLocaleIdentifiers()

<sub>Function</sub>

Returns an array of CFString objects that represents all locales for which locale data is available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFLocaleCopyAvailableLocaleIdentifiers() -> CFArray!
```

## Return Value

An array of CFString objects that represents all locales for which locale data is available. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).
