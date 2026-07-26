---
title: 'CFPreferencesSynchronize(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpreferencessynchronize(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpreferencessynchronize(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpreferencessynchronize%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4f721be4e1354aa9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPreferencesSynchronize(_:_:_:)

<sub>Function</sub>

For the specified domain, writes all pending changes to preference data to permanent storage, and reads latest preference data from permanent storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPreferencesSynchronize(_ applicationID: CFString, _ userName: CFString, _ hostName: CFString) -> Bool
```

## Parameters

- `applicationID` — The ID of the application whose preferences you wish to modify. Takes the form of a Java package name, `com.foosoft`.

- `userName` — [kCFPreferencesCurrentUser](kcfpreferencescurrentuser.md) to modify the current user’s preferences, otherwise [kCFPreferencesAnyUser](kcfpreferencesanyuser.md) to modify the preferences of all users.

- `hostName` — [kCFPreferencesCurrentHost](kcfpreferencescurrenthost.md) to search the current-host domain, otherwise [kCFPreferencesAnyHost](kcfpreferencesanyhost.md) to search the any-host domain.

## Return Value

`true` if synchronization was successful, `false` if an error occurred.

## Discussion

This function is the primitive synchronize mechanism for the higher level preference function [CFPreferencesAppSynchronize](<cfpreferencesappsynchronize(__).md>); it writes updated preferences to permanent storage, and reads the latest preferences from permanent storage. Only the exact domain specified is modified. Note that to modify “Any User” preferences requires root privileges (or Admin privileges prior to OS X v10.7)—see [Authorization Services Programming Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/authorization_concepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000995).

Do not use this function directly unless you have a specific need. All arguments must be non- `NULL`. Do not use arbitrary user and host names, instead pass the pre-defined constants.

## See Also

### Synchronizing Preferences

- [CFPreferencesAppSynchronize](<cfpreferencesappsynchronize(__).md>) — Writes to permanent storage all pending changes to the preference data for the application, and reads the latest preference data from permanent storage.
