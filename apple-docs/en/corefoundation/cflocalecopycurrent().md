---
title: CFLocaleCopyCurrent()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cflocalecopycurrent()
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalecopycurrent()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalecopycurrent%28%29.json'
content_hash: 'sha256:f0c8c7d04f588bdb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleCopyCurrent()

<sub>Function</sub>

Returns a copy of the logical locale for the current user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFLocaleCopyCurrent() -> CFLocale!
```

## Return Value

The logical locale for the current user that is formed from the settings for the current user’s chosen system locale overlaid with any custom settings the user has specified in System Preferences. May return a retained cached object, not a new object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Settings you get from this locale do not change as a user’s preferences are changed so that your operations are consistent. Typically you perform some operations on the returned object and then release it. Since the returned object may be cached, you do not need to hold on to it indefinitely.

Note that locale settings are independent of the user’s language setting. The language of the current locale may not correspond to the language at the first index in the `AppleLanguages` array from user defaults. For more details, see Locale Concepts in Locales Programming Guide; see also [CFLocaleCopyPreferredLanguages](<cflocalecopypreferredlanguages().md>).

## See Also

### Creating a Locale

- [CFLocaleCreate](<cflocalecreate(____).md>) — Creates a locale for the given arbitrary locale identifier.
- [CFLocaleCreateCopy](<cflocalecreatecopy(____).md>) — Returns a copy of a locale.
- [CFLocaleGetSystem](<cflocalegetsystem().md>) — Returns the root, canonical locale.
