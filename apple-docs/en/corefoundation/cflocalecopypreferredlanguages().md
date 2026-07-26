---
title: CFLocaleCopyPreferredLanguages()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cflocalecopypreferredlanguages()
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalecopypreferredlanguages()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalecopypreferredlanguages%28%29.json'
content_hash: 'sha256:67cd9de148eaac8f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleCopyPreferredLanguages()

<sub>Function</sub>

Returns the array of canonicalized language IDs that the user prefers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFLocaleCopyPreferredLanguages() -> CFArray!
```

## Return Value

The array of canonicalized `CFString` language IDs that the current user prefers. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).
