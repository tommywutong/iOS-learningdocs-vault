---
title: 'CFPreferencesSetAppValue(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpreferencessetappvalue(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpreferencessetappvalue(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpreferencessetappvalue%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:fdf459f03ed29e4b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPreferencesSetAppValue(_:_:_:)

<sub>Function</sub>

Adds, modifies, or removes a preference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPreferencesSetAppValue(_ key: CFString, _ value: CFPropertyList?, _ applicationID: CFString)
```

## Parameters

- `key` — The preference key whose value you wish to set.

- `value` — The value to set for the specified `key` and application. Pass `NULL` to remove the specified key from the application’s preferences.

- `applicationID` — The ID of the application whose preferences you wish to create or modify, typically [kCFPreferencesCurrentApplication](kcfpreferencescurrentapplication.md). Do not pass `NULL` or [kCFPreferencesAnyApplication](kcfpreferencesanyapplication.md). Takes the form of a Java package name, `com.foosoft`.

## Discussion

New preference values are stored in the standard application preference location, `~/Library/Preferences/`. When called with [kCFPreferencesCurrentApplication](kcfpreferencescurrentapplication.md), modifications are performed in the preference domain “Current User, Current Application, Any Host.” If you need to create preferences in some other domain, use the low-level function [CFPreferencesSetValue](<cfpreferencessetvalue(__________).md>).

You must call the [CFPreferencesAppSynchronize](<cfpreferencesappsynchronize(__).md>) function in order for your changes to be saved to permanent storage.

## See Also

### Setting Preference Values

- [CFPreferencesSetMultiple](<cfpreferencessetmultiple(__________).md>) — Convenience function that allows you to set and remove multiple preference values.
- [CFPreferencesSetValue](<cfpreferencessetvalue(__________).md>) — Adds, modifies, or removes a preference value for the specified domain.
