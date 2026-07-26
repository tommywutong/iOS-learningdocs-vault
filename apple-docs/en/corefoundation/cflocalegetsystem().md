---
title: CFLocaleGetSystem()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cflocalegetsystem()
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalegetsystem()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalegetsystem%28%29.json'
content_hash: 'sha256:8c4ec1d4771105de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleGetSystem()

<sub>Function</sub>

Returns the root, canonical locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFLocaleGetSystem() -> CFLocale!
```

## Return Value

The root, canonical locale. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

The root locale contains fixed backstop settings for all locale information.

## See Also

### Creating a Locale

- [CFLocaleCopyCurrent](<cflocalecopycurrent().md>) — Returns a copy of the logical locale for the current user.
- [CFLocaleCreate](<cflocalecreate(____).md>) — Creates a locale for the given arbitrary locale identifier.
- [CFLocaleCreateCopy](<cflocalecreatecopy(____).md>) — Returns a copy of a locale.
