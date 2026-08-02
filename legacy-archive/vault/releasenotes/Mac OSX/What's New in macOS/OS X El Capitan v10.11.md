---
title: What's New in macOS
apple_id: TP40001812
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/WhatsNewInOSX/Articles/MacOSX10_11.html
archived_at: '2026-07-18T02:58:48.054388Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [What's New in macOS](Introduction.md)


[Next](OS%20X%20Yosemite%20v10.10.md)[Previous](OS%20X%20El%20Capitan%20v10.11.2.md)

# OS X El Capitan v10.11

This article summarizes the key technology changes and improvements in OS X v10.11. The information about these changes is organized into sections by technology area.

For a detailed list of API changes, see _[OS X v10.11 API Diffs](https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/index.html#//apple_ref/doc/uid/TP40016197)_.

Please file any bug reports about this release or this documentation at [http://bugreport.apple.com/](http://bugreport.apple.com/).

The following sections highlight OS X v10.11 features that span multiple technology areas or that are otherwise of particular importance to most developers.

__Metal__ is now available in OS X. The Metal framework supports GPU-accelerated advanced 3D graphics rendering and data-parallel computation workloads. Metal provides a modern and streamlined API for fine-grained, low-level control of the organization, processing, and submission of graphics and computation commands, as well as the management of the associated data and resources for these commands. A primary goal of Metal is to minimize the CPU overhead incurred by executing GPU workloads.

OS X v10.11 provides flexible and efficient new controls for managing windows.

You can now put two windows in a full-screen space. These windows may belong to the same application or two different applications.

There are two ways to create a split-view space. First, you can long-press on the green full-screen button of a window that supports full screen. Place the first window on one half of the screen, then choose a second window from an exposé arrangement of eligible windows.

Alternatively, you can drag a window that supports full screen up through the menu bar to open Mission Control. In Mission Control’s Spaces Bar, you are given an option to create a new full-screen space. You can then select a second window and drag it on top of the full-screen thumbnail to create a split view.

Window minimum sizes are respected, so you are only able to combine two windows if their combined minimum widths fit within the width of the screen.

Once in a split-view space, you can drag the divider between the two windows left or right to resize them. You can drag the toolbar of either window to the other side to cause the two windows to swap sides.

Mission Control gives you easier access to your windows. The Spaces Bar is minimized in Mission Control, providing maximum real estate for window arrangement. You can move the mouse over the Spaces Bar to show the full thumbnails for each space.

Swift 2.0 is modern, powerful, expressive, and easy to use. It extends Swift 1.2 with:

- __Error Handling__. Now you can create routines that throw, catch and manage errors in Swift. You can surface and deal with recoverable errors, like “file-not-found” or network timeouts. Swift 2.0’s error handling interoperates seamlessly with [NSError](https://developer.apple.com/documentation/foundation/nserror).
- __Availability.__ Availability features enable you to mark up methods with the OS that they are available on, providing compile time checking and preventing unavailable methods from being used. You can adopt new APIs while still deploying back to older OS versions, and provides compile-time errors when you’re using API that isn’t guaranteed to be available on the deployment target.
- __Protocol extensions.__ You can now add methods and properties to any class that conforms to a particular protocol, allowing you to reuse more of your code. For example, in the standard library, instead of having to use global functions for all of the generic algorithms in the standard library (such as map, filter, and sort), those generic algorithms are now available as methods on all of the collection types.
- __Testability.__ With testability, you are now able to write tests of Swift 2.0 frameworks and apps without having to make all of your internal routines public. Use `@testable import {ModuleName}` in your test source code to make all public and internal routines usable by XCTest targets, but not by other framework and app targets.

For more details on these and other new features, see _The Swift Programming Language_.

Objective-C has been updated to enable it and Swift to work together more seamlessly and efficiently. The new Objective-C language features include:

- __Generics.__ Allow you to specify type information for collection classes like [NSArray](https://developer.apple.com/documentation/foundation/nsarray), [NSSet](https://developer.apple.com/documentation/foundation/nsset), and [NSDictionary](https://developer.apple.com/documentation/foundation/nsdictionary). The type information improves Swift access when you bridge from Objective-C and simplifies the code you have to write.
- __Nullability annotation.__ Lets you indicate in Objective-C source when to expect a value to be nil or non-nil, smoothing the use of Objective-C frameworks and modules from Swift code.
- __Kind-Of.__ Objects declared as `__kindof` types express “some kind of X” to the compiler and can be used within generic parameters to constrain types to a particular class or its subclasses. Using `__kindof` allows constraints to be more flexible than an explicit class, and more explicit than just using `id`.

These new language features help the Objective-C/Swift interaction. They express more information to the compiler about your expectations in the code rather than in documentation, which provides a means for Xcode to inform you of problems earlier in the development cycle, before your code is run. See _Using Swift with Cocoa and Objective-C_ for more details.

Improvements in security make both network and local activities safer.

App Transport Security (ATS) enforces best practices in the secure connections between an app and its back end. ATS prevents accidental disclosure, provides secure default behavior, and is easy to adopt; it is also on by default in OS X v10.11 and iOS 9. You should adopt ATS as soon as possible, regardless of whether you’re creating a new app or updating an existing one.

If you’re developing a new app, you should use HTTPS exclusively. If you have an existing app, you should use HTTPS as much as you can right now, and create a plan for migrating the rest of your app as soon as possible. In addition, your communication through higher-level APIs needs to be encrypted using TLS version 1.2 with forward secrecy. If you try to make a connection that doesn't follow this requirement, an error is thrown. If your app needs to make a request to an insecure domain, you have to specify this domain in your app's `Info.plist` file.

A new security policy that applies to every running process, including privileged code and code that runs out of the sandbox. The policy extends additional protections to components on disk and at run-time, only allowing system binaries to be modified by the system installer and software updates. Code injection and runtime attachments to system binaries are no longer permitted.

__Shared Links Extensibility.__ App developers can use the new Shared Links API extension to add link suggestions to the shared links feed on Safari for OS X and iOS.

__Content Blocking API for Safari extensions.__ Safari extension developers can easily block content from a large collection of sources with minimal resources and incredibly high performance.

__Force Touch Trackpad Mouse Events.__ Create interactivity like never before using new events and force information from the Force Touch Trackpad.

__CSS Scroll Snapping.__ Use CSS scroll snapping to keep the focal point of your content in view when scrolling momentum stops.

__AirPlay for HTML5 Media.__ If you use custom controls for your HTML5 media, use JavaScript AirPlay support to add your own control to stream audio and video to AirPlay devices.

__HTML5 Video PiP.__ Use new JavaScript PiP support to add your own picture-in-picture control to custom controls for HTML5 videos.

__FairPlay Streaming.__ Stream premium web video content securely with FairPlay Streaming support in Safari on OS X.

__Backdrop Filters.__ Add advanced image filters to the backdrop of your elements to achieve modern iOS and OS X material effects in your web content layouts.

AppKit contains new APIs for interacting with Force Touch trackpads. You can now write apps that provide haptic feedback at specific times, such as when objects snap into alignment or when the user reaches the end of something, such as a track view in an audio/video app. New pressure configuration features provide greater control over the behavior and progression of pressure gestures, such as whether acceleration or force clicks are supported. New spring loading features make it easier to activate objects, such as buttons and segmented controls, by force clicking during drag operations. New APIs allow you to implement actions, such as swipe to delete, on table view rows.

WebKit also introduces new APIs for detecting and responding to force pressure from within HTML pages.

Even small inefficiencies in apps add up, significantly affecting battery life, performance, and responsiveness. As an app developer, you have an obligation to make sure your app runs as efficiently as possible. _[Energy Efficiency Guide for Mac Apps](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/index.html#//apple_ref/doc/uid/TP40013929)_ provides comprehensive guidelines and recommendations for developing energy efficient Mac apps that perform great help users achieve all-day battery life.

Traditionally, there were a number of Auto Layout techniques that required dummy views—empty views that did not have any visual elements of their own. Instead, they simply served to define a rectangular region in the view hierarchy. [NSLayoutGuide](https://developer.apple.com/documentation/appkit/nslayoutguide) provide a lightweight alternative. Layout guides define a rectangular region that can interact with Auto Layout. and can be used to define negative space or to group a number of individual items.

For more information, see _[NSLayoutGuide Class Reference](https://developer.apple.com/documentation/appkit/nslayoutguide)_ and _[NSView Class Reference](https://developer.apple.com/documentation/appkit/nsview)_.

Provide a fluent interface for programmatically creating Auto Layout constraints. This new API produces simpler, cleaner code that is easier to read, while also providing additional type check information to help prevent the accidental creation of invalid constraints.

For more information, see _[NSLayoutAnchor Class Reference](https://developer.apple.com/documentation/appkit/nslayoutanchor)_.

[NSStackView](https://developer.apple.com/documentation/appkit/nsstackview) has additional subview distribution options, and is also available on iOS.

If you have a CloudKit app, you can use CloudKit web services or CloudKit JS, a JavaScript library, to provide a web interface for users to access the same data as your app. You must have the schema for your databases already created to use a web interface to fetch, create, update, and delete records, zones, and subscriptions.

For more information, see [CloudKit JavaScript Reference](https://developer.apple.com/library/prerelease/ios/documentation/CloudKitJS/Reference/CloudKitJavaScriptReference/index.html), [CloudKit Web Services Reference](https://developer.apple.com/library/prerelease/ios/documentation/DataManagement/Conceptual/CloutKitWebServicesReference/Introduction/Introduction.html), and [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](https://cdn.apple-cloudkit.com/cloudkit-catalog/).

Provide users access to filters and editing tools directly from within the Photos app on Mac.

The following sections highlight changes to frameworks and framework technologies in OS X v10.11.

The following frameworks have been added in OS X v10.11:

- __Contacts__ (`Contacts.framework`). Provides a modern object-oriented replacement for the Address Book framework. To learn more, see _[Contacts Framework Reference](https://developer.apple.com/documentation/contacts)_.
- __GameplayKit__ (`GameplayKit.framework`). Provides foundational technologies for building games. Use GameplayKit to develop gameplay mechanics, and combine it with any high-level graphics engine—such as SceneKit or SpriteKit—to build a complete game. To learn more about GameplayKit, see _[GameplayKit Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172)_ and _[GameplayKit Framework Reference](https://developer.apple.com/documentation/gameplaykit)_.
- __Metal__ (`Metal.framework`). Provides GPU-accelerated 3D graphics rendering and data-parallel computation workloads. See _[Metal Programming Guide](../../../documentation/Miscellaneous/Metal%20Programming%20Guide/About%20Metal%20and%20This%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrr)_ and related references.
- __MetalKit__ (`MetalKit.framework`). Contains functions and classes that reduce the effort required to create a Metal application. See _[MetalKit Framework Reference](https://developer.apple.com/documentation/metalkit)_ and _[MetalKit Functions Reference](https://developer.apple.com/documentation/metalkit/metalkit_functions)_.
- __Model I/O__ (`ModelIO.framework`). The Model I/O framework provides a system-level understanding of 3D model assets and related resources. To learn more about Model I/O, see _[Model I/O Framework Reference](https://developer.apple.com/documentation/modelio)_.
- __Network Extension__ (`NetworkExtension.framework`). Provides support for configuring and controlling Virtual Private Network (VPN) tunnels.

A number of new functions have been added to vDSP, and the capabilities of `vDSP_biquadm` and its associated routines have been enhanced.

The following sections highlight changes and enhancements in the AppKit framework. For detailed information about changes in the AppKit programming interfaces, see _[AppKit Release Notes for macOS 10.13](../../App%20Kit/AppKit%20Release%20Notes%20for%20macOS%2010.13.md)_.

The power, flexibility, and scalability of the iOS `UICollectionView` class is now available on OS X 10.11. The new [NSCollectionView](https://developer.apple.com/documentation/appkit/nscollectionview) can present heterogeneous collections of variable-sized items, allows for completely customizable layout, supports sections with optional header and footer views, and recycles and lazily instantiates items to enable scaling to large numbers of objects.

The [NSStackView](https://developer.apple.com/documentation/appkit/nsstackview) class is significantly updated. It creates significantly fewer constraints to accomplish its layouts, and removes private views from its view hierarchy, instead using [NSLayoutGuide](https://developer.apple.com/documentation/appkit/nslayoutguide) where needed.

All the functionality available in the iOS version of `TextKit` is now available on OS X. Features include exclusion paths, the maximum number of lines restriction, `CGGlyph`-based [NSLayoutManager](https://developer.apple.com/documentation/uikit/nslayoutmanager) API, detailed layout controls via [NSLayoutManagerDelegate Protocol](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate), and more.

The [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) class now supports full-screen tiling. The system implicitly determines candidate windows for a full-screen tile based on window properties, such as the window being resizable and not a panel or sheet. Secondary full screen tiles do not need to be full-screen capable windows.

The [NSSplitViewItem](https://developer.apple.com/documentation/appkit/nssplitviewitem) class adds several properties that describe the associated metrics.

`NSSplitViewItem` also has support for flexible sidebars, which have the ability to auto-hide as the window shrinks, which is especially useful in split screen.

The [NSTableView](https://developer.apple.com/documentation/appkit/nstableview) class supports a new feature called “Swipe To Delete.” The delegate can implement `tableView:rowActionsForRow:edge:` and return an array of [NSTableViewRowAction](https://developer.apple.com/documentation/appkit/nstableviewrowaction) objects that represent buttons.

`NSTableView` also has methods to hide individual rows.

The [NSMenu](https://developer.apple.com/documentation/appkit/nsmenu) class provides a [userInterfaceLayoutDirection](https://developer.apple.com/documentation/appkit/nsview/1483254-userinterfacelayoutdirection) property for explicit control of the menu content layout direction. If not specified, a menu uses the layout direction of the application.

A new `centersPlaceholder` property controls whether the placeholder, magnifier search button and search menu are centered when the search field does not have focus and does not contain text. When it has focus, the control animates its contents to the edge.

Defines version 3 of the widely-used Audio Unit plug-in model.

The AVFoundation framework includes the following enhancements:

- `AVAudioConnectionPoint` adds support for splitting an audio signal chain in [AVAudioEngine](https://developer.apple.com/documentation/avfoundation/avaudioengine).
- `AVAudioConverter` and `AVAudioCompressedBuffer` add support for working with encoded audio formats.
- `AVAudioSequencer` plays back MIDI compositions to instruments using [AVAudioEngine](https://developer.apple.com/documentation/avfoundation/avaudioengine).
- For file-based assets, [AVMediaSelectionGroup](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup) objects for the media constant [AVMediaCharacteristicAudible](https://developer.apple.com/documentation/avfoundation/avmediacharacteristicaudible) now consolidate multiple encodings of the same audio content, such as AAC and AC-3 encodings, into a single [AVMediaSelectionOption](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption) object. The choice of which of the available encodings to employ for an [AVMediaSelectionOption](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption) object is made internally, by _[AVPlayer Class Reference](https://developer.apple.com/documentation/avfoundation/avplayer)_. If your code assumes that an [AVMediaSelectionOption](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption) object for audio content should or should not be selected based on its [mediaSubTypes](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1385587-mediasubtypes) property, you may need to account for this new, smarter behavior for file-based content.
- The [AVMutableMovie](https://developer.apple.com/documentation/avfoundation/avmutablemovie) adds the ability to perform edits on QuickTime movies and ISO-based media formats such as .mp4.
- You can apply `CoreImage` filters to movies for playback and export purposes.
- You can mix HLS (streaming) and file-based items in any instance of [AVPlayer](https://developer.apple.com/documentation/avfoundation/avplayer), including [AVQueuePlayer](https://developer.apple.com/documentation/avfoundation/avqueueplayer) objects.

Core Animation has adopted Metal as its rendering engine, improving rendering performance and efficiency.

The CASpringAnimation class provides a representation of a physical mass on a spring with a damper system.

Added batch delete functionality and remote merge notification capability. _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_ is significantly updated.

The Core Image framework includes the following enhancements:

- Metal is now supported as a rendering path. You create a [CIContext](https://developer.apple.com/documentation/coreimage/cicontext) that targets a specific Metal device and use it to render to a _[MTLTextureDescriptor Class Reference](https://developer.apple.com/documentation/metal/mtltexturedescriptor)_ object.
- The same filters and image detectors are available on both iOS and OS X.
- A common infrastructure for kernels can be used to write custom image kernels once and deploy them on both iOS and OS X.
- A new image detector, `CIDetectorTypeText`, finds regions of text inside an image.

Added the ability to access calendar delegates.

The following sections highlight changes and enhancements in the Foundation framework. For detailed information about changes in the Foundation programming interfaces, see _[Foundation Release Notes for macOS 10.13 and iOS 11](../../Foundation/Foundation%20Release%20Notes%20for%20macOS%2010.13%20and%20iOS%2011.md)_.

[NSNotificationCenter](https://developer.apple.com/documentation/foundation/notificationcenter) and [NSDistributedNotificationCenter](https://developer.apple.com/documentation/foundation/nsdistributednotificationcenter) no longer send notifications to registered observers that may be deallocated. If the observer is able to be stored as a zeroing-weak reference the underlying storage stores the observer as a zeroing weak reference. Alternatively, if the object cannot be stored weakly (because it has a custom retain/release mechanism that would prevent the runtime from being able to store the object weakly) the object is stored as a non-weak zeroing reference. This means that observers are not required to un-register in their deallocation method.

[NSProgress](https://developer.apple.com/documentation/foundation/progress) has a -resume method, which parallels the behavior of the existing -pause method.

`NSProgress` supports composition of progress objects into trees both implicitly and explicitly.

In OS X 10.10 and earlier, instances of [NSCoder](https://developer.apple.com/documentation/foundation/nscoder) communicated errors primarily through [NSException](https://developer.apple.com/documentation/foundation/nsexception), even if the underlying problem was not a programmer error. All `NSCoder` implementations now have support for error notification through [NSError](https://developer.apple.com/documentation/foundation/nserror) out-parameters, making it much easier to unarchive data in Swift.

[NSUndoManager](https://developer.apple.com/documentation/foundation/nsundomanager) supports block undo operations.

[NSString](https://developer.apple.com/documentation/foundation/nsstring) exposes API for transliteration. This was available in `CFString` previously.

You can now provide different width-variations for a string in a stringsdict file, the same file meant for different cardinalities. The -`[NSBundle localizedStringForKey:value:table:]` method reads the stringsdict file and creates an [NSString](https://developer.apple.com/documentation/foundation/nsstring) object that knows about the different variations.

In order to make instances of `NSError` as rich as possible, with localized description, failure reason, recovery attempter, and so forth, the `NSError` class allows you to specify a block as the userInfoValueProvider for a domain.

Adds support for querying transit ETAs and launching Maps into transit directions. In addition:

- [MKMapView](https://developer.apple.com/documentation/mapkit/mkmapview) supports a 3D flyover mode.
- MKAnnotations can be fully customized.
- Map Kit and [CLGeocoder](https://developer.apple.com/documentation/corelocation/clgeocoder) search results provide a time zone for the result.

New features in Scene Kit for OS X v10.11 include:

- __Metal rendering support.__ See the [SCNView](https://developer.apple.com/documentation/scenekit/scnview) and [SCNSceneRenderer](https://developer.apple.com/documentation/scenekit/scnscenerenderer) classes to enable high-performance Metal rendering on supported devices.
- __New Scene Editor in Xcode.__ Build games and interactive 3D apps with less time and less code by designing scenes in Xcode.
- __Positional audio.__ See the [SCNAudioPlayer](https://developer.apple.com/documentation/scenekit/scnaudioplayer) and [SCNNode](https://developer.apple.com/documentation/scenekit/scnnode) classes to add spatial audio effects that automatically track the listener’s position in a scene.

For details on these and many other new features, see _[SceneKit Framework Reference](https://developer.apple.com/documentation/scenekit)_.

The Web Kit framework includes many enhancements.

__Support for backdrop filters.__ Allows websites to apply a filter (for example, blur or grayscale) to all the content behind a specific piece of web content.

__Scroll snapping.__ Allows websites to add sophisticated scrolling behavior (for example, snapping from photo to photo in a gallery rather than scrolling to a random point based on the user’s momentum) with a few lines of CSS.

__CSS4 support.__ Allows more sophisticated selector matching behaviors, and allows you to collapse repeated rules into a single rule.

__ES6 support.__ Adds new class syntax, template strings, improvements to Number object, and more.

__Unprefixed CSS properties.__ Allows you to simplify your CSS rules.

__Support for AirPlay.__ The same JavaScript API previously available on iOS is now available on OS X, allowing you to add AirPlay support to your custom media controls.

__Support for Force Trackpads.__ JavaScript API allows you to listen for changes in the user’s force and when the user force clicks.

__New Design.__ Web Inspector has a tab-based design for easier tool access.

__Responsive Design Tool.__ Safari features a Responsive Design tool that makes it easier for you to create websites that are responsive to various widths.

__Type Profiler.__ Web Inspector supports a type profiler that annotates your JavaScript source with inferred type information, making it easier to debug.

__Code Coverage.__ Web Inspector provides a code coverage mode highlighting code that has been run, making it easier to see relevant code during debugging.

__Paint Indicator.__ Web Inspector has a paint indicator that flashes when elements get repainted, making it easier for you to improve responsiveness in your website by seeing if portions of the web page are painting too much.

__Frame Rendering Track.__ Web Inspector has a Rendering Frames track to see where a website is not getting 60 fps.

The following frameworks are no longer part of the OS X SDK as of version 10.11:

- __SharedFileList.__ Use `ServiceManagement.framework` instead.
- __VideoDecodeAcceleration.__ Use `VideoToolbox.framework` instead.

[Next](OS%20X%20Yosemite%20v10.10.md)[Previous](OS%20X%20El%20Capitan%20v10.11.2.md)

