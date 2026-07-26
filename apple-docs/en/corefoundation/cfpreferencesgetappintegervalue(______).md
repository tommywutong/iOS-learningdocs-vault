---
title: 'CFPreferencesGetAppIntegerValue(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpreferencesgetappintegervalue(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpreferencesgetappintegervalue(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpreferencesgetappintegervalue%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:7cf6985d0939500d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPreferencesGetAppIntegerValue(_:_:_:)

<sub>Function</sub>

Convenience function that directly obtains an integer preference value for the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPreferencesGetAppIntegerValue(_ key: CFString, _ applicationID: CFString, _ keyExistsAndHasValidFormat: UnsafeMutablePointer<DarwinBoolean>?) -> CFIndex
```

## Parameters

- `key` — The preference key whose value you wish to obtain. The key must specify a preference whose value is of type `int`.

- `applicationID` — The identifier of the application whose preferences you wish to search, typically [kCFPreferencesCurrentApplication](kcfpreferencescurrentapplication.md). Do not pass `NULL` or [kCFPreferencesAnyApplication](kcfpreferencesanyapplication.md). Takes the form of a Java package name, `com.foosoft`.

- `keyExistsAndHasValidFormat` — On return, indicates whether the preference value for the specified key was located and found to be of type `int`.

## Return Value

The preference data for the specified key and application. If no value was located, `0` is returned.

## See Also

### Getting Preference Values

- [CFPreferencesCopyAppValue](<cfpreferencescopyappvalue(____).md>) — Obtains a preference value for the specified key and application.
- [CFPreferencesCopyKeyList](<cfpreferencescopykeylist(______).md>) — Constructs and returns the list of all keys set in the specified domain.
- [CFPreferencesCopyMultiple](<cfpreferencescopymultiple(________).md>) — Returns a dictionary containing preference values for multiple keys.
- [CFPreferencesCopyValue](<cfpreferencescopyvalue(________).md>) — Returns a preference value for a given domain.
- [CFPreferencesGetAppBooleanValue](<cfpreferencesgetappbooleanvalue(______).md>) — Convenience function that directly obtains a Boolean preference value for the specified key.
