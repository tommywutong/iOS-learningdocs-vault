---
title: What's New in macOS
apple_id: TP40001812
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/WhatsNewInOSX/Articles/MacOSX10_8.html
archived_at: '2026-07-18T02:58:53.453824Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [What's New in macOS](Introduction.md)


[Next](OS%20X%20Lion%20v10.7.md)[Previous](OS%20X%20Mavericks%20v10.9.md)

# OS X Mountain Lion v10.8

This article summarizes the key technology changes and improvements available in OS X v10.8. The information about these changes is organized into sections by technology area.

- [Major Features](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytmmzufvjvomq) describes important features that impact developers.
- [Framework-Level Features](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytmmzufvjvomy) describes changes to system frameworks.
- [App Features](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytmmzufvjvomzq) describes changes in built-in apps.
- [BSD and Kernel Features](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytmmzufvjvona) describes changes to the UNIX/POSIX portions of OS X.

For a detailed list of API changes, see _[OS X v10.8 API Diffs](https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/index.html#//apple_ref/doc/uid/TP40011748)_.

Please file any bug reports about this release or this documentation at [http://bugreport.apple.com/](http://bugreport.apple.com/).

The following sections highlight OS X v10.8 features that span multiple technology areas or that are otherwise of particular importance to most developers.

Game Center on OS X v10.8 accesses the same social-gaming network as on iOS, allowing users to track scores on a leaderboard, compare their in-game achievements, invite friends to play a game, and start a multiplayer game through automatic matching. Game Center functionality is provided in two parts:

- The Game Center app, in which users sign in to their account, discover new games and new friends, add friends to their gaming network, and browse leaderboards and achievements.
- The Game Kit framework, which contains the APIs developers use to support live multiplayer or turn-based games and adopt other Game Center features, such as in-game voice chat and leaderboard access.

Apple supports Game Center with the online Game Center service, which performs player authentication, provides leaderboard and achievement information, and handles invitations and automatching for multiplayer games. You interact with the Game Center service only indirectly, using the Game Kit APIs.

In your game, use the Game Kit APIs to post scores and achievements to the Game Center service and to display leaderboards in your user interface. You can also use Game Kit APIs to help users find others to play with in a multiplayer game.

To learn more about adding Game Center support to your app, see _[Game Center Programming Guide](../../../documentation/Networking%20Internet/Game%20Center%20Programming%20Guide/About%20Game%20Center.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmbu)_.

OS X v10.8 introduces the iCloud Document Library, which gives users an easy way to access the app-specific documents they’ve stored in iCloud. When users start an app that participates in iCloud storage, the iCloud Document Library appears and allows them to open, share, duplicate, and organize their documents.

If your app is `NSDocument` based, you can take advantage of the following things:

- The iCloud Document Library view in the Open window
- The appropriate menu items added to your app’s File menu and to a document’s Versions menu
- A dialog that helps users resolve conflicts (when they open a document that they changed using another device)

To learn more about integrating iCloud into your app, see _[iCloud Design Guide](../../../documentation/General/iCloud%20Design%20Guide/About%20Incorporating%20iCloud%20into%20Your%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaoju)_.

Notification Center provides a way for users to receive and view app notifications in an attractive, unobtrusive way. For each app, users can specify how they want to be notified of an item’s arrival; they can also reveal Notification Center to view all the items that have been delivered.

When you use the `NSUserNotification` and `NSUserNotificationCenter` APIs introduced in OS X v10.8, you can configure the user-visible portions of a notification item, schedule items for delivery, and find out when items have been delivered. You can also determine whether your app has launched as a result of a notification and, if it has, whether that notification originated locally or remotely.

To learn more about integrating the Notification Center into your app, see _[NSUserNotification Class Reference](https://developer.apple.com/documentation/foundation/nsusernotification)_ and _[NSUserNotificationCenter Class Reference](https://developer.apple.com/documentation/foundation/nsusernotificationcenter)_.

The sharing service introduced in OS X v10.8 provides a consistent user experience for sharing content among many types of services. For example, a user might want to share a photo by attaching it to an email or a Twitter message, or sending it to another Mac user via AirDrop.

The new AppKit `NSSharingService` API allows you to get information about available services and share items with them directly. As a result, you can display a custom UI to present the services. You can also use the `NSSharingServicePicker` API to display a list of sharing services (including custom services that you define) from which the user can choose. When a service is performed, the system-provided sharing window is displayed. There the user can comment or add recipients. To learn more about the sharing service APIs, see _[NSSharingService Class Reference](https://developer.apple.com/documentation/appkit/nssharingservice)_ and _[NSSharingServicePicker Class Reference](https://developer.apple.com/documentation/appkit/nssharingservicepicker)_.

To allow your custom mail app to participate in sharing services, add the `MailSharingSupported` key to your `Info.plist` file and register a custom event handler, specifying the `mail` event class and the `shim` event ID. Then, in your event handler implementation, use the `shud` keyword to retrieve the event's descriptor data.

In OS X v10.8 users can turn on Gatekeeper, which allows them to block the installation of software that does not come from the Mac App Store and identified developers. If your app is not signed with a Developer ID certificate issued by Apple, it will not launch on systems that have this security option selected. If you plan to distribute your app outside of the Mac App Store, be sure to test the installation of your app on a Gatekeeper-enabled system so that you can provide a good user experience.

Xcode supports most of the tasks that you need to perform to get a Developer ID certificate and code sign your app. To learn how to submit your app to the Mac App Store—or test app installation on a Gatekeeper-enabled system—read _Tools Workflow Guide for Mac_.

OS X v10.8 includes the following enhancements to Objective-C:

- Default synthesis of accessor methods for declared properties
- Object literals for `NSArray`, `NSDictionary`, and `NSNumber`
- No need for forward declarations for methods that are used only within `@implementation` blocks
- Streamlined object subscripting
- Type-safe enums

OS X v10.8 requires a Mac that uses the 64-bit kernel. Additionally, OS X v10.8 does not support 32-bit kernel extensions (KEXTs). Both 32-bit and 64-bit apps can run in OS X v10.8.

The following sections highlight changes to frameworks and technologies in OS X v10.8.

The following frameworks have been added in OS X v10.8:

- __Accounts__ (`Accounts.framework`). This framework provides a single sign-on model for supported account types. Single sign-on improves the user experience because apps no longer need to prompt a user separately for login information related to an account. It also simplifies the development model for you by managing the account authorization process for your app. To learn more about the Accounts API, see _[ACAccount Class Reference](https://developer.apple.com/documentation/accounts/acaccount)_.
- __Audio Video Bridging__ (`AudioVideoBridging.framework`). This framework supports Audio Video Bridging (AVB) and implements the IEEE P1722.1 draft standard. AVB enhances the quality of service and provides guaranteed latency and bandwidth for media streams over an AVB network. The Audio Video Bridging API gives you access to the Entity discovery and control protocols of IEEE P1722.1 over an Ethernet network.
- __Event Kit__ (`EventKit.framework`). The Event Kit framework provides an interface for accessing a user’s calendar events and reminder items. You can use the APIs in this framework to get existing events and to add new events to the user’s calendar. Events that are created using Event Kit APIs are automatically propagated to the CalDAV or Exchange calendars on other devices, which allows your app to display up-to-date calendar information without requiring users to open the Calendar app. (Calendar events can include configurable alarms with rules for when they should be delivered.)

  You can also use Event Kit APIs to access reminder lists, create new reminders, add an alarm to a reminder, set the due and start date for a reminder, and mark a reminder as complete. To learn more about the Event Kit APIs, see _[Event Kit Framework Reference](https://developer.apple.com/documentation/eventkit)_.
- __Game Kit__ (`GameKit.framework`). As described in [Game Center](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytmmzufvjvony), the Game Kit framework provides APIs that allow your app to participate in Game Center. You can use Game Kit APIs to display leaderboards in your game and to give users the opportunity to share their in-game achievements and play multiplayer games. To learn more about using Game Kit APIs in your app, see _[Game Kit Framework Reference](https://developer.apple.com/documentation/gamekit)_.
- __GLKit__ (`GLKit.framework`). The GLKit framework provides libraries of commonly needed functions and classes that can help reduce the effort required to create an OpenGL app. In addition, the GLKit framework includes APIs that perform several optimized mathematical operations, reduce the effort in loading texture data, and provide standard implementations of commonly needed shader effects. To learn more about using GLKit APIs in your app, see _[GLKit Framework Reference](https://developer.apple.com/documentation/glkit)_.
- __Scene Kit__ (`SceneKit.framework`). The Scene Kit framework provides a high-level, Objective-C API that you can use to efficiently load, manipulate, and render 3D scenes in your app. Scene Kit allows you to import Digital Asset Exchange files (`.dae` files) that are created by popular content-creation applications and gives you access to the objects, lights, cameras, and geometry data that define a 3D scene. Using an approach based on scene graphs, Scene Kit makes it simple to modify, animate, and render your 3D scenes. For more information about using Scene Kit APIs in your app, see _[SceneKit Programming Guide](../../../documentation/3D%20Drawing/SceneKit%20Programming%20Guide/Introduction%20to%20Scene%20Kit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdeobs)_.
- __Social__ (`Social.framework`). The Social framework provides an API for sending requests to supported social networking services that can perform operations on behalf of your users. You can also use the Social framework to retrieve information for integrating a user’s social networking accounts into your app. To learn more about using the Social framework in your app, see _[Social Framework Reference](https://developer.apple.com/documentation/social)_.
- __Video Toolbox__ (`VideoToolbox.framework`). The Video Toolbox framework comprises the 64-bit replacement for the QuickTime Image Compression Manager. The Video Toolbox APIs provide services for video compression and decompression, and for conversion between raster image formats stored in Core Video pixel buffers.

The following sections highlight changes and enhancements in the AppKit framework. For detailed information about changes in the AppKit programming interfaces, see _[AppKit Release Notes for macOS 10.13](../../App%20Kit/AppKit%20Release%20Notes%20for%20macOS%2010.13.md)_.

The AppKit framework introduces new `NSView` APIs that enhance the implementation and performance of layer-backed views. When you use layer-backed views in your app, Core Animation can perform view animations asynchronously, which can result in better, smoother animations. To benefit from the enhancements to layer-backed views in OS X v10.8, set the `layerContentsRedrawPolicy` property on your custom views to `NSViewLayerContentsRedrawOnSetNeedsDisplay`. If you do any custom drawing, refactor it to use subviews as much as possible (you can add subviews to a view at design time, or you can allow subviews to be added lazily in the `layout` method).

In addition, you can use other new `NSView` APIs to update a view’s layer declaratively. For example, you can return `YES` in `wantsUpdateLayer` and then implement `updateLayer` to set the layer’s properties. Typically, you set the layer’s contents to an `NSImage` object and set the `contentsCenter` property to specify the proper way to stretch the image. Or you can set simple layer properties, such as `backgroundColor` and `borderColor`. To learn more about the new `NSView` APIs, see _[NSView Class Reference](https://developer.apple.com/documentation/appkit/nsview)_.

Because a layer object often works with `CGColorRef` objects, you might need to convert between an `NSColor` object and a `CGColorRef` object frequently. To help you easily perform these conversions, the `NSColor` class provides the new `CGColor` and `colorWithCGColor:` methods. To learn more about new `NSColor` methods, see _[NSColor Class Reference](https://developer.apple.com/documentation/appkit/nscolor)_.

In OS X v10.8, text rendering in transparent layers is enhanced. For example, `NSTextField`—in addition to other AppKit UI controls—can properly render text with font smoothing on a transparent layer background. At the same time, AppKit explicitly disables font smoothing in custom-rendered transparent layers to avoid drawing artifacts.

New AppKit APIs make it easier for you to adopt modern gestures in your app and to provide a better zoom experience without redrawing your content. For example, `NSScrollView` now has built-in support for the smart zoom gesture (that is, a two-finger double-tap on a trackpad). When you provide the semantic layout of your content, `NSScrollView` can intelligently magnify the content under the pointer. In addition, you can use this new API to respond to the lookup gesture (that is, a three-finger tap on a trackpad). To learn more about the new `NSScrollView` APIs, see _[NSScrollView Class Reference](https://developer.apple.com/documentation/appkit/nsscrollview)_.

The new `NSPageController` class, which controls swipe navigation between views or view content, helps you implement a multipage book or browsing history user experience in your app. You can use `NSPageController` and its delegate to manage navigation through a predefined set of content views (such as the pages in a book) or a history of content snapshots, which changes when the user visits different views. To learn how to use `NSPageController`, see _[NSPageController Class Reference](https://developer.apple.com/documentation/appkit/nspagecontroller)_.

The new `NSTextAlternatives` class stores a list of alternatives for a specific piece of text and can notify your app when the user chooses an alternative. To support dictation, for example, you might use `NSTextAlternatives` to present a list of alternative interpretations for a word or phrase the user speaks. If the user chooses to replace the initial interpretation with an alternative, `NSTextAlternatives` notifies you of the choice so that you can update the text appropriately.

Enhancements to various AppKit classes improve their support for Auto Layout. For example, you can use the new `NSSplitView` holding priority API to specify how the panes of a split view should react to changes in the split view's size. To allow the height of a fixed-width text field to grow when its content increases, you can use the new `NSTextField` method `setPreferredMaxLayoutWidth`. If you use `NSMatrix` objects in your app, you can use the new `setAutorecalculatesCellSize` method to cause the object’s cell contents to determine the cell size.

The new `NSImage` method `imageWithSize:flipped:drawingHandler:` allows you to create an image that delegates its drawing to a block. Because the block is invoked at draw time, the drawing can be adjusted to suit the destination’s pixel density, color space, and other properties. The `imageWithSize:flipped:drawingHandler:` method can be a good alternative to using the [lockFocus](https://developer.apple.com/documentation/appkit/nsimage/1519891-lockfocus) and [unlockFocus](https://developer.apple.com/documentation/appkit/nsimage/1519853-unlockfocus) methods, especially when you need to support moving images between displays that have different properties. To learn how to optimize your app so that it looks great on a Retina display, see _[High Resolution Guidelines for OS X](../../../documentation/Graphics%20Animation/High%20Resolution%20Guidelines%20for%20OS%20X/About%20High%20Resolution%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmbs)_.

In OS X v10.8 some parts of the Auto Save user experience changed. If your document-based app participates in iCloud, the system automatically saves untitled documents in iCloud as soon as the user begins editing. (If your app doesn’t participate in iCloud, untitled documents are saved in the user’s Documents folder.) If the user provides a title in the Save dialog, the new title is used instead. To duplicate a document, the Duplicate menu item now allows users to supply a name for the document copy. When users close a duplicated document that has not been saved explicitly, they’re asked whether they want to keep the document or delete it.

When a user edits an old document, the default setting that governs whether an alert appears has changed from on to off. Specifically, the alert that states “The document is locked because you haven’t made any changes to it recently” does not appear unless the user turns on the setting in Time Machine preferences. By default, a document is considered old if it has not been changed in at least 2 weeks.

If a document-based app that adopts Auto Save is in the foreground when the user starts Time Machine, the Versions feature displays previous versions of the document.

The AV Foundation framework includes the following enhancements:

- The `AVAsset` and `AVPlayerItem` classes include new properties that help you find media-resource options that accommodate language preferences, accessibility requirements, and other needs, and then select them for playback.
- New methods extend the `AVPlayer` class so that you can schedule playback to start at an arbitrary host time and can ensure that it remains synchronized with another time-based operation, such as audio playback that’s performed using Audio Toolbox APIs.
- The new `AVSampleBufferDisplayLayer` class allows you to display a sequence of video frames in a Core Animation layer. You can also use this class to control timing and optional synchronization with an audio device clock.
- The new `AVPlayerItemOutput` class, in conjunction with new `AVPlayerItem` methods, allows you to get decoded video frames during playback so that your app can process them.

Core Animation introduces the new `drawsAsynchronously` property for a `CALayer` object. When the value of this property is `YES`, the graphics context object that is passed to the layer’s `drawInContext` method can queue its drawing commands so that they are executed asynchronously. When drawing commands are executed asynchronously, drawing operations can be done more efficiently.

When you use the `drawsAsynchronously` property, make sure to handle the memory management of your app’s context resources (such as shadings, images, and functions) in accordance with the requirements of the Quartz 2D API. In particular, a resource must avoid referencing transient memory (such as data on the stack) because the resource might persist after the function returns to its caller.

The Core Graphics framework introduces streaming APIs for capturing updates to the display in a real-time manner and for providing scaling and color-space-conversion services. The framework also adds support for viewing and modifying metadata for popular image formats.

The Core Location framework introduces the `CLGeocoder` and `CLPlacemark` classes to give users information about a location. For example, you can use a geocoder object to convert latitude and longitude (that pinpoint a location) to a user-friendly description of that location. The user-friendly description—which typically includes street, city, and country information—is stored in a `CLPlacemark` object. You can also use a `CLGeocoder` object to convert an address dictionary from Contacts or a human-readable address string—such as “1 Infinite Loop, Cupertino, CA 95014”—into geographical coordinates.

The Core Location framework also enables region monitoring. In particular, you can use the `startUpdatingForRegion` and `stopUpdatingForRegion` methods to receive callbacks when the user enters or exits a region that you specify. To learn more about the new classes in the Core Location framework, see _[Core Location Framework Reference](https://developer.apple.com/documentation/corelocation)_.

The Core Media framework introduces the `CMSync` API, which defines two fundamental media time services objects:

- `CMClock`, which represents a source of timing information such as `mach_absolute_time` or an audio device
- `CMTimebase`, which represents a timeline that is under app control (that is, a timeline on which you can set the time and the rate at which the media plays)

The Core Media framework also introduces the `CMAudioDeviceClock` and `CMMemoryPool` APIs. The `CMAudioDeviceClock` API provides a `CMClock` object that’s synchronized to an audio device. The `CMMemoryPool` API maintains a pool of recently deallocated memory blocks so that subsequent allocations of the same size can be made more quickly. For example, clients of the Video Toolbox video compression services can get an allocator from a `CMMemoryPool` object and pass it to a `VTCompressionSession` object. As a result, the video encoder can benefit from pooling behavior when the encoder allocates memory for compressed video frames.

The Core Text framework includes support for optical glyph bounds and unregistered data fonts. It also introduces:

- AAT (Apple Advanced Typography) text features that help you access common OpenType layout tags
- String attributes that allow you to use baseline alignments
- The `CTLineGetBoundsWithOptions` function, which gives you finer-grained control of line metrics

To learn more about using Core Text in your app, see _[Core Text Programming Guide](../../../documentation/Strings%20Text%20Fonts/Core%20Text%20Programming%20Guide/About%20Core%20Text.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmzt)_.

The Foundation framework introduces the following enhancements:

- The new `NSUUID` class helps you create objects that represent various types of UUIDs (Universally Unique Identifiers). For example, you can create an `NSUUID` object with [RFC 4122](http://www.ietf.org/rfc/rfc4122.txt) v4 random bytes, or you can base the UUID on an existing string. To learn more about the `NSUUID` class, see _[NSUUID Class Reference](https://developer.apple.com/documentation/foundation/nsuuid)_.
- The new `NSXPCConnection` class provides a Cocoa interface to the XPC library for communicating between processes, and allows you to use your own objects and classes. To learn more about the `NSXPCConnection` class, see _[NSXPCConnection Class Reference](https://developer.apple.com/documentation/foundation/nsxpcconnection)_.
- New `NSFileManager` API allows you to discover the currently active iCloud account and detect when the user logs into or out of it.

For detailed information about changes in the Foundation programming interfaces, see _[Foundation Release Notes for macOS 10.13 and iOS 11](../../Foundation/Foundation%20Release%20Notes%20for%20macOS%2010.13%20and%20iOS%2011.md)_.

In OS X v10.8 three functions related to OpenGL context copying are deprecated:

- `CGLCopyContext`
- [aglCopyContext](https://developer.apple.com/documentation/agl/1392835-aglcopycontext)
- [copyAttributesFromContext:withMask:](https://developer.apple.com/documentation/appkit/nsopenglcontext/1436166-copyattributesfromcontext)

The Store Kit framework introduces the ability to make your In-App Purchase content available in the Mac App Store. The content can be uploaded to iTunes Connect via Xcode or Application Loader and downloaded in your app using the following Store Kit APIs:

- The [SKPaymentQueue](https://developer.apple.com/documentation/storekit/skpaymentqueue) class has new methods to start, pause, and cancel downloads.
- The new [SKDownload](https://developer.apple.com/documentation/storekit/skdownload) class represents the status of a download from the Mac App Store and provides methods that allow you to get information about the download, including the percentage complete and an estimate of the time remaining.

The System Configuration framework introduces the captive network API, which allows apps to provide a better user experience when interacting with a captive network. (A _captive network_, such as a public Wi-Fi hotspot, requires user interaction before providing Internet access.) Captive network support (CNS) improves the user’s connectivity experience by identifying whether a network is captive and, if it is, looking for another app that might be able to handle the connection. If no such app can be found, CNS then attempts to log in with credentials the user has saved. If neither of these solutions works, CNS displays the network’s login webpage so that the user can log in to the network. Without CNS, users might not get prompted to log in to a captive network, and so they might assume that the resulting delay is the app’s fault.

You can use the captive network API to tell CNS to mark an interface as online or offline. You can also use it to provide information about the SSIDs (service set IDs) that CNS should relinquish control of in favor of apps that can handle captive network connectivity.

In OS X v10.8, most of the APIs in the Carbon Core framework are deprecated (Carbon Core is a subframework of the Core Services umbrella framework). In many cases, there are alternative APIs you can use, such as APIs in the Core Foundation, Foundation, and Disk Arbitration frameworks.

Some of the deprecated APIs are high-level wrappers around functions in the POSIX or BSD layers, such as [malloc](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/malloc.3.html#//apple_ref/doc/man/3/malloc), [pthread](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/pthread.3.html#//apple_ref/doc/man/3/pthread), and [sysctl](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html#//apple_ref/doc/man/3/sysctl). In place of using a deprecated wrapper function, you should use the appropriate lower-level API directly. In some cases, you can use GCD (Grand Central Dispatch) instead. Finally, some of the deprecated APIs are no longer needed or recommended, such as the bit-operation functions in `ToolUtils.h`. (The bit-operation functions were needed in Pascal development, and C provides bit operators.) To learn more about the Carbon Core APIs that are deprecated, see _[Carbon Core Deprecations](https://developer.apple.com/library/archive/releasenotes/General/CarbonCoreDeprecations/index.html#//apple_ref/doc/uid/TP40012224)_.

Notable in OS X v10.8 are changes to Safari.

Safari 6.0 includes the following new features and enhancements:

- __SVG filters__. SVG (scalable vector graphics) filters combine filter-primitive elements and light source elements into a single sophisticated filter, which you can then apply to any SVG element.
- __Web notifications__. The web notifications API sends a notification from a Safari extension or webpage. Users receive these notifications in Notification Center, along with other notifications they choose to receive.
- __Redesigned Web Inspector__. The Web Inspector in Safari 6.0 features a navigation sidebar—for displaying information about resources, storage, and instruments—and a details sidebar—for quickly and easily editing the CSS for any DOM element. The new Web Inspector also includes a more contextual JavaScript evaluation area that is separate from the error log, streamlined instrumentation and profiling tools, and a more accessible page source view.
- __The Web Audio API__. JavaScript Web Audio API synthesizes and processes audio in web apps having complex audio requirements, such as a modern game audio engine or an interactive audio production app.
- __HTML5 media controllers__. Using an HTML5 media controller, you can coordinate the playback of multiple HTML5 media elements. For example, you can use a media controller to synchronize a sign-language-interpretation track with a video track.
- __HTML5-timed text tracks__. You can use an HTML5-timed text track to specify the timing at which text (such as captions or subtitles) appears within an HTML5 video element.
- __CSS filters__. You can use CSS filters to apply pixel effects, such as invert and blur, to an image or webpage element. You can also combine CSS filters, and you can use CSS transitions and animations to animate changes to a filter.

To learn more about Safari 6.0, read [Safari and WebKit Release Notes](https://developer.apple.com/devcenter/download.action?path=/Safari/safari_5.2_update_2/safari5_2lionupdate2releasenotes.pdf) (login required).

Xcode 4.4 adds numerous features that support OS X v10.8, notably:

- Compiler support for the Objective-C enhancements described in [Objective-C Enhancements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytmmzufvjvooa)
- The ability to open a project in multiple workspaces
- Enhanced internationalization support, including the ability to add a base locale to your project and define a strings file that contains localized strings

For more information about Xcode enhancements, see _What's New in Xcode_.

Grand Central Dispatch (GCD) and XPC (interprocess communication) objects support Automated Reference Counting (ARC) in Objective-C. Using GCD and XPC with ARC requires a minimum deployment target of OS X v10.8 (this functionality is unavailable if you have a 32-bit Intel machine).

[Next](OS%20X%20Lion%20v10.7.md)[Previous](OS%20X%20Mavericks%20v10.9.md)

