---
title: Carbon Framework Release Notes
apple_id: TP40010634
resource_type: Release Note
platform: macOS
topic: null
technology: Carbon
published: '2011-04-11'
source_url: https://developer.apple.com/library/archive/releasenotes/Carbon/RN-CarbonFramework/index.html
archived_at: '2026-07-18T02:50:21.769750Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Carbon Framework Release Notes

This document describes new features and issues with the Carbon framework in OS X v10.7.

#### Contents:

- [Transparent Application Lifecycle](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmmzufvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Scroll Bars](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmmzufvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ni)
- [Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmmzufvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nq)

### Transparent Application Lifecycle

### Persistent State

All Carbon applications support Persistent State restoration across logout/shutdown and login automatically or when the user selects "Quit and Keep Windows" menu item from the application menu. When this menu item is chosen, the OS records a list of all open disk-based documents to re-open at next launch. In addition to the standard state like window size, position and toolbar visibility, your application can preserve custom state such as current selection. See `SetWindowProperty` and `ChangeWindowPropertyAttributes`, the attribute `kWindowPropertyPersistent`, and `kEventWindowRestoredAfterRelaunch`.

### Sudden Termination

When Sudden termination is enabled (either using the `NSSupportsSuddenTermination` key in the application’s Info.plist file or the [NSProcessInfo](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProcessInfo/Description.html#//apple_ref/occ/cl/NSProcessInfo) method [enableSuddenTermination](https://developer.apple.com/documentation/foundation/processinfo/1409836-enablesuddentermination)), the app can be terminated immediately, without sending the `kAEQuitApplication` AppleEvent. Sudden termination is automatically disabled when a window’s close box shows the modified state indicator (via the `SetWindowModified` API).

### Automatic Termination

An application may adopt the automatic termination capability by adding the `NSSupportsAutomaticTermination` key to its Info.plist. The application’s File menu automatically gains a "Close All" menu item which uses the new `kHICommandCloseAll` and dispatches a `kEventWindowCloseAll` event. Your application should implement `kEventWindowCloseAll` to prevent multiple sheets for unsaved changes and allow the user to review unsaved changes in each document singly. With no visible documents and when deactivated, such applications may be converted to UIElements, disappear from the Dock or application switcher, and be terminated to recover memory. If termination should not occur (due to background task), the application may use [NSProcessInfo](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProcessInfo/Description.html#//apple_ref/occ/cl/NSProcessInfo) methods `disableAutomaticTermination` and `enableAutomaticTermination`.

### Scroll Bars

Carbon now uses the new overlay scrollbar appearance for the standard scrollbar control and for scrollbars drawn with the HITheme API. Carbon does not support the automatic scrollbar hiding behavior provided by AppKit; for Carbon applications, the scrollbars will always remain visible.

### Known Issues

There are a few issues with Carbon in the current seed. There is no need to file bugs on these specific problems:

- Window close/minimize/zoom buttons are positioned too low in the window title bar.
- Resizing a window from any edge or corner is only available for compositing windows.
