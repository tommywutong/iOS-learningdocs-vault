---
title: 'CFPreferencesAddSuitePreferencesToApp(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpreferencesaddsuitepreferencestoapp(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpreferencesaddsuitepreferencestoapp(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpreferencesaddsuitepreferencestoapp%28_%3A_%3A%29.json'
content_hash: 'sha256:c6267524a0a6ce6c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPreferencesAddSuitePreferencesToApp(_:_:)

<sub>Function</sub>

Adds suite preferences to an application’s preference search chain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPreferencesAddSuitePreferencesToApp(_ applicationID: CFString, _ suiteID: CFString)
```

## Parameters

- `applicationID` — The ID of the application to which to add suite preferences, typically [kCFPreferencesCurrentApplication](kcfpreferencescurrentapplication.md). Do not pass `NULL` or [kCFPreferencesAnyApplication](kcfpreferencesanyapplication.md). Takes the form of a Java package name, `com.foosoft`.

- `suiteID` — The ID of the application suite preferences to add. Takes the form of a Java package name, `com.foosoft`.

## Discussion

Suite preferences allow you to maintain a set of preferences that are common to all applications in the suite. When a suite is added to an application’s search chain, all of the domains pertaining to that suite are inserted into the chain. Suite preferences are added between the “Current Application” domains and the “Any Application” domains. If you add multiple suite preferences to one application, the order of the suites in the search chain is non-deterministic. You can override a suite preference for a given application by defining the same preference key in the application specific preferences.

## See Also

### Adding and Removing Suite Preferences

- [CFPreferencesRemoveSuitePreferencesFromApp](<cfpreferencesremovesuitepreferencesfromapp(____).md>) — Removes suite preferences from an application’s search chain.
