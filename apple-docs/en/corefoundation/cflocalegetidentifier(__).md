---
title: 'CFLocaleGetIdentifier(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cflocalegetidentifier(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalegetidentifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalegetidentifier%28_%3A%29.json'
content_hash: 'sha256:cccbb4fa77550885'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleGetIdentifier(_:)

<sub>Function</sub>

Returns the given locale’s identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFLocaleGetIdentifier(_ locale: CFLocale!) -> CFLocaleIdentifier!
```

## Parameters

- `locale` — The locale object to examine.

## Return Value

A string representation of `locale`’s identifier. This may not be the same string that was used to create the locale—it may be canonicalized. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Getting Information About a Locale

- [CFLocaleCopyDisplayNameForPropertyValue](<cflocalecopydisplaynameforpropertyvalue(______).md>) — Returns the display name for the given value.
- [CFLocaleGetValue](<cflocalegetvalue(____).md>) — Returns the corresponding value for the given key of a locale’s key-value pair.
