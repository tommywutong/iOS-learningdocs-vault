---
title: 'CFPreferencesGetAppBooleanValue(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpreferencesgetappbooleanvalue(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpreferencesgetappbooleanvalue(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpreferencesgetappbooleanvalue%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:cb33fbe75b01826f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPreferencesGetAppBooleanValue(_:_:_:)

<sub>Function</sub>

Convenience function that directly obtains a Boolean preference value for the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPreferencesGetAppBooleanValue(_ key: CFString, _ applicationID: CFString, _ keyExistsAndHasValidFormat: UnsafeMutablePointer<DarwinBoolean>?) -> Bool
```

## Parameters

- `key` — The preference key whose value to obtain. The key must specify a preference whose value is of type `Boolean`.

- `applicationID` — The identifier of the application whose preferences are searched, typically [kCFPreferencesCurrentApplication](kcfpreferencescurrentapplication.md). Do not pass `NULL` or [kCFPreferencesAnyApplication](kcfpreferencesanyapplication.md). Takes the form of a Java package name, such as `com.foosoft`.

- `keyExistsAndHasValidFormat` — On return, `true` if the preference value for the specified key was located and found to be of type `Boolean`, otherwise `false`.

## Return Value

The preference data for the specified key and application, or if no value was located, `false`.

## See Also

### Getting Preference Values

- [CFPreferencesCopyAppValue](<cfpreferencescopyappvalue(____).md>) — Obtains a preference value for the specified key and application.
- [CFPreferencesCopyKeyList](<cfpreferencescopykeylist(______).md>) — Constructs and returns the list of all keys set in the specified domain.
- [CFPreferencesCopyMultiple](<cfpreferencescopymultiple(________).md>) — Returns a dictionary containing preference values for multiple keys.
- [CFPreferencesCopyValue](<cfpreferencescopyvalue(________).md>) — Returns a preference value for a given domain.
- [CFPreferencesGetAppIntegerValue](<cfpreferencesgetappintegervalue(______).md>) — Convenience function that directly obtains an integer preference value for the specified key.
