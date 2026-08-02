---
title: Preference Pane Programming Guide
apple_id: 10000110i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PreferencePanes/Tasks/Preferences.html
archived_at: '2026-07-18T02:12:32.522906Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Preference Pane Programming Guide](Introduction.md)


[Next](Communicating%20With%20the%20Target%20Application.md)[Previous](Wrapping%20Long%20Labels.md)

# Using Preference Services

Core Foundation Preference Services provides functions for reading and writing preferences to and from any available preference domain (see [Preference Services](Managing%20User%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydgljrgazdiojz)). Preference data are stored in property lists as a series of key-value pairs. The key is a string identifying the preference. The value is the preference setting, which can be any of the following data types: CFData, CFString, CFArray, CFDictionary, CFDate, CFBoolean, and CFNumber. When the value is a CFArray or CFDictionary, each of its elements must be one of the allowed data types. Except for CFBoolean (which has no equivalent object), each of the Core Foundation types are interchangeable with their Cocoa equivalents (NSData, NSString, and so forth).

Reading and writing preferences look like this:

```c
#include <CoreFoundation/CFPreferences.h>

CFStringRef appID, userName, hostName; // Assigned elsewhere
CFStringRef key = CFSTR(“PrefKey”);
CFPropertyListRef value; // Any allowed data type

value = CFPreferencesCopyValue(key, appID, userName, hostName);
CFPreferencesSetValue(key, value, appID, userName, hostName);
```

If a key does not exist in the given domain, the `CFPreferencesCopyValue` function returns `NULL`. Conversely, passing `NULL` to `CFPreferencesSetValue` for the key’s value removes the key from that domain. For performance reasons, changes made to a domain are cached. To force changes to be flushed to disk, call `CFPreferencesSynchronize` for the particular domain. This can be an expensive operation since it requires accessing the disk, so do not synchronize too often.

Several convenience functions automatically search through the domains of a particular application for a requested key and associated value. The search proceeds from the most specific domain—current user, the particular application, current host—at the top of [Table 1](Managing%20User%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4ydgljrga2tcobu) to the most general domain—any user, any application, any host—at the bottom of the table, until a matching key is found. When writing a value, it is stored in the application’s default domain: current user, the particular application, any host. Use of these routines looks like this:

```
value = CFPreferencesCopyAppValue(key, appID);
CFPreferencesSetAppValue(key, value, appID);
```

If a suite of applications share certain preferences, they can be stored together in their own set of domains defined by a suite ID, similar to the application ID. The suite domains can be added to the search path of the `CFPreferencesCopyAppValue` function with the `CFPreferencesAddSuitePreferencesToApp` function. Multiple suites of domains can be added. After searching each application-specific domain, Preference Services searches the corresponding suite-specific domains before searching the general domain. Preferences are still stored in the application’s default domain when using these functions, though.

For user-specific and application-specific preferences, these functions should suffice. For system-level preferences, you need to use the more general functions.

[Next](Communicating%20With%20the%20Target%20Application.md)[Previous](Wrapping%20Long%20Labels.md)

