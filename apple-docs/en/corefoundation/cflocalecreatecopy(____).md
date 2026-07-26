---
title: 'CFLocaleCreateCopy(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cflocalecreatecopy(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalecreatecopy(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalecreatecopy%28_%3A_%3A%29.json'
content_hash: 'sha256:d17a3ab32e43cd3a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleCreateCopy(_:_:)

<sub>Function</sub>

Returns a copy of a locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFLocaleCreateCopy(_ allocator: CFAllocator!, _ locale: CFLocale!) -> CFLocale!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `locale` — The locale object to copy.

## Return Value

A new locale that is a copy of `locale`. Returns `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Locale

- [CFLocaleCopyCurrent](<cflocalecopycurrent().md>) — Returns a copy of the logical locale for the current user.
- [CFLocaleCreate](<cflocalecreate(____).md>) — Creates a locale for the given arbitrary locale identifier.
- [CFLocaleGetSystem](<cflocalegetsystem().md>) — Returns the root, canonical locale.
