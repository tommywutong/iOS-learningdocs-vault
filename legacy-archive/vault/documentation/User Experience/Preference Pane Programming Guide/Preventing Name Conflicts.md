---
title: Preference Pane Programming Guide
apple_id: 10000110i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PreferencePanes/Tasks/Conflicts.html
archived_at: '2026-07-18T02:12:29.962762Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Preference Pane Programming Guide](Introduction.md)


[Next](Wrapping%20Long%20Labels.md)[Previous](Updating%20Preference%20Panes.md)

# Preventing Name Conflicts

The Objective-C runtime provides only a single flat, global name space per process for all exported symbols. This includes all global variables, nonstatic functions, class names, and categories declared for individual classes; protocols have a separate global name space of their own.

Because preference pane plug-ins from different vendors must coexist in the same process, you must follow conventions to avoid symbol name collisions. Every exported symbol in a preference pane plug-in must be prefixed with an identifier unique to the plug-in. This requirement is not circumvented by unloading each plug-in before loading the next one. Once an Objective-C symbol (class names, protocols and categories) gets loaded, it cannot be unloaded.

Your preference pane plug-in should derive its unique prefix from its bundle identifier using the following algorithm:

1. Start with the bundle identifier (`com.mycompany.preference.sound`)
2. Capitalize the first letter of each period-separated component (`Com.Mycompany.Preference.Sound`)
3. Remove the periods (`ComMycompanyPreferenceSound`)

Note that this convention depends on the uniqueness of each bundle identifier. To guarantee uniqueness of the bundle identifier, each organization should prefix its identifiers with its reverse-ordered ICANN domain name (for example, “`com.mycompany`”).

Each organization should institute its own processes and conventions to avoid bundle identifier collisions among bundles developed within the organization.

To avoid having to use the full, prefixed symbol names in source code, you can create shorthand preprocessor macros. These macros can be defined in a single header file that is imported into every source file. For example:

```
#define SoundPref ComMycompanyPreferenceSoundPref
#define AlertController ComMycompanyPreferenceSoundAlertController
#define MicrophoneController ComMycompanyPreferenceSoundMicrophoneController
```

Obviously, these shortcuts are only valid in Objective-C source files that include the header file. References to class names outside of such source files (for example, in the bundle property list and in the main nib file) must specify the full, real name.

Preference pane plug-ins should avoid using Objective-C categories to override methods of classes in public frameworks. If multiple panels attempt to override the same method of the same class, only one override takes effect, leading to unpredictable behavior.

[Next](Wrapping%20Long%20Labels.md)[Previous](Updating%20Preference%20Panes.md)

