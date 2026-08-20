---
title: Daemons and Services Programming Guide
apple_id: 10000172i
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLoginItems.html
archived_at: '2026-07-15T08:16:27.279377Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Daemons and Services Programming Guide](About%20Daemons%20and%20Services.md)


[Next](Creating%20XPC%20Services.md)[Previous](The%20Life%20Cycle%20of%20a%20Daemon.md)

# Adding Login Items

There are two ways to add a login item: using the Service Management framework, and using a shared file list

Login items installed using the Service Management framework are not visible in System Preferences and can only be removed by the application that installed them.

Login items installed using a shared file list are visible in System Preferences; users have direct control over them. If you use this API, your login item can be disabled by the user, so any other application that communicates with it it should have reasonable fallback behavior in case the login item is disabled.

Applications can contain a helper application as a full application bundle, stored inside the main application bundle in the `Contents/Library/LoginItems` directory. Set either the `LSUIElement` or `LSBackgroundOnly` key in the `Info.plist` file of the helper application’s bundle.

Use the `SMLoginItemSetEnabled` function (available in OS X v10.6.6 and later) to enable a helper application. It takes two arguments, a `CFStringRef` containing the bundle identifier of the helper application, and a `Boolean` specifying the desired state. Pass `true` to start the helper application immediately and indicate that it should be started every time the user logs in. Pass `false` to terminate the helper application and indicate that it should no longer be launched when the user logs in. This function returns `true` if the requested change has taken effect; otherwise, it returns `false`. This function can be used to manage any number of helper applications.

If multiple applications (for example, several applications from the same company) contain a helper application with the same bundle identifier, only the one with the greatest bundle version number is launched. Any of the applications that contain a copy of the helper application can enable and disable it.

This method is available in OS X v10.5 and later. For specific details, see the appropriate functions in _[Launch Services Reference](https://developer.apple.com/documentation/coreservices/launch_services)_.

In previous versions of OS X, it is possible to add login items by sending an Apple event, by using the CFPreferences API, and by manually editing a property list file. These approaches are deprecated.

If you need to maintain compatibility with versions of OS X prior to v10.5, the preferred approach is to use Apple events; for details, see _[LoginItemsAE](../../../samplecode/LoginItemsAE/LoginItemsAE.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzyha)_. Using the CFPreferences API is an acceptable alternative. You should not directly edit the property list file on any version of OS X.

[Next](Creating%20XPC%20Services.md)[Previous](The%20Life%20Cycle%20of%20a%20Daemon.md)

