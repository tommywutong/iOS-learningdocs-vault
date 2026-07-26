---
title: 'CFPreferencesCopyMultiple(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpreferencescopymultiple(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpreferencescopymultiple(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpreferencescopymultiple%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:841e9c66bd5b9e33'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPreferencesCopyMultiple(_:_:_:_:)

<sub>Function</sub>

Returns a dictionary containing preference values for multiple keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPreferencesCopyMultiple(_ keysToFetch: CFArray?, _ applicationID: CFString, _ userName: CFString, _ hostName: CFString) -> CFDictionary
```

## Parameters

- `keysToFetch` — An array of preference keys the values of which to obtain.

- `applicationID` — The ID of the application whose preferences are searched. Takes the form of a Java package name, such as `com.foosoft`.

- `userName` — [kCFPreferencesCurrentUser](kcfpreferencescurrentuser.md) to search the current-user domain, otherwise [kCFPreferencesAnyUser](kcfpreferencesanyuser.md) to search the any-user domain.

- `hostName` — [kCFPreferencesCurrentHost](kcfpreferencescurrenthost.md) to search the current-host domain, otherwise [kCFPreferencesAnyHost](kcfpreferencesanyhost.md) to search the any-host domain.

## Return Value

A dictionary containing the preference values for the keys specified by `keysToFetch` for the specified domain. If no values were located, returns an empty dictionary. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Note that values returned from this function are immutable, even if you have recently set the value using a mutable object.

## See Also

### Getting Preference Values

- [CFPreferencesCopyAppValue](<cfpreferencescopyappvalue(____).md>) — Obtains a preference value for the specified key and application.
- [CFPreferencesCopyKeyList](<cfpreferencescopykeylist(______).md>) — Constructs and returns the list of all keys set in the specified domain.
- [CFPreferencesCopyValue](<cfpreferencescopyvalue(________).md>) — Returns a preference value for a given domain.
- [CFPreferencesGetAppBooleanValue](<cfpreferencesgetappbooleanvalue(______).md>) — Convenience function that directly obtains a Boolean preference value for the specified key.
- [CFPreferencesGetAppIntegerValue](<cfpreferencesgetappintegervalue(______).md>) — Convenience function that directly obtains an integer preference value for the specified key.
