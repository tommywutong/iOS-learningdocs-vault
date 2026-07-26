---
title: 'CFPreferencesAppValueIsForced(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpreferencesappvalueisforced(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpreferencesappvalueisforced(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpreferencesappvalueisforced%28_%3A_%3A%29.json'
content_hash: 'sha256:58a731df7c448f17'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPreferencesAppValueIsForced(_:_:)

<sub>Function</sub>

Determines whether or not a given key has been imposed on the user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPreferencesAppValueIsForced(_ key: CFString, _ applicationID: CFString) -> Bool
```

## Parameters

- `key` — The key you are querying.

- `applicationID` — The application’s ID, typically [kCFPreferencesCurrentApplication](kcfpreferencescurrentapplication.md). Do not pass `NULL` or [kCFPreferencesAnyApplication](kcfpreferencesanyapplication.md). Takes the form of a Java package name, `com.foosoft`.

## Return Value

`true` if value of the key cannot be changed by the user, otherwise `false`.

## Discussion

In cases where machines and/or users are under some kind of management, you should use this function to determine whether or not to disable UI elements corresponding to those preference keys.

## See Also

### Miscellaneous Functions

- [CFPreferencesCopyApplicationList](<cfpreferencescopyapplicationlist(____).md>) — Constructs and returns the list of all applications that have preferences in the scope of the specified user and host. _(deprecated)_
