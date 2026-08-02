---
title: Sync Services Programming Guide
apple_id: TP40001178
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/Articles/SyncingPreferences.html
archived_at: '2026-07-15T07:19:45.723225Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sync Services Programming Guide](Introduction%20to%20Sync%20Services%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Syncing%20Core%20Data%20Applications.md)

# Syncing Preferences

Users can sync application preferences to multiple computers over MobileMe. By syncing preferences, the user preserves their application settings when moving from computer to computer similar to the advantages of using a network home directory. The user enables this feature, in a way similar to selecting sync schemas, using the MobileMe Sync pane in System Preferences. The user must first configure MobileMe and enable syncing before enabling this feature. For many applications this is a convenient mechanism that requires no source code changes. However, if syncing preferences does not make sense for your application, you can turn this feature off for all or selected application preferences. This article describes several approaches to controlling what application preferences are synced.

Set the `com.apple.PreferenceSync.ExcludeAllSyncKeys` key to `true` to exclude all your application preferences from syncing. The default value is `false`—all application preferences are synced.

If you want to exclude just some preferences, set the `com.apple.PreferenceSync.ExcludeSyncKeys` key to an array of keys that you want to exclude from syncing. The keys are represented by string values and are not localized.

You can either use the application information property list, user defaults, or application preferences to set these keys. The defaults for the preference domain is first checked for these settings. If they are not found in the defaults, the application’s `info.plist` file is checked. Therefore, if you set these keys programmatically at runtime, you override any values set in the application’s `info.plist` file.

You can also use preference domains to exclude some keys from being synced. Use preference domains to specify that some application preferences are host-specific and should not be synced. This is recommended for preferences that are intended for a single computer only. Read [Preference Domains](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPreferences/Concepts/PreferenceDomains.html#//apple_ref/doc/uid/20001168) in _[Preferences Programming Topics for Core Foundation](../../Core%20Foundation/Preferences%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Preferences%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezds2i)_ for more information.

Set the `com.apple.PreferenceSync.ExcludeAllSyncKeys` key to `true` in the application’s `info.plist` file to exclude all application preferences from syncing as show in Listing 1.

__Listing 1__  Excluding all preferences using the information property list

```xml
<plist version="1.0">
<dict>
    ...
    <key>com.apple.PreferenceSync.ExcludeAllSyncKeys</key>
    <true/>
</dict>
</plist
```

Alternatively, exclude selected keys by setting the `com.apple.PreferenceSync.ExcludeSyncKeys` key to an array of keys in the application’s `info.plist` file as show in Listing 2.

__Listing 2__  Excluding selected preferences using the information property list

```xml
<plist version="1.0">
<dict>
    ...

    <key>com.apple.PreferenceSync.ExcludeSyncKeys</key>
    <array>
        <string>preferenceX</string>
        <string>preferenceY</string>
    </array>
</dict>
</plist
```

The advantage of setting these keys in the application’s `info.plist` file is that your application or an installer doesn’t need to run to set these keys.

In addition, you can set these keys programmatically using application preferences or user defaults.

The following code fragment uses the `CFPreferences` opaque type to set the `com.apple.PreferenceSync.ExcludeAllSyncKeys` key to `kCFBooleanTrue`:

```
CFPreferencesSetAppValue(CFSTR("com.apple.PreferenceSync.ExcludeAllSyncKeys"), kCFBooleanTrue, kCFPreferencesCurrentApplication);
```

Read _[Preferences Programming Topics for Core Foundation](../../Core%20Foundation/Preferences%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Preferences%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezds2i)_ to learn more about the `CFPreferences` opaque type.

The following Objective-C code fragment uses user defaults to exclude all application preferences from syncing by setting the `com.apple.PreferenceSync.ExcludeAllSyncKeys` key to `YES`:

```
[[NSUserDefaults standardUserDefaults] setObject:[NSNumber numberWithBool:YES] forKey:@"com.apple.PreferenceSync.ExcludeAllSyncKeys"];
```

Read _[Preferences and Settings Programming Guide](../Preferences%20and%20Settings%20Programming%20Guide/About%20Preferences%20and%20Settings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2ts2i)_ to learn more about the `NSUserDefaults` class.

You can also set user defaults from the command line. The following command sets the `com.apple.PreferenceSync.ExcludeSyncKeys` key to exclude the `preferenceX` and `preferenceY` preferences from syncing:

```
defaults write com.apple.myapp com.apple.PreferenceSync.ExcludeSyncKeys -array preferenceX preferenceY
```

The disadvantage of using preferences or user defaults is that your application or an installer needs to run to set these keys.

[Next](Document%20Revision%20History.md)[Previous](Syncing%20Core%20Data%20Applications.md)

