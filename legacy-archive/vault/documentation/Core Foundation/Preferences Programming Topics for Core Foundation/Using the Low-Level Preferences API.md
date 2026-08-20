---
title: Preferences Programming Topics for Core Foundation
apple_id: 10000129i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPreferences/Tasks/UsingLowAPI.html
archived_at: '2026-07-15T07:22:45.055705Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Preferences Programming Topics for Core Foundation](Introduction%20to%20Preferences%20Programming%20Topics%20for%20Core%20Foundation.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20the%20High-Level%20Preferences%20API.md)

# Using the Low-Level Preferences API

There are some cases where using the high-level API is not appropriate. If you are building some sort of “helper tool” that runs on behalf of another application, or an application that stores preferences for other applications, you will need to use the low-level preferences API to write to the other application’s preferences. [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3talkcineukscgiraq) shows you how to do this.

__Listing 1__  Writing a value to another application’s preferences.

```
CFStringRef appID = CFSTR("com.apple.anotherapp");
CFStringRef defaultTextColorKey = CFSTR("defaultTextColor");
CFStringRef colorBLUE = CFSTR("BLUE");

// Set up the preference.
CFPreferencesSetValue(defaultTextColorKey,
                colorBLUE,
                appID,
                kCFPreferencesCurrentUser,
                kCFPreferencesAnyHost);

// Write out the preference data.
CFPreferencesSynchronize(appID,
                kCFPreferencesCurrentUser,
                kCFPreferencesAnyHost);
```

Note that this example writes to another application’s preferences. There’s no way to get the bundle ID directly from the other application, so it’s necessary to hardcode the application ID.

[Next](Document%20Revision%20History.md)[Previous](Using%20the%20High-Level%20Preferences%20API.md)

