---
title: 'CFPreferencesCopyValue(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpreferencescopyvalue(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpreferencescopyvalue(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpreferencescopyvalue%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:5f08b49a080335a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPreferencesCopyValue(_:_:_:_:)

<sub>Function</sub>

Returns a preference value for a given domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPreferencesCopyValue(_ key: CFString, _ applicationID: CFString, _ userName: CFString, _ hostName: CFString) -> CFPropertyList?
```

## Parameters

- `key` — Preferences key for the value to obtain.

- `applicationID` — The ID of the application whose preferences are searched. Takes the form of a Java package name, such as `com.foosoft`.

- `userName` — [kCFPreferencesCurrentUser](kcfpreferencescurrentuser.md) if to search the current-user domain, otherwise [kCFPreferencesAnyUser](kcfpreferencesanyuser.md) to search the any-user domain.

- `hostName` — [kCFPreferencesCurrentHost](kcfpreferencescurrenthost.md) if to search the current-host domain, otherwise [kCFPreferencesAnyHost](kcfpreferencesanyhost.md) to search the any-host domain.

## Return Value

The preference data for the specified domain. If the no value was located, returns `NULL`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function is the primitive get mechanism for the higher level preference function [CFPreferencesCopyAppValue](<cfpreferencescopyappvalue(____).md>) Unlike the high-level function, [CFPreferencesCopyValue](<cfpreferencescopyvalue(________).md>) searches only the exact domain specified. Do not use this function directly unless you have a need. All arguments must be non-`NULL`. Do not use arbitrary user and host names, instead pass the pre-defined domain qualifier constants.

Note that values returned from this function are immutable, even if you have recently set the value using a mutable object.

## See Also

### Getting Preference Values

- [CFPreferencesCopyAppValue](<cfpreferencescopyappvalue(____).md>) — Obtains a preference value for the specified key and application.
- [CFPreferencesCopyKeyList](<cfpreferencescopykeylist(______).md>) — Constructs and returns the list of all keys set in the specified domain.
- [CFPreferencesCopyMultiple](<cfpreferencescopymultiple(________).md>) — Returns a dictionary containing preference values for multiple keys.
- [CFPreferencesGetAppBooleanValue](<cfpreferencesgetappbooleanvalue(______).md>) — Convenience function that directly obtains a Boolean preference value for the specified key.
- [CFPreferencesGetAppIntegerValue](<cfpreferencesgetappintegervalue(______).md>) — Convenience function that directly obtains an integer preference value for the specified key.
