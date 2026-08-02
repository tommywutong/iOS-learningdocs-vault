---
title: Code Loading Programming Topics
apple_id: 10000052i
resource_type: Guide
platform: macOS
topic: General
technology: Foundation
published: '2013-12-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LoadingCode/Tasks/NameConflicts.html
archived_at: '2026-07-15T07:16:31.406262Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Loading Programming Topics](Introduction%20to%20Dynamically%20Loading%20Code.md)


[Next](Loading%20Objective-C%20Libraries%20From%20Java.md)[Previous](Creating%20Plug-in%20Architectures.md)

# Preventing Name Conflicts

Because the Objective-C runtime uses a flat name space, you must be careful when developing a plug-in not to choose a name that conflicts with the application code or another plug-in loaded by the application. This section describes how to name your classes and other symbols to avoid this kind of conflict.

The Objective-C runtime provides only a single flat, global name space per process for all exported symbols. This includes all global variables, nonstatic functions, class names, and categories declared for individual classes; protocols have a separate global name space of their own.

Because plug-ins from different vendors must coexist in the same process, you must follow conventions to avoid symbol name collisions. Every exported symbol in a plug-in must be prefixed with an identifier unique to the plug-in. This requirement is not circumvented by unloading each plug-in before loading the next one. Once an Objective-C symbol (class names, protocols and categories) gets loaded, it cannot be unloaded.

Your plug-in should derive its unique prefix from its bundle identifier using the following algorithm:

1. Start with the bundle identifier (`com.apple.preference.sound`)
2. Capitalize the first letter of each period-separated component (`Com.Apple.Preference.Sound`)
3. Remove the periods (`ComApplePreferenceSound`)

Note that this convention depends on the uniqueness of each bundle identifier. To guarantee uniqueness of the bundle identifier, each organization should prefix its identifiers with its reverse-ordered ICANN domain name (for example, `com.apple`).

Each organization should institute its own processes and conventions to avoid bundle identifier collisions among bundles developed within the organization.

To avoid having to use the full, prefixed symbol names in source code, you can create shorthand preprocessor macros. These macros can be defined in a single header file that is imported into every source file. For example:

```
#define SoundPref ComApplePreferenceSoundPref
#define AlertController ComApplePreferenceSoundAlertController
#define MicrophoneController ComApplePreferenceSoundMicrophoneController
```

These shortcuts are only valid in Objective-C source files that include the header file. References to class names outside of such source files (for example, in the bundle property list and in the main nib file) must specify the full, real name.

Plug-ins should avoid using Objective-C categories to override methods of classes in public frameworks. If multiple plug-ins attempt to override the same method of the same class, only one override takes effect, leading to unpredictable behavior.

[Next](Loading%20Objective-C%20Libraries%20From%20Java.md)[Previous](Creating%20Plug-in%20Architectures.md)

