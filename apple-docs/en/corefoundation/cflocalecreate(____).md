---
title: 'CFLocaleCreate(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cflocalecreate(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalecreate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalecreate%28_%3A_%3A%29.json'
content_hash: 'sha256:c475341729b8e71c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleCreate(_:_:)

<sub>Function</sub>

Creates a locale for the given arbitrary locale identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFLocaleCreate(_ allocator: CFAllocator!, _ localeIdentifier: CFLocaleIdentifier!) -> CFLocale!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `localeIdentifier` — A string representation of an arbitrary locale identifier.

## Return Value

A new locale that corresponds to the arbitrary locale identifier `localeIdentifier`. Returns `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Locale

- [CFLocaleCopyCurrent](<cflocalecopycurrent().md>) — Returns a copy of the logical locale for the current user.
- [CFLocaleCreateCopy](<cflocalecreatecopy(____).md>) — Returns a copy of a locale.
- [CFLocaleGetSystem](<cflocalegetsystem().md>) — Returns the root, canonical locale.
