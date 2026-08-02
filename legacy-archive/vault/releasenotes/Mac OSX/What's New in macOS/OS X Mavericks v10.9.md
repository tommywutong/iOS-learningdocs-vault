---
title: What's New in macOS
apple_id: TP40001812
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/WhatsNewInOSX/Articles/MacOSX10_9.html
archived_at: '2026-07-18T02:58:53.949499Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [What's New in macOS](Introduction.md)


[Next](OS%20X%20Mountain%20Lion%20v10.8.md)[Previous](OS%20X%20Yosemite%20v10.10.md)

# OS X Mavericks v10.9

This article summarizes the key technology changes and improvements available in OS X v10.9. The information about these changes is organized into sections by technology area.

- [Major Features](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztembxfvjvomq) describes important features that impact developers.
- [Framework-Level Features](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztembxfvjvomy) describes changes to system frameworks.
- [App Features](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztembxfvjvomzq) describes changes in built-in apps.
- [Xcode Tools Enhancements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztembxfvjvomrz) describes changes in Xcode.
- [BSD and Kernel Features](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztembxfvjvona) describes changes to the UNIX/POSIX portions of OS X.

For a detailed list of API changes, see _[OS X v10.9 API Diffs](https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/index.html#//apple_ref/doc/uid/TP40013007)_.

Please file any bug reports about this release or this documentation at [http://bugreport.apple.com/](http://bugreport.apple.com/).

The following sections highlight OS X v10.9 features that span multiple technology areas or that are otherwise of particular importance to most developers.

__App Nap__ reduces power consumption by completely suspending your app’s execution when it meets certain criteria. This ensures that your app does not periodically wake up to do unnecessary work. An app is considered to be a candidate for sleep if:

- It is not visible—if all of an app’s windows are either hidden by other windows or minimized in a hidden dock, and the app is not in the foreground
- It is not audible
- It has not explicitly disabled automatic termination
- It has not taken any power management assertions

When all of these conditions are met, OS X may put the app to sleep. While asleep, the app is placed on a scheduling queue that rarely gets actual time on the CPU.

The app wakes up automatically when the user brings the app to the foreground or when the app receives a Mach message or Apple event.

To support activities that should not be suspended, the [NSProcessInfo](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSProcessInfo/Description.html#//apple_ref/occ/cl/NSProcessInfo) class has three new methods—`beginActivityWithOptions:reason:`, `endActivity:`, and `performActivityWithOptions:reason:block:`—to tell OS X that your app is actively doing something important. These methods do two things:

- Allow your app to temporarily suspend idle sleep, display sleep, sudden termination, and automatic termination for the duration of a particular operation
- Allow your app to temporarily increase the scheduler timer precision while your app is performing latency-critical operations

For more information, see _[Foundation Release Notes for macOS 10.13 and iOS 11](../../Foundation/Foundation%20Release%20Notes%20for%20macOS%2010.13%20and%20iOS%2011.md)_.

In the Finder, the user can now add arbitrary tags to files and folders, providing additional groupings independent of the hierarchical folder structure. The user can later search for items by their tags and can assign highlight colors to files based on their tags.

As an app developer, your app can query, add, and remove tags associated with a particular URL by getting or setting the `NSURLTagNamesKey` property on the URL. In addition, your app can specify whether a save panel should show the tag names field, and can set an initial default set of tags on the [NSSavePanel](https://developer.apple.com/documentation/appkit/nssavepanel) object, which the user can then modify.

For more information, see _[Foundation Release Notes for macOS 10.13 and iOS 11](../../Foundation/Foundation%20Release%20Notes%20for%20macOS%2010.13%20and%20iOS%2011.md)_.

The following sections highlight changes to frameworks and technologies in OS X v10.9.

The following frameworks have been added in OS X v10.9:

- __AV Kit__ (`AVKit.framework`). AV Kit is a modern API for incorporating media playback capabilities into apps. AV Kit provides view-level services for media playback, complete with user controls, chapter navigation, and support for subtitles and closed captioning. Built on the most modern OS X media technology, AV Kit is an ideal starting point for developers looking to transition their QuickTime-based applications to AV Foundation.

  For more information, read _[AVKit Framework Reference](https://developer.apple.com/documentation/avkit)_.
- __Sprite Kit__ (`SpriteKit.framework`). Sprite Kit is a powerful graphics framework for developing 2D games such as side-scrolling shooters, puzzle games, and platform games.

  When you use Sprite Kit, you set various sprite attributes such as position, size, rotation, gravity, and mass. Built-in support for actions and physics makes animations look real, and particle systems let you create essential game effects such as fire, explosions, and smoke. Sprite Kit’s OpenGL-based renderer then efficiently animates 2D scenes based on the parameters you specify.

  To assist you in developing games based on Sprite Kit, Xcode provides support for texture atlas creation and includes a particle editor.

  For more information, read _[SpriteKit Programming Guide](../../../documentation/Graphics%20Animation/SpriteKit%20Programming%20Guide/About%20SpriteKit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbt)_.
- __Map Kit__ (`MapKit.framework`). Map Kit provides an interface for embedding maps directly into your App Store app’s windows and views. It also provides support for annotating a map, adding overlays, and performing reverse-geocoding lookups to determine placemark information for a given set of map coordinates.

  For more information, read _[Map Kit Framework Reference](https://developer.apple.com/documentation/mapkit)_.
- __Game Controller__ (`GameController.framework`). Game Controller provides a high-level Objective-C API for accepting input from Made-for-iPhone/iPod/iPad (MFi) game controllers in games. The MFi game controller specification provides a standard way for accessory developers to build controllers with analog d-pads, buttons, triggers, and thumb sticks. Game controllers declare support for a standard or extended profile that indicates which controls they provide. Games can support either profile or both, and you can tailor their behavior according to which controls are available.

  For more information, read _[Game Controller Programming Guide](../../../documentation/Game%20Controller%20Programming%20Guide/About%20Game%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztenzw)_.
- __Media Accessibility__ (`MediaAccessibility.framework`). Media Accessibility provides support for getting and setting global user preferences that control the behavior and appearance of captions and subtitles when playing movies.
- __Media Library__ (`MediaLibrary.framework`). Media Library provides support for accessing media provided by iLife apps, Aperture, Final Cut Pro, Logic, and the user’s Movies folder from within sandboxed apps.

  For more information, read _[Media Library Framework Reference](https://developer.apple.com/documentation/medialibrary)_.
- __iTunes Library__ (`iTunesLibrary.framework` in `/Library/Frameworks`). iTunes Library provides support for accessing media provided by iTunes from within sandboxed apps. This framework is considered to be a public API as of iTunes 11. For more information, see _[iTunes Library Framework Reference](https://developer.apple.com/documentation/ituneslibrary)_.

From time to time, Apple adds deprecation macros to APIs to indicate that those APIs should no longer be used in active development. When a deprecation occurs, it is not an immediate end of life to the specified API. Instead, it is the beginning of a grace period for transitioning off that API and onto newer and more modern replacements. Deprecated APIs typically remain present and usable in the system for some reasonable amount of time past the release in which they were deprecated. However, active development on them ceases, and the APIs receive only minor changes to accommodate security patches or to fix other critical bugs. Deprecated APIs may be removed entirely from a future version of the operating system.

As a developer, it is important that you avoid using deprecated APIs in your code as soon as possible. At a minimum, new code you write should never use deprecated APIs. And if you have existing code that uses deprecated APIs, you should update that code as soon as possible. Fortunately, the compiler generates warnings whenever it spots the use of a deprecated API in your code. You can use those warnings to track down and remove all references to those APIs.

The following frameworks are deprecated in OS X v10.9:

- Instant Message framework
- QuickTime framework
- QTKit framework (except for `QTMovieModernizer`)

The Instant Message framework is superseded by the Social framework. Because the Messages application no longer provides functionality that the Instant Message framework requires, in OS X v10.9 and later this framework always returns an empty buddy list.

The QuickTime and QTKit frameworks are superseded by AV Kit and AV Foundation. You can learn more about transitioning to AV Kit and AV Foundation by reading _[Transitioning QTKit Code to AV Foundation](https://developer.apple.com/library/archive/technotes/tn2300/_index.html#//apple_ref/doc/uid/DTS40012852)_.

The newly added `QTMovieModernizer` class in QTKit provides support for converting media encoded using older codecs into modern formats that are forward-compatible with AV Foundation.

The following frameworks are no longer part of the OS X SDK as of version 10.9:

- `Message`—Use Apple events to ask the Mail application to send mail instead.
- `ServerNotification`—Use push notifications instead.

The following sections highlight changes and enhancements in the AppKit framework. For detailed information about changes in the AppKit programming interfaces, see _[AppKit Release Notes for macOS 10.13](../../App%20Kit/AppKit%20Release%20Notes%20for%20macOS%2010.13.md)_.

In OS X v10.9, multiple monitor support is enhanced to allow you to pin a full-screen app on a screen while continuing to use other apps on a second display. To support this feature, AppKit has added two new `NSWindow` delegate methods: `customWindowsToEnterFullScreenForWindow:onScreen:` and `window:startCustomAnimationToEnterFullScreenOnScreen:withDuration:`.

__Responsive scrolling__ is an AppKit enhancement that makes scrolling smoother. This involves two significant changes to the way your app draws content:

- Scroll views ask their child views to draw extra content outside their normal view area so that the content can be immediately made available for scrolling purposes. This additional window backing is stored in purgeable memory to minimize additional paging.
- The scrolling thread attempts to redraw the view at 60 frames per second, but it backs off if the app is unable to keep up.
- Scrolling events are processed on a background thread.

Most apps automatically receive this responsive scrolling behavior. However, some views must explicitly opt in, including layer-backed views, custom scroll view or clip view subclasses that override `drawRect:`, `NSSurface`-based document views, transparent document views, and document views that override the `lockFocus` method.

For views in which responsive scrolling is automatically enabled, the behavior change should be entirely transparent to you as a developer. However, if your app exhibits any unusual behavior while scrolling, please file bugs.

For more details, see _[AppKit Release Notes for macOS 10.13](../../App%20Kit/AppKit%20Release%20Notes%20for%20macOS%2010.13.md)_.

`NSStackView` is a new Auto Layout–based view that creates and manages the constraints needed to create horizontal or vertical stacks of views. It dynamically adds and removes its constraints when views are removed or added to its stack. With customization, it can also react and influence the layout around it—implicitly growing and shrinking when views get removed or added, dropping views from its stack when its size becomes too small, and so on.

`NSMediaLibraryBrowserController` is a new controller class that can provide browsing of and drag-and-drop from the media libraries provided by the Media Library framework.

Core Image now takes advantage of OpenCL on the GPU to perform image processing operations on recent Macs. It also adds additional standard filters (`CIFilter`) that perform common low-level operations that are used across a wide array of image processing tasks.

The following APIs have been removed in the OS X v10.9 SDK:

- Open Transport
- Power management (`Power.h`)

The `DAApprovalSessionRef` type has been replaced by `DASessionRef` throughout this framework. (The two types are functionally equivalent.)

The following sections highlight changes and enhancements in the Foundation framework. For detailed information about changes in the Foundation programming interfaces, see _[Foundation Release Notes for macOS 10.13 and iOS 11](../../Foundation/Foundation%20Release%20Notes%20for%20macOS%2010.13%20and%20iOS%2011.md)_.

The `NSCalendar` class adds the `enumerateDatesStartingAfterDate:matchingComponents:options:usingBlock:` method for iterating forwards or backwards through dates that match a particular pattern until the callback block tells it to stop. For example, an `NSCalendar` object might call your block for every Saturday beginning from the current date.

Also, existing `NSCalendar` methods that convert between date and date components now use stricter parameter checking to prevent unreasonable combinations of day-identifying calendrical units. The allowed combinations are:

- Era Year Month Day-of-month
- Era Year Month Weekday-ordinality Weekday
- Era Year Month Week-of-month Weekday
- Era Year-for-week-of-year Week-of-year Weekday

along with various harmless subsets of the above, in combination with hour, minute, and so on. For example, using the `NSYearForWeekOfYearCalendarUnit` and `NSYearCalendarUnit` units in the same call to `components:fromDate:` now returns an error.

The [NSURL](https://developer.apple.com/documentation/foundation/nsurl) class and the `NSURLComponents` class provide significantly expanded support for obtaining and working with portions of URLs, including path components, host, port, query strings, and so on. This class supersedes the path component functionality in `NSString`.

In addition, the `NSURL` class provides support for getting and setting tags on files and directories.

The `NSProcessInfo` class provides the `beginActivityWithOptions:reason:`, `endActivity:`, and `performActivityWithOptions:reason:block:` methods (and associated constants) for temporarily suspending sudden termination, automatic termination, throttling (App Nap), and idle and display sleep.

The `NSProgress` class provides a standard mechanism that can be used for providing notification of the progress of long-running operations—downloads, for example—to interested parties.

The [NSNetService](https://developer.apple.com/documentation/foundation/netservice) class now provides a lightweight way to listen for incoming connections. If you set the `NSNetServiceListenForConnections` option flag in the options value passed to [publishWithOptions:](https://developer.apple.com/documentation/foundation/nsnetservice/1414390-publishwithoptions), OS X automatically handles all of the connection management for you.

When a client connects, the `NSNetService` object calls its delegate’s `netService:didAcceptConnectionWithInputStream:outputStream:` method, passing it a pair of `NSStream` objects that represent the newly established connection.

The [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) class now provides the following methods for converting to and from Base64 encoding:

- `initWithBase64EncodedString:options:`
- `base64EncodedStringWithOptions:`
- `initWithBase64EncodedData:options:`
- `base64EncodedDataWithOptions:`

The [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession) class is a new API for making HTTP requests in the context of a browser or in other situations where multiple requests are related. It provides the ability to resume downloads and uploads in the background, with notification when those downloads are complete. It also provides support for custom cookie stores, authentication, and caching in a manner that provides greater transparency and that gives your app greater control compared with earlier `NSURL` APIs.

The JavaScript Core framework (`JavaScriptCore.framework`) now provides cross-platform (OS X and iOS) Objective-C wrapper classes for many standard JavaScript objects. Use this framework to evaluate JavaScript code and parse JSON data. For information about the classes of this framework, see the header files.

The Open Directory plug-in API has been redesigned for OS X v10.9. Existing Open Directory plug-ins must be rewritten to conform to the new API. The new plug-in scheme is significantly less complex than the previous scheme, and Xcode templates are available to make creating these plug-ins easier. For more information, see _[Open Directory Release Notes](../../Networking%20Internet%20Web/Open%20Directory%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztgojy)_.

OS X v10.9 supports the OpenGL 4.1 Core Profile on Macs with GPUs that are capable of supporting its feature set. Read _[OpenGL Programming Guide for Mac](../../../documentation/Graphics%20Imaging/OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobx)_ to learn about choosing a profile.

OS X v10.9 supports OpenCL 1.2 using the GPU on recent Macs, including those with Intel HD Graphics 4000.

The Security framework (`Security.framework`) adds support for syncing passwords between user's devices via iCloud. Apps can mark their keychain items for iCloud via a new keychain attribute. For more information about this attribute, see the framework header files. For general information about the keychain, see _Keychain Services Programming Guide_.

In addition, a number of trust-related iOS APIs, such as [SecTrustCopyExceptions](https://developer.apple.com/documentation/security/1400106-sectrustcopyexceptions), are now available in OS X.

OS X v10.9 supports auto-renewable subscriptions for In-App Purchases.

In OS X v10.9, secure cookie storage is no longer shared between Safari and WebKit.

Notable in OS X v10.9 are changes to Messages.

The video chat functionality has been removed from the Messages app in OS X v10.9, in favor of the standardized, iOS-compatible video chat functionality built into the FaceTime app. This change potentially affects developers in two ways:

- The Instant Message Framework is no longer supported, and all methods return an empty list. Use the Social framework instead.
- Multiway video chats are no longer supported.

Xcode 5.0 adds numerous features that support OS X v10.9, notably:

- The LLDB debugger now supports kernel extension debugging; to learn more about transitioning from GDB to LLDB, read [LLDB Command Map](http://lldb.llvm.org/lldb-gdb.html) and _[LLDB Quick Start Guide](../../../documentation/IDEs/LLDB%20Quick%20Start%20Guide/About%20LLDB%20and%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdsmjx)_.
- The GDB debugger has been removed.

For more information about Xcode enhancements, see _[What’s New in Xcode](../../../documentation/Developer%20Tools/What%E2%80%99s%20New%20in%20Xcode/What%27s%20New%20in%20Xcode%209.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmrw)_.

The BSD, driver, and kernel layers of OS X have been enhanced as follows:

- OS X supports remote kernel and kernel extension debugging using LLDB.
- The OS X v10.9 kernel debug kit now includes kext macros for LLDB.
- Developers producing kernel extensions for OS X v10.9 should sign their extensions with a Developer ID certificate and install them in `/Library/Extensions/`. Extensions in `/Library/Extensions/` are not loaded unless they are properly signed.

  OS X v10.9 also warns the user when an unsigned or improperly signed kernel extension in `/System/Library/Extensions/` is loaded into the kernel or added to a kext cache.

[Next](OS%20X%20Mountain%20Lion%20v10.8.md)[Previous](OS%20X%20Yosemite%20v10.10.md)

