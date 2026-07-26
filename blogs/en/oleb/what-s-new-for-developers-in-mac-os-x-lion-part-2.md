---
title: 'What''s New for Developers in Mac OS X Lion (Part 2)'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/08/whats-new-for-developers-in-lion-part-2/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:e8585c76b6f62687'
translated: false
---

> 原文：[What's New for Developers in Mac OS X Lion (Part 2)](https://oleb.net/blog/2011/08/whats-new-for-developers-in-lion-part-2/)　·　Ole Begemann

# What's New for Developers in Mac OS X Lion (Part 2)

This is the second part of my overview of new developer APIs in Mac OS X Lion. Check out the other parts if you haven’t done so already:

- [Part 1](https://oleb.net/blog/2011/07/whats-new-for-developers-in-lion-part-1/): Major new features: Application persistence, automatic document saving, versioning, file coordination, Cocoa autolayout, full-screen apps, popover windows, sandboxing, push notifications.
- Part 2: New frameworks: AV Foundation, Store Kit (in-app purchasing) and IMServicePlugIn. Changes in AppKit.
- [Part 3](https://oleb.net/blog/2011/08/whats-new-for-developers-in-lion-part-3/): Changes in Core Data, Core Foundation, Core Location, Foundation, QTKit, Quartz and Quartz Core.

With 3,000 new and changed APIs in Lion, it doesn’t make sense to list them all. After all, many of the changes are small, such as the continued modernization of older APIs without fundamentally changing them.

For instance, in a process that has been going on since Leopard, Apple has turned informal protocols (implemented as categories on `NSObject`) into formal protocols. Examples of this in Lion are the new protocols [`NSURLConnectionDelegate`](http://developer.apple.com/library/mac/documentation/Foundation/Reference/NSURLConnectionDelegate_Protocol/Reference/Reference.html#//apple_ref/occ/intf/NSURLConnectionDelegate) and [`NSFileManagerDelegate`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSFileManagerDelegate_Protocol/Reference/Reference.html#//apple_ref/occ/intf/NSFileManagerDelegate) and many more.

The list of things that are actually _really_ new is still very long. In this post, I will cover a few new frameworks and some welcome changes in AppKit.

# New Frameworks

## AV Foundation

Ported from iOS to OS X, [AV Foundation](https://developer.apple.com/reference/avfoundation) is Apple’s new unified multimedia framework for both platforms. It is native 64-bit and supports full hardware acceleration. Going forward, Apple recommends AV Foundation over its older multimedia frameworks like QTKit:

> AV Foundation is the recommended API for all new development involving time-based audiovisual media, whether you are examining, creating, editing, manipulating, or reencoding audiovisual data. AV Foundation is also recommended for transitioning existing applications that were based on QuickTime or QTKit.

Read more in the [AV Foundation Programming Guide](http://developer.apple.com/library/mac/documentation/AudioVideo/Conceptual/AVFoundationPG/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40010188) and the [AV Foundation Framework Reference](https://developer.apple.com/reference/avfoundation). If you have already used AV Foundation in iOS, this will be very familiar territory.

## Store Kit

Another feature that originated on iOS and has now been ported to the Mac is In-App Purchasing. Apps that are distributed via the Mac App Store can sell additional functionality and/or content via the [Store Kit APIs](http://developer.apple.com/library/mac/#documentation/StoreKit/Reference/StoreKit_Collection/_index.html). Implementing in-app purchasing in a Mac app works exactly as it does in iOS. The [In App Purchase Programming Guide](http://developer.apple.com/library/mac/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008267) has all the details. Before you start working on this, [beware of the risk of being sued for patent infringement](https://fosspatents.blogspot.com/2011/05/lodsys-sues-7-app-developers-in-eastern.html), though.

## IMServicePlugIn

The new [IMServicePlugIn](https://developer.apple.com/reference/imserviceplugin) framework allows you to write plug-ins to make iChat work with additional instant messaging services that it does not support out of the box. The framework provides support for all essential IM features, including group chat and file transfers.

It also seems that not only iChat can profit from these plugins but other IM clients as well: the documentation provides information for both plug-ins and client applications on which protocols they have to implement to be able to work together.

An IM application that wants to support an IMService plug-in must implement the [`IMServiceApplication`](https://developer.apple.com/reference/imserviceplugin/imserviceapplication) protocol. It contains methods that the plug-in can call to inform the application when certain events have occured. The principal class of the plug-in offering the IM service must implement the [`IMServicePlugIn`](https://developer.apple.com/reference/imserviceplugin/imserviceplugin) protocol and handle stuff like logging the user in and out.

By implementing a number of other protocols that are all well documented, both the plug-in and the application can signal their (lack of) support for certain features like one-to-one IM ([`IMServicePlugInInstantMessagingSupport`](http://developer.apple.com/library/mac/documentation/AppleApplications/Reference/IMServicePluginInstantMessagingSupportRef/IMServicePlugInInstantMessagingSupport.html#//apple_ref/doc/uid/TP40009488), [`IMServiceApplicationInstantMessagingSupport`](http://developer.apple.com/library/mac/documentation/AppleApplications/Reference/IMClientInterfaceInstantMessagingSupportRef/IMServiceApplicationInstantMessagingSupport.html#//apple_ref/doc/uid/TP40009487)), presence information, group chats, file transfers, etc. The actual exchange of instant messages and other information then takes place through the methods implemented in these protocols. See the framework documentation for details.

**Update August 27, 2011:** Apple provides a sample IMServicePlugIn that implements the IRC protocol that should be useful if you want to write your own plug-in. See and download [IRCServicePlugIn](http://developer.apple.com/library/mac/#samplecode/IRCServicePlugIn/Listings/readme_txt.html). (via [Rafael Bugajewski on Twitter](https://twitter.com/chiefsucker/status/107077900771147776))

# AppKit Changes

AppKit is one of the most important frameworks for Mac developers, and it got a lot of new features in Lion. I already covered many of the higher-profile changes in [part 1](https://oleb.net/blog/2011/07/whats-new-for-developers-in-lion-part-1/), such as Cocoa Autolayout, Fullscreen Apps, Popover Windows and Application Persistence. Let’s look at some more:

### View-based Table and Outline Views

Continuing the adaptation of APIs that originated in iOS, both [NSTableView](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSTableView_Class/Reference/Reference.html#//apple_ref/occ/cl/NSTableView) and [NSOutlineView](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSOutlineView_Class/Reference/Reference.html#//apple_ref/occ/cl/NSOutlineView) now give you the option to use `NSView` objects as your table cells. The old `NSCell`-based style still works, of course.

The main reason for the existence of `NSCell` were performance considerations that were probably valid at the time of OS X 10.0. Nowadays, no halfway decent computer will have a problem compositing a table view that contains a few dozen subviews. Using views makes it much easier to design cells with complex UIs, specifically:

- Cells that change their layout when resized.
- Cells that contain multiple subviews to respond to multiple mouse events.
- Cells that display animations.

The full Interface Builder support for the new model helps a lot, too. View-based table views also support smooth animations for rows that are added and deleted from a table, just like `UITableView` on iOS.

Two new classes, [`NSTableCellView`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSTableCellView_Class/Reference/Reference.html#//apple_ref/occ/cl/NSTableCellView) and [`NSTableRowView`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSTableRowView_Class/Reference/Reference.html#//apple_ref/occ/cl/NSTableRowView) form the base of view-based table views. Read about [View-based table views in the Table View Programming Guide](http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/TableView/ViewBasedTables/ViewBasedTables.html).

### Scrolling and Gestures

Lion has not only changed the default scrolling direction, it also brought scrolling up to iOS standards (again) by hiding the scroll bars as well as adding scroll momentum and elasticty. `NSScrollView` supports all this out of the box, of course. It lets you control whether you want scroll elasticity in one or both directions ([`setHorizontalScrollElasticity`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSScrollView_Class/Reference/Reference.html#//apple_ref/doc/uid/20000341-SW6), [`setVerticalScrollElasticity:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSScrollView_Class/Reference/Reference.html#//apple_ref/doc/uid/20000341-SW8)). Make sure to test your app with both hidden and legacy scrollbars.

If you write your own code to interpret mouse events, `NSEvent` includes new data for scroll wheel momentum ([`momentumPhase`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSEvent_Class/Reference/Reference.html#//apple_ref/doc/uid/20000016-SW212)), and [`scrollingDeltaX`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSEvent_Class/Reference/Reference.html#//apple_ref/doc/uid/20000016-SW207) and [`scrollingDeltaY`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSEvent_Class/Reference/Reference.html#//apple_ref/doc/uid/20000016-SW208) now give you access to scroll wheel data in points instead of scroll wheel ticks. The [`hasPreciseScrollingDeltas`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSEvent_Class/Reference/Reference.html#//apple_ref/occ/instm/NSEvent/hasPreciseScrollingDeltas) gives you information how precise the data coming from the scroll wheel is.

The new method [`trackSwipeEventWithOptions:dampenAmountThresholdMin:max:usingHandler:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSEvent_Class/Reference/Reference.html#//apple_ref/doc/uid/20000016-SW214) lets you track swipe gestures beyond the end of the physical gesture until the completion of the UI animation that represents the swipe, essentially providing you with pre-calculated elasticity values that mimic the behavior of built-in scroll views.

### Animations

Before Lion, `NSView`-based animations lacked an often vital feature: without stepping down into Core Animation territory, it was not possible to react to the end of an animation. Thankfully, Lion corrects this oversight: [`NSAnimationContext runAnimationGroup:completionHandler:`](http://developer.apple.com/library/mac/documentation/cocoa/reference/NSAnimationContext_class/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004682-CH1-DontLinkElementID_2) lets you pass a block that is then executed when the animation has finished.

### Resolution Independence

In Lion, Quartz’s device-independent model has been extended to screens: screen size and window frames are now in points rather than pixels. **Update August 29, 2011:** As a result, the concept of a “base” coordinate system is no longer valid in Lion. The old conversion methods such as `convertPointToBase:` and `convertPointFromBase:` have been deprecated in favor of new methods such as [`convertPointToBacking:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSView_Class/Reference/NSView.html#//apple_ref/doc/uid/20000014-SW167) and [`convertPointFromBacking:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSView_Class/Reference/NSView.html#//apple_ref/doc/uid/20000014-SW168) to convert between points and backing store pixels. Many more apps should now work with resolution independence out of the box (though that does not have any practical implications until Apple starts to ship desktop or laptop “retina displays”).

Instead of going for true resolution independence as Apple had intended when it shipped Leopard, they seem to have settled on the iOS way: double the horizontal and vertical pixel counts of displays and have developers add `@2x` bitmap images to their apps. While obviously not as flexible, this simple model is easy for developers to adopt and avoids problems with graphics becoming blurry because they end up occupying fractional pixels. It won’t hurt if you already include `@2x` graphics in your app bundles.

**Update August 29, 2011:** See the [High-Resolution Operation Release Notes](http://developer.apple.com/library/mac/#releasenotes/GraphicsAnimation/RN-HiDPI/_index.html) for details on how to make your own app compatible with the HiDPI mode. The [AppKit Release Notes for Lion](http://developer.apple.com/library/mac/releasenotes/Cocoa/AppKit.html#10_7HighResolution) also have a good overview of the changes regarding resolution independence.

### NSTextFinder

Lion does away with the default modal Find panel and replaces it with a less obtrusive search and replace bar that appears at the top of a view. [`NSTextView`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSTextView_Class/) has built-in support for the new find bar ([`setUsesFindBar:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSTextView_Class/Reference/Reference.html#//apple_ref/occ/instm/NSTextView/setUsesFindBar:)).

To use it in other views, look at the [`NSTextFinder`](http://developer.apple.com/library/mac/#documentation/AppKit/Reference/NSTextFinder_Class/Reference/Reference.html) class. The class reference documentation contains a step-by-step guide how to integrate it into your own app. The object that manages the searchable text must implement the [`NSTextFinderClient`](http://developer.apple.com/library/mac/documentation/AppKit/Reference/NSTextFinderClient_Protocol/Reference/Reference.html#//apple_ref/occ/intf/NSTextFinderClient) protocol.

Matt Gemmell has written [a great post on the many capabilities of the find bar](http://mattgemmell.com/2011/07/24/find-patterns-in-text-on-lion) from a user’s perspective. Looks like a very useful class.

### Drag & Drop

Drag and drop has become more powerful in Lion. If you have dragged multiple files in the Finder, for instance, you may have noticed that dragged items flock together and can change their appearance during the drag. Apple calls this “icon drag flocking” and exposes the functionality to developers:

> Mac OS X v.10.7 introduces the notion of icon drag flocking. Drag flocking allows fine-grained control over icon dragging. The source application can change the image of the drag, as can the destination of the drag. When multiple items are dragged, they “flock” together into a stack.

Just like in many other places, drag and drop is another area that sees previously informal protocols being turned into formal ones in Lion. Unlike most other protocols, however, [`NSDraggingSource`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Protocols/NSDraggingSource_Protocol/) has not only been formalized but also features a significantly changed interface.

The new method that an `NSDraggingSource` must implement is [`draggingSession:sourceOperationMaskForDraggingContext:`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Protocols/NSDraggingSource_Protocol/Reference/Reference.html#//apple_ref/occ/intfm/NSDraggingSource/draggingSession:sourceOperationMaskForDraggingContext:) to declare the types of drag operations it allows. The arguments of that method are an instance of the new [`NSDraggingSession`](http://developer.apple.com/library/mac/documentation/AppKit/Reference/NSDraggingSession_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSDraggingSession) class and an [`NSDraggingContext`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Protocols/NSDraggingInfo_Protocol/Reference/Reference.html#//apple_ref/c/tdef/NSDraggingContext).

An `NSDraggingSession` represents the drag and drop operation and allows both the source and the target to modify the drag while it is happening. For example, we could set the session’s [`draggingFormation`](http://developer.apple.com/library/mac/documentation/AppKit/Reference/NSDraggingSession_Class/Reference/Reference.html#//apple_ref/occ/instp/NSDraggingSession/draggingFormation) to control whether the dragged items should flock into a pile, list or stack during the drag.

The dragging session also allows us to enumerate over all dragged items, each of them represented by an instance of the new [`NSDraggingItem`](https://developer.apple.com/reference/appkit/nsdraggingitem) class. Each dragging item has an array of [`imageComponents`](http://developer.apple.com/library/mac/documentation/AppKit/Reference/NSDraggingItem_Class/Reference/Reference.html#//apple_ref/occ/instp/NSDraggingItem/imageComponents) that are composited together by the system to create the actual drag image while the drag action is in progress. The items in the `imageComponents` array are instances of [`NSDraggingImageComponent`](http://developer.apple.com/library/mac/documentation/AppKit/Reference/NSDraggingImageComponent_Class/Reference/Reference.html#//apple_ref/occ/cl/NSDraggingImageComponent).

The dragging context specifies if a drag operation ends within or outside the application.

### Font Collections

The Font Book app lets users create collections of fonts. Before Lion, developers had to use the C-based [`CTFontCollection`](http://developer.apple.com/library/mac/documentation/Carbon/Reference/CTFontCollectionRef/Reference/reference.html#//apple_ref/doc/uid/TP40005104) API to access these collections. Now, [`NSFontCollection`](http://developer.apple.com/library/mac/documentation/AppKit/Reference/NSFontCollection_Class/Reference/Reference.html#//apple_ref/occ/cl/NSFontCollection) offers an Objective-C interface to the same information. The new class is nothing more than a wrapper for the `CTFontCollection` functions, though (not that there is anything wrong with such wrappers).
