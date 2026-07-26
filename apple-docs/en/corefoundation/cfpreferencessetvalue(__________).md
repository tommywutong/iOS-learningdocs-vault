---
title: 'CFPreferencesSetValue(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpreferencessetvalue(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpreferencessetvalue(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpreferencessetvalue%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:07f5569da8965b99'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPreferencesSetValue(_:_:_:_:_:)

<sub>Function</sub>

Adds, modifies, or removes a preference value for the specified domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPreferencesSetValue(_ key: CFString, _ value: CFPropertyList?, _ applicationID: CFString, _ userName: CFString, _ hostName: CFString)
```

## Parameters

- `key` — Preferences key for the value you wish to set.

- `value` — The value to set for `key` and application. Pass `NULL` to remove `key` from the domain.

- `applicationID` — The ID of the application whose preferences you wish to modify. Takes the form of a Java package name, `com.foosoft`.

- `userName` — [kCFPreferencesCurrentUser](kcfpreferencescurrentuser.md) to modify the current user’s preferences, otherwise [kCFPreferencesAnyUser](kcfpreferencesanyuser.md) to modify the preferences of all users.

- `hostName` — [kCFPreferencesCurrentHost](kcfpreferencescurrenthost.md) to modify the preferences of the current host, otherwise [kCFPreferencesAnyHost](kcfpreferencesanyhost.md) to modify the preferences of all hosts.

## Discussion

This function is the primitive set mechanism for the higher level preference function [CFPreferencesSetAppValue](<cfpreferencessetappvalue(______).md>). Only the exact domain specified is modified. Do not use this function directly unless you have a specific need. All arguments except `value` must be non-`NULL`. Do not use arbitrary user and host names, instead pass the pre-defined constants.

You must call the [CFPreferencesSynchronize](<cfpreferencessynchronize(______).md>) function in order for your changes to be saved to permanent storage. Note that you can only save preferences for “Any User” if you have root privileges (or Admin privileges prior to OS X v10.6).

## See Also

### Setting Preference Values

- [CFPreferencesSetAppValue](<cfpreferencessetappvalue(______).md>) — Adds, modifies, or removes a preference.
- [CFPreferencesSetMultiple](<cfpreferencessetmultiple(__________).md>) — Convenience function that allows you to set and remove multiple preference values.
