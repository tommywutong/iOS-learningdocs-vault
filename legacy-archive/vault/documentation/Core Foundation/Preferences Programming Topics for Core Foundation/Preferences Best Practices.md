---
title: Preferences Programming Topics for Core Foundation
apple_id: 10000129i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPreferences/Concepts/BestPractices.html
archived_at: '2026-07-15T07:22:43.199607Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Preferences Programming Topics for Core Foundation](Introduction%20to%20Preferences%20Programming%20Topics%20for%20Core%20Foundation.md)


[Next](Application%20IDs.md)[Previous](Introduction%20to%20Preferences%20Programming%20Topics%20for%20Core%20Foundation.md)

# Preferences Best Practices

CFPreferences is Apple’s standard API for storing and retrieving preference keys and values, allowing the calling process to concentrate on native types and key-value pair meanings rather than the mechanisms of writing to files and so on. While it provides a convenient API, it is also easy to use incorrectly. This document gives an overview of when it is appropriate to use what API, and how to synchronize preferences across process boundaries.

The following general guiding principles apply to the CFPreferences API:

- You should typically use [CFPreferencesCopyAppValue](https://developer.apple.com/documentation/corefoundation/1515497-cfpreferencescopyappvalue) to read preference keys.
- You should use [CFPreferencesSetAppValue](https://developer.apple.com/documentation/corefoundation/1515528-cfpreferencessetappvalue) to write preference keys for “current user/any host.”
- If you need to write a by-host preference for the current user, use [CFPreferencesSetValue](https://developer.apple.com/documentation/corefoundation/1515525-cfpreferencessetvalue). Make sure this is absolutely necessary.

Note that, although they are treated separately in the documentation, high-level API and low-level API are not exclusive. It may be appropriate to use high-level API in some parts of an application, and low-level API in another. For example, you can set a preference key/value pair with `CFPreferencesSetValue(key, value, app, user, host)` and then read it with `CFPreferencesCopyAppValue(key, value, app)`— indeed you probably do want to read it with the latter function since it traverses the search path.

As much as possible, you should use [CFPreferencesCopyAppValue](https://developer.apple.com/documentation/corefoundation/1515497-cfpreferencescopyappvalue) to retrieve preference keys. This function traverses the search path looking for the matching key and returns the value from the most-specific domain.

Users of particular machines may also be subject to “management” through “Workgroup Manager” or the “Capabilities” option of the Accounts preference pane in System Preferences. Either of these mechanisms may force preference values on the user. These values are also picked up by the [CFPreferencesCopyAppValue](https://developer.apple.com/documentation/corefoundation/1515497-cfpreferencescopyappvalue) API—you should use this function to ensure your application properly responds to management of this kind.

If your application needs to distinguish between “the current host” and “any host” then you use the low level API. If for some reason you need to search for a key-value pair in a specific domain, you should use [CFPreferencesCopyValue](https://developer.apple.com/documentation/corefoundation/1515500-cfpreferencescopyvalue)—you should not use this function as a general retrieval mechanism.

The Rule of Thumb on CFPreferences synchronization:

1. Only synchronize when absolutely necessary
2. If you have to communicate across process boundaries, use notifications with appropriate granularity, keeping 1) in mind. Typically, this means setting a flag in client processes, and only if a changed key is required should you trigger a synchronize.

Many processes in OS X write a preference key-value pair for use in another process. While it would be convenient for preference key-value pairs to auto-update in other processes, guaranteeing auto-update in all circumstances would incur a performance penalty and also make it difficult to ensure related preferences are read and written consistently. Processes should always have the choice of when to elect to accept new information into their space. For preference values, [CFPreferencesSynchronize](https://developer.apple.com/documentation/corefoundation/1515504-cfpreferencessynchronize) and [CFPreferencesAppSynchronize](https://developer.apple.com/documentation/corefoundation/1515510-cfpreferencesappsynchronize) are the function calls that providing the information choke-point. You should typically not, however, call these functions before every read of a preference key.

Preferences files are stored in the system’s or user’s preferences directories. On OS X versions 10.0 to 10.4 these are in `/Library/Preferences` and in `/Library/Preferences` in the user’s home directory respectively. When debugging an application, it may sometimes be useful to inspect these files to determine that preferences have been saved correctly, however you should _never_ hardcode these paths into an application. If you do need to access the directory programmatically you should use the [NSSearchPathForDirectoriesInDomains](https://developer.apple.com/documentation/foundation/1414224-nssearchpathfordirectoriesindoma) API, although there should typically be no reason to do so.

Note that preferences you set up in the registration domain (see Defaults Domains in _[Preferences and Settings Programming Guide](../../Cocoa/Preferences%20and%20Settings%20Programming%20Guide/About%20Preferences%20and%20Settings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2ts2i)_) are _not_ stored in the preferences file. Put another way, the preferences file stores only values that are different from those in the registration domain, so you should not expect to see “default defaults” in the preferences file after you run your application.

OS X v10.2 introduced the concept of “managed preferences.” The function `CFPreferencesAppValueIsForced` determines whether or not a given key has been imposed on the user. For managed keys, you should disable any user interface that allows the user to modify the value for the key.

[Next](Application%20IDs.md)[Previous](Introduction%20to%20Preferences%20Programming%20Topics%20for%20Core%20Foundation.md)

