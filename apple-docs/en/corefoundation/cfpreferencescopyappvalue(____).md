---
title: 'CFPreferencesCopyAppValue(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpreferencescopyappvalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpreferencescopyappvalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpreferencescopyappvalue%28_%3A_%3A%29.json'
content_hash: 'sha256:4ce34124ff3aee58'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPreferencesCopyAppValue(_:_:)

<sub>Function</sub>

Obtains a preference value for the specified key and application.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPreferencesCopyAppValue(_ key: CFString, _ applicationID: CFString) -> CFPropertyList?
```

## Parameters

- `key` — The preference key whose value to obtain.

- `applicationID` — The identifier of the application whose preferences to search, typically [kCFPreferencesCurrentApplication](kcfpreferencescurrentapplication.md). Do not pass `NULL` or [kCFPreferencesAnyApplication](kcfpreferencesanyapplication.md). Takes the form of a Java package name, `com.foosoft`.

## Return Value

The preference data for the specified key and application. If no value was located, returns `NULL`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Note that values returned from this function are immutable, even if you have recently set the value using a mutable object.

## See Also

### Getting Preference Values

- [CFPreferencesCopyKeyList](<cfpreferencescopykeylist(______).md>) — Constructs and returns the list of all keys set in the specified domain.
- [CFPreferencesCopyMultiple](<cfpreferencescopymultiple(________).md>) — Returns a dictionary containing preference values for multiple keys.
- [CFPreferencesCopyValue](<cfpreferencescopyvalue(________).md>) — Returns a preference value for a given domain.
- [CFPreferencesGetAppBooleanValue](<cfpreferencesgetappbooleanvalue(______).md>) — Convenience function that directly obtains a Boolean preference value for the specified key.
- [CFPreferencesGetAppIntegerValue](<cfpreferencesgetappintegervalue(______).md>) — Convenience function that directly obtains an integer preference value for the specified key.
