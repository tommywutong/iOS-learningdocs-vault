---
title: Preferences Utilities
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/preferences-utilities
source_url: 'https://developer.apple.com/documentation/corefoundation/preferences-utilities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/preferences-utilities.json'
content_hash: 'sha256:18db9e9d43a7f967'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# Preferences Utilities

<sub>API Collection</sub>

## Overview

Several functions return a preference value as a Core Foundation property list object.

You can use the function [CFGetTypeID](<cfgettypeid(__).md>) to determine the value’s type. For more information about property lists, see [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i).

### Overview

Core Foundation provides a simple, standard way to manage user (and application) preferences. Core Foundation stores preferences as key-value pairs that are assigned a scope using a combination of user name, application ID, and host (computer) names. This makes it possible to save and retrieve preferences that apply to different classes of users. Core Foundation preferences is useful to all applications that support user preferences. Note that modification of some preferences domains (those not belonging to the “Current User”) requires root privileges (or Admin privileges prior to OS X v10.6)—see [Authorization Services Programming Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/authorization_concepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000995) for information on how to gain suitable privileges.

Unlike some other Core Foundation types, CFPreferences is not toll-free bridged to its corresponding Cocoa Foundation framework class (`NSUserDefaults`). CFPreferences is thread-safe.

## Topics

### Getting Preference Values

- [CFPreferencesCopyAppValue](<cfpreferencescopyappvalue(____).md>) — Obtains a preference value for the specified key and application.
- [CFPreferencesCopyKeyList](<cfpreferencescopykeylist(______).md>) — Constructs and returns the list of all keys set in the specified domain.
- [CFPreferencesCopyMultiple](<cfpreferencescopymultiple(________).md>) — Returns a dictionary containing preference values for multiple keys.
- [CFPreferencesCopyValue](<cfpreferencescopyvalue(________).md>) — Returns a preference value for a given domain.
- [CFPreferencesGetAppBooleanValue](<cfpreferencesgetappbooleanvalue(______).md>) — Convenience function that directly obtains a Boolean preference value for the specified key.
- [CFPreferencesGetAppIntegerValue](<cfpreferencesgetappintegervalue(______).md>) — Convenience function that directly obtains an integer preference value for the specified key.

### Setting Preference Values

- [CFPreferencesSetAppValue](<cfpreferencessetappvalue(______).md>) — Adds, modifies, or removes a preference.
- [CFPreferencesSetMultiple](<cfpreferencessetmultiple(__________).md>) — Convenience function that allows you to set and remove multiple preference values.
- [CFPreferencesSetValue](<cfpreferencessetvalue(__________).md>) — Adds, modifies, or removes a preference value for the specified domain.

### Synchronizing Preferences

- [CFPreferencesAppSynchronize](<cfpreferencesappsynchronize(__).md>) — Writes to permanent storage all pending changes to the preference data for the application, and reads the latest preference data from permanent storage.
- [CFPreferencesSynchronize](<cfpreferencessynchronize(______).md>) — For the specified domain, writes all pending changes to preference data to permanent storage, and reads latest preference data from permanent storage.

### Adding and Removing Suite Preferences

- [CFPreferencesAddSuitePreferencesToApp](<cfpreferencesaddsuitepreferencestoapp(____).md>) — Adds suite preferences to an application’s preference search chain.
- [CFPreferencesRemoveSuitePreferencesFromApp](<cfpreferencesremovesuitepreferencesfromapp(____).md>) — Removes suite preferences from an application’s search chain.

### Miscellaneous Functions

- [CFPreferencesAppValueIsForced](<cfpreferencesappvalueisforced(____).md>) — Determines whether or not a given key has been imposed on the user.
- [CFPreferencesCopyApplicationList](<cfpreferencescopyapplicationlist(____).md>) — Constructs and returns the list of all applications that have preferences in the scope of the specified user and host. _(deprecated)_

### Constants

- [Application, Host, and User Keys](application-host-and-user-keys.md) — Keys used to specify the common preference domains.

## See Also

### Related Documentation

- [Preferences Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPreferences/CFPreferences.html#//apple_ref/doc/uid/10000129i)

### Utilities

- [Base Utilities](base-utilities.md)
- [Byte-Order Utilities](byte-order-utilities.md)
- [Core Foundation URL Access Utilities](core-foundation-url-access-utilities.md)
- [Socket Name Server Utilities](socket-name-server-utilities.md)
- [Time Utilities](time-utilities.md)
