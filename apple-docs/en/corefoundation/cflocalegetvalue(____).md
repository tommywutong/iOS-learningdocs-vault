---
title: 'CFLocaleGetValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cflocalegetvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalegetvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalegetvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:663e785c9ed3e881'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleGetValue(_:_:)

<sub>Function</sub>

Returns the corresponding value for the given key of a locale’s key-value pair.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFLocaleGetValue(_ locale: CFLocale!, _ key: CFLocaleKey!) -> CFTypeRef!
```

## Parameters

- `locale` — The locale object to examine.

- `key` — The key for which to obtain the corresponding value. Possible values are described in [Locale Property Keys](locale-property-keys.md).

## Return Value

The value corresponding to the given key in locale. The value may be any type of CFType object. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

Locale objects use key-value pairs to store property values. Use this function to get the value of a specific property.

## See Also

### Getting Information About a Locale

- [CFLocaleCopyDisplayNameForPropertyValue](<cflocalecopydisplaynameforpropertyvalue(______).md>) — Returns the display name for the given value.
- [CFLocaleGetIdentifier](<cflocalegetidentifier(__).md>) — Returns the given locale’s identifier.
