---
title: What's New in macOS
apple_id: TP40001812
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/WhatsNewInOSX/Articles/MacOSX10_10.html
archived_at: '2026-07-18T02:58:47.663589Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [What's New in macOS](Introduction.md)


[Next](OS%20X%20Mavericks%20v10.9.md)[Previous](OS%20X%20El%20Capitan%20v10.11.md)

# OS X Yosemite v10.10

This article summarizes the key technology changes and improvements in OS X v10.10. For a detailed list of API changes, see _[OS X v10.10 API Diffs](https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/index.html#//apple_ref/doc/uid/TP40014444)_.

- [OS X Yosemite v10.10.3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobufvjvomzy) new features
- [OS X Yosemite v10.10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2diobufvjvomzw) new features

Please file any bug reports about this release or this documentation at [http://bugreport.apple.com/](http://bugreport.apple.com/).

AppKit contains new properties and methods that support Force Touch trackpads. Developers can now write apps that respond to force clicks (pressing harder) and changes in pressure as the user operates the trackpad. In the Calendar app, for example, a user can force click a date to create a new event. In QuickTime, a user can adjust the speed of fast forward and rewind with variable pressure.

Buttons and segmented controls can also now be set as spring loaded. This feature allows a user to activate a button or segment by dragging selected items over it and force clicking without dropping the selected items. The user can then continue dragging the items, possibly to perform additional actions. A practical example of this feature can be found in the Calendar app. A selected calendar event can be dragged over the Calendars button in the toolbar. Force clicking on the button displays the calendar list without releasing the selected event. The event can then be dropped onto a calendar in the list, which assigns it to that calendar.

The following sections highlight changes and enhancements in the AppKit framework that are related to Force Touch Trackpad support.

[NSButton](https://developer.apple.com/documentation/appkit/nsbutton) now includes the following new properties:

- [springLoaded](https://developer.apple.com/documentation/appkit/nsbutton/1532300-springloaded)—Indicates whether spring loading is enabled for the button.
- [maxAcceleratorLevel](https://developer.apple.com/documentation/appkit/nsbutton/1534413-maxacceleratorlevel)—Indicates the maximum number of discrete levels of pressure for a button of type [NSMultiLevelAcceleratorButton](https://developer.apple.com/documentation/appkit/nsmultilevelacceleratorbutton).

The [NSButtonType](https://developer.apple.com/documentation/appkit/nsbutton/buttontype) constant of [NSButtonCell](https://developer.apple.com/documentation/appkit/nsbuttoncell) now includes the following button types:

- [NSAcceleratorButton](https://developer.apple.com/documentation/appkit/nsacceleratorbutton)—When the user force clicks (applies pressure), an accelerator button sends repeating actions as pressure changes occur. It stops sending actions when the user releases pressure entirely.
- [NSMultiLevelAcceleratorButton](https://developer.apple.com/documentation/appkit/nsmultilevelacceleratorbutton)—A multilevel accelerator button is a variation of a normal accelerator button that allows for a configurable number of stepped pressure levels. As each one is reached, the user receives light tactile feedback and an action is sent.

The properties [phase](https://developer.apple.com/documentation/appkit/nsevent/1533550-phase) and [pressure](https://developer.apple.com/documentation/appkit/nsevent/1534543-pressure) now support pressure events.

[NSEvent](https://developer.apple.com/documentation/appkit/nsevent) now includes the following new properties:

- [stage](https://developer.apple.com/documentation/appkit/nsevent/1527242-stage)—Pressure events can go through multiple stages, each representing a pressure curve—not enough pressure for a click, enough pressure for a click, or more than enough pressure for a click (force click). This property indicates the current stage of the event.
- [stageTransition](https://developer.apple.com/documentation/appkit/nsevent/1526739-stagetransition)—This property is specifically intended to provide a value for the transition animation between the stages of a pressure gesture event.
- [associatedEventsMask](https://developer.apple.com/documentation/appkit/nsevent/1529610-associatedeventsmask)—This property pertains to mouse events, and may be used to determine if the input device issuing the event can simultaneously issue pressure events.

The [NSEventType](https://developer.apple.com/documentation/appkit/nsevent/eventtype) constant of `NSEvent` now includes an `NSEventTypePressure` event type.

The NSEventMaskFromType constant of `NSEvent` now includes an `NSEventMaskPressure` mask.

[NSGestureRecognizer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer) now includes a new method [pressureChangeWithEvent:](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/1527009-pressurechangewithevent), which is invoked when a pressure change occurs as the result of an event.

[NSResponder](https://developer.apple.com/documentation/appkit/nsresponder) now includes a new method [pressureChangeWithEvent:](https://developer.apple.com/documentation/appkit/nsresponder/1534071-pressurechangewithevent), which is invoked when a pressure change occurs as the result of an event.

[NSSegmentedControl](https://developer.apple.com/documentation/appkit/nssegmentedcontrol) now includes the following new properties:

- [springLoaded](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/1534122-isspringloaded)—Indicates whether spring loading is enabled for the control.
- [trackingMode](https://developer.apple.com/documentation/appkit/nssegmentedcell/1500200-trackingmode)—The type of tracking behavior the control exhibits.

`NSSegmentedControl` includes a new method [doubleValueForSelectedSegment](https://developer.apple.com/documentation/appkit/nssegmentedcontrol/1529727-doublevalueforselectedsegment), which returns the value of the selected segment when the tracking mode of the segmented control is set to [NSSegmentSwitchTrackingMomentaryAccelerator](https://developer.apple.com/documentation/appkit/nssegmentswitchtracking/nssegmentswitchtrackingmomentaryaccelerator).

The [NSSegmentSwitchTracking](https://developer.apple.com/documentation/appkit/nssegmentswitchtracking) constant of `NSSegmentedControl` now includes an [NSSegmentSwitchTrackingMomentaryAccelerator](https://developer.apple.com/documentation/appkit/nssegmentswitchtracking/nssegmentswitchtrackingmomentaryaccelerator) tracking type, which specifies that a segment should activate when the user force clicks it, send actions at repeating intervals or as changes in pressure occur, and deactivate when the user releases pressure entirely.

OS X lets you extend select areas of the system with an app extension, which is code that enables custom functionality within the context of a user task. For example, if you have an app for a great photo sharing service, you can provide an extension within your app so your service becomes available throughout OS X from the Share menu. In this example, your custom sharing extension provides the code that accepts, validates, and posts the user’s photos. The system lists the extension in the sharing menu and instantiates it when the user chooses it.

You create an app extension by adding an app extension target to an app. After users install an app that contains extensions, they can enable the extensions in System Preferences. When users are running other apps, enabled extensions can be made available in the appropriate system UI, such as the sharing menu.

OS X supports app extensions for the following areas, which are known as extension points:

- __Share__. Share content with social websites or other entities.
- __Action__. Perform a simple task with the selected content.
- __Today__. Provide a quick update or brief function in the Today view of Notification Center.
- __Finder Sync__. Enable services for custom file and sync providers.

Each extension point defines APIs that an app extension uses to communicate with the extension point. When you use an Xcode app extension template to begin development, you get a default target that contains method stubs and property list settings defined by the extension point you chose.

For more information on creating extensions, see _[App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214)_.

Handoff enables users to begin an activity on one device, then switch to another device and resume the same activity on the other device. For example, a user who is browsing a long article in Safari moves to an iOS device that's signed into the same Apple ID, and the same webpage automatically opens in Safari on iOS, with the same scroll position as on the original device. Handoff makes this experience as seamless as possible.

To participate in Handoff, an app adopts a small API in Foundation. Each ongoing activity in an app is represented by a user activity object that contains the data needed to resume an activity on another device. When the user chooses to resume that activity, the object is sent to the resuming device. Each user activity object has a delegate object that is invoked to refresh the activity state at opportune times, such as just before the user activity object gets sent between devices.

If continuing an activity requires more data than is easily transferred by the user activity object, the resuming app has the option to open a stream to the originating app. Document-based apps automatically support activity continuation for users working with iCloud-based documents.

For more information, see _[Handoff Programming Guide](../../../documentation/User%20Experience/Handoff%20Programming%20Guide/About%20Handoff.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dgmzy)_.

Starting in Xcode 6, you can use storyboards to lay out all the different views you will show your users, arranging them much like the storyboard for a movie. Each view, also called a _scene_, is connected to other views by transition or containment relationships known as _segues_. You specify a trigger for a segue in terms of an action such as a button click or a menu item choice.

Mac storyboards work much like iOS storyboards do, but with a greater focus on containment of views rather than transitions between them. For example, on the Mac you express the containment between a tab view controller and its tab scenes with containment segues.

Mac storyboards depend on capabilities provided by the new view controller classes [NSSplitViewController](https://developer.apple.com/documentation/appkit/nssplitviewcontroller)and [NSTabViewController](https://developer.apple.com/documentation/appkit/nstabviewcontroller), and enhancements to the [NSViewController](https://developer.apple.com/documentation/appkit/nsviewcontroller) and [NSWindowController](https://developer.apple.com/documentation/appkit/nswindowcontroller) classes. For more information, refer to the overview sections in the corresponding reference documents.

iCloud includes changes that impact the behavior of existing apps and that will affect users of those apps.

The iCloud infrastructure is more robust and reliable when transferring documents and data between user devices and the server. When a user installs OS X v10.10 and logs into the device with an iCloud account, the iCloud server performs a one-time migration of the documents and data in that user’s account. This migration involves copying the documents and data to a new version of the app’s container directory. This new container is accessible only to devices running OS X v10.10 or iOS 8. Devices running older operating systems will continue to have access to the original container, but changes made in that container will not appear in the new container and vice versa.

Cloud Kit (`CloudKit.framework`) provides a conduit for moving data between your app and iCloud. Unlike other iCloud technologies where data transfers happen transparently, Cloud Kit gives you control over when transfers occur. You can use Cloud Kit to manage all types of data.

Apps that use Cloud Kit directly can store data in a repository that is shared by all users. This public repository is tied to the app itself, so it’s available even on devices without a registered iCloud account. As the app developer, you can manage the data in this container directly and see any changes made by users through the Cloud Kit dashboard.

For more information, see _[Cloud Kit Framework Reference](https://developer.apple.com/documentation/cloudkit)_.

The following sections highlight changes to frameworks and framework technologies in OS X v10.10.

Many frameworks on OS X have adopted small interface changes that take advantage of modern Objective-C syntax:

- Getter and setter methods are replaced by properties in most classes. Code using the existing getter and setter methods should continue to work with this change.
- Initialization methods are updated to have a return value of `instancetype` instead of `id`.
- Designated initializers are declared as such where appropriate.

In most cases, these changes do not require any additional work in your own app. However, you may also want to implement these changes in your own Objective-C code. In particular, you may want to modernize your Objective-C code for the best experience when interoperating with Swift code.

For more information, see _[Adopting Modern Objective-C](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/ModernizationObjC/AdoptingModernObjective-C/AdoptingModernObjective-C.html#//apple_ref/doc/uid/TP40014150)_.

The following frameworks are new in OS X v10.10:

- __Crypto Token Kit__ (`CryptoTokenKit.framework`). The Crypto Token Kit framework provides native support for smart cards, including:

  - Enumerating connected smart card readers and monitoring them for card insertion and removal
  - Transmitting commands and responses to and from smart cards in the reader
  - Supporting new smart card reader hardware
- __FinderSync__ (`FinderSync.framework`). The FinderSync framework enables Finder extensions to:

  - Express interest in specific folder hierarchies
  - Provide "badges" to indicate the status of items inside those hierarchies
  - Provide dynamic menu items in Finder contextual menus, when the selected items (or the window target) are in those hierarchies
  - Provide a Toolbar Item that displays a menu with dynamic items (even if the selection is unrelated)
- __Hypervisor__ (`Hypervisor.framework`). The Hypervisor framework allows virtualization vendors to build virtualization solutions on top of OS X without needing to deploy third-party kernel extensions (KEXTs). Included is a lightweight hypervisor that enables virtualization of the host CPUs.
- __Multipeer Connectivity__ (`MultipeerConnectivity.framework`). The Multipeer Connectivity framework brings OS X to parity with iOS and allows cross-platform connections between devices running iOS 7, iOS 8, and OS v10.10.
- __Notification Center__ (`NotificationCenter.framework`). The Notification Center framework helps you create and manage extensions—typically called widgets—in the Today view. The framework provides an API you can use to specify whether a widget has content to display and to customize aspects of its appearance and behavior on both platforms. In OS X, the Notification Center framework also enables you to customize the editing and searching experience in a widget.

  For more information, see _[Notification Center Framework Reference](https://developer.apple.com/documentation/notificationcenter)_.

The following sections highlight changes and enhancements in the AppKit framework.

`NSWindowController` has a new `contentViewController` property that mirrors the `contentViewController` property of the associated window. An `NSWindowController` object that’s part of a storyboard is required to have a `contentViewController`—a requirement that the Xcode storyboard editor helps you to fulfill when you drag a window controller (`NSWindowController`) into the storyboard canvas.

`NSViewController` now has a suite of methods for presentation hooks:

- `viewWillAppear`
- `viewDidAppear`
- `viewWillDisappear`
- `viewDidDisappear`

See the header comments in `NSViewController.h` for more details.

`NSViewController` adds a `-viewDidLoad` method that can be overridden for instances that want to know when the view has been loaded in order to perform additional setup work.

`NSViewController` adds the following new features, all commented in great detail in `NSViewController.h`:

- Parent/child container view controller methods
- View controller presentation options
- View controller transition options

The new class `NSVisualEffectView` enables you to create translucent backgrounds and support vibrancy. `NSVisualEffectView` is automatically used by the system in many places, including `NSPopover` objects, `NSTableView` "source lists” and sidebars, and sheets. Please see the header for detailed information.

Gesture recognizers are now available in AppKit. The API is nearly identical to the UIKit version. See `NSGestureRecognizer.h`. There is a `NSGestureRecognizer (NSSubclassUse)` category that is explicitly provided for subclassers to override and call. Non-subclassers should never directly access these category methods and properties.

In Mac OS X v10.10, named images are now retained. Previously, named images had been weakly referenced, and sometimes cached. Retention allows applications to register a named image using `-[NSImage setName:]` and retrieve it later using `+[NSImage imageNamed:]`. To achieve the same pattern on prior releases, it was necessary to hold an extra reference to the image.

AV Foundation framework adds support for a broad cross-section of audio functionality at a higher level of abstraction than Core Audio. The new AV Foundation audio capabilities are available in both OS X and iOS and include a new API that allows manual control of the camera focus, white balance, and exposure settings. In addition, bracketed exposure captures allow automatic capturing of images with different exposure settings.

You can now capture metadata over time while shooting video. This capability allows arbitrary types of metadata to be embedded with a video recording at various points in time. For example, you might record the current physical location in a video created by a moving camera device.

Other new capabilities in AV Foundation include:

- Audio recording and playback
- Audio file parsing and conversion
- Audio units that allow for the creation of sound effects, filters, audio distortion, and reverberation effects
- Pitch and playback speed management
- A built-in equalizer and mixer that you can use in your applications
- Stereo and 3D audio environments
- MIDI compatibility
- Automatic access to audio input and output hardware

For information about the classes of this framework, see _[AV Foundation Framework Reference](https://developer.apple.com/documentation/avfoundation)_.

The Core Data framework (`CoreData.framework`) enables you to update multiple records in a store without first loading the record data into memory.

For information about the classes of this framework, see _[Core Data Framework Reference](https://developer.apple.com/documentation/coredata)_.

The Core Image framework (`CoreImage.framework`) includes the following changes:

- Accessing the second GPU in the Mac Pro is significantly easier. Use the `offlineGPUCount` method to find the number of GPUs that are not currently driving a display and can be used for image processing. Use the `offlineGPUAtIndex` method to create a `CIContext` based on an offline GPU index.
- You can use core image detectors to detect rectangles and QR codes in an image.

For information about the classes of this framework, see _[Core Image Reference Collection](https://developer.apple.com/documentation/coreimage)_.

The Core Location framework (`CoreLocation.framework`) now allows you to determine which floor the device is on if the device is in a multistory building.

For information about the classes of this framework, see _[Core Location Framework Reference](https://developer.apple.com/documentation/corelocation)_.

The following sections highlight changes and enhancements in the Foundation framework.

NSString adds an API that can be used to detect the string encoding of an array of bytes. This API is used to detect the string encoding of raw data and can also do lossy string conversion. It converts the data to a string in the detected string encoding.

The `NSDateIntervalFormatter` class is new in OS X v10.10. It’s used to format a date interval in a locale-sensitive way. A date interval is defined by two—for example, September 1st, 2013 - October 1st, 2013. In different countries and different regions, people use different languages and different formats to express a date interval. `NSDateIntervalFormatter` is designed to easily format a date interval into a localized string.

Foundation now provides localized formatting of durations and quantities of time using the new `NSDateComponentsFormatter` class. The header file `NSDateComponentsFormatter.h` is extensively commented with examples, information, and usage guidelines.

Three new unit formatters have been added in OS X v10.10: `NSMassFormatter`, `NSLengthFormatter`, and `NSEnergyFormatter`. These formatters can format a combination of a value and a unit into a localized string. They can also be used to get a localized string of a unit and to determine whether the unit is singular or plural, based on the given value. These formatters do not support either parsing or unit conversion.

In OS X v10.10, `NSXPCConnection` and `NSProgress` have been integrated to work together seamlessly. To receive progress updates from work done in another process, make an `NSProgress` object current before calling out to your `remoteObjectProxy` object. If the other side supports reporting progress, the `NSProgress` object in your process is updated as work is completed in the remote process.

`NSFileCoordinator` has a new reading option that facilitates uploading user documents to web services, such as web pages or mail servers, that only understand regular files and not file packages.

To use this API, request a coordinated read on any user document, the same that you would for normal reading, but use `NSFileCoordinatorReadingForUploading`. Before your accessor block is invoked, `NSFileCoordinator` determines whether the file is a directory. If it is, it creates a zip archive of that directory in a temporary folder that your app can access. If the file is not a directory, then it is copied to that directory. The URL to the newly created temporary file is accessible within your accessor block.

The Game Kit framework (`GameKit.framework`) has the following changes:

- Features that were added in iOS 7 are now available on OS X 10.10, making it easier to use these features in a cross-platform game.
- The new `GKSavedGame` class makes it easy to save and restore a user’s progress. The data is stored on iCloud; Game Kit does the necessary work to synchronize the files between the device and iCloud.
- Methods and properties that use player identifier strings are now deprecated. Instead, use [GKPlayer](https://developer.apple.com/documentation/gamekit/gkplayer) objects to identify players. Replacement properties and methods have been added that take [GKPlayer](https://developer.apple.com/documentation/gamekit/gkplayer) objects.

For information about the classes of this framework, see _[Game Kit Framework Reference](https://developer.apple.com/documentation/gamekit)_.

The Javascript Core Framework introduces APIs to expose and aid in debugging JavaScript in JavaScriptCore JSContexts and WebKit WebViews.

The Scene Kit framework includes several enhancements to support developing casual 3D games and apps with 3D content:

- __Integration with Sprite Kit.__ Use the [overlaySKScene](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1524051-overlayskscene) method to render a Sprite Kit scene above the 3D content in a Scene Kit view—this option is useful for adding a heads-up display to a game. You can also use Sprite Kit textures (see the [SKTexture](https://developer.apple.com/documentation/spritekit/sktexture) class) or entire animated scenes (see the [SKScene](https://developer.apple.com/documentation/spritekit/skscene) class) in Scene Kit materials, mapping their contents onto 3D objects.
- __Game development features.__ Use the [SCNAction](https://developer.apple.com/documentation/scenekit/scnaction) class for a declarative way to animate your scene (matching the [SKAction](https://developer.apple.com/documentation/spritekit/skaction) programming model in Sprite Kit). You can also use the [SCNAction](https://developer.apple.com/documentation/scenekit/scnaction) class to implement new methods in the [SCNSceneRendererDelegate](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate) protocol to manage your game’s scene graph in a traditional update/render loop.
- __Physics.__ Scene Kit physics simulation models the effects of forces and collisions on objects, and it updates the displayed node tree automatically. Use the [SCNPhysicsBody](https://developer.apple.com/documentation/scenekit/scnphysicsbody) class to add physics characteristics to nodes. Use the [SCNPhysicsWorld](https://developer.apple.com/documentation/scenekit/scnphysicsworld) object attached to your scene to control global attributes of the physics simulation.

  Advanced physics features include fields that apply forces to all bodies in their area of effect (see the [SCNPhysicsField](https://developer.apple.com/documentation/scenekit/scnphysicsfield) class); joints for connecting physics bodies (see the [SCNPhysicsBehavior](https://developer.apple.com/documentation/scenekit/scnphysicsbehavior) class); and vehicle behaviors that easily and efficiently simulate cars or similar vehicles (see the [SCNPhysicsVehicle](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle) class).
- __Visual effects and animations.__ Use the [subdivisionLevel](https://developer.apple.com/documentation/scenekit/scngeometry/1524177-subdivisionlevel) property on [SCNGeometry](https://developer.apple.com/documentation/scenekit/scngeometry) objects to create smooth surfaces from low-resolution geometry. The [SCNLight](https://developer.apple.com/documentation/scenekit/scnlight) class supports new shadow rendering options. The [SCNSkinner](https://developer.apple.com/documentation/scenekit/scnskinner) class can now create and edit skeletal animations for 3D models. The [SCNTechnique](https://developer.apple.com/documentation/scenekit/scntechnique) class enables you to build custom shader-based post-processing techniques such as color grading, motion blur, and screen-space ambient occlusion. The [SCNParticleSystem](https://developer.apple.com/documentation/scenekit/scnparticlesystem) class implements animated 3D particle effects that you can add to a scene, such as fireworks, smoke, and rain. Use the Scene Kit Particle System editor in Xcode 6 to experiment with particle system settings.
- __Asset management.__ All Scene Kit objects support the [NSSecureCoding](https://developer.apple.com/documentation/foundation/nssecurecoding) protocol, so you can save and restore entire scene graphs—including Scene Kit features such as physics, particle systems, and constraints—with the [NSKeyedArchiver](https://developer.apple.com/documentation/foundation/nskeyedarchiver) and [NSKeyedUnarchiver](https://developer.apple.com/documentation/foundation/nskeyedunarchiver) classes. Scene Kit can now load scene content from files in Alembic (ABC) format, used widely in the 3D authoring industry, in addition to existing support for reading and writing files in Digital Asset Exchange (DAE) format. Use `.scnassets` folders in Xcode 6 to optimize 3D assets for quick loading and smooth rendering at runtime.

In addition, the default behaviors of several Scene Kit classes change for apps built with the OS X v10.10 SDK or later:

- Animations loaded from scene files automatically play repeatedly using the system time. To change this behavior, use the [SCNSceneSourceAnimationImportPolicyKey](https://developer.apple.com/documentation/scenekit/scnscenesourceanimationimportpolicykey) option.
- Custom GLSL programs ([SCNProgram](https://developer.apple.com/documentation/scenekit/scnprogram)) are assumed to render opaque fragments. Use the [opaque](https://developer.apple.com/documentation/scenekit/scnprogram/1522844-opaque) property to tell Scene Kit when your program requires alpha blending.
- Lights that cast shadows use forward rendering. This option improves performance but disables shadow coloring. Use the [shadowMode](https://developer.apple.com/documentation/scenekit/scnlight/1522847-shadowmode) property to enable deferred shadowing (the default on OS X v10.9 and earlier).
- The default type for newly created lights is [SCNLightTypeOmni](https://developer.apple.com/documentation/scenekit/scnlighttypeomni).
- The [locksAmbientWithDiffuse](https://developer.apple.com/documentation/scenekit/scnmaterial/1462522-locksambientwithdiffuse) property of materials defaults to `YES`.
- The [shininess](https://developer.apple.com/documentation/scenekit/scnmaterial/1462533-shininess) property of materials no longer has a maximum of `1.0`.

Scene Kit is also available in iOS 8, so you can build cross-platform games or create custom tools for OS X to aid development of your own 3D games for iOS.

For information about the classes of this framework, see _[Scene Kit Framework Reference](https://developer.apple.com/documentation/scenekit)_.

The Sprite Kit framework (`SpriteKit.framework`) adds new features to make it easier than ever to support advanced game effects. These features include built-in support for custom OpenGL ES shaders and lighting, integration with Scene Kit, and support for advanced new physics effects and animations.

Xcode 6 also incorporates many new Sprite Kit editors, including shader and scene editors that save you time as you create your game. Create a scene’s contents, specifying which nodes appear in the scene and characteristics of those nodes, including physics effects. The scene is then serialized to a file that your game can easily load.

For information about the classes of this framework, see _[Sprite Kit Framework Reference](https://developer.apple.com/documentation/spritekit)_ and _[SpriteKit Programming Guide](../../../documentation/Graphics%20Animation/SpriteKit%20Programming%20Guide/About%20SpriteKit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbt)_.

The Store Kit Framework adds support to the In-App Purchases API for a deferred transaction—a transaction for which there is an indeterminate delay before the transaction reaches its final state of succeeded or failed.

The WebKit framework introduces a unified, extensible API for iOS and OS X and exposes the new underlying multiprocess architecture.

Periodically, Apple adds deprecation macros to APIs to indicate that those APIs should no longer be used in active development. When a deprecation occurs, it is not an immediate end of life for the specified API. Instead, it is the beginning of a grace period for transitioning from that API and to newer and more modern replacements. Deprecated APIs typically remain present and usable in the system for a reasonable time past the release in which they were deprecated. However, active development on them ceases, and the APIs receive only minor changes to accommodate security patches or to fix other critical bugs. Deprecated APIs may be removed entirely from a future version of the operating system.

As a developer, avoid using deprecated APIs in your code as soon as possible. At a minimum, new code you write should never use deprecated APIs. And if your existing code uses deprecated APIs, update that code as soon as possible. Fortunately, the compiler generates warnings whenever it spots the use of a deprecated API in your code. You can use those warnings to track down and remove all references to those APIs.

The following frameworks and APIs are deprecated in OS X v10.10:

- The IOAudioFamily framework
- Methods and properties in Game Kit that use player identifier strings
- The `NSGarbageCollector` class (execution support for garbage collection is not affected)
- The `NS_DEPRECATED_MAC` attribute has been added to many previously soft-deprecated AppKit methods. Searching AppKit headers for `NS_DEPRECATED_MAC` and filtering for 10_10 will yield a list of affected symbols.

The following frameworks are no longer part of the OS X SDK as of version 10.10:

- AppleShareClientCore
- RubyCocoa

Notable in OS X v10.10 are changes to Safari.

Safari includes a variety of enhancements, such as:

- __WebGL__. Safari support for WebGL allows developers to create 3D experiences that work natively in the browser.
- __IndexedDB__. The IndexedDB API allows web developers to store structured data for web applications that work online or require large amounts of data to be cached client side.
- __JavaScript Promises__. Safari enables JavaScript authors to more naturally work with asynchronous programming patterns.
- __CSS Shapes and Compositing__. Using CSS, websites can now easily flow text around images and geometry shapes, and perform image compositing operations on DOM elements.
- __SPDY__. Safari supports SPDY, an open networking protocol that websites can adopt to reduce page load latency and improve security.
- __HTML5 Premium Video__. Websites that provide video can now take advantage of EME to deliver encrypted, energy-efficient video in the browser.

Xcode 6 adds numerous features that support OS X v10.10, notably:

- __Swift.__ Swift is a new object-oriented programming language for iOS and OS X development. Swift is modern, powerful, expressive, and easy to use.
- __View debugging.__ The View Debugger makes debugging an app’s appearance as easy as debugging the lines of code. A single button click pauses your running app and “explodes” the paused UI into a 3D rendering, separating each layer of the stack of views. The View Debugger immediately shows why an image may be clipped and invisible, and the order of the graphical elements becomes clear.
- __Live rendering.__ Interface Builder displays your custom objects at design time, appearing as they do when your app is run. When you update the code for your custom view, the Interface Builder design canvas updates automatically with the new look you just typed into the source editor, with no need to build and run.
- __Performance testing.__ The enhanced XCTest framework now supports performance tests and an asynchronous testing API, fully integrated into both Xcode and Xcode Server. Asynchronous testing allows you to test code that is distributed in asynchronously executing blocks. With performance tests, you can quantify the performance of each part of an application.
- __Extensions support.__ Add an extension target to any iOS or OS X app to expose your app’s functionality more deeply in the OS. Xcode connects to the extension when launched, debugging the extension as it runs in the safe, embedded OS context.
- __Storyboards for OS X.__ Storyboards come to OS X with Xcode 6, taking advantage of the new View Controller APIs in App Kit. Storyboards make it easy to wire together multiple views quickly and define segue animations without writing code.

For more information about Xcode enhancements, see _[What’s New in Xcode](../../../documentation/Developer%20Tools/What%E2%80%99s%20New%20in%20Xcode/What%27s%20New%20in%20Xcode%209.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmrw)_.

[Next](OS%20X%20Mavericks%20v10.9.md)[Previous](OS%20X%20El%20Capitan%20v10.11.md)

