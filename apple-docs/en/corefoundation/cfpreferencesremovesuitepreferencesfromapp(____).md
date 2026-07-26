---
title: 'CFPreferencesRemoveSuitePreferencesFromApp(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpreferencesremovesuitepreferencesfromapp(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpreferencesremovesuitepreferencesfromapp(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpreferencesremovesuitepreferencesfromapp%28_%3A_%3A%29.json'
content_hash: 'sha256:8c672b6e531c43a5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPreferencesRemoveSuitePreferencesFromApp(_:_:)

<sub>Function</sub>

Removes suite preferences from an application’s search chain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPreferencesRemoveSuitePreferencesFromApp(_ applicationID: CFString, _ suiteID: CFString)
```

## Parameters

- `applicationID` — The ID of the application from which to remove suite preferences, typically [kCFPreferencesCurrentApplication](kcfpreferencescurrentapplication.md). Do not pass `NULL` or [kCFPreferencesAnyApplication](kcfpreferencesanyapplication.md). Takes the form of a Java package name, `com.foosoft`.

- `suiteID` — The ID of the application suite preferences to remove. Takes the form of a Java package name, `com.foosoft`.

## See Also

### Adding and Removing Suite Preferences

- [CFPreferencesAddSuitePreferencesToApp](<cfpreferencesaddsuitepreferencestoapp(____).md>) — Adds suite preferences to an application’s preference search chain.
