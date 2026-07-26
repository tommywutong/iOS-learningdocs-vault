---
title: 'CFPreferencesAppSynchronize(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpreferencesappsynchronize(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpreferencesappsynchronize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpreferencesappsynchronize%28_%3A%29.json'
content_hash: 'sha256:16ada58adae2bd10'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPreferencesAppSynchronize(_:)

<sub>Function</sub>

Writes to permanent storage all pending changes to the preference data for the application, and reads the latest preference data from permanent storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPreferencesAppSynchronize(_ applicationID: CFString) -> Bool
```

## Parameters

- `applicationID` — The ID of the application whose preferences to write to storage, typically [kCFPreferencesCurrentApplication](kcfpreferencescurrentapplication.md). Do not pass `NULL` or [kCFPreferencesAnyApplication](kcfpreferencesanyapplication.md). Takes the form of a Java package name, `com.foosoft`.

## Return Value

`true` if synchronization was successful, otherwise `false`.

## Discussion

Calling the function [CFPreferencesSetAppValue](<cfpreferencessetappvalue(______).md>) is not in itself sufficient for storing preferences. The [CFPreferencesAppSynchronize](<cfpreferencesappsynchronize(__).md>) function writes to permanent storage all pending preference changes for the application. Typically you would call this function after multiple calls to [CFPreferencesSetAppValue](<cfpreferencessetappvalue(______).md>). Conversely, preference data is cached after it is first read. Changes made externally are not automatically incorporated. The [CFPreferencesAppSynchronize](<cfpreferencesappsynchronize(__).md>) function reads the latest preferences from permanent storage.

## See Also

### Synchronizing Preferences

- [CFPreferencesSynchronize](<cfpreferencessynchronize(______).md>) — For the specified domain, writes all pending changes to preference data to permanent storage, and reads latest preference data from permanent storage.
