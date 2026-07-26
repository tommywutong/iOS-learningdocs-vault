---
title: 'CFPreferencesSetMultiple(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpreferencessetmultiple(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpreferencessetmultiple(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpreferencessetmultiple%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:2b5051164b2730f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPreferencesSetMultiple(_:_:_:_:_:)

<sub>Function</sub>

Convenience function that allows you to set and remove multiple preference values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPreferencesSetMultiple(_ keysToSet: CFDictionary?, _ keysToRemove: CFArray?, _ applicationID: CFString, _ userName: CFString, _ hostName: CFString)
```

## Parameters

- `keysToSet` — A dictionary containing the key/value pairs for the preferences  to set.

- `keysToRemove` — An array containing a list of keys to remove.

- `applicationID` — The ID of the application whose preferences you wish to modify. Takes the form of a Java package name, `com.foosoft`.

- `userName` — [kCFPreferencesCurrentUser](kcfpreferencescurrentuser.md) to modify the current user’s preferences, otherwise [kCFPreferencesAnyUser](kcfpreferencesanyuser.md) to modify the preferences of all users.

- `hostName` — [kCFPreferencesCurrentHost](kcfpreferencescurrenthost.md) to modify the preferences of the current host, otherwise [kCFPreferencesAnyHost](kcfpreferencesanyhost.md) to modify the preferences of all hosts.

## Discussion

Behavior is undefined if a key is in both `keysToSet` and `keysToRemove`

## See Also

### Setting Preference Values

- [CFPreferencesSetAppValue](<cfpreferencessetappvalue(______).md>) — Adds, modifies, or removes a preference.
- [CFPreferencesSetValue](<cfpreferencessetvalue(__________).md>) — Adds, modifies, or removes a preference value for the specified domain.
