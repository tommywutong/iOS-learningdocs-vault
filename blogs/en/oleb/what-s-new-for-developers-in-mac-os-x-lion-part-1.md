---
title: 'What''s New for Developers in Mac OS X Lion (Part 1)'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/07/whats-new-for-developers-in-lion-part-1/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:36bc048e85d1f7c1'
translated: false
---

> 原文：[What's New for Developers in Mac OS X Lion (Part 1)](https://oleb.net/blog/2011/07/whats-new-for-developers-in-lion-part-1/)　·　Ole Begemann

# What's New for Developers in Mac OS X Lion (Part 1)

Now that the final version of OS X Lion has reached the Mac App Store, let’s have a look at what is new for developers. And that is so much that I am going to split the news into three posts. Check out parts two and three after reading this post:

- Part 1: Major new features: Application persistence, automatic document saving, versioning, file coordination, Cocoa autolayout, full-screen apps, popover windows, sandboxing, push notifications.
- [Part 2](https://oleb.net/blog/2011/08/whats-new-for-developers-in-lion-part-2/): New frameworks: AV Foundation, Store Kit (in-app purchasing) and IMServicePlugIn. Changes in AppKit.
- [Part 3](https://oleb.net/blog/2011/08/whats-new-for-developers-in-lion-part-3/): Changes in Core Data, Core Foundation, Core Location, Foundation, QTKit, Quartz and Quartz Core.

What follows is a look at the major new developer features in Lion, more or less corresponding to the [What’s New in Mac OS X v10.7 Lion](http://developer.apple.com/library/mac/releasenotes/MacOSX/WhatsNewInOSX/Articles/MacOSX10_7.html#//apple_ref/doc/uid/TP40010355-SW5) document.

# Application Persistence

When a user logs out, Lion offers them the option to restore all open apps to their current state when logging back in. To support this feature in your app you must determine for each window whether its state should be preserved using the [`-setRestorable:`](https://developer.apple.com/reference/appkit/nswindow/1526255-isrestorable) method. Cocoa will then take care of saving the state (size, position, etc.) of your windows and their associated window controllers, giving you the option to write out additional state information of custom objects associated with the windows.

To restore your application’s state when it is relaunched, every window must specify a so-called _restoration class_ through the [`+restoreWindowWithIdentifier:state:completionHandler:`](http://developer.apple.com/library/mac/documentation/AppKit/Reference/NSWindowRestoration_protocol/Reference/Reference.html#//apple_ref/occ/intfcm/NSWindowRestoration/restoreWindowWithIdentifier:state:completionHandler:) class method (defined in the `NSWindowRestoration` protocol). The restoration class is then responsible for instantiating the window and its associated objects (such as the window controller). See the [User Interface Preservation](http://developer.apple.com/library/mac/documentation/General/Conceptual/MOSXAppProgrammingGuide/CoreAppDesign/CoreAppDesign.html#//apple_ref/doc/uid/TP40010543-CH3-SW26) topic in the Mac OS X Application Programming Guide for a step by step guide.

**Update August 29, 2011:** The [`enableRelaunchOnLogin`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSApplication_Class/Reference/Reference.html#//apple_ref/doc/uid/20000012-SW116) and [`disableRelaunchOnLogin`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSApplication_Class/Reference/Reference.html#//apple_ref/doc/uid/20000012-SW117) methods of `NSApplication` allow you to specify at runtime whether your application should be relaunched (for example, you would not want to relaunch if your app is an installer).

A related feature is [Automatic Termination](http://developer.apple.com/library/mac/documentation/General/Conceptual/MOSXAppProgrammingGuide/CoreAppDesign/CoreAppDesign.html#//apple_ref/doc/uid/TP40010543-CH3-SW27), giving the OS the option to quit your app automatically when it is not being used, just like on iOS. When your app supports automatic termination by setting the corresponding `Info.plist` key but does not restore its windows to the previous state when the system silently relaunches it, the user might think the app has crashed.

**Update August 29, 2011:** To dynamically enable or disable automatic termination depending on the state of your app, use the methods [`enableAutomaticTermination:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSProcessInfo_Class/Reference/Reference.html#//apple_ref/doc/uid/20000316-SW22) and [`disableAutomaticTermination:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/Foundation/Classes/NSProcessInfo_Class/Reference/Reference.html#//apple_ref/doc/uid/20000316-SW23) of the `NSProcessInfo` class.

# Automatic Document Saving and Versioning

Another major user-level feature of Lion is that users should not need to be concerned about losing unsaved changes or overwritten data anymore. If your app saves data to user-visible documents, users will expect it to support autosaving and versioning very soon. Fortunately, supporting this is pretty easy. If your app is [`NSDocument`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSDocument_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40004035)-based, you can add autosaving support by simply returning `YES` from the [`+autosavesInPlace`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSDocument_Class/Reference/Reference.html#//apple_ref/occ/clm/NSDocument/autosavesInPlace) method in your overridden document class.

And since all apps that support autosaving automatically support versioning as well, you’re already done. See [Documents Are Automatically Saved](http://developer.apple.com/library/mac/documentation/General/Conceptual/MOSXAppProgrammingGuide/DocumentBasedDesign/DocumentBasedDesign.html#//apple_ref/doc/uid/TP40010543-CH5-SW14) in the Mac OS X Application Programming Guide for more.

The save methods of `NSDocument` have been rewritten in Lion to perform their work on a background thread, thereby making all apps more responsive and making autosaving viable for an even greater number of apps, even if you work with very large documents. To enable this feature, return `YES` from [`-canAsynchronouslyWriteToURL:ofType:forSaveOperation:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSDocument_Class/Reference/Reference.html#//apple_ref/occ/instm/NSDocument/canAsynchronouslyWriteToURL:ofType:forSaveOperation:) and call [`-unblockUserInteraction`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSDocument_Class/Reference/Reference.html#//apple_ref/occ/instm/NSDocument/unblockUserInteraction) on the main thread as soon as your app has prepared an immutable snapshot of the document that can be saved (by default, the system will block the main thread to ensure that user actions do not cause the document to save an inconsistent state to disk).

Cocoa uses a new concept called file coordination to maintain sequential read and write access to the same file. This is an important part of the autosaving feature, ensuring that files remain in a consistent state even if accessed by multiple processes simultaneously. `NSDocument`-based applications use file coordination automatically.

**Update August 29, 2011:** If your app is not `NSDocument`-based, implementing autosaving and versioning involves quite a bit of extra work. To enable the OS to manage multiple processes accessing the same file (that potentially contains unsaved data), the objects that your app used to view or edit files must implement the [`NSFilePresenter`](http://developer.apple.com/library/mac/documentation/Foundation/Reference/NSFilePresenter_protocol/) protocol. At the same time, you must use instances of the [`NSFileCoordinator`](http://developer.apple.com/library/mac/documentation/Foundation/Reference/NSFileCoordinator_class/Reference/Reference.html#//apple_ref/doc/uid/TP40010585) class to read from and write to files. All file presenters need to register themselves with the `NSFileCoordinator` class.

To access existing version of a file or to create a new version, your app uses the [`NSFileVersion`](http://developer.apple.com/library/mac/#documentation/Foundation/Reference/NSFileVersion_Class/Reference/Reference.html) class.

# Cocoa Autolayout

This is one of the biggest new developer features. The familiar springs and struts model with autosizing masks has been with Cocoa developers since the very beginnings at NeXT, and OS X 10.7 is the first time Apple brings us something better:

> Instead of using autosizing masks, you define layout constraints that express your intent, such as “these views line up head to tail,” or “this plus/minus button segmented control should move with this split view subview.”

Each constraint is represented by an instance of `NSLayoutConstraint` attached to a view. The best thing: not only does Interface Builder support autolayout in Xcode 4.1, Apple has also developed a domain-specific language called the [Visual Format Language](http://developer.apple.com/library/mac/documentation/UserExperience/Conceptual/AutolayoutPG/Articles/formatLanguage.html#//apple_ref/doc/uid/TP40010853-CH3-SW1) which makes it dead easy to specify autolayout constraints in code with just a little bit of ASCII art that makes for very readable code.

[![Examples of the Cocoa Autolayout Visual Format Language syntax](https://oleb.net/media/cocoa-autolayout-format-syntax.png)](https://oleb.net/media/cocoa-autolayout-format-syntax.png)

<sub>Examples of the Cocoa Autolayout Visual Format Language syntax.</sub>

To enable autolayout in Interface Builder, open your `.xib` file and check the “Use Auto Layout” checkbox in the Identity inspector.

Apple lists the following advantages over autosizing masks:

> - Localization by just swapping strings, not adjusting layout in the majority of cases.
> - Mirroring of UI for right-to-left languages, such as Arabic and Hebrew.
> - Simpler expression of existing concepts in UIs.
> - Better layering of responsibility between view and controller layers.
> - Pixel-perfect layout at all scale factors with resolution independence.

For more information, check out the [Cocoa Autolayout Guide](https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/AutolayoutPG/).

[![Editing Cocoa Autolayout constraints in Interface Builder in Xcode 4.1](https://oleb.net/media/xcode-4-1-editing-autolayout-screenshot.png)](https://oleb.net/media/xcode-4-1-editing-autolayout-screenshot.png)

<sub>Editing Cocoa Autolayout constraints in Interface Builder in Xcode 4.1.</sub>

# Full-Screen Apps

Lion’s beautiful full-screen mode is off by default but it takes just one line of code to enable it in your app. Specifically, call [`-setCollectionBehavior:`] with the `NSWindowCollectionBehaviorFullScreenPrimary` flag on your main window. (By setting a window’s collection behavior to `NSWindowCollectionBehaviorFullScreenAuxiliary`, it can be shown on the same space as the fullscreen window; use this for secondary windows.). **Update:** You can also set the collection behavior in Interface Builder.

A window is taken into or out of fullscreen mode with the [`-toggleFullScreen:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSWindow_Class/Reference/Reference.html#//apple_ref/occ/instm/NSWindow/toggleFullScreen:) action. The [`NSWindowDelegate`](https://developer.apple.com/reference/appkit/nswindowdelegate) protocol was also extended by several new methods that inform the delegate about the entering and exiting of full-screen mode and allow it to set a custom [content size](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSWindowDelegate_Protocol/Reference/Reference.html#//apple_ref/occ/intfm/NSWindowDelegate/window:willUseFullScreenContentSize:) and [presentation options](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSWindowDelegate_Protocol/Reference/Reference.html#//apple_ref/occ/intfm/NSWindowDelegate/window:willUseFullScreenPresentationOptions:) for full-screen display. You can also customize the animation into and out of full-screen mode with the following methods:

- [`-window:startCustomAnimationToEnterFullScreenWithDuration:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSWindowDelegate_Protocol/Reference/Reference.html#//apple_ref/occ/intfm/NSWindowDelegate/window:startCustomAnimationToEnterFullScreenWithDuration:)
- [`-window:startCustomAnimationToExitFullScreenWithDuration:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSWindowDelegate_Protocol/Reference/Reference.html#//apple_ref/occ/intfm/NSWindowDelegate/window:startCustomAnimationToExitFullScreenWithDuration:)
- [`-customWindowsToEnterFullScreenForWindow:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSWindowDelegate_Protocol/Reference/Reference.html#//apple_ref/occ/intfm/NSWindowDelegate/customWindowsToEnterFullScreenForWindow:)
- [`-customWindowsToExitFullScreenForWindow:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSWindowDelegate_Protocol/Reference/Reference.html#//apple_ref/occ/intfm/NSWindowDelegate/customWindowsToExitFullScreenForWindow:)

The [`NSApplication`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSApplication_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40004004) instance includes the `NSApplicationPresentationFullScreen` flag in its [`-presentationOptions`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSApplication_Class/Reference/Reference.html#//apple_ref/occ/instm/NSApplication/presentationOptions) when an app is currently in full-screen mode.

# Popover Windows

Similar to `UIPopoverController` on the iPad, the `NSPopover` class lets you display additional content in a nice popover window. Popover take an `NSViewController` object that controls the contents of the popover window. The popover itself manages its position relative to a rectangle in a certain view (for example, a toolbar button’s frame).

Popovers can have a variable `appearance` (either `NSPopoverAppearanceMinimal` or `NSPopoverAppearanceHUD`) and `behavior`: a transient popover (`NSPopoverBehaviorTransient`) is closed automatically when the user interacts with any other UI element outside the popover. A semitransient popover (`NSPopoverBehaviorSemitransient`) is closed upon user interaction with the window containing the view the popover belongs to. If the automatic behaviors don’t suit your needs, set the behavior to `NSPopoverBehaviorApplicationDefined` to close the popover yourself at the appropriate times.

A popover can also have a [`delegate`](https://developer.apple.com/reference/appkit/nspopoverdelegate). One interesting delegate method is [`-detachableWindowForPopover:`](https://developer.apple.com/reference/appkit/nspopoverdelegate/1534822-detachablewindow). It allows you to detach a popover and convert it into a regular draggable window.

# Sandboxing

While Mac OS X will probably never be as locked down as iOS, Apple offers apps the ability to put themselves into an OS-controlled sandbox that limits their access to certain files and/or system services. This is a completely optional feature at the moment but one can be sure that proper self-sandboxing will sooner or later become a requirement for any app on the Mac App Store.

Enabling sandboxing is as easy as checking a few checkboxes in Xcode 4.1. By doing so, you restrict your app’s access to the file system and network, certain hardware components such as camera, microphone, USB ports and printer as well as privacy-sensitive APIs like the address book, calendar and location services.

[![Application Sandboxing settings in Xcode 4.1](https://oleb.net/media/xcode-4-1-sandboxing-screenshot.png)](https://oleb.net/media/xcode-4-1-sandboxing-screenshot.png)

<sub>Application Sandboxing settings in Xcode 4.1.</sub>

The operating system will enforce these restrictions while your app is running. To the user, this certainly means additional security and control, especially since Apple was smart enough to engineer sandboxing in such a way that it only takes effect in situations that have been initiated without any user interaction. Just because an app has no general access to the file system (apart from its own folder in `~/Library/Application Support`) does not mean that it cannot open any file from an arbitrary location on disk _as long as the user directly initiated that action._

At first glance, sandboxing sounds like a bad deal for developers since it means more work and your app can do less as a result. Apple tries to sell this to developers with the argument of higher security: if someone manages to compromise an app you developed, the potential damage it can cause on your users’ machines is limited.

# Push Notifications

Another feature that Lion got from iOS is Push Notifications. And they are implemented pretty much the same way. To enable your app to receive push notifications, call [`-[NSApplication registerForRemoteNotificationTypes:]`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSApplication_Class/Reference/Reference.html#//apple_ref/occ/instm/NSApplication/registerForRemoteNotificationTypes:) and implement the delegate methods [`-application:didRegisterForRemoteNotificationsWithDeviceToken:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSApplicationDelegate_Protocol/Reference/Reference.html#//apple_ref/occ/intfm/NSApplicationDelegate/application:didRegisterForRemoteNotificationsWithDeviceToken:) and [`– application:didFailToRegisterForRemoteNotificationsWithError:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSApplicationDelegate_Protocol/Reference/Reference.html#//apple_ref/occ/intfm/NSApplicationDelegate/application:didFailToRegisterForRemoteNotificationsWithError:). Your app is then responsible to submit the _deviceToken_ it received in the delegate method to your server that sends the notifications.

When your app receives a push notification while it is running, the system sends a [`-application:didReceiveRemoteNotification:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSApplicationDelegate_Protocol/Reference/Reference.html#//apple_ref/occ/intfm/NSApplicationDelegate/application:didReceiveRemoteNotification:) message to your application delegate where you can then handle the notification. Just like on iOS, the payload of the notification consist of up to 256 bytes of JSON.

Unlike on iOS, the system will not automatically launch your app if it receives a notification for you while the app is not running. Instead, it will just badge the app icon if the notification contains this information:

> the only supported notification type for non-running applications in Mac OS X is icon-badging

The next time the user launches your app, you can retrieve the notification’s contents from the _userInfo_ dictionary of the notification object that is passed to `applicationDidFinishLaunching:` using the key `NSApplicationLaunchRemoteNotificationKey`.

Read the _Local and Push Notification Programming Guide_ for details.

# What about iCloud?

Just like the entire [iCloud](http://www.apple.com/icloud/) service, the iCloud developer APIs are still in beta. iCloud will be released in the fall together with iOS 5 and will then also become part of Lion. Until then, iCloud is not part of the official Lion release.

# What about Automatic Reference Counting?

Maybe the biggest developer feature introduced at WWDC was [Automatic Reference Counting](http://clang.llvm.org/docs/AutomaticReferenceCounting.html), a new capability of the LLVM compiler to automatically insert `retain` and `release` calls into your application’s machine code, thereby essentially managing the memory for you. It’s even more of a deal for iOS since iOS does not support garbage collection, but will also be interesting to Mac developers.

ARC is a compiler-level feature and will be included in the upcoming LLVM 3.0 compiler. Xcode 4.1 for Lion currently ships with LLVM 2.1, which doesn’t support ARC. So while ARC is not available on Lion at the moment, it will be when Xcode 4.2 gets released, probably together with iOS 5 in the fall.
