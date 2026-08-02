---
title: 64-Bit Guide for Carbon Developers
apple_id: TP40004381
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Carbon64BitGuide/HIToolboxChanges/HIToolboxChanges.html
archived_at: '2026-07-15T05:22:31.419866Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [64-Bit Guide for Carbon Developers](Introduction%20to%2064-Bit%20Guide%20for%20Carbon%20Developers.md)


[Next](Changes%20in%20Other%20C%20APIs.md)[Previous](Modifying%20Your%20Application%20to%20Use%2064-Bit%20Addressing.md)

# Changes in the Human Interface Toolbox

This chapter discusses 64-bit changes in the Carbon Human Interface Toolbox, which includes APIs in the HIToolbox, HIServices, and Navigation Services frameworks. The APIs are listed in alphabetical order.

__Carbon: Appearance.h__

Most Appearance Manager functions are not available to 64-bit applications. The Appearance Manager is largely based on QuickDraw, while the newer HITheme API is based on Quartz 2D. You should use HITheme to draw appearance primitives. Refer to _Appearance Manager Reference_ for detailed information about function availability.

The function `GetThemeMetric` is available so that 64-bit applications can determine:

- How large various theme-capable objects should be
- The size of the bounding rectangle to pass to HITheme functions to get the right appearance

__Carbon: MacApplication.h__

A number of functions in the Application Manager are not available to 64-bit applications. Refer to _Application Manager Reference_ for detailed information about function availability.

Because there are no Cocoa equivalents, the following functions are still available:

- `GetSystemUIMode`
- `SetSystemUIMode`
- `GetApplicationTextEncoding`
- `HISearchWindowShow`
- `HIDictionaryWindowShow`

__Carbon: CarbonEvents.h, CarbonEventsCore.h__

Some Carbon Event Manager functions and events are not available to 64-bit applications. Refer to _Carbon Event Manager Reference_ for detailed information about function availability. To learn about handling events in Cocoa, see _[Cocoa Event Handling Guide](../../Cocoa/Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_.

With the introduction of 64-bit support in the Carbon Event Manager, four kinds of event parameters require changes to their underlying data types. The parameters that have changed are used to pass user-specified data, byte counts, byte offsets, and graphics devices.

In the case of refcon data, byte counts, and byte offsets, these parameters use `typeSInt32` or `typeLongInteger` as the event parameter type prior to OS X v10.5. Unfortunately, `typeSInt32` and `typeLongInteger` specify a 32-bit value, and in OS X v10.5, these parameters must be 64 bits wide when compiling for the 64-bit API so that 64-bit pointers, byte counts, and byte offsets may be passed without truncation.

The Carbon Event Manager defines three new event parameter types to provide source compatibility between 32-bit and 64-bit applications: `typeRefCon`, `typeByteCount`, and `typeByteOffset`. Use of these new types by 32-bit applications is optional. The toolbox provides automatic coercion between the old and new types so existing applications will continue to run. You may recompile your 32-bit application in OS X v10.5 without modification, but in a 64-bit application you must modify your source to use the new types.

The actual value of these constants depends on whether you are compiling for a 32-bit or 64-bit target and on the value of the preprocessor macro `MAC_OS_X_VERSION_MIN_REQUIRED`, which specifies the minimum OS X system version on which your application will run.

When compiling your code using the OS X v10.5 header files, if you want your code to run cleanly in both 32-bit and 64-bit targets, you should modify your calls to `GetEventParameter` to use `typeRefCon`, `typeByteCount`, or `typeByteOffset` instead of `typeSInt32` or `typeLongInteger`. Using these preferred types will allow your 32-bit application to run in OS X v10.5 and earlier, and will allow your 64-bit application to run in OS X v10.5 and later.

Note that when you extract data from an event parameter of type `typeRefCon`, the data type of the variable to which the parameter data is written should always be pointer sized; in other words, use `SRefCon`, `URefCon`, or `PRefCon`, not `SInt32`. Using a 32-bit variable will fail on 64-bit targets. Similarly, when extracting data from an event parameter of type `typeByteCount` or `typeByteOffset`, always use the corresponding standard type (`ByteCount` or `ByteOffset`), and use `sizeof(ByteCount)` or `sizeof(ByteOffset)`, not `sizeof(SInt32)` or `sizeof(UInt32)`, to specify the amount of data that you need.

The following Carbon events use `typeRefCon`:

```
kEventTSMDocumentAccessGetLength
kEventTSMDocumentAccessGetSelectedRange
kEventTSMDocumentAccessGetCharactersPtr
kEventTSMDocumentAccessGetCharactersPtrForLargestBuffer
kEventTSMDocumentAccessGetCharacters
kEventTSMDocumentAccessGetFont
kEventTSMDocumentAccessGetGlyphInfo
kEventTSMDocumentAccessLockDocument
kEventTSMDocumentAccessUnlockDocument
kEventTextInputUpdateActiveInputArea
kEventTextInputUnicodeForKeyEvent
kEventTextInputOffsetToPos
kEventTextInputPosToOffset
kEventTextInputShowHideBottomWindow
kEventTextInputGetSelectedText
kEventTextInputFilterText
kEventAppLaunchNotification
kEventControlArbitraryMessage
```

The following Carbon events use `typeByteCount`:

```
kEventTextInputUpdateActiveInputArea
kEventControlSetData
kEventControlGetData
```

The following Carbon events use `typeByteOffset`:

```
kEventTextInputOffsetToPos
kEventTextInputPosToOffset
```


In the case of graphics devices, some event parameters used `typeGDHandle` prior to OS X v10.5. However, the `GDHandle` type is not available to 64-bit applications at runtime. In OS X v10.5 and later, these parameters contain values of type `CGDirectDisplayID` instead.

The Carbon Event Manager defines a new event parameter type, `typeCGDisplayID`, to indicate that the data type of a graphics device event parameter is `CGDirectDisplayID` instead of `GDHandle`. You need to explicitly choose in your code the type of graphics device identifier you need. Use of `typeCGDisplayID` by 32-bit applications is optional. The toolbox provides automatic coercion between `typeCGDisplayID` and `typeGDHandle`, so existing applications will continue to run. You may recompile a 32-bit application in OS X v10.5 without modification, but in a 64-bit application you must use `typeCGDisplayID` to retrieve the graphics device identifier.

The following 32-bit Carbon events use `typeCGDisplayID`:

```
kEventAppAvailableWindowBoundsChanged
kEventWindowConstrain
kEventMenuGetFrameBounds
```


__Carbon: MacHelp.h__

The Carbon Help Manager is used to display help tags for elements in an application’s user interface. You typically define help tags in Interface Builder, where they are called tool tips.

The Carbon Help Manager is not available to 64-bit applications. To learn about displaying help tags for Cocoa views, see _[Online Help](../../Cocoa/Online%20Help/Introduction%20to%20Online%20Help.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgayds2i)_.

__Carbon: Controls.h and related headers__

The Control Manager is not available to 64-bit applications. In a Cocoa user interface, you must use Cocoa controls. See _[Control and Cell Programming Topics](../../Cocoa/Control%20and%20Cell%20Programming%20Topics/Introduction%20to%20Control%20and%20Cell%20Programming%20Topics%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytk2i)_.

__Carbon: HIDataBrowser.h__

The Data Browser is not available to 64-bit applications. The recommended replacements are the Cocoa classes [NSBrowser](https://developer.apple.com/documentation/appkit/nsbrowser), [NSTableView](https://developer.apple.com/documentation/appkit/nstableview), and [NSOutlineView](https://developer.apple.com/documentation/appkit/nsoutlineview). For additional information about Cocoa browsers, see _[Browser Programming Topics](../../Cocoa/Browser%20Programming%20Topics/Introduction%20to%20Browsers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytq2i)_.

__Carbon: Dialogs.h__

The Dialog Manager is not available to 64-bit applications. Cocoa provides both sheet and application-model dialogs. For information about using dialogs or panels in Cocoa, see _[Window Programming Guide](../../Cocoa/Window%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaztc2i)_ and _[Sheet Programming Topics](../../Cocoa/Sheet%20Programming%20Topics/Introduction%20to%20Sheets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgayde2i)_.

__Carbon: Drag.h__

The Drag Manager is not available to 64-bit applications. For information about drag-and-drop capabilities in Cocoa windows and views, see _[Drag and Drop Programming Topics](../../Cocoa/Drag%20and%20Drop%20Programming%20Topics/Introduction%20to%20Drag%20and%20Drop.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3ds2i)_.

__Carbon: Events.h__

Most Event Manager functions are not available to 64-bit applications. Refer to _Event Manager Reference_ for detailed information about function availability. To learn about handling events in Cocoa, see _[Cocoa Event Handling Guide](../../Cocoa/Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_.

The `GetMouse` function returns a point in local coordinates in the current graphics port. Since there is no QuickDraw graphics port in 64-bit applications, this function is not available. You should use the Carbon Event Manager function `HIGetMousePosition` instead. See `Carbon/HIToolbox/CarbonEventsCore.h`.

The `KeyTranslate` function is not available. You should use [UCKeyTranslate](https://developer.apple.com/documentation/coreservices/1390584-uckeytranslate) in Unicode Utilities instead.

__Carbon: HIArchive.h__

HIArchive is not available to 64-bit applications. Cocoa provides archiving capabilities for both data and objects. For more information, see _[Archives and Serializations Programming Guide](../../Cocoa/Archives%20and%20Serializations%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2do2i)_.

__Carbon: HIGeometry.h__

The `HIGetScaleFactor` function returns the scale factor of an application’s user interface. This function is not available to 64-bit applications, which must use Cocoa to implement their user interfaces. The Cocoa classes [NSScreen](https://developer.apple.com/documentation/appkit/nsscreen) and [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) have methods that return the same information.

__Carbon: HIObject.h__

Some HIObject functions are not available to 64-bit applications. Refer to _HIObject Reference_ for detailed information about function availability. In Cocoa, most objects are subclasses of the [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject) class. For more information about `NSObject`, see _[Cocoa Fundamentals Guide](../../Cocoa/Cocoa%20Fundamentals%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzu)_.

__ApplicationServices: HIShape.h__

The `HIShapeSetQDClip` function sets the current clip in a graphics port to a shape. Since there is no QuickDraw graphics port in 64-bit applications, this function has been removed. You should use [HIShapeReplacePathInCGContext](https://developer.apple.com/documentation/applicationservices/1460747-hishapereplacepathincgcontext) followed by [CGContextClip](https://developer.apple.com/documentation/coregraphics/1455262-cgcontextclip) instead.

__Carbon: HIToolbar.h__

HIToolbar is not available to 64-bit applications. Window toolbars are an integral feature in Cocoa. For more information, see _[Toolbar Programming Topics for Cocoa](../../Cocoa/Toolbar%20Programming%20Topics%20for%20Cocoa/Introduction%20to%20Toolbars.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyds2i)_.

__Carbon: HIView.h and related headers__

HIView is not available to 64-bit applications. The [NSView](https://developer.apple.com/documentation/appkit/nsview) class in Cocoa defines the basic drawing, event-handling, and printing architecture of an application. For more information, see _[Cocoa Fundamentals Guide](../../Cocoa/Cocoa%20Fundamentals%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzu)_ and _[View Programming Guide](../../Cocoa/View%20Programming%20Guide/Introduction%20to%20View%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzy)_.

__Carbon: IBCarbonRuntime.h__

Interface Builder Services includes functions such as `CreateNibReference` that are used to instantiate user interface objects from Carbon nib files.

Interface Builder Services is not available to 64-bit applications. If you’re developing a 64-bit application, you should design a nib-based Cocoa user interface and use Cocoa to instantiate the user interface at runtime. To learn more about Cocoa nib files, see _[Resource Programming Guide](../../Cocoa/Resource%20Programming%20Guide/About%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2i)_.

__Carbon: Keyboards.h__

All functions in Keyboard Layout Services except `KBGetLayoutType` have been deprecated and are not available to 64-bit applications. The replacement functions are in the new Text Input Source Services API. For more information, see _Text Input Source Services Reference_.

__Carbon: Lists.h__

The List Manager is deprecated in OS X v10.5 and is not available to 64-bit applications. The recommended replacements are the Cocoa classes [NSBrowser](https://developer.apple.com/documentation/appkit/nsbrowser), [NSTableView](https://developer.apple.com/documentation/appkit/nstableview), and [NSOutlineView](https://developer.apple.com/documentation/appkit/nsoutlineview). For additional information about Cocoa browsers, see _[Browser Programming Topics](../../Cocoa/Browser%20Programming%20Topics/Introduction%20to%20Browsers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaytq2i)_.

__Carbon: Menus.h__

Most Menu Manager functions are not available to 64-bit applications. Refer to _Menu Manager Reference_ for detailed information about function availability. The Cocoa classes [NSMenu](https://developer.apple.com/documentation/appkit/nsmenu) and [NSMenuItem](https://developer.apple.com/documentation/appkit/nsmenuitem) are the basis for all types of menus in a Cocoa user interface. See _[Application Menu and Pop-up List Programming Topics](../../Cocoa/Application%20Menu%20and%20Pop-up%20List%20Programming%20Topics/Introduction%20to%20Application%20Menus%20and%20Pop-up%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazte2i)_.

The contextual menu plug-in functionality is not available to 64-bit applications. CM plug-ins are ignored by 64-bit applications and never given a chance to add menu items to a contextual menu before it is displayed. In OS X v10.6 and later, the recommended replacement is Cocoa services. Cocoa adds menu items provided by services to the contextual menus displayed by Cocoa applications. For more information, see _[Services Implementation Guide](../../Cocoa/Services%20Implementation%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydc2i)_.

__Carbon: MacTextEditor.h, HITextViews.h__

MLTE is not available to 64-bit applications. You should use the Cocoa text system instead. For information about the Cocoa text system, see _Text System Overview_.

__Carbon: Navigation.h__

Navigation Services is not available to 64-bit applications. Navigation Services dialogs are now implemented using the Cocoa classes [NSOpenPanel](https://developer.apple.com/documentation/appkit/nsopenpanel) and [NSSavePanel](https://developer.apple.com/documentation/appkit/nssavepanel). In 64-bit applications, you must use these classes directly.

__Carbon: Notification.h__

The Notification Manager is not available to 64-bit applications. The recommended replacement is CFUserNotification, which is designed for use in applications that do not otherwise have user interfaces but may need occasional interaction with the user. For more information, see _[CFUserNotification Reference](https://developer.apple.com/documentation/corefoundation/cfusernotification-rd5)_.

For information about notifications in Cocoa, see _[Notification Programming Topics](../../Cocoa/Notification%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2dg2i)_. For general guidelines about user notifications from background processes and applications, see _Apple Human Interface Guidelines_.

__Carbon: Scrap.h__

The Scrap Manager is deprecated in OS X v10.5 and is not available to 64-bit applications. The recommended replacements are the Pasteboard Manager or the Cocoa class [NSPasteboard](https://developer.apple.com/documentation/appkit/nspasteboard). For more information, see _[Pasteboard Manager Programming Guide](../Pasteboard%20Manager%20Programming%20Guide/Introduction%20to%20Pasteboard%20Manager%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytimzz)_ or _[Pasteboard Programming Topics for Cocoa](../../Cocoa/Pasteboard%20Programming%20Topics%20for%20Cocoa/Introduction%20to%20Pasteboards%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3dq2i)_.

__Carbon: TextEdit.h, TSMTE.h__

The TextEdit Manager and Text Services Manager for Text Edit (TSMTE) are not available to 64-bit applications. You should use Cocoa text views instead. For more information, see _[Text Editing Programming Guide](../../Cocoa/Text%20Editing%20Programming%20Guide/Introduction%20to%20Text%20Editing%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2to2i)_.

__Carbon: TextServices.h__

Almost all Text Services Manager (TSM) functions are not available to 64-bit applications. The replacement for most of these functions is the new Text Input Source Services API. For more information, see _Text Input Source Services Reference_.

The `TSMSetInlineInputRegion` function, which depends on QuickDraw regions, is not available. A new Carbon event, `kEventTextInputIsMouseEventInInlineInputArea`, replaces this function.

The Text Services Manager Apple events are not sent or handled in 64-bit applications. These events were deprecated in OS X v10.0. You should use the TSM Carbon events instead.

__Carbon: MacWindows.h__

The Window Manager is not available to 64-bit applications. For information about using windows in a Cocoa user interface, see _[Window Programming Guide](../../Cocoa/Window%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgaztc2i)_.

[Next](Changes%20in%20Other%20C%20APIs.md)[Previous](Modifying%20Your%20Application%20to%20Use%2064-Bit%20Addressing.md)

