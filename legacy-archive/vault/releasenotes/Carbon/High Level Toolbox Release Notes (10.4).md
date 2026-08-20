---
title: High Level Toolbox Release Notes (10.4)
apple_id: TP40001013
resource_type: Release Note
platform: macOS
topic: null
technology: null
published: '2006-01-10'
source_url: https://developer.apple.com/library/archive/releasenotes/Carbon/RN-HIToolbox/index.html
archived_at: '2026-07-18T02:50:21.969697Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# High Level Toolbox, HIServices, and NavigationServices Release Notes for Mac OS X v10.4

> [!IMPORTANT]
> 

For High Level Toolbox release notes for 10.3 and earlier, please refer to HIToolboxOlderNotes.

The High Level Toolbox is a subsystem of the Carbon framework for Mac OS X. It is composed of three frameworks: HIToolbox, HIServices, and NavigationServices. This document discusses changes in these three frameworks for Mac OS X 10.4.

#### Contents:

- [Features and Enhancements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Tips for Compatibility with Mac OS X 10.4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6oa)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6oi)
- [Version Checking](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjq)
- [Feedback](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjr)
- [General Changes to HIToolbox](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjs)
- [Accessibility](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjt)
- [Appearance Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mju)
- [Application Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mjy)
- [Carbon Event Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mrr)
- [Appearance Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mrv)
- [Application Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mrz)
- [Carbon Event Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mzs)
- [Dialog Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mzz)
- [Drag Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nbr)
- [Help Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nbt)
- [HIGeometry](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nbw)
- [HIObjects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nby)
- [HIShape](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6njr)
- [HIToolbar](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nju)
- [IBCarbonRuntime](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6njx)
- [Icon Services](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6njz)
- [Menu Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nrs)
- [Navigation Services](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nrx)
- [Process Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nzq)
- [Text Services Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nzs)
- [MLTE](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6nzu)
- [Universal Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6obt)
- [Window Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6obv)

### Features and Enhancements

The major new features in the HIToolbox, HIServices, and NavigationServices frameworks for Mac OS X 10.4 are:

- - HIObject archiving
- - Support for resolution independent windows and views (additional information is available in the "Carbon Resolution Independence Notes" release note)
- - Support for HIShape in the Control Manager
- - New features in MLTE: spell checking, font panel, typography panel, custom scrolling behavior, improved undo groups, read/write for CFURL
- - Improved Accessibility support across the toolbox
- - Improved window interaction in applications that use both Carbon and Cocoa windows
- - New HIView replacements for most Control Manager APIs (i.e. GetControl32BitValue -> HIViewGetValue).
- - Support for CGImage display in most controls
- - Per-window toolbar item state, and control over a toolbar item's selected and enabled appearance
- - New DataBrowser features, including alternating row colors
- - New API in Navigation Services to allow filtering by UTI, and support in Navigation Services dialogs for Spotlight searches
- - Carbon events to allow pre- and post-filtering of changes to editable Unicode text controls

### Tips for Compatibility with Mac OS X 10.4

### Carbon Event Manager

When a Mighty Mouse or scrolling trackpad on a 2005 PowerBook is in use, the kEventMouseWheel event is no longer posted to the event queue; the kEventMouseScroll event is posted instead. If you are looking in the event queue for kEventMouseWheel, you'll need to also check for kEventMouseScroll. See Q&A 1453 for more details.

The behavior of the AddEventTypesToHandler API has changed in Mac OS X 10.4 to match its behavior in 10.0 and 10.1. The intended behavior of this API has always been that handling of the new event types should be the same as if those event types were provided when the handler was originally installed. For example, if you do this:

- - insert handler 1 with event 1
- - insert handler 2 with event 2
- - add event 2 to handler 1

and then send event 2, then handler 2 should receive the event. That is what happens on 10.0, 10.1, and 10.4.

Unfortunately, in Mac OS X 10.2 and 10.3, the implementation of AddEventTypesToHandler was slightly broken, and the new types were not properly inserted into the handler table. Instead of being inserted at the same location as the existing handler, they were effectively inserted as if a new handler were installed with the additional types on top of any existing handlers. Therefore, on 10.2 and 10.3, handler 1 will receive the event, rather than handler 2.

In Mac OS X 10.4, we have corrected this problem and restored the proper behavior from 10.0 and 10.1. However, if you've never tested your application on 10.0 or 10.1, you may be inadvertently depending on this incorrect behavior in 10.2 and 10.3. We have only found one application with a dependency on the incorrect behavior, but if you use AddEventTypesToHandler, be aware of this change in behavior. If this change causes a problem for a shipping application, please file a bug in Radar and we will consider adding a workaround for that application.

### HIView Manager

The UserPane control no longer uses SetControlDataHandle to store its private per-instance data. We have noted that some applications are using GetControlDataHandle to access the UserPane control's private data handle on Mac OS X 10.3 and earlier releases. This practice has never been supported and will cause a crash on Mac OS X 10.4 since the data handle will be NULL. Do not access any undocumented data of any control; always use public accessor APIs or SetControlData tags.

Since the WWDC build, the HIScrollView control no longer automatically turns on the kHIScrollViewOptionsAllowGrow option bit when both the kHIScrollViewOptionsVertScroll and kHIScrollViewOptionsHorizScroll options are requested. This was done so the HIScrollView could independently auto-hide its horizontal and vertical scroll bars. When both scroll bars are requested, the allow grow option is not requested, and only one scroll bar is necessary, the HIScrollView will position the single scroll bar across/down the entire width (for horizontal scroll bars) or height (for vertical scroll bars) of the scroll view, which draws part of the scroll bar where the grow box would be if there were one. For maximum compatibility on all versions of Mac OS X, you should manually specify the kHIScrollViewOptionsAllowGrow option bit when you need the grow box space to be reserved.

If your application uses the HIViewRender API, we highly recommend that you only pass the root view of a window to this API. The behavior of this API when passed a non-root view was poorly defined in Mac OS X 10.3 and has changed in Mac OS X 10.4. In 10.3, calling this API on a non-root view would entirely validate all of the views in the window that intersect the specified view, including portions that did not intersect the specified view and so were not actually drawn. In 10.4, calling this API on a non-root view will only validate those portions of each view that intersect the specified view.

### Menu Manager

The menubar is now drawn into an actual WindowRef, and the menubar window appears in the window list. Since the menubar is generally the frontmost visible window, the GetFrontWindowOfClass API, which returns the frontmost visible window of a specified class, now generally returns the menubar window when passed the kAllWindowClasses constant, as does the GetWindowList API. If you are using GetFrontWindowOfClass(kAllWindowClasses) or GetWindowList() to find the frontmost document or dialog window, you should switch to the FrontNonFloatingWindow API (introduced in Mac OS 8.5) or the ActiveNonFloatingWindow API (introduced in CarbonLib 1.4 and Mac OS X 10.0). Note that even in previous versions of Mac OS X, there was no guarantee that a document or dialog window would be the frontmost visible window; you might also find a help tag, menu, or Text Services Manager bottom-line input window at the front of the window list.

For compatibility with existing applications, the FrontWindow API (which is also documented to return the frontmost visible window) always ignores the menubar window, and instead returns the frontmost visible window behind the menubar. Also, the GetFrontWindowOfClass and GetWindowList APIs have been modified to ignore the menubar window if the current application is either CFM, or mach-o but linked on a version of Mac OS X prior to 10.4. If you have a mach-o application, you should verify that your code can handle seeing the menubar window in the window list when you link on 10.4 or later.

### Window Manager

The Window Manager uses the kEventControlGetFrameMetrics event to determine the separation between a window's structure and content regions. This event is sent to a window's frame view. In previous versions of Mac OS X, this event was only sent once, at window creation time, and was not sent again. In Mac OS X 10.4, it is now sent whenever a window is resized, to allow the window's structure widths to change during resizing. This change may cause problems for custom window frame views that do not actually implement this event. In prior versions of Mac OS X, leaving this event unimplemented did not cause any problems, but in 10.4, leaving it unimplemented can cause a window to be resized incorrectly. If you implement a custom window frame view, be sure to handle kEventControlGetFrameMetrics and return appropriate values.

The Window Manager assumes that a custom window frame view will always create and embed a content view inside the frame view. In previous versions of Mac OS X, however, not creating a content view was usually not a fatal error; in certain cases the Window Manager would get errors while attempting to use the (non-existent) content view, but these errors were generally safely ignored. In Mac OS X 10.4, the Window Manager requires that a window must have a content view, and may crash if no content view is available. If you implement a custom window frame view, be sure to also embed a content view inside your frame view, and set its view ID to kHIViewWindowContentID.

The Window Manager now uses non-zero window levels for the standard modal, floating, and toolbar window groups. Some applications are already setting these window groups to use non-zero levels in prior versions of Mac OS X; such applications may need to be modified to stop doing this in 10.4, since it is no longer necessary. Do not assume that the standard window groups will use any particular value for their window levels.

When using the standard window event handler, a kEventCommandProcess event containing kHICommandSelectWindow will now be sent in response to all clicks in a window, even if the window is already active. Previously, this event would only be sent if the window was inactive. This change was made to ensure that the clicked window would always be z-ordered above other windows at the same window level, and fixes a common problem when using Cocoa windows in a Carbon application that caused Carbon windows to get stuck behind Cocoa windows. If you handle this command ID, do not assume that it will only be sent to inactive windows; behave appropriately if the window is already active (typically, by z-ordering the window, but probably not changing activation or focus).

The Window Manager on Mac OS X has always flushed the window buffers of all visible windows during any call to the event loop, including calls to the StillDown, WaitMouseUp, and EventAvail APIs. These APIs have historically been fast, light-weight calls, and the addition of flushing in the Mac OS X implementation has been considered a drawback by some applications. We hope to address this issue in a future release of Mac OS X by changing the behavior of these APIs, but there is no behavioral change in Mac OS X 10.4. For compatibility with future versions of Mac OS X, we recommend that you do not rely on StillDown, WaitMouseUp, or EventAvail causing a window flush. If your application has a tight loop that calls no event API except one of these three, which should be rare in a modern Carbon application, you can simply add an explicit call to QDFlushPortBuffer to flush the appropriate window.

The CoreGraphics framework in Mac OS X 10.4 has introduced a new behavior called “coalesced updates” that improves visual consistency and eliminates tearing during scrolling, animation, and video display. However, this change can also affect the performance of existing applications. We have made changes to HIToolbox to minimize the performance effect of coalesced updates, but you should evaluate your own application's behavior as well to determine if your application needs to change.

To understand coalesced updates, let's start with a brief overview of how the Mac OS X windowing system works. All application windows in Mac OS X are double-buffered; when an application draws to its window, the pixels that are modified are contained in a window buffer that is managed by CoreGraphics. The changes to the window buffer do not appear onscreen until the window is flushed. This happens automatically each time through the event loop for Carbon and Cocoa applications, and can be explicitly requested by calling the QDFlushPortBuffer API. The flushing operation itself is asynchronous: when HIToolbox, AppKit, or the application requests a flush via a call to CoreGraphics, the call returns immediately, allowing the application to continue execution, while CoreGraphics uses a separate thread of execution in the WindowServer process to gather the current contents of the window buffer and send it to video memory. This operation may also include sending the window buffer contents to the graphics card GPU if Quartz Extreme is enabled. If the application attempts to modify the window buffer while the flushing operation is still underway (for example, by calling a CoreGraphics API to draw to the window), then the application's call to CoreGraphics will block, stopping all execution of that application thread, until the flushing operation is complete. This prevents the application from modifying the window buffer while its contents are still being copied to video memory. The CoreGraphics team has always recommended that applications avoid writing to a window buffer immediately after requesting a window flush, because there was always a potential for the application to block, unable to proceed with its drawing thread, during the time from flush request to flush completion.

In previous versions of Mac OS X, a flush request made to CoreGraphics caused the flush to begin immediately. Therefore, there was generally a fairly short window of time between the flush request and the end of the flushing operation, and most applications did not spend a significant amount of time blocking while waiting for the flush to finish. In Mac OS X 10.4, however, CoreGraphics has changed the timing of flush operations. When a flush request is received by CoreGraphics, the window buffer is not immediately flushed; instead, all flush requests from all processes are coalesced together until the next display refresh, and then sent to the graphics hardware simultaneously. On a CRT display, the display refresh cycle occurs at the VBL interrupt rate; on an LCD display, the display refresh cycle always occurs at 60Hz. In this way, all flush requests occur in unison, which greatly improves visual appearance and eliminates tearing. However, deferring the flush request can significantly decrease the performance of an application that flushes a window and then immediately draws to the same window, because the delay from the flush request to the end of the flush operation is now much longer than on previous versions of Mac OS X; the delay is potentially up to one display refresh cycle length, or commonly 1/60th of a second.

For example, say you have an application which presents frames of animation on the screen. Your application can draw animation frames very quickly, in much less than 1/60th of a second. Your application has a main loop that simply draws a frame of animation, calls QDFlushPortBuffer, draws the next frame of animation, calls QDFlushPortBuffer, etc. In previous versions of Mac OS X, your drawing operation probably blocked a little bit while each flush completed, but not for very long, so you were able to draw many more than 60 frames of animation per second. However, since the display still refreshed at only 60 frames per second, not all of those animation frames were visible; only the last frame that was flushed prior to a display refresh was actually visible.

In Mac OS X 10.4, each flush request will be deferred until the next display refresh. Because your application immediately attempts to draw again after flushing, half of your drawing will block for almost the length of a display refresh cycle as well, until the previous flush request has been completed. Therefore, your application will be limited to drawing at the display refresh rate, and can never show more than 60 frames of animation per second.

The best approach for drawing on Mac OS X, which will optimize your drawing speed for both version 10.4 and prior versions, is twofold: don't draw more often than the refresh rate, and don't flush more often than the refresh rate. Drawing more often than the refresh rate, if each drawing operation replaces all of the area drawn by the previous operation, is pointless; only the last drawing operation prior to the refresh will be visible anyways, so drawing more than once per refresh is just doing unnecessary work. Flushing more often than the refresh rate is also pointless; again, only the last flush before the refresh will be visible, and flushing more often will just cause your application to block on its next drawing operation. This is true on both Mac OS X 10.4 and prior versions.

To improve application compatibility with coalesced updates, HIToolbox has changed its code that automatically flushes application windows on calls to the event system. Previously, any call to the event system that checked for new events would also cause all windows to be flushed. HIToolbox now throttles the frequency of window flushing to be no more than the refresh rate of the main display. The greatest impact from this change is seen when scrolling; without this change, Carbon application scrolling usually slows down significantly on Mac OS X 10.4, because each redraw of the window blocks on the previous flush operation and prevents the window from scrolling more often than the refresh rate. With this change, the application can redraw its window contents during scroll tracking multiple times per refresh cycle, and only the last redraw is flushed to the screen.

For best compatibility with existing applications, the CoreGraphics framework only enables coalesced updates for mach-o applications that are linked on Mac OS X 10.4 or later, and the HIToolbox change described above will only apply for such applications as well. All CFM applications, and mach-o applications linked on earlier versions of Mac OS X, will not use coalesced updates, and HIToolbox will flush on every call to the event loop. Therefore, you should not see any performance regressions due to coalesced updates in your existing applications on Mac OS X 10.4. However, you should examine your application for performance issues when you relink on 10.4, and ensure that you are not drawing or flushing faster than the display refresh rate. You can determine the refresh rate of the main display by calling the CGDisplayCurrentMode API, passing CGMainDisplayID(), and then getting the value of the kCGDisplayRefreshRate key from the dictionary returned by CGDisplayCurrentMode.

The QuartzDebug utility in /Developer/Applications/Performance Tools has new options in Mac OS X 10.4 that allow you to force coalesced updates on for all applications. You will find this to be useful when determining whether your existing application might have performance problems when it is relinked on 10.4 or later.

### Font Panel

The Font Panel window provided by Cocoa is now a true floating window, instead of a document window. In general, this improves the user experience when the user changes focus to the Font Panel; the active document window is no longer deactivated. However, if your application uses the Font Panel and has focusable content in your document window that is not implemented as a ControlRef or HIViewRef, you may need to use handlers for kEventWindowFocusAcquired/Relinquish on your window event target to detect when your window loses focus and to show that loss of focus in your content representation (for example, by turning off a blinking insertion point, or redrawing to remove a focus ring). The standard views provided by HIToolbox already respond to these events properly, and if you are only using standard text-editing views, you should already be compatible with Mac OS X 10.4.

### Known Issues

We have found a few problems in the High Level Toolbox frameworks since Mac OS X Tiger shipped. These bugs are known to exist:

In BBEdit, menu items that have submenus sometimes do not show the submenu triangle (4059804). This bug is fixed by Mac OS X 10.4.2.

Collapsing a window with a drawer, and then expanding the window again, will sometimes cause the drawer to detach from its parent window (the drawer no longer moves when the parent window moves). Also, sometimes when multiple windows with drawers are open, all of the parent windows can become grouped together so that they all move simultaneously (4060883). This bug is fixed by Mac OS X 10.4.2.

When a Navigation Services dialog is in column view, and the user press the command-up-arrow keyboard sequence to move upwards from a volume into the "Computer" column, the "Computer" column will get an extra volume entry and selection and highlighting of volumes will behave incorrectly (4065226). This bug is fixed by Mac OS X 10.4.2.

When mixing Carbon and Cocoa windows, sometimes a Cocoa panel window can be positioned at the wrong z-order relative to other Carbon windows. For example, this occurs in some Carbon applications when choosing Save to PDF in the Print dialog, then switching out to another app, then switching back to the original app (4068534). This bug is fixed by Mac OS X 10.4.2.

In some cases, menus that use custom menu content HIViews will incorrectly resize when the user moves the mouse into and out of the menu (4086478). This bug is fixed by Mac OS X 10.4.3.

When a control is destroyed, kEventControlDispose (and potentially other events, including kEventControlOwningWindowChanged) may be sent after kEventHIObjectDispose is sent (4055506). In prior versions of Mac OS X, kEventHIObjectDispose was the last event to be sent. This bug is fixed by Mac OS X 10.4.2.

Controls that are embedded inside a placard control using Interface Builder are not instantiated at runtime when the placard's window is loaded from the nib (4076443). This bug is fixed by Mac OS X 10.4.2.

Sending the AXPress accessibility action to an AXMenuBarItem does not cause the menu to open (4099617); instead, the Apple menu title is highlighted. This also prevents the Speech Recognition system from opening a menu when you speak its title. This bug is fixed by Mac OS X 10.4.3.

The user pane control is not setting the current port to the window's port before calling the user pane tracking procedure (4073540). This bug is fixed by Mac OS X 10.4.2.

HITextViews in composited windows can ignore mouse clicks in some cases (4137938). This bug is fixed by Mac OS X 10.4.3.

### Bug Reporting

We encourage all developers to file bugs found in Mac OS X 10.4 at <[http://bugreport.apple.com](http://bugreport.apple.com/)>. Duplicate bugs are not a problem; please don't hesitate to file a bug with the thought that "surely someone else must have found this already."

### Version Checking

On Mac OS X 10.3 and later, HIToolbox.framework exports a global variable, kHIToolboxVersionNumber, which contains the internal build number for the running version of HIToolbox. You can use this version number to check for bug fixes or feature changes in newer versions of HIToolbox. On Mac OS X 10.4, the build number was 219.0.

### Feedback

For feedback and comments about HIToolbox, HIServices, and Navigation Services APIs and features, you can email hitoolbox-feedback@group.apple.com. The intent of this address is to provide developers with a direct channel to the engineering team responsible for these technologies. We will read your input, and will try to acknowledge it, but we might not always have time for replies. Please use this address for feedback and comments on the APIs and features (for instance "please add QuickTime wrapper classes to HIToolbox" or "I need API to do this and that"), but not for support type questions (for instance, "I can't install OS X" or "How does one create a new bundle in Xcode?") or comments in other areas (for instance, "why is the dock centered in Aqua?"). We also highly recommend that you file feature requests in Radar, where you can more easily track our progress on your request.

### General Changes to HIToolbox

HIToolbox geometry types (HIRect, HIPoint and HISize) have been moved to their own header file, HIGeometry.h.

The following APIs are considered deprecated in Mac OS X 10.4 and later:

- IdleControls
- TXNSetViewRect
- TXNCanUndo
- TXNCanRedo
- TXNGetActionChangeCount
- TXNClearActionChangeCount
- TXNSetDataFromCFURLRef
- TXNFlattenObjectToCFDataRef
- TXNSave
- all TSMTE and TextEdit APIs

### Accessibility

Header files (HIServices): AXConstants.h, AXError.h, AXUIElement.h, AXValue.h

__Features and Enhancements__

The HICopyAccessibilityRoleDescription and HICopyAccessibilityActionDescription APIs allow access to the standard role and action descriptions provided by Mac OS X. These APIs are meant for use by custom views and other customized accessibility handlers.

The HIObjectSetAuxiliaryAccessibilityAttribute API allows associating an additional accessibility attribute with a HIObject or accessible subpart.

The HIObjectOverrideAccessibilityContainment API allows overriding the AXUIElementRefs that an HIObject would normally supply as the values of its AXParent, AXWindow, and AXTopLevelUIElement attributes.

The AXWindowMoved and AXWindowResized notifications are now sent only at the end of a window move or resize, rather than continuously while the window is moved or resized by the user (3371560).

The children of the AXMenuBar object are no longer AXMenus, but are now AXMenuBarItems. Each AXMenuBarItem has a single child, which is the AXMenu visible in the menubar.

The AXMenu accessible object no longer supports the AXTitle attribute, since in the accessibility hierarchy, the title of a menu is not displayed by the menu itself, but by another object, either an AXMenuBarItem or an AXMenuItem. The AXMenu object now supports the AXTitleUIElement attribute, which will point back to either an AXMenuBarItem or AXMenuItem object. AXMenuBarItem and AXMenuItem objects now support the AXServesAsTitleForUIElements attribute, which will point to the AXMenu that is a child of the item (3566815).

The AXUIElementCopyMultipleAttributeValues API has been added to allow copying multiple accessible attribute values at once (3213224).

The AXUIElementSetMessagingTimeout API has been added to allow control over the timeout of an accessibility request from a client to a target application (3439067).

The maxValues parameter of AXUIElementCopyAttributeValues may now be zero (2917089). In this case, an empty array is returned.

AXUIElementIsAttributeSupported on an element that doesn't support the given attribute now returns kAXErrorAttributeUnsupported instead of kAXErrorSuccess (3522115).

__Notable Bug Fixes__

A memory leak has been fixed that occurred in the target application whenever an observer was registered for a notification (3442856).

The kAXFocusedUIElement attribute of a Carbon application object is now returned correctly (3458791). If a menu is open, the attribute value will be the focused menu (3502735).

### Appearance Manager

__Header files (HIToolbox): Appearance.h, HITheme.h__

### Features and Enhancements

The HIThemeSetStrokeColor, HIThemeSetFillColor, HIThemeSetTextFillColor APIs have been added to allow setting the fill and stroke colors of a CGContextRef using a ThemeBrush, ThemePen, or ThemeTextColor.

The HIThemeTabPaneDrawInfo structure has been updated with new fields to allow drawing Panther-style tabs.

The kThemeBrushListViewOddRowBackground and kThemeBrushListViewEvenRowBackground theme brush constants have been added to provide the background of even and odd rows in list views that use an alternating row background color.

The kThemeBrushListViewColumnDivider theme brush constant has been added to provide the color of a column divider in a list view.

HIThemeBrushCreateCGColor has been added to allow translating a theme brush into a CGColorRef for use with Quartz.

New ThemeButton constants were introduced for use with HIThemeDrawButton. The added constants are: kThemePushButtonInset, kThemePushButtonInsetSmall and kThemeRoundButtonHelp.

HIThemeDrawSegment has been added to allow theme compliant segment drawing. Some supporting types and constants for HIThemeDrawSegment have also been added: HIThemeSegmentPosition, HIThemeSegmentKind, HIThemeSegmentSize, HIThemeSegmentAdornment and HIThemeSegmentDrawInfo. They are used to pass specifications to HIThemeDrawSegment.

### Implementation Changes

kThemeDisclosureButton has been renamed kThemeDisclosureTriangle to reduce confusion.

### Notable Bug Fixes

The HIThemeDrawTextBox API was previously limited to drawing text inside a 16-bit integer coordinate range, even though its text bounds parameter is a floating-point HIRect. This limitation has now been lifted. Text can be drawn at any coordinate expressible as a float.

### Application Manager

__Header file (HIToolbox): MacApplication.h__

### User Interface Changes

When using the kUIOptionAutoShowMenuBar option to SetSystemUIMode, the Menu Manager now requires that the mouse be moved into the top four pixels of the screen, and stay there for 0.15 second, before the menubar is shown. This should help to reduce problems with the menubar being unintentionally shown when there are other views at the top of a full-screen window.

### Notable Bug Fixes

When using any of the kUIOptionDisableProcessSwitch, kUIOptionDisableForceQuit, or kUIOptionDisableSessionTerminate options to SetSystemUIMode, the keyboard hotkeys for the following features are now automatically disabled (3972482):

- - Exposé
- - Dashboard
- - Display prefs
- - Dictionary popup

These hotkeys are automatically re-enabled when some other application becomes frontmost, or when the application that called SetSystemUIMode quits.

The window created by the HIAboutBox API is now automatically excluded from the standard window menu (3497812). Also, if no copyright information is provided, the static text item for the Copyright text is now automatically made invisible.

### Carbon Event Manager

__Header files (HIToolbox): CarbonEvents.h, CarbonEventsCore.h__

### Features and Enhancements

The PushSymbolicHotKeyMode, PopSymbolicHotKeyMode, and GetSymbolicHotKeyMode APIs have been introduced to allow applications to temporarily disable system-wide hotkeys. These APIs should be used with caution; applications should not turn off hotkeys except under very specific circumstances, when the user is clearly aware of the current mode. For example, an application might temporarily disable hotkeys while a user is entering a string of keystrokes in a keystroke macro generation dialog.

The CopyServicesMenuCommandKeys API provides a list of the command keys currently in use by the Services menu.

A new event, kEventWindowGetClickModality, is now sent by the event dispatcher and the Window Manager to determine whether a mouse event is blocked by a modal window. Previously, this determination was made by examining the modality of visible uncollapsed windows above the clicked window; this event now allows applications to customize the modality determination based on their own application state.

The following event parameter types are now retained when added to an EventRef:

- typeHIShapeRef
- typeMenuRef

The standard window handler, when it receives a kEventWindowActivated event, now sends a kEventWindowHandleActivate event; when the standard handler receives kEventWindowHandleActivate, it calls ActivateControl on the root control. This change was actually in Mac OS X 10.3 and later, but was not previously documented. There is also a kEventWindowHandleDeactivate event that is sent when kEventWindowDeactivated is received. Because kEventWindowActivated/Deactivated are sent with the SendToAllHandlers event dispatching option, it is impossible to prevent them from being received by the standard event handler. Some applications need to prevent the standard handler from activating or deactivating the window's contents in response to an activate or deactivate event, however; the new kEventWindowHandleActivate/Deactivate events are provided to support this.

The default application event handler and the default window event handler now support two new Carbon events, kEventAppFocusDrawer and kEventWindowFocusDrawer. These events are sent when the user presses the drawer-focus hotkey (currently cmd-option-`). The default window event handler responds to kEventWindowFocusDrawer by moving keyboard focus to the open drawer attached to the focused window, if any.

The basic window event handler now handles the kEventWindowFocusAcquired and kEventWindowFocusRelinquish events by forwarding these events to the focused control in the window. Previously, this behavior was only provided by the standard window event handler. Since Mac OS X 10.2, the Control Manager has handled these events by automatically invalidating the area covered by the control. In combination with changes to the standard views to only draw a focus ring if the control is in the user focus window, these changes allow text-editing views in a document window to automatically deactivate when the focus moves to a floating window or drawer (3472680).

Event routing for kEventClassCommand events sent to menus has changed. Previously, a command event (either UpdateStatus or Process) that was not handled by a menu would next be sent to the focused control in the user focus window. Events are now routed to the menu's parent menu (including the root menu, for menus that are inserted in the menubar). Only after the event has been sent to a menu that has no parent, which effectively means that it has reached either the root menu or the root of a popup menu hierarchy, is the event propagated to the user focus target.

Handling of command events with the kHICommandHide, kHICommandHideOthers, kHICommandShowAll, and kHICommandAppHelp command IDs now occurs in the default application event handler (3662186). Previously, these command IDs were handled by event handlers installed on the Application and Help menus, which made it more difficult for applications to customize the behavior of the App Help command, or to send a Hide/HideOthers/ShowAll command event manually and have it be handled by the OS.

The standard window event handler now detects Return, Escape, Cancel, and Cmd-Period text input that occurs in a drawer attached to a parent window that has a default or cancel button, and invokes the appropriate button (3706654). We have also provided a new HIView attribute, kHIViewAttributeIsFieldEditor, which must be used by developers to make this work properly; this attribute should be specified on any edit text controls in a drawer, so that the edit text control will ignore the Return and Enter keystrokes and allow these to be handled by the standard window handler. This happens automatically for edit text controls that are placed in the same window as a default button, but when the edit field is in a drawer and the default button is in the parent window, the edit control cannot detect this case automatically and must be assisted by the application.

ConvertEventRefToEventRecord can now convert a kEventControlTrack Carbon event to a mouseDown EventRecord.

The kEventMouseScroll event provides support for smooth scrolling, and is generated when a Mighty Mouse or a scrolling trackpad on 2005 PowerBooks is in use. See Q&A 1453 for more details.

### New and Improved Carbon Events

The following Carbon events are new for Mac OS X 10.4:

- -- Application

  - kEventAppFocusDrawer
- -- HIView Manager

  - kEventComboBoxListItemSelected
  - kEventSearchFieldSearchClicked
  - kEventTextShouldChangeInRange
  - kEventTextDidChange
  - kEventControlTrackingAreaEntered
  - kEventControlTrackingAreaExited
  - kEventClockDateOrTimeChanged
- -- HIObject Manager

  - kEventHIObjectEncode
- -- HIToolbar

  - kEventToolbarGetSelectableIdentifiers
  - kEventToolbarItemSelectedStateChanged
- -- User Input

  - kEventMouseScroll
- -- Text Services Manager

  - kEventTextInputFilterText
  - kEventTSMDocumentAccessGetBoundsForRange
- -- Window Manager

  - kEventWindowHandleActivate
  - kEventWindowHandleDeactivate
  - kEventWindowGetClickModality
  - kEventWindowSheetOpening
  - kEventWindowSheetOpened
  - kEventWindowSheetClosing
  - kEventWindowSheetClosed
  - kEventWindowFocusDrawer

### Notable Bug Fixes

The kEventWindowPathSelect event was unusable in all previous versions of CarbonLib and Mac OS X because the standard window handler did not retrieve the MenuRef from the event properly. Therefore, even if a handler for this event added a menu to the event, the menu would not be displayed. This bug is now fixed.

RunApplicationModalLoopForWindow no longer returns windowWrongStateErr if the process is hidden (3703740).

### Appearance Manager

__Header files (HIToolbox): Appearance.h, HITheme.h__

### Features and Enhancements

The HIThemeSetStrokeColor, HIThemeSetFillColor, HIThemeSetTextFillColor APIs have been added to allow setting the fill and stroke colors of a CGContextRef using a ThemeBrush, ThemePen, or ThemeTextColor.

The HIThemeTabPaneDrawInfo structure has been updated with new fields to allow drawing Panther-style tabs.

The kThemeBrushListViewOddRowBackground and kThemeBrushListViewEvenRowBackground theme brush constants have been added to provide the background of even and odd rows in list views that use an alternating row background color.

The kThemeBrushListViewColumnDivider theme brush constant has been added to provide the color of a column divider in a list view.

HIThemeBrushCreateCGColor has been added to allow translating a theme brush into a CGColorRef for use with Quartz.

New ThemeButton constants were introduced for use with HIThemeDrawButton. The added constants are: kThemePushButtonInset, kThemePushButtonInsetSmall and kThemeRoundButtonHelp.

HIThemeDrawSegment has been added to allow theme compliant segment drawing. Some supporting types and constants for HIThemeDrawSegment have also been added: HIThemeSegmentPosition, HIThemeSegmentKind, HIThemeSegmentSize, HIThemeSegmentAdornment and HIThemeSegmentDrawInfo. They are used to pass specifications to HIThemeDrawSegment.

### Implementation Changes

kThemeDisclosureButton has been renamed kThemeDisclosureTriangle to reduce confusion.

### Notable Bug Fixes

The HIThemeDrawTextBox API was previously limited to drawing text inside a 16-bit integer coordinate range, even though its text bounds parameter is a floating-point HIRect. This limitation has now been lifted. Text can be drawn at any coordinate expressible as a float.

### Application Manager

__Header file (HIToolbox): MacApplication.h__

### User Interface Changes

When using the kUIOptionAutoShowMenuBar option to SetSystemUIMode, the Menu Manager now requires that the mouse be moved into the top four pixels of the screen, and stay there for 0.15 second, before the menubar is shown. This should help to reduce problems with the menubar being unintentionally shown when there are other views at the top of a full-screen window.

### Notable Bug Fixes

When using any of the kUIOptionDisableProcessSwitch, kUIOptionDisableForceQuit, or kUIOptionDisableSessionTerminate options to SetSystemUIMode, the keyboard hotkeys for the following features are now automatically disabled (3972482):

- - Exposé
- - Dashboard
- - Display prefs
- - Dictionary popup

These hotkeys are automatically re-enabled when some other application becomes frontmost, or when the application that called SetSystemUIMode quits.

The window created by the HIAboutBox API is now automatically excluded from the standard window menu (3497812). Also, if no copyright information is provided, the static text item for the Copyright text is now automatically made invisible.

### Carbon Event Manager

__Header files (HIToolbox): CarbonEvents.h, CarbonEventsCore.h__

### Features and Enhancements

The PushSymbolicHotKeyMode, PopSymbolicHotKeyMode, and GetSymbolicHotKeyMode APIs have been introduced to allow applications to temporarily disable system-wide hotkeys. These APIs should be used with caution; applications should not turn off hotkeys except under very specific circumstances, when the user is clearly aware of the current mode. For example, an application might temporarily disable hotkeys while a user is entering a string of keystrokes in a keystroke macro generation dialog.

The CopyServicesMenuCommandKeys API provides a list of the command keys currently in use by the Services menu.

A new event, kEventWindowGetClickModality, is now sent by the event dispatcher and the Window Manager to determine whether a mouse event is blocked by a modal window. Previously, this determination was made by examining the modality of visible uncollapsed windows above the clicked window; this event now allows applications to customize the modality determination based on their own application state.

The following event parameter types are now retained when added to an EventRef:

- typeHIShapeRef
- typeMenuRef

The standard window handler, when it receives a kEventWindowActivated event, now sends a kEventWindowHandleActivate event; when the standard handler receives kEventWindowHandleActivate, it calls ActivateControl on the root control. This change was actually in Mac OS X 10.3 and later, but was not previously documented. There is also a kEventWindowHandleDeactivate event that is sent when kEventWindowDeactivated is received. Because kEventWindowActivated/Deactivated are sent with the SendToAllHandlers event dispatching option, it is impossible to prevent them from being received by the standard event handler. Some applications need to prevent the standard handler from activating or deactivating the window's contents in response to an activate or deactivate event, however; the new kEventWindowHandleActivate/Deactivate events are provided to support this.

The default application event handler and the default window event handler now support two new Carbon events, kEventAppFocusDrawer and kEventWindowFocusDrawer. These events are sent when the user presses the drawer-focus hotkey (currently cmd-option-`). The default window event handler responds to kEventWindowFocusDrawer by moving keyboard focus to the open drawer attached to the focused window, if any.

The basic window event handler now handles the kEventWindowFocusAcquired and kEventWindowFocusRelinquish events by forwarding these events to the focused control in the window. Previously, this behavior was only provided by the standard window event handler. Since Mac OS X 10.2, the Control Manager has handled these events by automatically invalidating the area covered by the control. In combination with changes to the standard views to only draw a focus ring if the control is in the user focus window, these changes allow text-editing views in a document window to automatically deactivate when the focus moves to a floating window or drawer (3472680).

Event routing for kEventClassCommand events sent to menus has changed. Previously, a command event (either UpdateStatus or Process) that was not handled by a menu would next be sent to the focused control in the user focus window. Events are now routed to the menu's parent menu (including the root menu, for menus that are inserted in the menubar). Only after the event has been sent to a menu that has no parent, which effectively means that it has reached either the root menu or the root of a popup menu hierarchy, is the event propagated to the user focus target.

Handling of command events with the kHICommandHide, kHICommandHideOthers, kHICommandShowAll, and kHICommandAppHelp command IDs now occurs in the default application event handler (3662186). Previously, these command IDs were handled by event handlers installed on the Application and Help menus, which made it more difficult for applications to customize the behavior of the App Help command, or to send a Hide/HideOthers/ShowAll command event manually and have it be handled by the OS.

The standard window event handler now detects Return, Escape, Cancel, and Cmd-Period text input that occurs in a drawer attached to a parent window that has a default or cancel button, and invokes the appropriate button (3706654). We have also provided a new HIView attribute, kHIViewAttributeIsFieldEditor, which must be used by developers to make this work properly; this attribute should be specified on any edit text controls in a drawer, so that the edit text control will ignore the Return and Enter keystrokes and allow these to be handled by the standard window handler. This happens automatically for edit text controls that are placed in the same window as a default button, but when the edit field is in a drawer and the default button is in the parent window, the edit control cannot detect this case automatically and must be assisted by the application.

ConvertEventRefToEventRecord can now convert a kEventControlTrack Carbon event to a mouseDown EventRecord.

The kEventMouseScroll event provides support for smooth scrolling, and is generated when a Mighty Mouse or a scrolling trackpad on 2005 PowerBooks is in use. See Q&A 1453 for more details.

### New and Improved Carbon Events

The following Carbon events are new for Mac OS X 10.4:

- -- Application

  - kEventAppFocusDrawer
- -- HIView Manager

  - Para
  - kEventComboBoxListItemSelected
  - kEventSearchFieldSearchClicked
  - kEventTextShouldChangeInRange
  - kEventTextDidChange
  - kEventControlTrackingAreaEntered
  - kEventControlTrackingAreaExited
  - kEventClockDateOrTimeChanged
- -- HIObject Manager

  - kEventHIObjectEncode
- -- HIToolbar

  - kEventToolbarGetSelectableIdentifiers
  - kEventToolbarItemSelectedStateChanged
- -- User Input

  - kEventMouseScroll
- -- Text Services Manager

  - kEventTextInputFilterText
  - kEventTSMDocumentAccessGetBoundsForRange
- -- Window Manager

  - kEventWindowHandleActivate
  - kEventWindowHandleDeactivate
  - kEventWindowGetClickModality
  - kEventWindowSheetOpening
  - kEventWindowSheetOpened
  - kEventWindowSheetClosing
  - kEventWindowSheetClosed
  - kEventWindowFocusDrawer

### Notable Bug Fixes

The kEventWindowPathSelect event was unusable in all previous versions of CarbonLib and Mac OS X because the standard window handler did not retrieve the MenuRef from the event properly. Therefore, even if a handler for this event added a menu to the event, the menu would not be displayed. This bug is now fixed.

RunApplicationModalLoopForWindow no longer returns windowWrongStateErr if the process is hidden (3703740).

### HIView Manager

__Header files (HIToolbox): HIView.h, Controls.h, ControlDefinitions.h__

Note that the HIView Manager was previously known as the Control Manager.

### Features and Enhancements

All standard views now support the HIArchive protocol. All subviews will be automatically archived with their parent if they support the archiving protocol.

The following views now support CGImageRef image content, specified using the ControlImageContentInfo structure (3567118):

- BevelButton
- DataBrowser ListView header
- ImageWell
- PushButton
- RoundButton
- Tab
- PopupButton (draws CGImage content attached to a menu item)

Note that HISegmentView has also supported CGImageRef content since its introduction in Mac OS X 10.3.

A new API, HICreateTransformedCGImage, allows creating a new CGImage from an original image while applying the standard selected or disabled appearance to the image. The toolbox uses this API internally when it needs to draw a CGImage in a selected or disabled state, so by using this API you can protect yourself from changes to the Mac OS X visual appearance. Note that you may find it useful for performance to cache the created image rather than recreating it every time you need it.

Several views now check whether their owning window is the user focus window to determine whether to draw a focus ring. This behavior was already present for many non-text-editing views in Mac OS X 10.3 and later; it is new in Mac OS X 10.4 for text-editing views, the DataBrowser, the ListBox, HIComboBox, and HISearchField. This change provides significant benefits in control behavior when focus moves from a document window to a floating window. Previously, if the focus was in an editable text control in a document window, and moved to a control in a floating window, the editable text control in the document window continued to show a blinking cursor, and to draw a focus ring, even though keyboard events no longer were received by the control. The editable text views now detect when their owning window loses focus, and in response, they cease to draw a focus ring and disable the blinking insertion point. These visual indicators are restored when the control's owning window regains focus.

New APIs and Carbon events have been introduced to support mouse tracking regions at the HIView level. We recommend use of these APIs when possible instead of the older MouseTrackingRegion APIs, as the older APIs only apply at the window level:

- HIViewNewTrackingArea
- HIViewChangeTrackingArea
- HIViewGetTrackingAreaID
- HIViewDisposeTrackingArea
- kEventControlTrackingAreaEntered
- kEventControlTrackingAreaExited

The HIView Manager implementation has been revised to use HIShapes instead of RgnHandles internally. The kEventControlGetPartRegion event has been enhanced to allow a view to report both RgnHandles and HIShapes; a view is often asked to report an HIShape, but is sometimes still required to report a RgnHandle instead. It is still always legal to report a RgnHandle even when the HIView Manager would prefer a shape. Providing the preferred data type is the only way to achieve optimal performance. See the header documentation for kEventControlGetPartRegion for more information. Note that the kEventControlCopyPartShape event previously introduced in Tiger has been withdrawn; it is no longer sent and has been removed from the headers. The kEventControlDraw event now has a kEventParamShape parameter which contains an HIShapeRef describing the area to be drawn; you should use this parameter if it is present.

New Carbon APIs and Carbon event parameters have been introduced to support HIShape-based view invalidation and painting:

- HIViewSetNeedsDisplayInRect
- HIViewSetNeedsDisplayInShape
- kEventParamShape/typeHIShapeRef

Two new HIShape APIs have been added, HIShapeCreateEmpty and HIShapeIntersectsRect.

The HIViewIsCompositingEnabled API has been introduced to indicate whether a view is currently drawing in composited mode. There are some cases, such as when a view is embedded into a Navigation Services dialog, when the view itself will not be drawing in composited mode even though the containing window is using compositing mode; this API will always return the actual mode of the view itself.

Two new Carbon events, kEventTextShouldChangeInRange and kEventTextDidChange, are sent by all Unicode-based editing views (HIComboBox, HISearchField, HITextView and EditUnicodeText). kEventTextShouldChangeInRange is sent before any editing operation changes the text in the view; applications can use this event to filter potential changes. kEventTextDidChange is sent after any editing operation changes the text in the view.

These new APIs were introduced so that fewer Control Manager APIs would have to be called with HIViewRefs:

- HIViewCopyShape
- HIViewCopyText
- HIViewCountSubviews
- HIViewGetCommandID
- HIViewGetEventTarget
- HIViewGetID
- HIViewGetIndexedSubview
- HIViewGetKind
- HIViewGetMaximum
- HIViewGetMinimum
- HIViewGetOptimalBounds
- HIViewGetValue
- HIViewGetViewSize
- HIViewIsActive
- HIViewIsEnabled
- HIViewIsLatentlyVisible
- HIViewIsValid
- HIViewSetActivated
- HIViewSetCommandID
- HIViewSetEnabled
- HIViewSetHilite
- HIViewSetID
- HIViewSetMaximum
- HIViewSetMinimum
- HIViewSetText
- HIViewSetValue
- HIViewSetViewSize

The HIViewCopyText and HIViewSetText APIs are notable for being more than simple replacements for Get/SetControlTitle. These new HIView APIs will first attempt to get the view's text using Get/SetControlData, and will fall back on the view's title if the view does not support the control data tag. This allows HIViewCopyText to return the text contained in an edit field, for example, and allows HIViewSetText to set the text of a static text control. Previously it was necessary to use Get/SetControlData to perform these tasks, which was a frequent source of confusion to developers.

An HIViewInstallEventHandler macro was also added to help install event handlers on HIViews.

A new HIView attribute, kHIViewAttributeIsFieldEditor, indicates that an edit text control should behave as if it were editing a field in a dialog and ignore metakeys such as Return, Enter, Escape, Tab, and Cmd-Period. This attribute is actually available in Mac OS X 10.3 as well, although not previously documented.

The HIComboBoxSetListVisible and HIComboBoxIsListVisible APIs allow control and access over whether the combo box list is currently visible.

The HIComboBox view now sends the kEventComboBoxListItemSelected event when the selection changes in the combo box list.

The HISearchField view now supports showing a search icon without an attached menu, via the kHISearchFieldAttributesSearchIcon attribute. When the search icon is clicked, the view now sends a kEventSearchFieldSearchClicked event.

The Clock control now sends the kEventClockDateOrTimeChanged event when the date or time of the control has been changed by the user.

HITextView now supports these standard ControlData tags: kControlEditTextCharCount, kControlEditTextSelectionTag, kControlEditTextCFStringTag, and kControlEditTextInsertCFStringRefTag.

The AXUIElementGetDataBrowserItemInfo and AXUIElementCreateWithDataBrowserAndItemInfo APIs allow customization of the accessibility information returned by a DataBrowser.

HIViewIsActive and HIViewIsEnabled can all optionally return latent state information. As a pre-existing API from Jaguar, HIViewIsVisible does not return the latent visibility of a view. HIViewIsLatentlyVisible has been added to check the latent visibility of a view.

The DataBrowser has several new features:

- - the kDataBrowserPopupMenuButtonless property flag is available for popup menu columns. This flag indicates that the popup will be drawn with a sleek buttonless appearance.
- - the DataBrowserGetAttributes and DataBrowserChangeAttributes APIs have been introduced to support various new attributes for controlling the appearance and behavior of a DataBrowser control.
- - the kDataBrowserAttributeColumnViewResizeWindow attribute indicates that the DataBrowser should automatically resize the containing window when columns are resized in column view.
- - the kDataBrowserAttributeListViewAlternatingRowColors attribute indicates that the DataBrowser should draw alternating row background colors in list view.
- - the kDataBrowserAttributeListViewDrawColumnDividers attribute indicates that the DataBrowser should draw a dividing line between columns in list view.
- - the DataBrowserGetMetric and DataBrowserSetMetric APIs have been introduced to allow control over the layout of a DataBrowser control.
- - the kDataBrowserListViewNoGapForIconInHeaderButton flag indicates that column headers in list view should not leave a gap for an icon if no icon is specified.

Subparts of Data Browser list view rows, such as disclosure triangles and checkboxes, are now accessible (3437725).

DataBrowser and HIToolbar now support kAXShownMenuUIElementAttribute and kAXShowMenuAction (3497544).

Most controls now support the kAXFocusedAttribute for accessibility (3456063). You cannot in general set the attribute's value to zero; the attribute is typically only used to focus something, not unfocus it. Therefore, some controls removed support for setting kAXFocusedAttribute to zero. To better match the accessibility design, some parts of a Data Browser control no longer support the kAXFocusedAttribute.

The standard controls now support the kAXTopLevelUIElementAttribute, which provides the top-level UI container for the control (3453287). This will be either the window that contains the control, or for controls in a sheet or drawer, the parent window of the sheet or drawer.

HISegmentedView is now accessible (3483191).

The AXRow objects returned by the DataBrowser in list view now support kAXIndexAttribute (3497181).

Disclosure triangle controls have a new role, kAXDisclosureTriangleRole (3502747). This role is also now returned by disclosure triangles in the DataBrowser.

DataBrowser's list view header buttons now report the kAXSortButton subrole (3502758).

The HIComboBox control now supports AXPressAction to open the list window and AXConfirmAction to close it (3521187).

The combo box button and group box label now support kAXWindowAttribute and kAXTopLevelUIElementAttribute (3526575).

HITextView is now much more accessible (3540460).

In list view, the DataBrowser's AXList object now supports kAXOrientationAttribute (3502740).

The AXWindow and AXEnabled attributes are now supported by the button and indicator elements of the scrollbar control (3453293).

The static text control now supports kControlSizeTag (3656845). Note that setting a custom font on the static text control with SetControlFontStyle will override the control's size; also, note that when the control is asked for its size with GetControlData and kControlSizeTag, it does not consult its custom font style to determine its size, so the control may return a size of kControlSizeNormal while still drawing text that is visually small if the control's font has been customized.

### Notable Bug Fixes

The popup button control and popup groupbox control on Mac OS X have had a long-standing behavioral difference from their classic Mac OS counterparts: when menu items are appended to the menu attached to one of these views, the menu items cannot be selected on the Mac OS X implementations of these views unless the developer manually sets the control maximum of the control to match the number of items in the menu. This difference is now removed. The popup button control now automatically sets its maximum value to be at least as large as the selected menu item index after the user has finished tracking the menu (2767230). Note that this maximum value may actually be greater than the number of items in the menu attached to the control, if the selected item was actually in a submenu that had a larger number of items.

HIViews were previously limited to drawing inside a 16-bit integer coordinate range, due to the use of QuickDraw regions in the HIView drawing pipeline. With the conversion of the HIView implementation to use HIShape, this limitation has now been lifted. HIViews can be invalidated and drawn at any integer coordinate expressible in a float. (Even though HIShapes can be built using HIRects [which are floating-point based], the internal storage for HIShapes only allows for integer coordinates.) Note that if a view limits its drawing to the invalid region contained in the kEventControlDraw event, it should use the HIShapeRef in the kEventParamShape parameter when running on 10.4, since the QuickDraw RgnHandle in the kEventParamRgnHandle parameter is still limited to 16-bit coordinates.

The popup button control now supports (draws) menu item icons that are specified using the kMenuCGImageRefType, kMenuSystemIconSelectorType, or kMenuIconResourceType constants.

The editable text of the HISearchField and HIComboBox controls will adjust their font size in order to provide the correct appearance to match the ControlSize of the control. This requires that the font of the editable text hasn't been overridden using the kControlUseFontMask or kControlUseFontIDMask masks of the ControlFontStyleRec.

Setting the kEventParamControlWouldAcceptDrop parameter to false or returning noErr with no kEventParamControlWouldAcceptDrop set from within a kEventControlDragEnter handler will now properly cause the HIView drag implementation not to send the remaining drag events. The only way to accomplish this in earlier systems was to return eventNotHandledErr instead. (3913427)

The following bugs in HISearchField's accessibility support have been fixed (3469892, 3487059):

- The search menu button and cancel button were reporting the Role, Role Description, and Parent attributes twice.
- The search menu button and cancel button didn't support the Focused, Enabled, Size, or Position attributes.
- The search menu button and cancel button didn't report the Press action.
- The control shouldn't return the focused attribute from itself (since its subcomponents are what is focused), and needed to deal with the focused child request.
- The control didn't accessibility hit test properly when inactive.
- The control reported an incorrect role.
- The control didn't report a subrole.
- The control didn't support the AXConfirm action.

The following controls no longer support the AXTitle attribute, since they do not have titles: disclosure button, disclosure triangle, icon, imagewell, picture, progress bar, scrollbar, and slider (3498128).

In column view, the rows in a DataBrowser now consider the column scroll position when hit-testing and reporting their bounds (3501831). This also affected a column's determination of its visible children.

### Dialog Manager

__Header file (HIToolbox): Dialogs.h__

### Features and Enhancements

A new option, kStdAlertDoNotCloseOnHelp, has been added to the CreateStandardAlert API. This option indicates that RunStandardAlert should not close the alert window when the user clicks on the Help button; this is intended to allow apps to display help in response to the button click while still leaving the alert open.

### Drag Manager

__Header file (HIToolbox): Drag.h__

HIRect, HIPoint and HISize definitions are now in HIGeometry.h

### Features and Enhancements

The kDragDoNotScaleImage option has been added to indicate that a drag image should not be scaled when the display scaling factor is not 1.0. By default, the Drag Manager will automatically scale drag images based on the display scaling factor; if your application is scaling-aware and has produced a drag image that is pre-scaled, you can use this option to ensure that the Drag Manager does not scale your image.

### Help Manager

__Header file (HIToolbox): MacHelp.h__

### Features and Enhancements

The HMHideTagWithOptions API has been added (2837257). This API allows hiding a help tag with optional fading and delay. The existing HMHideTag API is equivalent to HMHideTagWithOptions( kHMHideTagImmediately ).

For applications that use the CFBundleHelpBookFolder key in their Info.plist to request automatic Help menu support for their help book, the default application-level toolbox event handler for kEventRawKeyDown now opens the app's help book in response to the Help key. Applications that wish to provide their own behavior in response to the Help key, while still using the CFBundleHelpBookFolder key, should respond to the kEventRawKeyDown event using an event handler installed anywhere on the user focus target chain.

Help tag windows now use the kAXHelpTag role, send out the kAXHelpTagCreated notification when becoming visible, and the kAXUIElementDestroyed notification when becoming invisible (3439640). They don't advertise the kAXMain and kAXMinimized accessibility attributes. They now advertise the kAXTitle attribute. The application object no longer includes help tags in the contents of its kAXWindows attribute.

### Notable Bug Fixes

Help tags for views and windows are now displayed at a window level that is at least one greater than the window level of the owning window (3263349).

### HIGeometry

__Header file (HIToolbox): HIGeometry.h__

### Features and Enhancements

The HIGetScaleFactor API returns the default user interface scaling factor in use for this application. HIGetScaleFactor was previously named "HIGetUserSpaceScaleFactor" in the WWDC release of Mac OS X 10.4.

The HIPointConvert, HISizeConvert, and HIRectConvert APIs allow conversion between global pixel coordinates, global virtual (72-dpi) coordinates, window coordinates, and view coordinates.

### HIObjects

__Header file (HIToolbox): HIObject.h, HIArchive.h__

### Features and Enhancements

The HIObject Manager now supports the keyed archiving and unarchiving of HIObjects.

The archive format is the binary plist, the same as the AppKit keyed archive format introduced in Mac OS X 10.2. The binary plist format has several advantages over a text XML format. The binary plist format can be several times smaller than its text XML counterpart due to features such as string uniqueing (~3x in the case of some nibs converted to archives). This leads to quicker load times that are several times faster (~5x for a cold load and ~3x for a hot load for some nibs converted to archives). The binary plist format also contains a table of contents allowing the client to access one of many top level objects without having to traverse the entire text XML tree. The binary plist format actually does represent an XML format. The text XML can be converted from the binary archive using /usr/bin/plutil, but the performance characteristics will be lost.

The following new APIs and Carbon events have been introduced to support archiving:

- HIObjectIsArchivingIgnored
- HIObjectSetArchivingIgnored
- HIObjectCopyCustomArchiveData
- HIObjectSetCustomArchiveData
- HIArchiveGetTypeID
- HIArchiveCreateForEncoding
- HIArchiveEncodeBoolean
- HIArchiveEncodeNumber
- HIArchiveEncodeCFType
- HIArchiveCopyEncodedData
- HIArchiveCreateForDecoding
- HIArchiveDecodeBoolean
- HIArchiveDecodeNumber
- HIArchiveCopyDecodedCFType
- kEventHIObjectEncode

### Notable Bug Fixes

The Panther HIObject.h header file documented the idea of an abstract class, which is defined by passing NULL for the class construction proc when calling HIObjectRegisterSubclass, but the implementation had several bugs and did not actually work. These problems have been fixed and it is now possible to actually create an abstract HIObject class (3759687). When creating an abstract class, you are not required to pass an event list containing the required events to HIObjectRegisterSubclass; just pass NULL for the event list and 0 for the event count.

### HIShape

__Header file (HIToolbox): HIShape.h__

### Features and Enhancements

The HIShape implementation now uses a CoreGraphics object to represent the shape, rather than a QuickDraw region as in Mac OS X 10.2 and 10.3. Therefore, HIShapes can now cover the entire extent of the floating-point coordinate range specified by an HIRect, rather than just the 16-bit coordinate range expressible by a QuickDraw region.

### Notable Bug Fixes

On Mac OS X 10.2 and 10.3, the HIShapeUnion API incorrectly required that the result shape be immutable. On Mac OS X 10.4 and later, this API correctly requires that the result shape be mutable. If you need to run on both 10.4 and earlier releases, you will need to account for this difference (3509574).

### HIToolbar

__Header file (HIToolbox): HIToolbar.h__

### Features and Enhancements

The HIToolbarItemGetAttributesInWindow and HIToolbarItemChangeAttributesInWindow APIs have been added to allow overriding toolbar item attributes separately for each window containing a shared toolbar. Previously, a toolbar item's attributes affected the display of all toolbars in all windows containing that item. Using the InWindow APIs, a toolbar item's attributes may be individually modified for each window containing an item, so that, for example, a toolbar item may be enabled in one window and disabled in another window.

The kHIToolbarItemDisabled attribute has been added to control the enabled state of a toolbar item. HIToolbarItemSetEnabled is now simply a wrapper function that sets or clears the kHIToolbarItemDisabled attribute on the specified item.

The kHIToolbarItemSelected attribute has been added to control the selected state of a toolbar item.

The kEventToolbarItemSelectedStateChanged Carbon event has been added. This event is sent when the selected state of a toolbar item changes. The standard toolbar item view installs a handler for this event on the toolbar item so that it may invalidate itself.

The toolbar is also capable of automatically managing the selected item in a toolbar such that simply clicking on an item will select it. To enable this feature, a toolbar's delegate must implement the kEventToolbarGetSelectableIdentifiers event, returning an array of toolbar item identifiers that should be selectable. A click on an item with an identifier found in this array will automatic set the Selected attribute on that item. Selection state is maintained at the per-window level; a toolbar that is shared between multiple windows may have a different selected item in each window.

The HIToolbarGetSelectedItemInWindow API has been added to provide the toolbar item that is selected in a given window.

### Notable Bug Fixes

The Window Manager now sends kEventWindowBoundsChanging and kEventWindowBoundsChanged events when a window's toolbar is shown or hidden (3138687).

### IBCarbonRuntime

__Header file (HIToolbox): IBCarbonRuntime.h__

### Features and Enhancements

The IB Carbon runtime now has support for the following design-time features added to Interface Builder in Mac OS X 10.4:

- - placard and window header controls.
- - segmented controls
- - disclosure buttons
- - the QuickTime movie view
- - control text foreground colors
- - control text justification
- - the kWindowMetalNoContentSeparatorAttribute, kWindowFrameworkScaledAttribute, and kWindowApplicationScaledAttribute window attributes (new in Mac OS X 10.4)
- - the kWindowInWindowMenuAttribute and kWindowDoesNotCycleAttribute window attributes
- - the kHIViewAttributeSendCommandToUserFocus and kHIViewAttributeIsFieldEditor view attributes
- - window resizing limits
- - automatic window positioning based on display size when a window is loaded

### Icon Services

__Header file (HIServices): Icons.h__

### Features and Enhancements

Icons may now include 256x256-pixel JPEG-encoded image data. This data is identified by the kIconServices256PixelDataARGB constant in <OSServices/IconStorage.h>.

### Notable Bug Fixes

The PlotIconRefInContext API no longer depends on a valid current GrafPort. Previously, when drawing an IconRef that had been formed by compositing together two other IconRefs, PlotIconRefInContext use the current port's state while combining the source IconRefs, and the result was subject to colorization depending on the foreground and background colors of the current port.

### Menu Manager

__Header file (HIToolbox): Menus.h__

### Features and Enhancements

Menus now support the HIArchive protocol. All hierarchical submenus will be automatically archived with their parent upon archiving of the parent menu.

SetMenuItemCommandKey now supports the space character as a command key (3340478). Previously, it returned paramErr. Note that there is no visual representation of the space char in the menu; the command key is blank, but pressing space plus the appropriate modifiers will invoke the menu item.

All menu item parameters in Menus.h that were previously typed as "short" or "SInt16" have been changed to "MenuItemIndex", which is an unsigned 16-bit integer type. We have not observed any compiler errors or warnings as a result of this change, but if you find that it's causing significant compilation problems with your codebase, please let us know.

New menu item command key glyph codes have been added for the Eject, Kana, and Eisu keys. Earlier pre-release builds of Mac OS X 10.4 also contained a constant for the F16 glyph, but this constant has been removed from the final version of Menus.h as we were not able to get the F16 glyph into Lucida for Mac OS X 10.4. We expect to provide the F16 glyph in a future version of Mac OS X.

In Mac OS X 10.3 and earlier, the IsShowContextualMenuEvent API always returned false if the event kind was not kEventMouseDown, kEventWindowClickContentRgn, kEventWindowClickStructureRgn, or kEventWindowHandleContentClick. In 10.4 and later, this API no longer requires a specific event kind; it only requires that the event contain kEventParamMouseButton and kEventParamKeyModifiers parameters.

The AXPick action, previously supported by menu items for simulating a menu item selection, is now considered obsolete. It is no longer returned by the Menu Manager in the list of accessible actions supported by menu items. The AXPick action is still supported by menu items for backwards compatibility with existing applications, but we recommend that all accessibility client applications adopt the AXPress action, which has the exact same effect as AXPick.

The kAXSelectedChildren attribute of menus (3456994) and the menubar (3559767) is now settable. Note that the value passed to AXUIElementSetAttributeValue should be a CFArrayRef with one entry, and that entry should itself be an AXUIElementRef that refers to either (1) a menu item in the menu element passed as the first parameter to AXUIElementSetAttributeValue, if the attribute is being set on a menu, or (2) a menubar item in the menubar element passed as the first parameter to AXUIElementSetAttributeValue, if the attribute is being set on a menubar.

A new accessible attribute, AXMenuItemPrimaryUIElement, is now supported by menu items (3466268). This attribute only has a value for menu items that are dynamic (i.e., have kMenuItemDynamicAttribute). For dynamic items, this attribute returns the AXUIElementRef identifying the primary menu item in the dynamic group, which is the item that has the fewest command key modifiers. Essentially, this is the item that will be shown when the menu is displayed if the user is not pressing any modifier keys.

The AXPick action is now considered obsolete (3466830). Any use of this action should be changed to use the AXPress action instead; the Press action is implemented in exactly the same way as the Pick action, on all releases of Mac OS X that support accessibility. The Pick action is no longer returned by the Menu Manager as an available action, but the implementation remains present for compatibility with existing applications.

Invoking the cancel action on a menu now only closes that menu, and any of its submenus that were showing (3473583). If you want to cancel all menu tracking, you should AXCancel the menu bar.

kAXFocusedUIElementChanged is no longer sent when the selected menu item changes; instead, we now send kAXSelectedChildrenChanged to the menu itself (3526865). Also, we now send kAXFocusedUIElementChanged when the mouse moves into a different menu, or into the menubar.

The AXMenuBarItem object now supports kAXSelectedAttribute (3559768).

The AXMenuBarItem object and the AXMenuItem object no longer support the kAXVisibleChildren and kAXSelectedChildren attributes (3566679).

The kAXTitle attribute for a separator menu item is now always an empty string; previously, it was sometimes an empty string and sometimes a dash (3536623).

For menu items that have only a command key glyph and no command key character or virtual key, the Menu Manager now attempts to convert the glyph to a character code when asked for the kAXMenuItemCmdChar attribute (3562396). Note that this will not always succeed; some glyphs cannot be converted to character codes. For best behavior, an accessibility client should access the glyph code and be prepared to interpret it.

### User Interface Changes

The Aqua Human Interface Guidelines for Mac OS X 10.4 have changed in regard to the enabling of menu titles. Previous guidelines recommended that a menu title be disabled if all items in the menu are disabled. The new guidelines instead recommend that menu titles should always be enabled, to indicate that the menu is always browseable, even if all items in the menu are disabled. To support this new guideline, we have made these changes:

- - menu titles are always drawn with an enabled appearance, even if the menu title (item 0) of the menu is disabled
- - the kMenuAttrAutoDisable menu attribute no longer has any effect; the title of a menu with this attribute is no longer disabled automatically if all items in the menu are disabled
- - the Menu Manager no longer sends kEventMenuEnableItems events at idle time to menus in the menubar (although this may return in the future once we support tear-off menus, which will require idle-time enabling).

Note that it is still possible to explicitly disable a menu's title using DisableMenuItem(menu, 0), and that this will still affect the availability of the menu items in the menu for purposes such as command key matching. Disabling the menu title is still a legitimate way to quickly disable all of the items in the menu, and the items will still be drawn with a disabled appearance; only the menu title will be drawn enabled.

The Menu Manager now detects when the frontmost application is deactivated and a UIElement app is activated, and in response, disables most items in the previously frontmost app's menus. The previously frontmost app's menus are still accessible to the user, since the active UIElement application does not have access to the menubar, but the menu items are unlikely to behave as the user expects since the app has been deactivated. The app's menu items will be re-enabled when the application becomes active again. It is possible to selectively enable menu items in this situation using a kEventMenuEnableItems event handler installed anywhere on the menu event chain, or by using a kEventCommandUpdateStatus handler installed on the menu itself. A kEventCommandUpdateStatus handler installed on a control, window, or application target will not be called in this situation; the handlers installed by the Menu Manager will receive the event first and handle it.

It is now possible to type-select a menu title in the menubar. This feature is enabled when you use the Focus on Menubar hotkey (by default, Control-F2) to place keyboard focus on the menubar. In previous releases of Mac OS X, this would cause the Apple menu to open, and keystrokes would select items in the Apple menu. In Mac OS X 10.4, this mode now begins with just the Apple menu title hilited, but without opening the menu. Typing the name of a menu title will select it, but will not open the menu; pressing the Space, Return, Enter, or down arrow keys will open the hilited menu. Once a menu has been opened, typing will select items in the open menu, as in previous versions of Mac OS X; pressing the Focus on Menubar hotkey while a menu is open will close all open menus and return you to menubar type-selelection mode.

When opening a popup menu control, the checked menu item is now initially selected, so you don't have to start from the first item when using the keyboard to change the selection.

If a menu item with a submenu is hilited during keyboard navigation, the Space, Return, and Enter keys will now open the submenu. Previously, they caused the menu to close.

The Menu Manager has slightly different behavior when VoiceOver is active:

- all dynamic menu items are made visible simultaneously. This allows users with visual disabilities to more easily see which menu items are available.

- menu keyboard navigation now allows disabled menu items to be hilited. This makes keyboard navigation more usable for users with visual disabilities. The user cannot actually invoke a disabled item, only hilite it; pressing Space, Return, or Enter while a disabled item is hilited will simply close the menu.

### Implementation Changes

The Menu Manager now uses an HIView to draw the menubar. The menubar itself is now contained in a WindowRef, which is present in the window list (usually, it is the topmost visible window in the window list).

During user command key substitution, the dictionary keys and menu item text are now normalized (NFKC), which in practice means that you can type either three periods or an ellipsis into the Keyboards pref pane to identify a menu item, and either style will work with any menu item (3358528).

In previous versions of Mac OS X, the Menu Manager would send a kEventMenuEnableItems event to a menu during command key matching before checking if any submenus of that menu contained a menu item matching a command key event. If the parent item of the submenu was disabled, the Menu Manager would not search the submenu. However, this only occurred if the command key cache was not valid; if the command key cache was valid, the Menu Manager would find the matching item in the submenu directly, would never send kEventMenuEnableItems to the parent menu, and would ignore the enable state of the parent item. To improve performance during command key matching when the command key cache is not valid, on Mac OS X 10.4 the Menu Manager no longer sends a kEventMenuEnableItems event to a menu that does not itself contain any matching menu items prior to searching submenus of that menu, and does not check the enable state of a parent menu item before searching the item's submenu. Since this behavior was already in effect for command key matching when the command key cache was valid, we don't expect it to cause any compatibility problems (3334051).

In previous versions of Mac OS X, the Menu Manager would send a kEventMenuEnableItems event to a menu during command key matching before sending a kEventMenuMatchKey event to that menu. This caused a significant performance degradation for menus that used kEventMenuMatchKey. In Mac OS X 10.4, the Menu Manager no longer sends a kEventMenuEnableItems event before sending kEventMenuMatchKey; it is now up to the event handler for kEventMenuMatchKey to determine whether the item should be enabled at that instant, and respond appropriately. This should make it much more feasible to use kEventMenuMatchKey (3345312).

### Notable Bug Fixes

The kAXMenuItemMarkChar attribute is now correctly returned when the mark char is a low-ASCII special character such as the checkmark (3438773).

When the position or size of a hidden menu item are queried, the Menu Manager now returns kAXErrorNoValue (3461953).

If kAXPressAction is invoked on a menubar item during menu tracking, the target menu now opens and menu tracking continues (3561240). Previously, the target menu would open, immediately close, and menu tracking would end.

If a menu with a menu ID of zero is passed to ContextualMenuSelect, and item three is selected, the value returned in the outUserSelectionType parameter is now correctly set to kCMMenuItemSelected (3687409). Previously, it would be set to kCMShowHelpSelected. You can work around this bug on previous versions of Mac OS X by using a non-zero menu ID for contextual menus. Note that when a new menu is created in InterfaceBuilder, its ID is automatically set to zero.

### Navigation Services

__Header File: Navigation.h__

### Features and Enhancements

The NavDialogSetFilterTypeIdentifiers API allows filtering the available files in a dialog against a list of Uniform Type Identifiers in GetFile or ChooseFile dialogs. This function can be called at any time during the dialogs existence and the file browser will update accordingly. The Uniform Type Identifier's display names will be added to the Enable popup allowing the user to filter the file browser contents manually.

The Navigation Services dialog now supports searching with Spotlight in a similar way to the Finder search user interface.

### Notable Bug Fixes

Sorting by modification date sometimes failed when viewing the contents of an AFP volume (3467302).

The presence or absence of an event proc is no longer used to enable certain features, including drag&drop support, modality, and resizability (3846988). These features are now all enabled by default.

When a new file type was chosen from the file type filter popup menu, filenames were not redrawn to indicate which files were now available or unavailable (3968398).

### Process Manager

__Header file (HIServices): Processes.h__

### Notable Bug Fixes

WakeUpProcess previously did not actually wake the process when called from any thread other than the main thread (3437206).

### Text Services Manager

__Header file (HIToolbox): TextServices.h__

### Features and Enhancements

NewTSMDocument has been changed to turn on the kTSMDocumentUnicodeInputWindowPropertyTag implicitly for TSMDocuments of interface type kUnicodeDocumentInterfaceType. This was done so that Unicode input sources (keyboard layouts) could remain available, not only in an editing mode where Unicode is supported by the application, but also outside of editing mode where no TSMDocument in particular would be active. This was also done for compatibility with many applications that have relied on Unicode input being available even without activating any of their own TSMDocuments, as well as other applications that do create their own Unicode-flavored TSMDocument but call UseInputWindow( ..., true ) which was really an undefined operation in the original Unicode/TSM specification (3484117).

The Text Services Manager implements the new kEventTextInputFilterText Carbon event to provide a single mechanism for filtering text produced by various input sources. Input sources whose output can be filtered via this event include Keyboard layouts, Keyboard Input Methods (such as Japanese, Chinese, etc), and Character Palette class input methods. TSM will dispatch the FilterText event to the user focus immediately before dispatching a UnicodeForKey (keyboard layout or character palette text) event or a UpdateActiveInputArea (input method) event. In the case of text produced by an input method, TSM will extract the "final form" text (i.e text being commited from an inline session), sending only this text for filtering, leaving the rest of the inline session intact. In all cases, TSM will merge the resulting filtered text (a returned by a FilterText event handler) back into the original TextInput event in question, adjusting all parameters as necessary for consistency. If any text is left after filtering, the original TextInput event will then be dispatched in the usual way. This event does not filter text that is pasted or dropped. For these operations, use the Scrap and Drag Manager. (3184946)

New APIs and input method component callbacks have been introduced to allow input methods to interact with the Input Mode palette:

- TSMInputModePaletteLoadButtons
- TSMInputModePaletteUpdateButtons

These APIs allow an input method to set and update views on the Input Mode palette, using a CFArray to pass information about the buttons. These views can include toggle buttons, push buttons, and drop-down menus.

- InputModePaletteItemHit

This Component Manager call is made by the Input Mode palette when one of input method-defined views is pressed.

- GetInputModePaletteMenu

This Component Manager call is made by the Input Mode palette when a drop-down menu is pressed in order to retrieve the current menu contents from the input menu. The menu content is returned in a CFArray describing the menu items.

### MLTE

__Header file (HIToolbox): MacTextEditor.h__

### Features and Enhancements

- - Support for spell checking and new API to turn support on / off
- - Support for Font Panel and Typography Panel and new API to turn support on / off
- - Better support for Carbon HICommand Events and new API
- - New control tags to control scrolling behavior
- - New API for accessibility
- - Improved support for undo groups
- - New API to read data from CFURL
- - New API to write data to CFURL
- - Built-in support for glyph variants

Support for QuickDraw text layout and drawing has been removed. All text drawing now uses Quartz, and text layout uses ATSUI.

### Spell Checking

For SpellChecking and general command support the following constants and API have been added to MacTextEditor.i.

```
enum unsigned long TXNCommandEventSupportOptions {
    kTXNSupportEditCommandProcessing            =   1<<0,
    kTXNSupportEditCommandUpdating                =   1<<1,
    kTXNSupportSpellCheckCommandProcessing            =   1<<2,
    kTXNSupportSpellCheckCommandUpdating            =   1<<3,
    kTXNSupportFontCommandProcessing            =   1<<4,
    kTXNSupportFontCommandUpdating                =   1<<5
};

TXNSetCommandEventSupport
TXNGetCommandEventSupport
```

The basic idea with these two functions is that the caller request support for a set of HICommands that are specified by one of the TXNCommandEventSupportOptions constants. A caller can request support for command processing and/or command updating. The commandIDs that are specified by a given constant should be listed in the headerdoc comment for that constant.

`TXNSetSpellCheckAsYouType`

`TXNGetSpellCheckAsYouType`

The new way to add an event target for MLTE. HIView objects that are enclosing a TXNObject should switch to this function as soon as possible. The input HIObjectRef becomes the target for all CarbonEvent handlers. With this function in place MLTE will deprecate using TXNSetTXNObjectControls to set the CarbonEvent targets.

`TXNSetContextualMenuSetup`

Allows the caller to specify a callback for the contextual menu. This function is called immediately before the contextual menu is displayed. Note that the menu passed to this function is fresh each time. Items, Handlers, etc that the client may have added to the contextual menu previously are not retained.

`TXNSetActionKeyMapper`

A new better way to provide a callback for supporting the undo and redo items in the Edit menu. It includes a userData parameter.

### Font Panel and Typography Panel Support

Clients can turn on support for the Font Panel and its sub-panels in MLTE by calling the TXNSetCommandEventSupport API, and setting one or both of the kTXNSupportFontCommandProcessing and kTXNSupportFontCommandUpdating constants. Please see the discussion of TXNSetCommandEventSupport API in the spell checking section. Once support is turned on, MLTE handles the following Carbon Events:

- - kHICommandShowHideFontPanel and kEventFontPanelClosed to show and hide the Carbon font panel
- - kEventFontSelection event to update the document after you select a new font, size, style, color, or any features setting from the Typography Panel

### Control tags to control scrolling behavior

The kTXNAutoScrollBehaviorTag constant allows an MLTE object to be configured to never auto-scroll or to only auto-scroll when the insertion point is visible but inserted text would not be visible (similiar to a console application). The default behavior for MLTE is to auto-scroll when text is added to an object.

### Accessibility API

The new TXNGetAccessibilityHIObject API allows MLTE clients to customize the accessibility attributes returned for an MLTE object.

MLTE now supports parameterized attributes for accessing the text inside an edit field (3162087).

### Undo group API

MLTE provides new API to support handling several actions as a single undo / redo operation. The TXNBeginActionGroup is called to initiate such a group, and the TXNEndActionGroup is called to end it. When calling TXNBeginActionGroup, the client can name the group using the iActionGroupName param.

There are two cases for MLTE when handling an undo group in the undo stack:

If you have asked MLTE to handle updating for the Edit menu you should call TXNSetActionNameMapper after calling TXNCanUndoAction so that MLTE can call back to you to get the correct strings for the undo item.

If the client will handle updating the undo edit menu, the client needs to call TXNCanUndoAction to determine whether the Undo item in the Edit menu should be enabled and to obtain the action name that should be used in that item. Redo is handled similarly.

In order to support undo groups, we also introduced a new set of action constants of CFStringRef type and deprecated old TXNActionKey and old undo/redo APIs which take TXNActionKey as input.

Note that nesting of groups is not supported. Calling TXNBeginActionGroup twice in a row without calling TXNEndActionGroup will return an error.

TXNCanUndoAction and TXNCanRedoAction return false if there is an active action group since you can't undo/redo in the middle of an action group.

### Read / Write API

The TXNReadFromCFURL API has been added to allow clients to read data from a CFURLRef. Similarly, the TXNWriteRangeToCFURL API has been added to write text object ranges to a CFURLRef. An auxiliary API, TXNCopyTypeIdentifiersForRange, has been added to allow clients to determine which document format they can use to write out a text range with no information loss.

The write API supports writing out a text range or the entire text object using different document formats and encodings. These options can be specified as values in the data options dictionary which is one of the input parameters to the APIs. By default data is written out using MLTE native format and UTF-16 encoding. Clients can also specify document attributes (for the Metadata framework) when writing data out using a file format that support such attributes (i.e. RTF and MLTE native file format). By default, no document attributes are written. In addition, the write API allows clients to write either a portion of the text object (i.e. a range) or the entire object.

The read API supports reading data in from a CFURLRef with different document formats and encodings. The format and encoding options can be specified as values in the data options dictionary which is one of the input parameters to the API. By default, data is assumed to be in MLTE native format and in UTF-16 encoding. Clients can also request retrieving document attributes (for the Metadata framework) when reading data from file formats that support such attributes (i.e. RTF and MLTE native file format). By default, no document attributes are read in. We recommend clients specify the format and encoding, if they are known, since it will improve the performance of the operation.

### Notable Bug Fixes

TXNCopy will return paramErr if you call it on an MLTE object which is in echo mode (displaying a password). The EditText and Unicode EditText views also no longer respond to kEventServiceCopy when the edit field is in password mode.

Added new control tag kTXNDisableLayoutAnddDrawTag. The new tag is equivalent to the old kTXNVisibilityTag but its name describes the tag behavior. The old name was confusing since the expectation was that it would show / hide an MLTE object.

### Universal Access

__Header file (HIServices): UniversalAccess.h__

### Features and Enhancements

The Universal Access Manager is a new set of APIs that allow applications to cooperate with the Universal Access features of Mac OS X. In Mac OS X 10.4, this manager has two APIs:

- UAZoomEnabled
- UAZoomChangeFocus

UAZoomEnabled returns whether the display-zooming capability of Universal Access is currently enabled.

UAZoomChangeFocus is used to indicate that the user's attention has shifted to a new area on the display. If Universal Access zooming is enabled, this will cause the zoom focus to follow the user's attention. This API would, for example, be used by an application that implements its own text-editing engine. Such an application would call UAZoomChangeFocus as the user types so that Universal Access zooming could track the insertion point.

### Window Manager

__Header file (HIToolbox): MacWindows.h__

### Features and Enhancements

Windows now support the HIArchive protocol. All contained views will be automatically archived with the window if they support the archiving protocol.

The HIWindowGetAvailability and HIWindowSetAvailability APIs allow control over whether a window is available during Exposé.

The HIWindowGetProxyFSRef and HIWindowSetProxyFSRef APIs allow setting a window's proxy icon by FSRef.

The HIWindowGetScaleMode returns the user interface scaling factor in use for a specified window.

The HIWindowInvalidateShadow API invalidates the window shadow, allowing it to be recalculated according to the window's opaque region and content.

A new window attribute, kWindowNoTitlebarAttribute, is now supported by document, floating, and utility windows. This attribute allows a window's titlebar to be dynamically added or removed.

A new window attribute, kWindowMetalNoContentSeparatorAttribute, indicates that no border should be drawn between the toolbar and window content.

A new window attribute, kWindowUnifiedTitleAndToolbarAttribute, indicates that a window's title bar and toolbar should be drawn using a unified appearance with no separator. This appearance is not fully implemented in Mac OS X 10.4, and this constant is not currently included in the HIToolbox headers, but will be included in a future release. See Q&A 1423 for more details.

Two new window attributes, kWindowFrameworkScaledAttribute and kWindowApplicationScaledAttribute, can be used to control the behavior of a window when the display scaling factor is not 1.0. The FrameworkScaled attribute indicates that the window's CGContextRef should be scaled to match the display scale factor. The ApplicationScaled attribute indicates that the details of window scaling will be taken care of primarily by the application. If neither of these attributes is set, and the display scaling factor is not 1.0, then the window will automatically be magnified to match the scale factor.

A new window region constant, kWindowToolbarButtonRgn, is now supported (2785303). This constant can be used with GetWindowRegion and GetWindowBounds to locate the toolbar button widget in the window titlebar.

The kWindowGroupAttrFixedLevel window group attribute and the GetWindowGroupLevelOfType and SetWindowGroupLevelOfType APIs have been introduced in support of changes to the window levels used by the standard Carbon window groups; see "Implementation Changes" for more details.

Four new Carbon events are now sent when a sheet is opening and closing: kEventWindowSheetOpening, kEventWindowSheetOpened, kEventWindowSheetClosing, and kEventWindowSheetClosed (3331139).

The kEventWindowZoomed event now has a WindowPartCode parameter containing the part code that was passed to ZoomWindow or ZoomWindowIdeal (3650297).

The Window Manager now implements the kAXSubroleAttribute for windows (3100179). A window's subrole is determined as follows: windows of class Alert, MovableAlert, Modal, or MovableModal are given the Dialog subrole; windows of class Floating are given the Floating subrole; windows of class Utility are given the SystemFloating subrole; windows of class Document are given either the Standard or the Dialog subrole, depending on whether the window uses one of the DialogBackground or ModelessDialogBackground theme brushes as its window brush; other windows are given either the Unknown subrole, or no subrole at all.

Sheet and drawer windows now return their parent window for the kAXWindow attribute, rather than the sheet or drawer window itself (3453287).

Sheet and drawer windows are no longer returned as kAXMainWindowAttribute for the application; the parent window is returned instead (3533684).

The AXWindow attribute is now returned by the proxy icon in a window titlebar (3453293).

New kAXResized, kAXMoved, and kAXCreated notifications are now sent when windows resize, move, or are shown (3462903).

Windows no longer report kAXFocusedAttribute in their list of supported attributes (3484671). They still handle get/set requests properly for backwards compatibility, but this should not be relied upon continuing in future releases.

The close button now supports kAXEditedAttribute (3488214).

### User Interface Changes

In a metal window, the toolbar now positions its toolbar item views using tighter spacing than in a non-metal window.

### Implementation Changes: Carbon/Cocoa Window Interaction

Several changes have been made to the Window Manager and Control Manager to improve behavior when both Carbon and Cocoa windows are present in the same process:

- - use of non-zero CoreGraphics window levels for the modal, floating, and toolbar window groups
- - use of kFloatingWindowClass instead of kDocumentWindowClass for floating Cocoa windows
- - automatic release of focus on click from Cocoa windows
- - focus-sensitive drawing of editable text views (see HIView Manager release notes for details)
- - clicks on windows that use the standard window event handler will now, by default, always z-order the window to the top of its window group, to ensure that the window is in front of any Cocoa window at the same window level. This is done by sending a kEventCommandProcess event containing the kHICommandSelectWindow command ID.
- - establishment of autorelease pools at certain times

### Non-zero CoreGraphics Window Levels

The most significant change in the Window Manager is to use non-zero CoreGraphics window levels for the dialog and floating window groups. Previously, all types of windows in window groups beneath the Utility window group used window level 0. The Window Manager used the window group hierarchy to ensure that, for example, dialog windows could not be positioned below floating windows.

In Mac OS X 10.4, the modal window group now uses kCGModalPanelWindowLevel, and the floating and toolbar window groups now use kCGFloatingWindowLevel (but which specific window levels are in use by any given window group is subject to change in the future if necessary, and should not be relied upon). This change improves window behavior when an application has both Carbon and Cocoa windows; previously, Cocoa floating windows would always be z-ordered above both Carbon floating windows and Carbon modal dialogs. With this change, Carbon dialogs are properly ordered above Cocoa floating windows, and Carbon/Cocoa floating and dialog windows can each intermix properly.

The implementation of this change involves a bit of subterfuge when applications create their own window groups. Applications that were written against pre-10.4 versions of Mac OS X have hardcoded information about what window levels are used by the standard window groups, and are not prepared for the Window Manager to use different window levels in 10.4. For example, an application might have created a custom window group with window level 0 and inserted it between the dialog and floating windows, expecting that windows in that group would always float above standard floating windows but below dialog windows. However, now that the Window Manager uses a non-zero window level for the floating window group, the windows in the application's custom group would float below the windows in the standard floating group, not above.

To prevent this problem, the window group implementation now automatically promotes the window levels of custom window groups to be at least as large as the window level of the next standard window group. In the above example, the application's window group level would be promoted from 0 to the window level used by the floating window group. This promotion occurs automatically and does not require any intervention by existing applications.

In general, we recommend that if your application did not previously set a custom window level on its window groups, that it should not do so on Mac OS X 10.4 either. Continue to use the default window level of 0 that is given to new window groups, and rely on automatic window level promotion to make your window groups match the level of the standard window groups. This will be most compatible with future versions of Mac OS X.

Some applications may wish to avoid automatic window level promotion. A new window group attribute, kWindowGroupAttrFixedLevel, may be used to request that the window group's level should not be promoted. We do not expect that many applications will require this attribute; using it may cause compatibility problems with future versions of Mac OS X if the window levels used by the standard window groups change again. Also, note that when the automatic window level promotion algorithm examines the window group hierarchy, it looks for the FixedLevel attribute to find window groups that should determine the promoted window level of groups higher in the hierarchy. If you create a custom window group with the FixedLevel attribute, all groups higher in the window group hierarchy than your group will be promoted to a window level at least as large as your group's level.

The new non-zero window levels used for the dialog, floating, and toolbar window groups only apply when an application is active. When an application is deactivated, the windows in these window groups are automatically reset to window level 0 to prevent these windows from continuing to float above the windows of the newly active application.

Two new APIs, GetWindowGroupLevelOfType and SetWindowGroupLevelOfType, have been introduced to allow access to all of the window levels now supported by a window group. Each window group now supports three separate window levels: the Active level, which is the default level used when the application is active; the Inactive level, which is the level used when the application is inactive; and the Promoted level, which is the level that is actually used when the application is active. If a group has the kWindowGroupAttrFixedLevel attribute, the Promoted level is always the same as the Active level; if a group does not have the FixedLevel attribute, the Promoted level is at least the same as the Active level, and may be greater if there is another group with a greater level beneath this group. GetWindowGroupLevelOfType may be used to read the Promoted level; we do not recommend setting the Promoted level, since any changes made by your application may be overwritten by the Window Manager. Your application may freely set the Active and Inactive levels usign SetWindowGroupLevelOfType.

The GetWindowGroupLevel API has changed behavior. It now returns either the Promoted level or the Inactive level, depending on whether the application is active or inactive.

The SetWindowGroupLevel API has changed behavior. It now sets the Active, Inactive, and Promoted window levels to the specified value, and then increases the Promoted level if necessary to ensure that the group has a level at least as large as the next FixedLevel group.

### Cocoa Floating Window Behavior

In previous releases of Mac OS X, Cocoa floating windows, such as the Font panel, used kDocumentWindowClass as the basis for the Carbon WindowRef that wrapped the Cocoa window. This caused a variety of problems: such windows would gain focus when an application was activated; they were listed in the application's Windows menu and in the Dock tile menu for the application; when focus moved to such a window, the application's document window became deactivated.

The Cocoa Font panel and other floating windows now use kFloatingWindowClass instead of kDocumentWindowClass for their Carbon WindowRef wrappers. This allows the Cocoa windows to follow standard focusing rules much more correctly. There is, however, one drawback to using kFloatingWindowClass for the WindowRef wrapper: in an application which does not use the standard window event handler (which calls SetUserFocusWindow in response to a click in a focusable control), and which does not call SetUserFocusWindow itself, a click in a document window will not transfer focus back from the Cocoa window to the clicked document window. To resolve this problem, Cocoa floating windows are now recognized by the Window Manager as requiring special focus management. If a Cocoa floating window is the user focus window, and some other window with activation scope kWindowActivationScopeAll is clicked, the user focus will automatically be transferred to the clicked window.

### Autorelease Pools

A common problem when integrating Cocoa code into a Carbon app is ensuring that an NSAutoreleasePool is available to the Cocoa code when it allocates and autoreleases memory. This is especially awkward for applications that use RunApplicationEventLoop, since there is no way to modify the behavior of RunApplicationEventLoop to create and drain an autorelease pool during each pass through the runloop and the event dispatcher. To help alleviate this problem, an NSAutoreleasePool is now automatically established and drained in the following locations:

- - RunApplicationEventLoop
- - RunAppModalLoopForWindow
- - ModalDialog
- - window drag and resize tracking
- - control tracking and indicator dragging
- - across dispatch of an event by the event dispatcher target
- - when a window's compositing views are redrawn

### Implementation Changes: WindowGroups with kWindowGroupAttrMoveTogether

The implementation of window groups that use kWindowGroupAttrMoveTogether (such as a window with a sheet, or a window with a drawer) has changed. In previous versions of Mac OS X, when a window in a MoveTogether window group was moved, the Window Manager moved all other windows in the group by disabling updates, moving each window, and re-enabling updates. In Mac OS X 10.4, the window group implementation now uses facilities provided by CoreGraphics to bind together all of the windows in a group, so that when a window in the group is moved, CoreGraphics automatically moves all of the other grouped windows. This has several significant advantages:

- - there is a notable increase in performance of dragging grouped windows, for two reasons: (1) CoreGraphics can now move all of the windows at once rather than moving them one at a time, and (2) disabling and re-enabling updates caused the entire contents of all grouped windows to be flushed on each window movement; this no longer occurs.
- - it is now possible to use async drag with a window in a MoveTogether window group. Previously, the Window Manager would automatically disable async drag for windows in a window group. Now, async drag is enabled as long as only one window in the group is draggable. If more than one window in the group is draggable, async drag is still disabled.

There is one significant behavioral change as a result of this new implementation. In previous versions of Mac OS X, all windows in a MoveTogether window group would get a kEventWindowBoundsChanging event prior to being moved, and a kEventWindowBoundsChanged event afterwards. It would theoretically have been possible to modify the window bounds in the BoundsChanging event and cause a grouped window to move in a way that would not have kept it grouped with the other windows. In Mac OS X 10.4, only the window being moved by the Window Manager will receive the kEventWindowBoundsChanging event; all other windows in the group will not. The other grouped windows will only receive kEventWindowBoundsChanged events.

### Notable Bug Fixes

Drawers attached to modal parent windows can now receive clicks (3629224). Previously, mouse events in the drawer were blocked by the parent's modality.

Drawers now resize when the toolbar of the parent window changes size, or is shown or hidden (3138687).

When a drawer parent window is zoomed out by ZoomWindowIdeal, it now zooms to a size that leaves open drawers visible. The ZoomWindow API's behavior has not changed; it still always zooms to the standard state specified in the WindowRef.

The presence of a sheet on a drawer's parent window now causes clicks to the drawer to be blocked, and causes the drawer content to lose focus and redraw with an inactive appearance (3331137).

Clicking on a drawer's window frame or background no longer causes focus to move to the drawer. Focus will only move if you click on a view in the drawer that acquires focus in response to a click, such as an edit view.

When a window group uses the kWindowGroupAttrMoveTogether attribute, the windows in the group are now bound together during Exposé (3542300). Previously, they would separate or disappear.

kAXMainAttribute is now only settable for windows that have an activation scope of kWindowActivationScopeAll (3486736).

kAXMainWindowChangedNotification is no longer sent when an application is activated (3497019).
