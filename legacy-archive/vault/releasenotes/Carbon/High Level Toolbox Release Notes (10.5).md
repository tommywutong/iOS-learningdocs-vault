---
title: High Level Toolbox Release Notes (10.5)
apple_id: TP40004744
resource_type: Release Note
platform: macOS
topic: null
technology: Carbon
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/releasenotes/Carbon/HIToolbox.html
archived_at: '2026-07-18T02:50:21.505784Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# HIToolbox Release Notes for OS X v10.5

|  |
| --- |
| Contents  - [1 OS X Leopard Developer Release Notes: High Level Toolbox](#apple-jvqwgx2pknpvqx2mmvxxaylsmrpuizlwmvwg64dfojpvezlmmvqxgzk7jzxxizlthjpuq2lhnbpuyzlwmvwf6vdpn5wge33y) - [2 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dt) - [3 Tips for Compatibility with OS X Leopard](#apple-kruxa427mzxxex2dn5wxaylunfrgs3djor4v653joruf6tlbmnpu6u27lbpuyzlpobqxeza) - [4 Bug Reporting](#apple-ij2wox2smvyg64tunfxgo) - [5 Feedback](#apple-izswkzdcmfrww) - [6 Accessibility](#apple-ifrwgzltonuwe2lmnf2hs)   - [6.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl4za) - [7 Appearance Manager](#apple-ifyhazlbojqw4y3fl5gwc3tbm5sxe)   - [7.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl4zq)   - [7.2 API Deprecation](#apple-ifiesx2emvyhezldmf2gs33o)   - [7.3 Implementation Changes](#apple-jfwxa3dfnvsw45dboruw63s7inugc3thmvzq) - [8 AppleEvents](#apple-ifyha3dfiv3gk3tuom)   - [8.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl42a) - [9 Application Manager](#apple-ifyha3djmnqxi2lpnzpu2ylomftwk4q)   - [9.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl42q) - [10 Carbon Event Manager](#apple-inqxeytpnzpuk5tfnz2f6tlbnzqwozls)   - [10.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl43a)   - [10.2 Notable Bug Fixes](#apple-jzxxiylcnrsv6qtvm5pum2lymvzq) - [11 Dialog Manager](#apple-iruwc3dpm5pu2ylomftwk4q)   - [11.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl43q)   - [11.2 Implementation Changes](#apple-jfwxa3dfnvsw45dboruw63s7inugc3thmvzv6mq) - [12 Drag Manager](#apple-irzgcz27jvqw4ylhmvza)   - [12.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl44a)   - [12.2 API Deprecation](#apple-ifiesx2emvyhezldmf2gs33ol4za)   - [12.3 Notable Bug Fixes](#apple-jzxxiylcnrsv6qtvm5pum2lymvzv6mq) - [13 Help Manager](#apple-jbswy4c7jvqw4ylhmvza)   - [13.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl44q) - [14 HIObjects](#apple-jbeu6ytkmvrxi4y)   - [14.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl4yta)   - [14.2 Notable Bug Fixes](#apple-jzxxiylcnrsv6qtvm5pum2lymvzv6my) - [15 HIShape](#apple-jbevg2dbobsq)   - [15.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl4ytc) - [16 HIToolbar](#apple-jbevi33pnrrgc4q)   - [16.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl4yte) - [17 HIView Manager](#apple-jbevm2lfo5pu2ylomftwk4q)   - [17.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl4ytg)   - [17.2 Notable Bug Fixes](#apple-jzxxiylcnrsv6qtvm5pum2lymvzv6na)   - [17.3 Notes](#apple-jzxxizlt) - [18 IBCarbonRuntime](#apple-jfbegylsmjxw4utvnz2gs3lf)   - [18.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl4yti)   - [18.2 Notable Bug Fixes](#apple-jzxxiylcnrsv6qtvm5pum2lymvzv6ni) - [19 Icon Services](#apple-jfrw63s7knsxe5tjmnsxg)   - [19.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl4ytk)   - [19.2 API Deprecation](#apple-ifiesx2emvyhezldmf2gs33ol4zq) - [20 Keyboard Manager](#apple-jnsxsytpmfzgix2nmfxgcz3foi)   - [20.1 API deprecation](#apple-ifiesx3emvyhezldmf2gs33o)   - [20.2 Notable Bug Fixes](#apple-jzxxiylcnrsv6qtvm5pum2lymvzv6nq) - [21 Keyboard Resources](#apple-jnsxsytpmfzgix2smvzw65lsmnsxg)   - [21.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl4ytm) - [22 List Manager](#apple-jruxg5c7jvqw4ylhmvza)   - [22.1 API Deprecation](#apple-ifiesx2emvyhezldmf2gs33ol42a) - [23 Menu Manager](#apple-jvsw45k7jvqw4ylhmvza)   - [23.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl4yto)   - [23.2 User Interface Changes](#apple-kvzwk4s7jfxhizlsmzqwgzk7inugc3thmvzq)   - [23.3 API Deprecation](#apple-ifiesx2emvyhezldmf2gs33ol42q)   - [23.4 Notable Bug Fixes](#apple-jzxxiylcnrsv6qtvm5pum2lymvzv6ny) - [24 MLTE](#apple-jvgfiri)   - [24.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl4ytq)   - [24.2 API Deprecation](#apple-ifiesx2emvyhezldmf2gs33ol43a) - [25 Navigation Services](#apple-jzqxm2lhmf2gs33ol5jwk4twnfrwk4y)   - [25.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl4yts)   - [25.2 API Deprecation](#apple-ifiesx2emvyhezldmf2gs33ol43q)   - [25.3 Notable Bug Fixes](#apple-jzxxiylcnrsv6qtvm5pum2lymvzv6oa) - [26 Pasteboard Manager](#apple-kbqxg5dfmjxwc4tel5gwc3tbm5sxe)   - [26.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl4zda) - [27 Scrap Manager](#apple-knrxeylql5gwc3tbm5sxe)   - [27.1 API Deprecation](#apple-ifiesx2emvyhezldmf2gs33ol44a) - [28 Script Manager](#apple-knrxe2lqorpu2ylomftwk4q)   - [28.1 API Deprecation](#apple-ifiesx2emvyhezldmf2gs33ol44q) - [29 Text Input Sources](#apple-krsxq5c7jfxha5lul5jw65lsmnsxg)   - [29.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl4zdc) - [30 Text Services Manager](#apple-krsxq5c7knsxe5tjmnsxgx2nmfxgcz3foi)   - [30.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl4zde)   - [30.2 API Deprecation](#apple-ifiesx2emvyhezldmf2gs33ol4yta)   - [30.3 Notable Bug Fixes](#apple-jzxxiylcnrsv6qtvm5pum2lymvzv6oi) - [31 Window Manager](#apple-k5uw4zdpo5pu2ylomftwk4q)   - [31.1 Features and Enhancements](#apple-izswc5dvojsxgx3bnzsf6rlonbqw4y3fnvsw45dtl4zdg)   - [31.2 User Interface Changes](#apple-kvzwk4s7jfxhizlsmzqwgzk7inugc3thmvzv6mq)   - [31.3 API Deprecation](#apple-ifiesx2emvyhezldmf2gs33ol4ytc)   - [31.4 Notable Bug Fixes](#apple-jzxxiylcnrsv6qtvm5pum2lymvzv6mjq) |

## OS X Leopard Developer Release Notes: High Level Toolbox

For High Level Toolbox release notes for 10.4 and earlier, please refer to HIToolboxOlderNotes.

The High Level Toolbox is a subsystem of the Carbon framework for OS X. It is composed of three frameworks: HIToolbox, HIServices, and NavigationServices. This document discusses changes in these three frameworks for OS X Leopard.

## Features and Enhancements

The major new features in the HIToolbox, HIServices, and NavigationServices frameworks for OS X Leopard are:

- The HIToolbox and HIServices frameworks are available for use in 64-bit applications, but not all APIs are available. In particular, the HIToolbox APIs for creating and managing UI elements (menus, windows, and views) are not available. Use Cocoa to build the UI for a 64-bit application. The NavigationServices framework does not provide a 64-bit API.
- HIToolbox supports high-resolution displays via framework scaling for compositing windows, and automatic magnification for existing applications. This feature is still in a developer-preview state and is not intended for use by end users; there are known bugs in the current implementation. However, the implementation has significantly improved since Tiger and we encourage application developers to enable framework-scaled mode in compositing windows and test their apps with non-1.0 scaling factors.
- A new HIView, HICocoaView, allows wrapping an arbitrary NSView into an HIView so that the NSView can be used inside a Carbon window.
- Navigation Services dialogs are now implemented using the Cocoa NSOpenPanel and NSSavePanel APIs, ensuring that Carbon applications receive the same UI improvements as Cocoa applications.
- A new API set, Text Input Sources, replaces most of the existing Script Manager, Keyboard, and TextServices APIs.
- Many standard views support specifying the view image content using a CFURLRef or CFString naming a resource in the application's bundle.
- Carbon event handlers may be used to receive and handle AppleEvents.
- New HIObject APIs allow an HIObject to be attached as a delegate to another HIObject.
- A Carbon event suite for HIObject delegates has been defined, and a sample delegate HIObject is provided that can be used to automatically limit the length of a text-editing field.
- The Menu Manager supports embedding HIViews in menu items.
- You can now specify a custom HIObject subclass ID and custom init event parameters in InterfaceBuilder for all of the standard controls and views. This capability requires the use of IB 3.0.
- The visual appearance for all types of windows (standard, unified, and metal) has changed to use a single common appearance similar to the pre-Leopard unified appearance.
- The HIThemeDrawTextBox and HIThemeGetTextDimensions APIs now support drawing and measuring CFAttributedStrings.
- The standard views that draw text, except for the EditText and EditUnicodeText views and HITextView, now support setting the text font to a CTFontRef.
- The Menu Manager now supports setting a menu item's text using an attributed string, and setting a menu or menu item's font using a CTFontRef.
- A new header file, HIToolboxDebugging.h, declares the debugging utility functions provided by HIToolbox for use from within gdb.
- The Window Manager provides a variety of new APIs that take or return window positions and shapes using HIRects and HIShapes.
- The Window Manager now supports providing a custom view that is positioned in the location of the toolbar, for use by applications that cannot use the standard HIToolbar API.
- The Pasteboard Manager now defines a protocol for promising files as drag content that is not based on the deprecated FSSpec type.
- New APIs are provided for determining whether a window or view should draw its content with a focused appearance, and for determining the focused window during menu tracking. See "Modal Focus" in the Window Manager.

## Tips for Compatibility with OS X Leopard

We've noticed that some apps may be incompatible with Leopard due to changes in HIToolbox or HIServices. Here are some changes that may affect your application, and how you can adapt to remain compatible:

- The windows created by the ShowStandardAlert and CreateStandardAlert APIs are now compositing. Some apps have added their own controls to these windows after the window is created and expect non-compositing-style event handling for the window (such as mouse coordinates in QuickDraw port coordinates rather than view-local coordinates). Apple does not recommend or support adding your own controls to a standard alert window, and if you do so, your application must be able to handle both non-compositing and compositing event handling.

- TrackDrag now returns dragNotAcceptedErr when the drag is not accepted by the receiver (4065651). Previously, userCanceledErr was returned in this case, but in Leopard userCanceledErr is reserved only for instances when the user explicitly cancels a drag via the escape or cmd-period key sequences. Your application should be prepared to receive dragNotAcceptedErr as a possible return value from TrackDrag.

- The Navigation Services dialogs offered prior to OS X Leopard happened to work when displayed from a cooperative thread that was not the main thread, although this was not officially supported. The new Cocoa implementation of Navigation Services dialogs does not work from any thread other than the main thread. Therefore, any calls to create or display a Nav dialog from a non-main thread will cause Navigation Services to switch into a compatibility mode in which it will use the classic Carbon-based dialogs rather than the Cocoa dialogs.

- HIViewCreateOffscreenImage now creates native-endian images (4555266). Your application should not assume a particular endian-ness for the CGImage data.

- Prior to Leopard, calling InstallStandardEventHandler on the application target had no effect. In Leopard, it now installs the standard app handler that is used by RunApplicationEventLoop. This handler will dispatch AppleEvents if it receives a kEventAppleEvent Carbon event. Some applications were calling InstallStandardEventHandler on the app target (presumably not realizing that it did nothing) and assuming that AppleEvents would not be dispatched until the application called RunApplicationEventLoop. This assumption is no longer correct. If your app doesn't need AppleEvents to be dispatched, don't install the standard event handler on the app target.

- Keyboard event routing during menu tracking has changed. Prior to Leopard, a keystroke that caused a change in the menu selection (such as the arrow keys, or Tab) would be handled immediately during menu tracking and would not be sent to other event targets beyond the menu itself. In Leopard, in order to support HIViews with keyboard focus embedded inside a menu, all key events are sent to the event dispatcher target, which converts them into kEventClassTextInput events and resends them to the event dispatcher target. The Menu Manager performs keyboard navigation and type-select based on the kEventTextInputUnicodeForKeyEvent event. This change in routing has caused problems for applications that install kEventRawKeyDown/Repeat event handlers on the event dispatcher or application targets. Previously, these handlers would not be called for keyboard navigation keystrokes such as the arrow keys, but in Leopard they are. There are several ways to avoid this problem: (1) use the kEventMenuBeginTracking and kEventMenuEndTracking events to monitor when menu tracking is occurring, and ignore raw key events that are received by your handlers during menu tracking; (2) install your raw key event handlers on a window or view rather than on the app or event dispatcher targets; or (3) don't install handlers for kEventRawKeyDown/Repeat, but use kEventTextInputUnicodeForKeyEvent instead, and install your handler on a window, view, or app target rather than on the event dispatcher target.

- When drawing with QuickDraw into the Dock tile for an application or window, some applications use QDFlushPortBuffer to cause drawing to be flushed to the Dock tile without calling EndQDContextForApplicationDockTile or ReleaseQDContextForCollapsedWindowDockTile. Due to a change in the Dock implementation in Leopard, flushing the QuickDraw port for the tile no longer has any effect. We hope to address this in a future Leopard software update, but until then we recommend that applications use CoreGraphics to draw into the Dock tile (creating the CG context with BeginCGContextForApplicationDockTile or HIWindowCreateCollapsedDockTileContext) and CGContextFlush to cause the Dock tile to update.

## Bug Reporting

We encourage all developers to file bugs found in OS X Leopard at <[http://bugreport.apple.com](http://bugreport.apple.com/)>. Duplicate bugs are not a problem; please don't hesitate to file a bug with the thought that "surely someone else must have found this already."

## Feedback

The primary method of submitting feedback, such as bug reports and enhancement requests, is to file bugs using Apple's bug reporter website, as described above. This is the only way to ensure that your feedback will be read and considered by Apple engineering.

For feedback and comments about HIToolbox, HIServices, and Navigation Services APIs and features, you can email hitoolbox-feedback@group.apple.com. The intent of this address is to provide developers with a direct channel to the engineering team responsible for these technologies. We will read your input, and will try to acknowledge it, but we might not always have time for replies. Please use this address for feedback and comments on the APIs and features (for instance "please add QuickTime wrapper classes to HIToolbox" or "I need API to do this and that"), but not for support type questions (for instance, "I can't install OS X" or "How does one create a new bundle in Xcode?") or comments in other areas (for instance, "why is the dock centered in Aqua?").

For discussion among developers, there is the carbon-dev@lists.apple.com mailing list. Like all of Apple's mailing lists, you can subscribe to this list at [http://lists.apple.com/](http://lists.apple.com/). Although some Apple employees do read and respond to this list, they do so on their own time, not as a part of their job duties. This list can help developers find solutions to their problems among themselves. Mentioning an issue on the list is not an channel for requesting help from Apple; the only ways to get help directly from Apple are by filing a bug or requesting assistance from Apple Developer Technical Support.

## Accessibility

__Header files (HIServices): AXConstants.h, AXError.h, AXUIElement.h, AXValue.h__
__Header files (HIToolbox): HIAccessibility.h__

#### Features and Enhancements

The Accessibility Carbon events and HIObject APIs have been moved into a separate header file, HIToolbox/HIAccessibility.h.

## Appearance Manager

__Header files (HIToolbox): Appearance.h, HITheme.h__

#### Features and Enhancements

Exported kThemeAdornmentArrowRightArrow to be used with HIThemeDrawButton and kThemeDisclosureTriangle when drawing the intermediate animation stages of the triangle (2641747). This constant also works on Tiger.

Added kThemeTrackHideTrack to be used in the attributes field of HIThemeTrackDrawInfo passed to HIThemeDrawTrack to omit the track part of the track (i.e. the gutter and arrows of a scroll bar or the groove of a slider) (3689743).

Exported kThemeMetricButtonRoundedHeight and kThemeMetricButtonRoundedRecessedHeight (4192445). These are the heights of the round-ended buttons as used in the Finder's Search query interface. These metrics were introduced late in Tiger, and were not publicized as the headers were frozen.

Added kThemeMetricSeparatorSize to get the height of a horizontal separator or the width of a vertical separator, where a separator is what is drawn by the separator control (which uses the HIThemeDrawSeparator theme primitive) (2885092).

The new API HIThemeGetTextColorForThemeBrush has been added. In conjunction with the new API HIWindowGetThemeBackground and HIThemeSetTextFill, it can be used to replace SetThemeTextColorForWindow.

Added HIThemeBeginFocus and HIThemeEndFocus to allow for drawing of focus around arbitrary Quartz drawing operations. HIThemeBegin/EndFocus can be used to replace calls to DrawThemeFocusRegion.

A new API, HIThemeGetUIFontType, is provided to convert a ThemeFontID to a CTFontUIFontType. Once you have a CTFontUIFontType, you can get a CTFontRef for that font type using CTFontCreateUIFontForLanguage. In this way, you can determine the CTFontRef that corresponds to a particular ThemeFontID.

Two new theme metrics, kThemeMetricTexturedPushButtonHeight and kThemeMetricTexturedSmallPushButtonHeight, are provided to return the optimum height for a button using the kThemePushButtonInset or kThemePushButtonInsetSmall theme button kinds. You can create such a button by creating a bevel button and calling SetControlData with kControlBevelButtonKindTag to set the bevel button's kind appropriately.

The HIThemeDrawTextBox and HIThemeGetTextDimensions APIs now support CFAttributedStringRef. You may pass an attributed string to these APIs and it will be drawn or measured appropriately. The theme font that you specify to these APIs is applied to any part of the string that does not already have a specified font; parts of the string that already have a font attribute will retain that attribute.

The inString parameter of the HIThemeDrawTextBox and HIThemeGetTextDimensions APIs is now typed as a CFTypeRef rather than a CFStringRef. This allows you to pass a CFAttributedStringRef without casting.

The older theme text APIs (DrawThemeTextBox, GetThemeTextDimensions, and TruncateThemeText) do not support CFAttributedStringRef, and will return paramErr if passed an attributed string.

#### API Deprecation

Most QuickDraw-based Appearance Manager APIs are now deprecated. You should switch to the CoreGraphics-based HITheme APIs instead. The following typedefs and APIs are deprecated for Leopard:

: ThemeTabTitleDrawProcPtr
: ThemeEraseProcPtr
: ThemeButtonDrawProcPtr
: WindowTitleDrawingProcPtr
: ThemeIteratorProcPtr
: MenuTitleDrawingProcPtr
: MenuItemDrawingProcPtr

: ApplyThemeBackground
: DrawThemeButton
: DrawThemeChasingArrows
: DrawThemeEditTextFrame
: DrawThemeFocusRect
: DrawThemeFocusRegion
: DrawThemeGenericWell
: DrawThemeListBoxFrame
: DrawThemeMenuBackground
: DrawThemeMenuBarBackground
: DrawThemeMenuItem
: DrawThemeMenuSeparator
: DrawThemeMenuTitle
: DrawThemeModelessDialogFrame
: DrawThemePlacard
: DrawThemePopupArrow
: DrawThemePrimaryGroup
: DrawThemeScrollBarArrows
: DrawThemeScrollBarDelimiters
: DrawThemeSecondaryGroup
: DrawThemeSeparator
: DrawThemeStandaloneGrowBox
: DrawThemeStandaloneNoGrowBox
: DrawThemeTab
: DrawThemeTabPane
: DrawThemeTextBox
: DrawThemeTickMark
: DrawThemeTitleBarWidget
: DrawThemeTrack
: DrawThemeTrackTickMarks
: DrawThemeWindowFrame
: DrawThemeWindowHeader
: DrawThemeWindowListViewHeader
: GetThemeButtonBackgroundBounds
: GetThemeButtonContentBounds
: GetThemeButtonRegion
: GetThemeFont
: GetThemeMenuBackgroundRegion
: GetThemeScrollBarTrackRect
: GetThemeStandaloneGrowBoxBounds
: GetThemeTabRegion
: GetThemeTextDimensions
: GetThemeTrackBounds
: GetThemeTrackDragRect
: GetThemeTrackLiveValue
: GetThemeTrackThumbPositionFromOffset
: GetThemeTrackThumbPositionFromRegion
: GetThemeTrackThumbRgn
: GetThemeWindowRegion
: GetThemeWindowRegionHit
: HitTestThemeScrollBarArrows
: HitTestThemeTrack
: IsThemeInColor
: IsValidAppearanceFileType
: IterateThemes
: SetTheme
: SetThemeBackground
: SetThemePen
: SetThemeTextColor
: TruncateThemeText
: UseThemeFont

#### Implementation Changes

The Appearance Manager supports high-resolution displays. It can now draw scalable artwork for all appearance primitives, providing a high-quality appearance at any resolution.

## AppleEvents

__Header file (HIToolbox): AEInteraction.h__

#### Features and Enhancements

The AEProcessEvent API has been introduced to allow handling of kEventAppleEvent Carbon events without first converting the Carbon event to an EventRecord. We expect to deprecate the classic Event Manager API in a future release of OS X, and this new API allows your application to process AppleEvents without using the classic Event Manager.

## Application Manager

__Header file (HIToolbox): MacApplication.h__

#### Features and Enhancements

A new API, HIApplicationCreateDockTileContext, is now available for creating a CGContextRef to draw into an application's Dock tile. Applications may optionally choose to use this API instead of the existing BeginCGContextForApplicationDockTile API. The new API offers applications the ability to draw into Dock tiles at a resolution other than 128x128, which was the size of all Dock tiles prior to Leopard. Dock tiles may now use different sizes when a user interface scaling factor other than 1.0 is in use. In this case, the existing BeginCGContext API will apply a transform to the returned CGContextRef to allow applications to continue drawing at 128x128; the drawing will be scaled to the actual size of the tile. The new API does not apply a transform, but does return the actual size of the tile, so applications can draw into the appropriate bounding rect.

Because the Dock's tile size can now change dynamically, applications that use HIApplicationCreateDockTileContext should be prepared to redraw their Dock tile as necessary. The kEventAppUpdateDockTile Carbon event is now sent when the application needs to redraw its Dock tile.

The HIApplicationGetFocus API is provided to allow applications to retrieve either the traditional (modeless) focus window or the modal focus window. See the Window Manager section of this documentation for more discussion of modal focus.

The kHIApplicationClassID constant is now published. This constant defines the HIObject class ID for the application object. It is valid in 10.3 and later. In 10.5 and later, you can create a subclass of this class ID and instantiate it as the first action in your main function, and your subclass will be used as the singleton Carbon application object for the process.

## Carbon Event Manager

__Header files (HIToolbox): CarbonEvents.h, CarbonEventsCore.h__

#### Features and Enhancements

The Carbon Event Manager now uses CGEventRefs internally when acquiring events from the window server. Two new APIs have been added to allow conversion between a Carbon event and a CGEventRef: CreateEventWithCGEvent and CopyEventCGEvent.

When the Carbon Event Manager receives a keyboard event from the window server, it now inspects the event to determine if it contains Unicode text that was added by the event creator using CGEventKeyboardSetUnicodeString. If so, rather than creating a kEventRawKeyDown Carbon event, a kEventTextInputUnicodeText event is created instead. This event is posted to the event queue as normal, and when the event dispatcher receives the event, the dispatcher calls SendTextInputEvent on the event. SendTextInputEvent converts the event into a kEventTextInputUnicodeForKeyEvent event and resends it to the event dispatcher. These changes allow direct introduction of Unicode text into Carbon and Cocoa applications using CGEventKeyboardSetUnicodeString, without needing to use virtual keycodes or the CGPostKeyboardEvent API.

The kEventParamPostOptions event parameter has been documented. This parameter may be added to an event that is being posted to the main event queue with PostEventToQueue. If present, its contents are passed to SendEventToEventTargetWithOptions when the event is handled by the event dispatcher target. This parameter is supported on OS X v10.0 and later.

Several new event parameter types have been added to aid in making your application compatible with both 32-bit and 64-bit HIToolbox: typeRefCon, typeByteCount, and typeByteOffset.

Event parameters that previously used typeGDHandle now use typeCGDisplayID (a CGDirectDisplayID).

The following event parameter coercions have been added:

: typeVoidPtr <--> typeSInt32 (32-bit only)
: typeVoidPtr <--> typeUInt32 (32-bit only)
: typeByteCount <--> typeSInt32 (32-bit only)
: typeByteOffset <--> typeSInt32 (32-bit only)
: typeGDHandle <--> typeCGDisplayID (32-bit only)

These new coercions provide compatibility with existing applications when requesting event parameters whose underlying data types have changed in Leopard.

The RemoveStandardEventHandler API has been added. This API requests that an event target remove the standard handler installed by InstallStandardEventHandler (if any). Calls to InstallStandardEventHandler and RemoveStandardEventHandler are nestable; the standard handler for an event target will only be removed when the same number of calls have been made to remove the handler as were made to install the handler.

The HIGetMousePosition API has been added. This is a modern replacement for the GetMouse API that will return the mouse position in an HIPoint parameter. Additionally, the position of the mouse can be requested relative to a window or view rather than just globally.

The HIObjectGetEventHandlerObject API, added to the HIObject Manager in Leopard, is useful in many types of Carbon event handlers. This API returns the HIObject that is currently handling an event (i.e., the HIObject on which an event handler is installed), or if the handler is installed on an HIObject delegate object, it returns the HIObject on which the delegate object is installed. You might find this API useful when handling an event that does not have a direct object parameter; in this case, you can use the API to find out which object has received the event.

The application event target now supports InstallStandardEventHandler. The standard application event handler is also installed automatically by RunApplicationEventLoop. The standard application event handler handles kEventCommandProcess (for the kHICommandAbout, kHICommandQuit, and kHICommandShowHideFontPanel command IDs) and kEventAppleEvent.

The kHICommandCloseFile command ID has been added for use with a “Close File” menu item, as specified in the OS X Human Interface Guidelines (4028591). There is no default handler for this command ID; applications must implement their own support for it.

A new API, RemoveEventParameter, allows you to remove a parameter that had previously been stored in an event.

The HIMouseTrackingGetParameters API supports three new selectors: kMouseParamsProxyIcon, kMouseParamsClickAndHold, and kMouseParamsDragInitiation.

In Events.h, a new set of constants is available that defines the standard virtual keycode values for an ANSI-standard US keyboard layout, as well as keyboard layout-independent keys and some JIS and ISO keys (3320456).

The documentation for the kEventWindowSetupProxyDragImage Carbon event now mentions that handlers for this event may return a CGImageRef instead of a GWorldPtr. Support for a CGImageRef parameter has actually been available since OS X v10.2.

The kEventWindowGetIdealStandardState event has been made public. This event is sent by IsWindowInStandardState and ZoomWindowIdeal to determine the standard (zoomed-out) state of a window. An application can override this event to customize the standard state; for example, if an application has tool palette windows around the edges of a display, it might want to adjust the standard state to avoid zooming underneath these palette windows. This event is actually available in OS X v10.4 and later.

A new option mask, kTrackMouseLocationOptionIncludeScrollWheel, is defined for use with TrackMouseLocationWithOptions, HIViewTrackMouseLocation, and HIViewTrackMouseShape (4537320). This option indicates that the tracking API should check for mouse-wheel Carbon events (kEventMouseWheelMoved and kEventMouseScroll) and return from the loop if either event is seen.

__New and Improved Carbon Events__

The following Carbon events are new for OS X Leopard:

: kEventMouseScroll (actually available since OS X v10.4)
: kEventSystemDisplaysAsleep (actually available since OS X v10.4)
: kEventSystemDisplaysAwake (actually available since OS X v10.4)
: kEventWindowTitleChanged (actually available since OS X v10.2)
: kEventControlFocusPartChanged
: kEventControlOptimalBoundsChanged
: kEventDataBrowserDrawCustomItem
: kEventTextInputIsMouseEventInInlineInputArea
: kEventTSMDocumentAccessGetFirstRectForRange
: kEventAppUpdateDockTile
: kEventWindowUpdateDockTile
: kEventWindowFocusLost
: kEventWindowFocusRestored
: kEventSystemDisplayReconfigured
: kEventHIObjectCreatedFromArchive
: kEventHIObjectGetInitParameters
: kEventDelegateInstalled
: kEventDelegateRemoved
: kEventDelegateGetTargetClasses
: kEventDelegateIsGroup
: kEventDelegateGetGroupClasses

The following event parameter types, available in Leopard, allow clients to explicitly state the coordinate space of the point, size, rectangle or scalar. Automatic translations are provided between the various coordinate spaces and original typeHIPoint, typeHISize, typeHIRect and typeCGFloat parameter types. For more information on coordinate spaces see HIGeometry.h.

: typeHIPoint72DPIGlobal
: typeHIPointScreenPixel
: typeHISize72DPIGlobal
: typeHISizeScreenPixel
: typeHIRect72DPIGlobal
: typeHIRectScreenPixel
: typeCGFloat72DPIGlobal
: typeCGFloatScreenPixel

The kEventControlHit event now includes a kEventParamClickCount parameter indicating the click count of the original mouse-down event (3842062). Note that this parameter is optional and won't be present in all instances of this event, particularly if the Accessibility API is being used to simulate a click on the control, or if a client has called HIViewSimulateClick.

Previously, scroll wheel events were always routed by the Window Server to the active application. Now, the Window Server routes these events to the application that owns the window under the mouse, even if that application is inactive. HIToolbox previously prevented scroll wheel events received by an inactive application from being turned into Carbon events, but now allows this conversion.

__Menu Context Flags__

The Spotlight Help feature in Leopard requires scanning the contents of an application's menus to build an index of the menu item text. This index is used when you type into the Help menu to find menu items that match your search string.

In order to support menu content that changes dynamically, the Spotlight Help feature has to re-index the menu content each time that the Help menu is opened. Before examining the content of a menu, Spotlight Help sends several Carbon events to allow the application to populate the menu with new menu content. This can be quite slow at times, especially if the menu content is expensive to determine.

To allow applications to optimize menu content updating, several new bit flags have been defined as part of the MenuContext bitfield. These flags are:

- kMenuContextInspection: indicates that a Carbon event is being sent because someone is inspecting the menu content.
- kMenuContentDontUpdate[Text|Icon|Key|Enabled]: indicates that the sender of the Carbon events does not need to inspect the specified menu content. This allows an event handler to optimize its content updating by not updating this content. For example, Spotlight Help doesn't need command keys, icons, or enable state, so it will set all of those flags.

These flags are included in Carbon events such as kEventMenuOpening, kEventMenuPopulate, kEventMenuEnableItems, and kEventCommandUpdateStatus.

__AppleEvent Handling with Carbon Events__

The Carbon Event Manager in Leopard allows AppleEvents to be handled using Carbon Event handlers.

To handle an AppleEvent using a Carbon event handler, you should:

- Install your Carbon event handler using the AppleEvent class and kind on the application event target.
- Use GetEventParameter to retrieve parameters from the AppleEvent.
- Alternately, use kEventParamAppleEvent/typeAppleEvent with GetEventParameter to retrieve an AppleEvent structure from the Carbon event. This is the original AppleEvent that was sent to your application. You can use AppleEvent Manager API to retrieve AppleEvent parameters and attributes from the event.
- Use SetEventParameter to store parameters into the reply AppleEvent.
- Alternately, use kEventParamAppleEventReply/typeAppleEvent to retrieve a reply AppleEvent structure from the Carbon event. Modify the reply using AppleEvent Manager API.

If you need to retrieve an AppleEvent parameter that is a list (AEDescList), you can use GetEventParameter with typeAEDescList to do this. The output buffer should be an AEDescList. In this case, you must call AEDisposeDesc on the AEDescList when you're done with it (unlike normal Carbon event parameters, which do not need to be freed).

As with normal Carbon event processing, if your handler returns eventNotHandledErr, the AppleEvent will be passed along to any other Carbon event handlers registered for the same AppleEvent, and then to any AppleEvent handlers. If your handler returns any other value, handling of the AppleEvent will stop with your handler.

Note that, while you may call CallNextEventHandler in your Carbon event handler for an AppleEvent, doing so will only call other Carbon event handlers for that AppleEvent; it will not call AppleEvent handlers. The AppleEvent handlers will not be called until your Carbon event handler returns.

#### Notable Bug Fixes

The ReleaseWindowMouseTrackingRegions API has been fixed to correctly release the regions (3102994). This API was not functioning correctly in previous releases (back to and including OS X v10.2). Prior to Leopard, clients must release MouseTrackingRefs with the ReleaseMouseTrackingRegion API for each reference.

InstallEventLoopTimer now installs the timer into the runloop using the CommonModes constant rather than the DefaultMode constant (4357867). This change is primarily intended to benefit applications that use both Carbon and Cocoa windows. While a mouse-down is being tracked in a control, AppKit will run the runloop in a mode that is not the default mode, which previously would disable Carbon event loop timers. With this change, event loop timers will continue to fire while tracking controls in a Cocoa window. This behavior was already in place for mach-o applications linked on OS X v10.3 and later; we have seen no compatibility issues from this change, so this behavior is now also used for mach-o applications linked on any release of OS X, and for all CFM applications.

## Dialog Manager

__Header file (HIToolbox): Dialogs.h__

#### Features and Enhancements

StandardAlert and CreateStandardAlert now allow the defaultButton and cancelButton fields of their AlertStdAlertParamRec/AlertStdCFStringAlertParamRec parameter to be set to the same value (2265821). This allows a standard alert to have the same button respond to both default and cancel keyboard equivalents.

StandardAlert and CreateStandardAlert now allow the defaultButton field of their AlertStdAlertParamRec/AlertStdCFStringAlertParamRec parameter to be set to zero (3484210). This allows a standard alert to have no default button at all.

Two new constants, kDialogFlagsUseCompositing and kAlertFlagsUseCompositing, can be used in 'dlgx' and 'alrx' resources in the flags field. These constants specify that the Dialog Manager should create the dialog or alert window using compositing mode. Note that a compositing dialog window also uses the standard window event handler, so a ModalFilterProcPtr passed to ModalDialog with such a window will never receive any events; the events will all be handled by the standard event handler.

#### Implementation Changes

For HiDPI compatibility, the StandardAlert dialogs are now compositing windows, and use framework-scaled mode (4494014). Note that this may cause compatibility issues with applications that add their own controls to standard alerts. See "Tips for Compatibility with OS X Leopard."

## Drag Manager

__Header file (HIToolbox): Drag.h__

#### Features and Enhancements

ShowDragHilite and HideDragHilite now call HiliteWindowFrameForDrag. The HiliteWindowFrameForDrag documentation states that it is called by these APIs, but it appears that they have never actually done so, at least not on OS X.

TrackDrag now accepts a NULL RgnHandle.

#### API Deprecation

All the Drag flavor APIs are deprecated for Leopard. Use GetDragPasteboard or NewDragWithPasteboard in addition to the Carbon Pasteboard APIs. The Drag hilite and scroll APIs have also been deprecated for Leopard. Use the kThemeBrushDragHilite theme brush and draw the highlight as part of your custom window or control drawing instead.

The following APIs are deprecated for Leopard:

: GetStandardDropLocation
: SetStandardDropLocation
: ZoomRects
: ZoomRegion
: SetDragItemFlavorData
: InstallTrackingHandler
: InstallReceiveHandler
: RemoveTrackingHandler
: RemoveReceiveHandler
: SetDragSendProc
: CountDragItems
: GetDragItemReferenceNumber
: CountDragItemFlavors
: GetFlavorType
: GetFlavorFlags
: GetFlavorDataSize
: GetFlavorData
: GetDropLocation
: SetDropLocation
: ShowDragHilite
: HideDragHilite
: DragPreScroll
: DragPostScroll
: UpdateDragHilite
: GetDragHiliteColor

#### Notable Bug Fixes

The SetDragImageWithCGImage API now accepts images created with any type of alpha value (4031183). Prior to Leopard, only images with an alpha info value between kCGImageAlphaPremultipliedLast and kCGImageAlphaFirst inclusive were properly accepted.

TrackDrag now returns dragNotAcceptedErr when the drag is not accepted by the receiver (4065651). userCanceledErr is reserved only for instances when the user explicitly cancels a drag via the escape or cmd-period key sequences.

## Help Manager

__Header file (HIToolbox): MacHelp.h__

#### Features and Enhancements

The Help Manager has always supported automatically adding an "<appname> Help" menu item to the the app's Help menu that will open the app's help book when selected. The implementation substitutes the application's name into a localized string to produce, for example, "My Great App Help".

In some languages it is necessary to use a different form of application name to get proper agreement with the localized word for "Help". The Help Manager now supports a new Info.plist key, "CFBundleHelpItemAppName", which can be customized to the proper form for the current language. If present, the value of this key are used instead of the application name for substitution in the format string.

For example, if you wanted your Help menu to contain "My Great App’s Help" instead of "My Great App Help", you could put a CFBundleHelpItemAppName key into your English InfoPlist.strings file and set the value of the key to be "My Great App’s".

Note that if you use this key in any localization, you must add it to all localizations.

## HIObjects

__Header file (HIToolbox): HIObject.h, HIArchive.h__

#### Features and Enhancements

The HIObject Manager supports several new APIs to allow attaching an HIObject as a delegate for Carbon events sent to another HIObject:

: HIObjectAddDelegate
: HIObjectRemoveDelegate
: HIObjectGetEventHandlerObject

(The last API, HIObjectGetEventHandlerObject, may also be useful in a normal non-delegate Carbon event handler.)

A delegate object may receive events sent to its target object either before or after the target object receives them. Using a delegate object is a convenient way to encapsulate the data and code for adding a particular behavior to an existing object, such as a standard HIToolbox view.

The HIArchiveCreateForDecoding API now supports a new option, kHIArchiveDecodingForEditor. This option is intended for use by UI editors that want to open an HIArchive without having the archived objects perform their typical actions when recreated from a nib. If this option is set, the kEventParamDecodingForEditor parameter of the kEventHIObjectInitialize and kEventHIObjectCreatedFromArchive events are set to true when these events are sent to objects in the archive.

The HIObjectRegisterSubclass API now supports a new option, kHIClassOptionSingleton. This option indicates that only a single instance of the class should be created. If HIObjectCreate is called more than once on the class ID of a singleton class, the first-created instance is returned each time (with an appropriate increment in the instance's refcount).

The kEventClassDelegate suite of Carbon events has been added. These Carbon events are for use by HIObject delegates. They allow a delegate object to be notified when it is installed on or removed from its target object, and to provide information about the behavior of the delegate.

A new API, HIObjectFromEventTarget, returns the HIObject that owns an EventTargetRef.

A new API, HIObjectCopyDelegates, returns a dictionary of the delegates that are attached to an HIObject.

A new Carbon event, kEventHIObjectCreatedFromArchive, is now sent to objects that are created from an XML-based or HIArchive-based nib file (4169417). The event is sent from within the call to CreateWindow/Menu/MenuBarFromNib. In order to handle this event, you need to use either a custom HIView embedded in a window, or an HIObject delegate object whose class ID is specified in the nib file. A typical use of this event would be to allow a custom HIView subclass to initialize its subviews after they have been created when the custom view is loaded from a nib file. In this example, your custom HIView would register for this event, and when the event was sent to your view's event handler, your view could locate and initialize its subviews.

A new sample HIObject delegate, HITextLengthFilter, is defined in HITextLengthFilter.h. This HIObject is designed to be instantiated by your application and installed as a delegate object on a text-editing object such as an EditUnicodeText view. Once installed as a delegate, the HITextLengthFilter object will ensure that the amount of text in the text-editing field is limited to a specific length (specified when you instantiated the HITextLengthFilter object).

#### Notable Bug Fixes

HIObjectCopyClassID may now be called from a kEventHIObjectConstruct handler without crashing (4347944).

## HIShape

__Header files (HIServices): HIShape.h__

#### Features and Enhancements

The HIShape API has been moved from HIToolbox (part of Carbon.framework) to HIServices (part of ApplicationServices.framework). Since Carbon.framework includes ApplicationServices.framework, this will not affect existing apps, but will allow apps that only link against ApplicationServices.framework to use the HIShape API.

New HIShape APIs have been added:

: HIShapeInset
: HIShapeSetWithShape
: HIShapeCreateXor
: HIShapeXor
: HIShapeEnumerate
: HIShapeCreateMutableWithRect
: HIShapeUnionWithRect

All of the APIs in HIShape.h are now thread safe, and are marked appropriately in the header documentation. Just the APIs themselves are thread safe -- HIShapeRefs are not. It is safe to call HIShape APIs on multiple threads, so long as no two threads try to operate on the same HIShapeRef at the same time. If you need multiple threads to operate on a single HIShapeRef at the same time, you must implement your own locking mechanism.

## HIToolbar

__Header file (HIToolbox): HIToolbar.h__

#### Features and Enhancements

A new API, HIToolbarItemCopyIconRef, returns the IconRef, if any, associated with a toolbar item.

Several new command IDs have been defined and are sent by the standard window view in order to request various toolbar behaviors:

: kHICommandToggleToolbar
: kHICommandToggleAllToolbars
: kHICommandCycleToolbarModeSmaller
: kHICommandCycleToolbarModeLarger

## HIView Manager

__Header files (HIToolbox): HIView.h, Controls.h, ControlDefinitions.h, various view-specific headers__
Note that the HIView Manager was previously known as the Control Manager.

#### Features and Enhancements

The view type and function declarations that were previously contained in ControlDefinitions.h and HIView.h have been split out into separate header files for easier maintainence and legibility. The new header files are:

: HIButtonViews.h
: HIClockView.h
: HIComboBox.h
: HIContainerViews.h
: HIDataBrowser.h
: HIDisclosureViews.h
: HIImageViews.h
: HILittleArrows.h
: HIMenuView.h
: HIPopupButton.h
: HIProgressViews.h
: HIRelevanceBar.h
: HIScrollView.h
: HISearchField.h
: HISeparator.h
: HISlider.h
: HITabbedView.h
: HITextViews.h
: HIWindowViews.h

ControlDefinitions.h now only contains declarations for views that are deprecated and considered obsolete: the non-Unicode EditText view, the ListBox view, the Picture view, and the Scrolling TextBox view.

A new set of APIs is available to manipulate the HIViewContentInfo structure introduced in OS X v10.4:

: HIViewSetImageContent
: HIViewCopyImageContentWithSize
: HIViewRetainImageContent
: HIViewReleaseImageContent

These APIs make it easier to set or retrieve the image content that is displayed by a view. The HIViewContentInfo structure has also been enlarged; new fields in this structure allow setting a view's image content to an IconRef specified by type and creator, an image file located in the application's Resources directory, or an image file located at a specified path. The views will automatically load an image file specified by name or path and create a CGImageRef from its contents.

These new fields in the HIViewContentInfo structure are supported by the following views: BevelButton, Icon, ImageWell, HIImageView, PushButton, RoundButton, Segment, and Tab.

A new API, HIViewSetSubviewsNeedDisplayInShape, allows invalidating both a view and all of its subviews. (The existing HIViewSetNeedsDisplay[InShape/Rect/Region] APIs only invalidate the specified view.)

A new API, HIViewAdvanceFocusWithOptions, allows more control over which view is focused. This API takes extra option bits to allow you to specify whether to focus traditionally or focus on any control, regardless of the user's current preferences. You can also prevent focus from wrapping around to the beginning or end of the view hierarchy.

Two new APIs, HIWindowGetFocus and HIWindowSetFocus, replace the existing SetKeyboardFocus and GetKeyboardFocus APIs. These APIs also allow you more control over whether a view becomes focused without consideration of the user's current focusing preferences.

Two new APIs, HIViewTrackMouseLocation and HIViewTrackMouseShape, provide view-centric equivalents of the TrackMouseLocation and TrackMouseRegion APIs (3123470).

A new API, HIViewSetUpTextColor, replaces the existing SetUpControlTextColor API. This API performs the same action as SetUpControlTextColor but with respect to the provided CGContextRef rather than the current port.

Two new APIs, HIImageViewGet/SetAutoTransform, allow image view images to automatically transform according to the state of the view (to behave like a deactivated/disabled ImageWell) (4030522).

Bevel buttons can now have implicit popup menu arrow sizes (2200323). Use SetControlData(..., kControlSizeTag, ...), where the default control size is kControlSizeAuto. kControlSizeAuto has the bevel button render its popup menu arrow at a size that is dependent on the size of the bevel button; this is the behavior on Tiger and earlier. kControlSizeNormal has it render the normal size arrow and kControlSizeSmall has it render the arrow small. All other sizes are invalid.

All views now automatically adjust the font of their title or label text to match the view's ControlSize. Previously, you needed to set an ControlFontStyle on the view to match its size; this is no longer necessary.

The Group Box view now supports the Normal, Small, and Mini sizes. Setting a ControlSize does not affect the appearance of the box, but it does cause the box label text to draw using an appropriately-sized font.

The Chasing Arrows view now supports the Normal and Large sizes. Previously, the view chose an image size based on its view bounds. This is still the default behavior, but you can now also force the control to pick a specific image size by setting the view's ControlSize.

Push buttons now support kControlPushButtonAnimatingTag to check if or control whether a button is animating (2903705).

The static text control now supports CFAttributedStringRefs. You can provide an attributed string to the static text control using HIViewSetText or SetControlData(kControlStaticTextCFStringTag). When using HIViewSetText, just cast the CFAttributedStringRef to a CFStringRef.

HIViewGetOptimalBounds (and GetBestControlRect) now take the title of a disclosure triangle into account when calculating (2231463). Also, the option to display the title has been exported through two new APIs: HIDisclosureTriangleSetDisplaysTitle and HIDisclosureTriangleGetDisplaysTitle. These APIs allow "drawTitle", set at creation in CreateDisclosureTriangleControl to be set on a disclosure triangle after it has been created.

The slider control's tick mark count and thumb orientation are now settable after the slider has been created via HISliderGetThumbOrientation, HISliderSetThumbOrientation, HISliderGetTickMarkCount and HISliderSetTickMarkCount (2780970). Note that the client application should explicitly resize the slider (to optimal bounds) to adjust for any thumb orientation or tick mark changes.

HIScrollView supports a new option, kHIScrollViewOptionsFillGrowArea, which requests that the scroll view should fill the grow area with white if both scrollbars are visible (3714266).

The HIObject class IDs for the Picture view and PopupArrow view have been added to ControlDefinitions.h. These class IDs are actually valid on Panther and later. It is possible to subclass these views on Panther and later as well, but in order to register your subclass on Panther and Tiger, you will first need to create an instance of the type of view you are subclassing, in order to force the view's class to be registered. On Leopard and later, these views will automatically register their HIObject classes, so it is not necessary to create an instance of the view before subclassing it.

The DataBrowser now supports kControlUseThemeFontIDMask in a ControlFontStyleRec.

The GDBShowControlHierarchy function now prints the entire control hierarchy of a window, starting from the window's root view. It previously started from the window's content view.

HIWindowViews.h now declares the HIViewIDs for all of the standard window frame views. Previously, only the view IDs for the content and grow box views were declared. Note that the window frame views use these view IDs on all versions of OS X since OS X v10.2, so even though the variables aren't exported, you can still declare your own HIViewID variables with the same contents if you need to access these views on earlier OS releases.

The kEventControlInterceptSubviewClick event now contains a DirectObject parameter, as documented (4450275).

A new Carbon event, kEventControlFocusPartChanged, is now sent when a view's focused part has changed. This event is easier and more obvious to use than the old technique to detect when a view's focus changed, which was to handle the kEventControlSetFocusPart event, call CallNextEventHandler, and then retrieve the output focus part.

The standard text-editing views now support spell-checking. Two new ControlData tags, kControlEditTextSpellCheckingTag and kControlEditTextSpellCheckAsYouTypeTag, may be used with Get/SetControlData to enable, disable, and inspect the current spell-checking state of a view.

The Data Browser view now supports a compositing custom draw event kEventClassDataBrowser/kEventDataBrowserDrawCustomItem.

The kControlContentAlertIconRes constant has been added to Controls.h, and the kHIViewAlertIconType constant has been added to HIView.h (2730877). The kControlContentAlertIconRes constant, actually supported in OS X v10.1 and later, is used in the contentType field of a ControlImageContentInfo structure to tell an Icon control to draw a Note, Caution, or Stop icon using the approved Aqua appearance. On recent versions of OS X, the Note and Stop icons are replaced by the application's icon, and the Caution icon is drawn with the application's icon as a badge. When using this content type with an Icon control, you should set the size of the control to 64x64. Likewise, the kHIViewAlertIconType constant is used in the contentType field of a HIViewContentInfo structure. This content type is supported by most controls that allow customizable image content on OS X v10.5 and later.

The HIViewShowsFocus API is provided to allow custom HIViews to determine whether they should draw focus indicators such as focus rings.

The HIViewSetTextFont, HIViewSetTextHorizontalFlush, HIViewSetTextVerticalFlush, HIViewSetTextTruncation, and HIViewGetThemeTextInfo APIs are provided to allow callers to set and query custom font and text attributes for controls that draw text. New Control tags are available for Get/SetControlData for custom views: kControlThemeTextFontTag, kControlThemeTextHorizontalFlushTag, kControlThemeTextVerticalFlushTag, kControlThemeTextTruncationTag, and kControlThemeTextInfoTag.

A new API, HIViewDrawNSImage, allows an HIView to draw NSImage content into the CGContextRef provided during the kEventControlDraw event.

The Clock control supports a new ControlData tag, kControlClockAbsoluteTimeTag, which allows setting or getting the clock time using a CFAbsoluteTime.

The Data Browser view supports two new attributes for use with DataBrowserChangeAttributes. The first, kDataBrowserAttributeAutoHideScrollBars, allows the Data Browser instance to automatically hide its horizontal and vertical scroll bars when they aren't necessary. The second, kDataBrowserAttributeReserveGrowBoxSpace, tells the Data Browser instance to always preserve room for a grow box at the bottom right of the view. The AutoHideScrollBars attribute is currently only implemented for list view; it may be set on a DataBrowser in column view, but currently has no effect. The ReserveGrowBoxSpace attribute is implemented for both list and column view.

The kEventControlTrackingAreaEntered and Exited events now include a DirectObject parameter containing the HIViewRef that is receiving the event (5198507).

When an HIView is archived, it now automatically archives all of its subviews for which HIObjectIsArchivingIgnored returns false.

The EditUnicodeText and HITextView controls now support drag and drop.

#### Notable Bug Fixes

The popup button now positions its menu so that the menu item text aligns with the button title.

Setting kControlTabInfoTag on a disabled tab no longer enables that tab. If you were relying on this undocumented and undesired side-effect, you may discover that your tabs are now disabled.

The bevel button, image well, icon, and picture views now call HIViewSetNeedsDisplay on themselves after SetControlData is used to modify any aspect of the view that affects its visual appearance.

The popup button once again supports drawing its button title using the style and font of the selected menu item (3385698). This capability was available in Mac OS 9 and early versions of OS X, but was broken in OS X v10.3 and 10.4.

All views now automatically invalidate themselves when the view's ControlSize changes if the view is being used in composited mode. Previously, most views did not invalidate themselves.

It is now possible to make the round button cease to be a help button by setting its ControlImageContentInfo.contentType to kControlContentNone (4413403).

The HIViewCreateOffscreenImage API now supports being passed the root view of a window (4431494). Previously, passing the root view would corrupt the root view's state such that subsequent Quickdraw-based drawing in the window would not appear.

#### Notes

Currently, an HICocoaView cannot be embedded in an HIScrollView. To workaround this, embed your scrollable content in an NSScrollView and associate that with the HICocoaView instead.

Using an HICocoaView in your app requires that you call NSApplicationLoad() at init time. Also, for building, be sure to link to the appropriate frameworks that contain the NSView of interest (e.g. AppKit.framework) and that the module compiles with the ObjC or ObjC++ compiler.

## IBCarbonRuntime

__Header file (HIToolbox): IBCarbonRuntime.h__

#### Features and Enhancements

IBCarbonRuntime now supports the ability to create subclasses of the standard controls and views. A future version of InterfaceBuilder will allow you to set the HIObject class ID and init event parameters of standard controls when editing a nib file. When the nib file is loaded into memory, IBCarbonRuntime will create an instance of your custom class rather than of the standard control. You are responsible for ensuring that your custom class actually is registered as a subclass of the standard class for that control type.

#### Notable Bug Fixes

If you use InterfaceBuilder to assign a command ID to a menu title in the menubar, you are now able to find that item in the root menu with GetIndMenuItemWithCommandID after calling SetMenuBarFromNib (3518358). For example, you could give your File menu a command ID of 'FILE' in InterfaceBuilder, and then use GetIndMenuItemWithCommandID( NULL, 'FILE', 1, &menu, &item ) to find the item in the root menu that contains the File menu. You could then use GetMenuItemHierarchicalMenu( menu, item, &fileMenu ) to get the MenuRef for the File menu. Note that you must use SetMenuBarFromNib to enable this behavior; you cannot use CreateMenuBarFromNib and then SetMenuBar, because the MenuBarHandle returned by CreateMenuBarFromNib has no room to keep the command ID for a top-level menu.

When creating a DataBrowser from a nib, the row height specified in the nib is now obeyed (4234674). Previously, the row height was ignored, and you had to call SetDataBrowserTableViewRowHeight yourself after creating the DataBrowser control.

When loading an object from an HIArchive-based nib, the CreateWindowFromNib and CreateMenuFromNib APIs now ensure that you get a new instance of the object each time, even if you are using the same IBNibRef (4424629). In Tiger, it is necessary to release the IBNibRef and reallocate it between multiple calls to get the same object from the nib in order to ensure that you get a new object each time; otherwise, you'll get back the same object with an incremented refcount.

## Icon Services

__Header file (HIServices): Icons.h__

#### Features and Enhancements

The Icon Services Manager provides three new APIs for combining IconRefs with modern HI types:

: IconRefContainsCGPoint
: IconRefIntersectsCGRect
: IconRefToHIShape

A new API, GetIconRefFromComponent, returns an IconRef based on the componentIconFamily field of the component's 'thng' resource. This API replaces GetComponentIconSuite, which has been removed from the 64-bit API.

#### API Deprecation

Most APIs for working with classic icon formats are now deprecated in Leopard, including:

: GetCIcon
: PlotCIcon
: DisposeCIcon
: GetIcon
: PlotIcon
: PlotIconID
: NewIconSuite
: AddIconToSuite
: GetIconFromSuite
: ForEachIconDo
: GetIconSuite
: DisposeIconSuite
: PlotIconSuite
: MakeIconCache
: LoadIconCache
: PlotIconMethod
: GetLabel
: PtInIconID
: PtInIconSuite
: PtInIconMethod
: RectInIconID
: RectInIconSuite
: RectInIconMethod
: IconIDToRgn
: IconSuiteToRgn
: IconMethodToRgn
: SetSuiteLabel
: GetSuiteLabel
: GetIconCacheData
: SetIconCacheData
: GetIconCacheProc
: SetIconCacheProc
: PlotIconHandle
: PlotSICNHandle
: PlotCIconHandle
: IconFamilyToIconSuite
: IconSuiteToIconFamily
: GetIconRefFromFile
: RegisterIconRefFromResource
: OverrideIconRefFromResource
: RegisterIconRefFromIconFile
: ReadIconFile
: WriteIconFile

In addition, some QuickDraw-based IconRef APIs are now deprecated:

: PlotIconRef
: PtInIconRef
: RectInIconRef
: IconRefToRgn

## Keyboard Manager

__Header file (HIToolbox): Keyboards.h__

#### API deprecation

Except for KBGetLayoutType, all of the functions in Keyboards.h are deprecated in Leopard and unavailable in the 64-bit API. The preferred alternatives are the functions in TextInputSources.h.

#### Notable Bug Fixes

KLGetCurrentKeyboardLayout previously returned the Script Manager's notion of current key layout - that is, the keyboard layout with numeric ID corresponding to GetScriptVariable( GetScriptManagerVariable(smKeyScript), smScriptKeys ). This had several problems: it would not return a Unicode-only layout if it was the current layout; it would not always return the current key layout in use if the calling application was not in focus; and it would not reflect the effect of key layout overrides, e.g. from calling TISSetInputMethodKeyboardLayoutOverride. Now KLGetCurrentKeyboardLayout returns the key layout that corresponds to the result of TISCopyCurrentKeyboardLayoutInputSource, which addresses these problems.

KLSetCurrentKeyboardLayout now also sets the keyboard layout override for input methods (effectively calling TISSetInputMethodKeyboardLayoutOverride).

KLGetKeyboardLayoutProperty now returns resNotFound if the requested property is kKLKCHRData but the value is NULL. This is a much more common scenario now that KCHR data is not available for many Apple-supplied keyboard layouts (for which the preferred format is uchr).

## Keyboard Resources

#### Features and Enhancements

The preferred format for keyboard layout data is the 'uchr' Unicode format. Accordingly, all Apple keyboard layouts have been converted to 'uchr' format. This keyboard layout data is available through the TISGetInputSourceProperty function (or through the deprecated KLGetKeyboardLayoutProperty function). KCHR-format data is still available for some of these layouts, but only through KLGetKeyboardLayoutProperty or GetResource.

HIToolbox provides KCAP resources describing the physical layout of various Apple keyboards.
These were not up to date in Tiger, but have now been updated to include KCAP resources for the desktop keyboards with F16 keys, for the keyboards in the PowerBook and MacBook Pro computers introduced in 2005, and for the new thin keyboards introduced with the new iMacs in August 2007.

## List Manager

__Header file (HIToolbox): Lists.h__

#### API Deprecation

The entire List Manager has been deprecated for Leopard. Applications should use the DataBrowser instead of the List Manager.

## Menu Manager

__Header file (HIToolbox): Menus.h__

#### Features and Enhancements

The Menu Manager now provides several new APIs to support embedding an HIView inside a menu item, as seen in the Finder's label color picker. These APIs are:

: HIMenuSetItemViewClass
: HIMenuCopyItemViewClass
: HIMenuGetItemView
: HIMenuItemViewGetEnclosingMenuItem
: HIMenuItemViewCancelMenuTracking

To embed an HIView in a menu item, an application simply calls HIMenuSetItemViewClass, passing the menu, menu item, HIObject class ID, and an optional initialization EventRef. The Menu Manager automatically instantiates the HIView as necessary when the menu is displayed. Note that the Menu Manager may choose to create more than one instance of a view, if the menu happens to be displayed in more than one window.

A menu item view must support the kEventControlGetOptimalBounds Carbon event to return its preferred size. The Menu Manager will send this event during CalcMenuSize to determine how much space to allocate for the menu item view. A menu item view may send the new kEventControlOptimalBoundsChanged Carbon event to itself if its optimal bounds changes; this will cause the menu size to be recalculated and the menu to be resized.

Once an HIView has been embedded in a menu item, the Menu Manager provides the following features automatically:

- The view is resized to fit the width of the menu. Its height will be set to the optimal height returned by the view.
- The view is positioned to track the position of the menu item in the menu. The view will be repositioned if other menu items are inserted or removed in front of the item containing the view. The view will scroll with the rest of the menu contents.
- The Menu Manager does not draw the normal contents of the menu item. The view is responsible for all drawing of the menu item.
- The view is inserted into the accessibility hierarchy as a child of the menu item.
- The view is available for keyboard navigation. When the mouse passes over the view, the Menu Manager automatically attempts to focus on the first part of the view, allowing keyboard navigation within the view. Once focus is on a view part, the user may use Tab and Shift-Tab to move forwards and backwards within the's view's parts; when the focus reaches the last or first part in the view, the next Tab/Shift-Tab will close the current menu and open the next menu. Keyboard events are routed first to the view; if the view does not handle a keyboard event, the Menu Manager will provide its default keyboard navigation handling.

In general, an HIView does not need any special awareness that it has been embedded in a menu; the standard HIView Carbon events are sufficient. In some cases, a view may wish to vary its behavior when it is embedded. A view can use the HIMenuItemViewGetEnclosingMenuItem API to determine if it, or any superview, is embedded inside a menu item.

The Menu Manager now supports dynamic resizing of an open menu. Any changes to a menu that occur while the menu is open (such as insertion or removal of menu items, hiding or showing items, or changing an item's text) will now cause the menu size to be recalculated and the menu window to resize appropriately. As part of this change, menus with dynamic items are now sized to fit just the currently visible items, and the menu resizes as the user presses the modifier keys to fit the newly visible dynamic items.

The kEventMenuEndTracking event now contains an EventRef parameter with the event that caused menu tracking to end. This may be useful for applications that wish to vary their behavior depending on exactly how a menu item was selected.

When a menu content view or another view embedded inside the content view of a menu receives a kEventControlSimulateHit event, the KeyModifiers parameter of the event now contains the most recently-pressed key modifier combination (4697376). Previously, it always contained zero. This change is meant to allow views that customize their behavior based on the modifiers to be able to easily access the modifier state.

The kEventMenuDrawItem and kEventMenuDrawItemContent Carbon events that are sent when a menu item has the kMenuItemAttrCustomDraw attribute now include a new event parameter, kEventParamMenuContextHeight. This parameter contains the height by which the context should be flipped to convert it from Cartesian to HIView-oriented coordinates. Previously, we recommended that you use the height of the current port to flip the context, and this recommendation is still valid in 32-bit mode, but 64-bit mode does not have a current port, so this new event parameter provides the necessary information.

Two new APIs, HIMenuSetAttributedItemText and HIMenuCopyAttributedItemText, allow a CFAttributedStringRef to be provided for a menu item. An item may have both attributed and non-attributed strings; setting an attributed string does not affect the non-attributed item text provided with SetMenuItemTextWithCFString. The Menu Manager will draw the menu item using the attributed text, but performs menu type-selection using the non-attributed text, so it is recommended that you always provide both. The non-attributed text is also used for accessibility.

Two new APIs, HIMenuSetFont and HIMenuCopyFont, allow a CTFontRef to be provided for a menu or menu item. Setting a font for a menu causes all items in the menu to be drawn with that font by default.

New "attributedText" and "font" fields have been added to the MenuItemDataRec structure to allow accessing an item's attributed text or a menu or item's CTFontRef. The kMenuItemDataAttributedText constant is now available to specify that the attributedText field should be used when setting or retrieving item data, and the kMenuItemDataFont constant is now available for accessing the font.

A new API, HIMenuSetSelection, allows setting the initial selection in a menu before the menu opens, or changing the selected item of an open menu.

A new API, HIMenuCopyParents, returns an array of the parent menus of a submenu (2811173).

When a menu uses a custom CTFontRef for all menu content (via HIMenuSetFont with the item parameter set to zero), the font is now applied to all submenus of the menu as well. For compatibility with existing applications, a menu with a custom QD font does not apply this font to its submenus.

#### User Interface Changes

When PopUpMenuSelect or ContextualMenuSelect is asked to display a popup menu, and the menu has zero width or height, these APIs now return immediately and do not enter a mouse-tracking loop (4058048).

The ContextualMenuSelect API has previously displayed a disabled Help menu item as the first item in the menu when passed the kCMHelpItemNoHelp or kCMHelpItemAppleGuide constants (2580665). The API has been changed so that passing these constants results in no Help item being displayed at all. A help item will now only be displayed if the application passes kCMHelpItemOtherHelp and its own help string.

The default positions for menu title and menu item help tags have changed (2828041). A menu title help tag with a tagSide of kHMDefaultSide is now displayed using kHMInsideBottomLeftCorner. A menu item help tag with a tagSide of kHMDefaultSide is now displayed using kHMOutsideRightTopAligned. The menu item positioning change, in particular, was meant to avoid obscuring other menu items.

#### API Deprecation

The MenuDefProcPtr type and all related menu definition functionality are deprecated for Leopard. Custom menu appearance and behavior should be implemented using a custom HIView, available in OS X v10.3 and later.

The following APIs are deprecated for Leopard:

: NewMenu
: GetMenuTitle
: SetMenuTitle
: AppendMenu
: InsertMenuItem
: AppendMenuItemText
: InsertMenuItemText
: SetMenuItemText
: GetMenuItemText
: SetItemIcon
: GetItemIcon
: SetMenuItemHierarchicalID
: GetMenuItemHierarchicalID
: GetMenuRetainCount
: RetainMenu
: ReleaseMenu
: InsertResMenu
: AppendResMenu
: InsertFontResMenu
: InsertIntlResMenu
: MenuKey
: SetMenuFlashCount
: DeleteMCEntries
: GetMCInfo
: SetMCInfo
: DisposeMCInfo
: GetMCEntry
: SetMCEntries
: EraseMenuBackground
: ScrollMenuImage
: InitContextualMenus

#### Notable Bug Fixes

It is now possible to use SetMenuItemIconHandle with the kMenuIconResourceTypeIcon icon type to provide an icon for a menu item in a window's Dock tile menu (4102535). Previously, this icon type only worked for an application's Dock tile menu.

When a menu item provided by a Contextual Menu plugin is added to the contextual menu, the item's command ID is now set to the command ID specified by the plugin (4161281). This allows a plugin to find its own menu items later, if necessary, via a kEventMenuOpening event handler installed on the application event target.

When unarchiving a menu, its menu ID and menu title enable state are properly restored (4240282). Previously, an unarchived menu would always have a menu ID of zero and the menu title would always be enabled.

The HIMenuViewGetMenu API now works properly for instances of the standard menu view (4137825). Previously, it returned NULL.

## MLTE

__Header file (HIToolbox): MacTextEditor.h__

#### Features and Enhancements

The TXNShowOffset API is provided to allow MLTE clients to show any offset, including offsets that are not part of the selected range.

MLTE now supports a subset of emacs control key combinations (control+BFPNAEHD). There is no support for control+KL at this time.

TXNControlData::uValue and TXNControlData::sValue changed from UInt32/SInt32 to unsigned long/long for 64-bit compatibility.

#### API Deprecation

Deprecated all QD TXNTypeRunAttributes/TXNTypeRunAttributeSizes constants since QuickDraw is deprecated in 32-bit and does not exist in 64-bit mode.

Deprecated TXNSetFontDefaults and TXNGetFontDefaults.

## Navigation Services

__Header File: Navigation.h__

#### Features and Enhancements

In Leopard, Navigation Services has been reimplemented atop Cocoa's NSSavePanel. A NavDialogRef may be cast to an NSSavePanel\* for put dialogs, an NSOpenPanel\* for get and choose dialogs and an NSAlert\* for the various ask save changes dialogs. Once cast to the appropriate Cocoa object you can call Cocoa APIs on that object normally. For instance, the custom area of the Nav dialog may be populated with Cocoa NSViews [(NSSavePanel\*)myNavDialogRef setAccesoryView:myNSView]. Exception: Once a dialog is created via the NavgationServices API it must be invoked with NavDialogRun. Custom preview support is no longer available on Leopard. NavPreview procedures are no longer called, the kNavCBAdjustPreview Nav event callback messages are no longer sent and the NavCBRec previewRect field will always be empty. Navigation Services now depends on QuickLook for preview rendering. Clients may write a QuickLook plug-in to generate custom previews for open dialogs as well as Finder and Spotlight.

#### API Deprecation

The legacy NavFooFile APIs have been deprecated for Leopard. Use the NavCreateFooDialog APIs instead.

The following APIs are deprecated for Leopard:

: NavLoad
: NavUnload
: NavLibraryVersion
: NavGetDefaultDialogOptions
: NavGetFile
: NavPutFile
: NavAskSaveChanges
: NavCustomAskSaveChanges
: NavAskDiscardChanges
: NavChooseFile
: NavChooseFolder
: NavChooseVolume
: NavChooseObject
: NavNewFolder
: NavTranslateFile
: NavServicesCanRun
: NavServicesAvailable

#### Notable Bug Fixes

The kNavCBPopupMenuSelect header documentation has been updated on how to better identify when a client's type menu item has been selected (4087669).

## Pasteboard Manager

__Header file (HIServices): Pasteboard.h__

#### Features and Enhancements

Addition of the PasteboardSet/GetStandardPasteLocation and PasteboardSet/GetItemBounds APIs allows clients to perform what used to be drag-specific operations on any pasteboard.

Addition of Pasteboard file url-based file promising with kPasteboardTypeFileURLPromise and kPasteboardTypeFilePromiseContent.

## Scrap Manager

__Header file (HIToolbox): Scrap.h__

#### API Deprecation

The entire Scrap Manager has been deprecated for Leopard. Use the Carbon Pasteboard APIs instead.

The following APIs are deprecated for Leopard:

: LoadScrap
: UnloadScrap
: GetScrapByName
: GetCurrentScrap
: GetScrapFlavorFlags
: GetScrapFlavorSize
: GetScrapFlavorData
: ClearCurrentScrap
: ClearScrap
: PutScrapFlavor
: SetScrapPromiseKeeper
: GetScrapFlavorCount
: GetScrapFlavorInfoList
: CallInScrapPromises

## Script Manager

__Header file (HIToolbox): Events.h__

#### API Deprecation

The KeyScript function is deprecated in Leopard and unavailable in the 64-bit API.

Positive verbs (i.e. ScriptCode) are replaced by the new TextInputSource API in TextInputSources.h.

Negative verbs used to either restrict access to keyboard input sources in the context of a text field, or to disable keyboard switching altogether, are replaced as "input context state" via 2 new TSMDocument properties in TextServices.h:

: kTSMDocumentEnabledInputSourcesPropertyTag
: kTSMDocumentInputSourceOverridePropertyTag

## Text Input Sources

__Header file (HIToolbox): TextInputSources.h__
 (also see Text Services Manager)

#### Features and Enhancements

This is a new API set designed to replace the text input management functions of Script Manager and Text Services Manager.
Most usage of the Script Manager is deprecated, and usage of the Text Services Manager should focus on management of text input context.
The Text Input Sources API provide the modern way to find information about text input sources, select/enable/disable them, and receive notifications about relevant changes.

Text input sources are of three general categories:

- Keyboard input sources (keyboard layouts, keyboard input methods and input modes)
- Palette input sources (e.g. Character Palette, Keyboard Viewer)
- Ink

A specific text input source is identified with a TISInputSourceRef, which refers to a CF object. The polymorphic CFBase functions can be used on this (CFRetain, CFRelease, etc.).

Each text input source has associated properties. The function TISGetInputSourceProperty can obtain the value of a specified property for a specified input source. The value associated with each property is a specific pointer type (e.g. CFStringRef, CFNumberRef, IconRef); TISGetInputSourceProperty returns a void\* for the specified value.

Property keys include the following:

- kTISPropertyInputSourceCategory
- kTISPropertyInputSourceType
- kTISPropertyInputSourceIsASCIICapable
- kTISPropertyInputSourceIsSelectable
- kTISPropertyInputSourceIsEnabled
- kTISPropertyInputSourceIsSelected
- kTISPropertyInputSourceID
- kTISPropertyBundleID
- kTISPropertyInputModeID
- kTISPropertyLocalizedName

(the following cannot be used in the dictionary passed to TISCreateInputSourceList)

- kTISPropertyInputSourceLanguages
- kTISPropertyUnicodeKeyLayoutData
- kTISPropertyIconRef
- kTISPropertyIconImageURL

The function TISCreateInputSourceList is used to obtain an array of TISInputSourceRefs matching a filter dictionary of property keys and corresponding values.

There are convenience functions for obtaining TISInputSourceRefs for various kinds of input sources:

- TISCopyCurrentKeyboardInputSource
- TISCopyCurrentASCIICapableKeyboardInputSource
- TISCopyCurrentASCIICapableKeyboardLayoutInputSource
- TISCopyInputSourceForLanguage
- TISCreateASCIICapableInputSourceList

Functions for manipulating input sources include:

- TISSelectInputSource
- TISDeselectInputSource
- TISEnableInputSource
- TISDisableInputSource

CF distributed notifications for input source changes include:

- kTISNotifySelectedKeyboardInputSourceChanged
- kTISNotifyEnabledKeyboardInputSourcesChanged

Functions that pertain to input methods include:

- TISSetInputMethodKeyboardLayoutOverride
- TISCopyInputMethodKeyboardLayoutOverride
- TISRegisterInputSource

Performance improvement: When rebuilding the registry of text input sources (due to the addition or removal of a source, for example), only the portion that corresponds to non-Apple input sources is rebuilt.

Add support for datafile input methods: Text files of type ".cin" or ".inputplugin" (in [~]/Library/Input Methods/) that specify behavior for a particular style of CJK text input.

Support new plist keys TISInputSourceID, TISIntendedLanguage for input methods/modes (as described in TextInputSources.h).

Support new plist keys TISInputSourceID, TISIntendedLanguage for key layouts (as described in textInputSources.h).

Add support for InputMethodKit-based palette input methods (plist key InputMethodType = palette).

## Text Services Manager

__Header file (HIToolbox): TextServices.h__
(also see Text Input Sources)

#### Features and Enhancements

TSM supports input methods based on the new IMKit.
These input methods are located in "/Library/Input Method/" directories in the various /System, /, or ~/ domains.

TSM Carbon Events (kEventClassTextInput, kEventClassTSMDocumentAccess)

- 64-bit

typeRefCon, typeByteCount, typeByteOffset

TSM events now specify these 64-bit friendly types instead of the old typeLongInteger (really a typeSInt32).
See notes in CarbonEvents section and documentation in CarbonEvents.h for automatic type coercion between typeLongInteger
and the modern types for binary compatibility on 32-bit.

- Modern TSM event parameters and types - equivalence with older parameter "sets"

: typeCTFontRef
: typeGlyphInfoRef
: typeCFAttributedStringRef

TSM has defined modern event parameters with the above types in a way that is binary compatible with the existing
event parameter sets. TSM is able to "promise" either the new parameter or members of the old parameter set by inspecting
an event both before it is dispatched to an application and before it is returned to an input method.
TSM can do this because input methods always dispatch via the SendTextInputEvent bottleneck API.

: kEventTSMDocumentAccessGetFont

kEventParamTSMDocAccessReplyCTFontRef (typeCTFontRef) encapsulates the following parameters:
kEventParamTSMDocAccessReplyATSFont
kEventParamTSMDocAccessReplyFontSize

: kEventTSMDocumentAccessGetGlyphInfo

kEventParamTSMDocAccessReplyCTGlyphInfoRef (typeCTGlyphInfoRef) can be requested instead of:
kEventParamTSMDocAccessReplyATSUGlyphSelector (typeGlyphSelector)

: kEventTextInputUnicodeForKeyEvent

kEventParamTextInputSendAttributedString (typeCFAttributedStringRef) encapsulates the following
parameters:

: kEventParamTextInputSendText
: kEventParamTextInputSendGlyphInfoArray

: kEventTextInputUpdateActiveInputArea

kEventParamTextInputSendAttributedString (typeCFAttributedStringRef) encapsulates the following
parameters:

: kEventParamTextInputSendText
: kEventParamTextInputSendUpdateRng
: kEventParamTextInputSendHiliteRng
: kEventParamTextInputSendClauseRng
: kEventParamTextInputSendPinRng
: kEventParamTextInputSendGlyphInfoArray

- Support resolution independence in TSM events

: typeHIPoint instead of typeQDPoint

CarbonEvents provides automatic type coercion for binary compatibility (on 32-bit only).

: typeHIPoint parameters in TSM events can be accessed using any of the variants that specify the coordinate

space of interest, i.e. typeHIPointScreenPixel.

: typeCGFloat replaces TSM use of the following types:
: typeFloat (see kEventParamTSMDocAccessReplyFontSize)

See detailed note on use of the old typeFloat (typeIEEE64BitFloatingPoint) in CarbonEvents.h for
this event parameter.

: typeFixed (see kEventParamTextInputReplyPointSize)

: typeSInt16 (see kEventParamTextInputReplyLineHeight, kEventParamTextInputReplyLineAscent)

Note that LineHeight and LineAscent can be accessed using the coordinate space variants
of typeCGFloat, such as typeCGFloatScreenPixel

- Event Parameter deprecation

: typeComponentInstance

The typeComponentInstance parameters are deprecated with TSM support for non-Component based
input methods (see kEventParamTSMDocAccessSendComponentInstance and
kEventParamTextInputSendComponentInstance)

: typeIntlWritingCode

The typeIntlWritingCode event parameters are deprecated. Most input methods are Unicode-based, and for
those that aren't, the ScriptCode can be inferred using the new TextInputSource API. In particular you can query the
kTISPropertyInputSourceLanguages property of the input source returned by TISCopyCurrentKeyboardInputSource.

Improved performance of ActivateTSMDocument (mostly eliminated calls to KLGetKeyboardLayoutProperty).

Some TSM Carbon event parameters that had changed in Leopard to use the new typeByteCount/typeByteOffset, and later typeCFIndex (for signedness), now use the explicit types typeSignedByteCount/typeSignedByteOffset. This is because typeCFIndex conveys some semantics when dealing with UniChar text buffers. The event parameters that use these new types are:

```
    kEventParamTextInputSendFixLen
    kEventParamTextInputSendTextOffset
```

See CarbonEvents.h for more information on these.

#### API Deprecation

All TSM API that deal with InputSource management have been deprecated and replaced by new TextInputSource (TIS) API
in TextInputSources.h:

: GetServiceList
: SetDefaultInputMethod
: GetDefaultInputMethod
: SetTextServiceLanguage
: GetTextServiceLanguage
: GetDefaultInputMethodOfClass
: SetDefaultInputMethodOfClass
: SelectTextService
: DeselectTextService
: IsTextServiceSelected

: TSMCopyInputMethodEnabledInputModes
: TSMSelectInputMode

Other deprecated API:

: OpenTextService
: CloseTextService
: SendAEFromTSMComponent
: TSMSetInlineInputRegion
: GetScriptLanguageSupport

: TSMInputModePaletteLoadButtons
: TSMInputModePaletteUpdateButtons
: InputModePaletteItemHit
: GetInputModePaletteMenu

The following functions are not formally deprecated but are not available in the 64-bit API:

: NewTSMDocument
: DeleteTSMDocument
: ActivateTSMDocument
: DeactivateTSMDocument
: FixTSMDocument
: SendTextInputEvent
: UseInputWindow
: InitiateTextService
: TerminateTextService
: ActivateTextService
: DeactivateTextService
: GetTextServiceMenu
: TextServiceEventRef
: FixTextService
: HidePaletteWindows
: GetTextServiceProperty
: SetTextServiceProperty
: CopyTextServiceInputModeList

#### Notable Bug Fixes

Fixed problems in which typing Korean or Chinese characters in the middle of a Latin-script dead-key sequence would produce Latin characters.

Fixed problems that prevented typing Chinese/Japanese/Korean in SecurityAgent's login window.

Fixed an issue with use of JIS keyboard kana key in Setup Assistant user registration fields.

Fixed a problem in which Carbon menu tracking could set the active TSMDocument to NULL for basic applications that only use the default TSMDocument (such as some basic Cocoa applications).

Fixed problems with Command-space (switch to previous input source) and JIS keyboard kana key not working after upgrade install.

When activating an input method (e.g. in ActivateTSMDocument), make sure to clear any previous key layout overrides before calling input method's activation.

Latin-script dead-key input was not working for key layouts without a 'KCHR' key layout resource (i.e. key layouts with only 'uchr'-format key layout data).

Prevent loss of unconfirmed Chinese text input when switching applications.

Improve the fix for clearing previous input method key layout overrides when activating.

Fixed more problems for key layouts with no 'KCHR' resource (only 'uchr' data): (1) An incorrect internal error caused a crash in Spotlight Preferences and other problems; (2) Can't type non-Mac-script characters in some cases (if the key layout specified by the Script Manager also has no 'KCHR' resource.

## Window Manager

__Header file (HIToolbox): MacWindows.h__

#### Features and Enhancements

Since QuickDraw is deprecated in 32-bit and does not exist in 64-bit mode, we are adding new API that uses CGDirectDisplayID instead of GDHandle, HIRect instead of Rect, and so on. The following APIs have been added:

: HIWindowCreate (replaces CreateNewWindow, CreateCustomWindow)
: HIWindowGetBounds (replaces GetWindowBounds)
: HIWindowSetBounds (replaces SetWindowBounds)
: HIWindowTrackProxyDrag (replaces TrackWindowProxyDrag and TrackWindowProxyFromExistingDrag)
: HIWindowGetIdealUserState (replaces GetWindowIdealUserState)
: HIWindowSetIdealUserState (replaces SetWindowIdealUserState)
: HIWindowIsInStandardState (replaces IsWindowInStandardState)
: HIWindowCopyShape (replaces GetWindowRegion)
: HIWindowConstrain (replaces ConstrainWindowToScreen)
: HIWindowFindAtLocation (replaces FindWindow and friends)
: HIWindowGetGreatestAreaDisplay (replaces GetWindowGreatestAreaDevice)
: HIWindowGetAvailablePositioningBounds (replaces GetAvailableWindowPositioningBounds)
: HIWindowCopyAvailablePositioningShape (replaces GetAvailableWindowPositioningRegion)
: HIWindowCreateCollapsedDockTileContext (replaces CreateQDContextForCollapsedWindowDockTile)
: HIWindowReleaseCollapsedDockTileContext (replaces ReleaseQDContextForCollapsedWindowDockTile)

Because the Dock's tile size can now change dynamically, applications that use HIWindowCreateCollapsedDockTileContext should be prepared to redraw their Dock tile as necessary. The kEventWindowUpdateDockTile Carbon event is now sent when the application needs to redraw a collapsed window's Dock tile.

The Window Manager now provides more than 32 window attribute bits, and so the attribute bit mask no longer fits in the 32-bit WindowAttributes type. Therefore, we have introduced new APIs to support an arbitrary number of attribute bits:

: HIWindowTestAttribute
: HIWindowChangeAttributes
: HIWindowIsAttributeAvailable

These new APIs use a new set of constants, prefixed with "kHIWindowBit", that are bit numbers, not bit masks. You must not use the older kWindowFooAttribute constants with these new APIs; you must only use the kHIWindowBit constants. Likewise, you must not use the kHIWindowBit constants with the older ChangeWindowAttributes API.

These new window attributes are now available:

: kHIWindowBitTexturedSquareCorners (also as kWindowTexturedSquareCornersAttribute)
: kHIWindowBitUnifiedTitleAndToolbar (also as kWindowUnifiedTitleAndToolbarAttribute)
: kHIWindowBitCanBeVisibleWithoutLogin (also as kWindowCanBeVisibleWithoutLoginAttribute)
: kHIWindowBitDoesNotHide
: kHIWindowBitAutoViewDragTracking
: kHIWindowBitRoundBottomBarCorners

kHIWindowBitTexturedSquareCorners indicates that a textured (metal) window has square corners, rather than the default round corners.

kHIWindowBitUnifiedTitleAndToolbar is actually supported on OS X v10.4 and later (see Q&A 1423). This attribute specifies that a window uses a unified appearance for its title and toolbar, with no separator drawn between the two areas. Since all windows use the unified appearance on Leopard, it is not necessary to set this attribute on Leopard.

kHIWindowBitCanBeVisibleWithoutLogin indicates that a window can be made visible prior to user login. By default, in Leopard and later no windows can be visible before a user logs into the system; this protects the user against certain types of malicious use of insecure applications. However, some software, such as input methods or other accessibility software, may need to deliberately make windows available prior to user login. Such software should add this window attribute to its windows.

kHIWindowBitDoesNotHide controls whether a window will hide when its application is hidden (3184642). By default, Utility-class windows have this bit set, and windows of other classes do not.

kHIWindowBitAutoViewDragTracking controls whether a window supports automatically sending kEventControlDrag\* Carbon events to views within the window. This window attribute is a replacement for the SetAutomaticControlDragTrackingEnabledForWindow API. Setting the attribute is exactly the same as calling the API. The API will be deprecated in a future release of OS X.

kHIWindowBitRoundBottomBarCorners applies to windows that do not use the kWindowMetalAttribute. By default, non-metal windows have square bottom corners; setting the RoundBottomBarCorners attributes causes the window to have round corners instead, if the window has a non-zero bottom content border size (see HIWindowSetContentBorderThickness).

The HIWindowGetCGWindowID API has been added to allow access to the window server's global window identifier for a WindowRef. This number is not usable with any other Carbon APIs, but may be passed to other APIs that do take window numbers, such as OpenGL.

A corresponding API, HIWindowFromCGWindowID, returns the WindowRef that has a specified CGWindowID, if any.

Windows that use the Alert, Modal, or AltPlain window classes now support compositing mode.

The HIWindowGetThemeBackground  API has been added. In conjunction with the new API HIThemeGetTextColorForThemeBrush and HIThemeSetTextFill it can be used to replace SetThemeTextColorForWindow.

Three constants have been added to identify the HIView part codes that a window frame view should support: kHIWindowTitleBarPart, kHIWindowDragPart, and kHIWindowTitleProxyIconPart.

Movable-modal windows now support close and zoom boxes (2884270).

Items in the standard window menu that have the kHICommandSelectWindow command ID now also provide a menu item property containing the WindowRef that will be selected when the item is chosen (3976543). The property creator is kHIWindowMenuCreator, and the property tag is kHIWindowMenuWindowTag. Your application can inspect the value of this property to determine which window will be selected when you receive a kEventCommandProcess event with kHICommandSelectWindow, and the command originates from a menu.

The Window Manager and the standard window frame view now support application-specified custom toolbar views. A custom toolbar view allows an application to implement its own toolbar appearance and behavior. An application is __not__ allowed to customize the toolbar view of a standard HIToolbarRef; when using the standard HIToolbar API, the toolbox still retains control over the toolbar view. The custom toolbar view API is only meant to allow applications that cannot use the HIToolbar API to provide their own toolbar.

A new API, HIWindowSetToolbarView, is provided to allow an application to set a custom toolbar view for a window. After setting a toolbar view, the standard window frame view will automatically show and hide the view when the toolbar button is clicked. A toolbar view must handle several required events, and may optionally respond to several new HICommands in order to implement toolbar customization, multi-window toolbar visibility changes, and toolbar display mode changes. See comments in MacWindows.h just above the prototype for HIWindowSetToolbarView for further documentation.

A new API, HIWindowCopyDrawers, returns a list of the drawers attached to a window (3842671).

Two new APIs, HIWindowGetBackingLocation and HIWindowSetBackingLocation, are available to control whether a window can be accelerated using the QuartzGL feature of the Leopard CoreGraphics framework.

Two new APIs, HIWindowGetSharingType and HIWindowSetSharingType, are available to control whether a window's backing buffer is visible during iChat screen sharing. A window is visible by default, but some applications may wish to make certain windows unavailable to screen sharing for security reasons.

Two new APIs, HIWindowSetContentBorderThickness and HIWindowGetContentBorderThickness, allow setting and retrieving the width of a window's bottom content border. The content border is an area at the sides of the window's content area where the window's window structure drawing extends into the content. By default, this width is zero on the left, right, and bottom for windows that do not use kWindowMetalAttribute. The HIWindowSetContentBorderThickness API allows an application to optionally make the bottom content border width non-zero (see Finder in Leopard for an example). The left and right content border widths are currently required to be zero-width and cannot be changed. An application would typically specify a non-zero bottom content border width and also place controls or textual status messages in this area.

The kWindowApplicationScaledAttribute constant, and all support for ApplicationScaled mode, has been removed from HIToolbox. This mode was never fully implemented and only was useful for windows that did not use compositing mode. Since 64-bit HIToolbox only supports compositing windows anyways, we have decided that there is little value in finishing the ApplicationScaled mode implementation. For high-resolution compatibility, applications should use compositing mode and FrameworkScaled windows.

For ideal interoperability with HIWindowTrackProxyDrag (and thus avoidance of Quickdraw), the BeginWindowProxyDrag API now allows you to pass a NULL outline RgnHandle.

A new flag bit, kHIWindowVisibleInAllSpaces, is now allowed for the HIWindowChangeAvailability API. This flag indicates that a window should be visible on all window sets managed by the Spaces feature in Leopard, rather than just the window set on which the window was created.

When a window is archived, window availability flags are now included in the archive.

TrackWindowProxyFromExistingDrag now accepts a NULL RgnHandle parameter.

__Modal Focus__

The Window and Control Managers and the standard HIToolbox views now support a new type of user focus called "modal focus". This focusing model is layered on top of the existing user focus window API provided by HIToolbox. The modal focus API is used by UI components that want to temporarily borrow keyboard focus from the user focus window while in a specified mode, and then return focus afterwards. Specifically, it's used by the Menu Manager to borrow keyboard focus while menu tracking is occuring. This allows controls such as edit fields to be embedded in menus, such as the Spotlight-enabled Help menu, and to receive keystrokes while the menu is open. When menu tracking ends, focus is returned to whatever window would normally be the user focus at that point.

The modal focus implementation uses a modal focus stack, which is a list of focused windows that override the user focus window. There is currently no API for modifying the modal focus stack. This capability is reserved for system components in Leopard, but may become public in a future release. The topmost window in the focus stack is called the effective focus; this is the window that actually receives keyboard input. The window returned by the GetUserFocusWindow API is now called the modeless focus; this is the window that becomes focused when all focus requests are removed from the modal focus stack. Note that it is possible to change the modeless focus with a call to SetUserFocusWindow without changing the effective focus. In this case, the new modeless focus window does not begin to receive keyboard input until the modal focus stack has been emptied.

Several new APIs and Carbon events are provided to manage modal focus:

- The HIApplicationGetFocus API returns either the effective focus or the modeless focus window. Applications can use this to determine if the two windows are different. An application with a custom HIView can also use this to determine if the application should show an insertion point. The insertion point should only be visible if the view is inside the window returned by HIApplicationGetFocus(true).

- The HIViewShowsFocus API indicates whether a view should show focus indicators such as focus rings. It encapsulates checking a variety of different view state, such as whether the view is focused, is active, is enabled, and is in a window that shows focus. Applications with custom HIViews can use this to determine if a view in a window should show the visual appearance of being focused.

- The HIWindowShowsFocus API indicates whether a window's content should show focus indicators such as focus rings. Currently, it returns true if the window is either the modeless or the effective focus window, but it may do more in the future. Applications that cannot use HIViewShowsFocus (perhaps because they have their own private view hierarchy implementation) can use this API to determine if window content should show the visual appearance of being focused.

- The kEventWindowFocusLost and kEventWindowFocusRestored Carbon events are sent when focus is, respectively, borrowed from the effective window and returned to the effective focus window. These are sent to the window gaining or losing focus, and are forwarded by the basic window handler to the focused control in that window, allowing it to invalidate and redraw itself to reflect the new state of the window.

Applications are not required to do anything to support modal focus, but an application with a custom HIView such as an edit field, which has both insertion point and focus ring indicators, will typically want to be aware of modal focus in order to match the behavior of the system-provided views. In the case of an edit field in the user focus window, when a menu opens, the insertion point in the edit field should stop blinking, but the focus ring around the edit field should remain. A custom view would implement this by listening for the kEventFocusLost and kEventFocusRestored Carbon events, disabling its insertion point when focus is lost and restoring the insertion point when focus is restored, and by using the HIViewShowsFocus API to determine whether to draw the focus ring.

#### User Interface Changes

The Window Manager now draws all windows using a single consistent visual appearance. The kWindowMetalAttribute and kWindowUnifiedTitleAndToolbarAttribute flags no longer affect the window appearance, except that metal windows automatically have a narrow border on the left, right, and bottom, to preserve compatibility with pre-Leopard window layouts.

Windows with a visible toolbar have no visual separation between the window titlebar and the window toolbar. Therefore, a contextual-menu click in the window titlebar is now forwarded to the toolbar view so that the toolbar can show its contextual menu (4479954).

Windows that have a proxy icon now additionally respond to a contextual-menu click in the window title text by displaying the window path popup menu (4031690). Previously, only a command-click would cause the path popup menu to be displayed.

#### API Deprecation

The WindowDefProcPtr type and all related window definition functionality are deprecated for Leopard. Custom window appearance and behavior should be implemented using a custom window frame HIView, available in OS X v10.2 and later.

The following APIs are deprecated for Leopard:

: NewWindow
: NewCWindow
: GetNewCWindow
: GetNewWindow
: CreateWindowFromResource
: StoreWindowIntoCollection
: CreateWindowFromCollection
: GetWindowOwnerCount
: CloneWindow
: GetWindowRetainCount
: RetainWindow
: ReleaseWindow
: SetWindowClass
: InstallWindowContentPaintProc
: ClipAbove
: PaintOne
: PaintBehind
: CalcVis
: CalcVisBehind
: CheckUpdate
: FrontWindow
: SetWindowPic
: GetWindowPic
: SetWindowProxyFSSpec
: GetWindowProxyFSSpec
: IsWindowPathSelectClick
: SetWTitle
: GetWTitle
: DrawGrowIcon
: GrowWindow
: DragGrayRgn
: DragTheRgn
: GetWVariant
: GetGrayRgn

#### Notable Bug Fixes

The standard window frame view (used for document and modal windows) would previously always reset the transparent state of the grow box view whenever the window attributes changed. (The grow box view's default transparency is determined by the window corners; windows with round corners have transparent grow boxes, and windows with square corners have, by default, opaque grow boxes.) This behavior meant that if you wanted to change the attributes of a non-metal window with a transparent grow box, you would need to always make the grow box transparent again after changing the window attributes, because the grow box would always be made opaque by the frame view. The frame view now only resets the grow box transparency when the window's square-corneredness changes (4687777); other attribute changes do not affect the grow box transparency.

Copyright © 2005-2007 Apple Inc.
