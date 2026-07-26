---
title: 'CFLocaleCopyDisplayNameForPropertyValue(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cflocalecopydisplaynameforpropertyvalue(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalecopydisplaynameforpropertyvalue(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalecopydisplaynameforpropertyvalue%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:aa7e6e7a61bcf121'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleCopyDisplayNameForPropertyValue(_:_:_:)

<sub>Function</sub>

Returns the display name for the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFLocaleCopyDisplayNameForPropertyValue(_ displayLocale: CFLocale!, _ key: CFLocaleKey!, _ value: CFString!) -> CFString!
```

## Parameters

- `displayLocale` — A locale object.

- `key` — A string that identifies the type that `value` is. It must be one of the standard locale property keys (see [Locale Property Keys](locale-property-keys.md)).

- `value` — The value for which the display name is required.

## Return Value

The display name for `value`. Returns `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Note that not all locale property keys have values with display name values.

## See Also

### Getting Information About a Locale

- [CFLocaleGetValue](<cflocalegetvalue(____).md>) — Returns the corresponding value for the given key of a locale’s key-value pair.
- [CFLocaleGetIdentifier](<cflocalegetidentifier(__).md>) — Returns the given locale’s identifier.
