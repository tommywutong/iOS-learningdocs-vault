---
title: 'CFPreferencesCopyKeyList(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpreferencescopykeylist(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpreferencescopykeylist(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpreferencescopykeylist%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:94475c8d648fc84a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPreferencesCopyKeyList(_:_:_:)

<sub>Function</sub>

Constructs and returns the list of all keys set in the specified domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPreferencesCopyKeyList(_ applicationID: CFString, _ userName: CFString, _ hostName: CFString) -> CFArray?
```

## Parameters

- `applicationID` — The ID of the application whose preferences to search. Takes the form of a Java package name, `com.foosoft`.

- `userName` — [kCFPreferencesCurrentUser](kcfpreferencescurrentuser.md) to search the current-user domain, otherwise [kCFPreferencesAnyUser](kcfpreferencesanyuser.md) to search the any-user domain.

- `hostName` — [kCFPreferencesCurrentHost](kcfpreferencescurrenthost.md) to search the current-host domain, otherwise [kCFPreferencesAnyHost](kcfpreferencesanyhost.md) to search the any-host domain.

## Return Value

The list of keys. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Getting Preference Values

- [CFPreferencesCopyAppValue](<cfpreferencescopyappvalue(____).md>) — Obtains a preference value for the specified key and application.
- [CFPreferencesCopyMultiple](<cfpreferencescopymultiple(________).md>) — Returns a dictionary containing preference values for multiple keys.
- [CFPreferencesCopyValue](<cfpreferencescopyvalue(________).md>) — Returns a preference value for a given domain.
- [CFPreferencesGetAppBooleanValue](<cfpreferencesgetappbooleanvalue(______).md>) — Convenience function that directly obtains a Boolean preference value for the specified key.
- [CFPreferencesGetAppIntegerValue](<cfpreferencesgetappintegervalue(______).md>) — Convenience function that directly obtains an integer preference value for the specified key.
