---
title: Optimizing Display Modes and Window Arrangement With the Display Manager
apple_id: TP40000920
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-05-03'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Optimizing_DisplayManager/03tasks/tasks.html
archived_at: '2026-07-15T05:23:54.672721Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Optimizing Display Modes and Window Arrangement With the Display Manager](Introduction%20to%20Optimizing%20Display%20Modes%20and%20Window%20Arrangement%20With%20the%20Display.md)


[Next](Document%20Revision%20History.md)[Previous](About%20the%20Display%20Manager.md)

# Using the Display Manager

The previous chapter explains how the Display Manager automatically repositions windows if necessary to ensure that windows are accessible when the user changes the display environment. If the Display Manager moves windows in a manner inappropriate for your application, your application should reposition them instead. Applications that use only the standard window definition functions provided by the Window Manager generally do not need to use the Display Manager.

However, you may need or want your application to perform its own window positioning under various circumstances, such as when

- your application benefits by displaying windows and their contents on the display controlled by the video device with the greatest pixel depth
- your application benefits by displaying windows on the largest available display
- your application uses nonstandard window definition functions that draw windows lacking title bars; examples include fixed-sized windows without title bars (games often use such windows), tool palettes with drag regions on the left sides of their windows, and floating windows

When necessary, the Display Manager automatically repositions windows of type `dBoxProc` (that is, alert boxes and modal dialog boxes) so that the lower-left corners of the windows appear onscreen. This gives users access to the area with the OK and Cancel buttons.

In addition, your application should respond to Display Manager changes if your application relies on display information that it stores internally. For example, if your application caches display positions, `GDevice` structures for displays other than the main screen, or the value in the `screenBits.bounds` field of the `screenBits` global variable, this information may become invalid after the user changes the display configuration. Therefore, your application should update its internal values accordingly after a display configuration change.

To determine whether the Display Manager is available, use the `Gestalt` function with the `gestaltDisplayMgrAttr` selector. Test the bit field indicated by the `gestaltDisplayMgrPresent` constant in the `response` parameter. If the bit is set, then the Display Manager is present.

Presence of the Display Manager does not guarantee that a computer also supports video mirroring. To determine whether QuickDraw supports video mirroring on the user’s computer system, use the `DMQDIsMirroringCapable` function.

Users indirectly inform the Display Manager of changes they wish to make to their display environment by using the Monitors control panel, or by attaching or removing additional displays. The Display Manager in turn sends an Apple event—the Display Notice event—to notify applications that the display environment has changed.

After changing the display environment, the Display Manager also generates an update event to notify all current applications to update their windows.

Your application should always handle update events for its windows. However, your application needs to respond to the Display Notice event only if your application repositions its own windows, uses nonstandard windows, or must update any display information that it stores internally.

To receive the Display Notice event informing you of changes to the user’s display configuration, you must either

- handle the Display Notice event as a high-level event in your application’s normal event loop; or
- use the `DMRegisterExtendedNotifyProc` function to register a function that handles the Display Notice event as soon as the Display Manager issues it

If you write a utility—such as a control panel—that does not handle events through a normal event loop, or if you want your application to handle the Display Notice event as soon as it is issued instead of waiting for it to appear in the event queue, you should use the `DMRegisterExtendedNotifyProc` function.

Here is a summary of the Display Notice event (remember that you must use Apple Event Manager functions to obtain the information contained in Apple events such as this):

Display Notice—respond to display configuration changes

**`Event class`**
: `kCoreEventClass`

**`Event ID`**
: `kAESystemConfigNotice`

**`Required parameter`**

**`Keyword:`**
: `kAEDisplayNotice`

**`Descriptor type:`**
: `AEDesc`

**`Data:`**
: A list of descriptor structures, each specified by the keyword `kDisplayID`. Each `kDisplayID` descriptor structure contains information about a video device attached to the user’s system. Within each `kDisplayID` descriptor structure are a pair of additional keyword-specified descriptor structures: `keyDisplayOldConfig` and `keyDisplayNewConfig`. A description of the video device’s previous state is saved in the `keyDisplayOldConfig` descriptor structure, and a description of the video device’s current state is saved in the `keyDisplayNewConfig` descriptor structure.

Descriptions of these keyword-specified descriptor structures are in Table 2-1.

**`Requested action`**
: Ensure that all windows appear to the user, and update any necessary display information that your application or utility stores internally.

__Table 2-1__  Keyword-specified descriptor structures.

| Keyword | Value | Type | Description |
| `keyDeviceDepthMode` | `'dddm'` | `typeLongInteger` | The depth mode for the video device; that is, the value of the `gdMode` field in the `GDevice` structure for the device |
| `keyDeviceFlags` | `'dddf'` | `typeShortInteger` | The attributes for the video device as maintained in the `gdFlags` field of the `GDevice` structure for the device |
| `keyDeviceRect` | `'dddr'` | `typeQDRectangle` | The boundary rectangle of the video device; that is, the value of the `gdRect` field in the `GDevice` structure for the device |
| `keyDisplayDevice` | `'dmdd'` | `typeLongInteger` | A handle to the `GDevice` structure for the video device |
| `keyDisplayID` | `'dmid'` | `typeLongInteger` | The display ID for the video device |
| `keyDisplayMode` | `'dmdm'` | `typeLongInteger` | The `sResource` number from the video device for this display mode |
| `keyDMConfigVersion` | `'dmcv'` | `typeLongInteger` | The version number for this Display Notice event |
| `keyPixMapAlignment` | `'dppa'` | `typeLongInteger` | Reserved for future use |
| `keyPixMapCmpCount` | `'dpcc'` | `typeShortInteger` | The number of components used to represent a color for a pixel; that is, the value of the `cmpCount` field in the `PixMap` structure for the `GDevice` structure for the device |
| `keyPixMapCmpSize` | `'dpcs'` | `typeShortInteger` | The size in bits of each component for a pixel; that is, the value of the `cmpSize` field in the `PixMap` structure for the `GDevice` structure for the device |
| `keyPixMapColorTableSeed` | `'dpct'` | `typeLongInteger` | The value of the `ctSeed` field of the `ColorTable` structure for the `PixMap` structure for the `GDevice` structure for the video device |
| `keyPixMapHResolution` | `'dphr'` | `typeFixed` | he horizontal resolution of the pixel image in the `PixMap` structure for the `GDevice` structure for the video device |
| `keyPixMapPixelSize` | `'dpps'` | `typeShortInteger` | Pixel depth for the device; that is, the value of the `pixelSize` field in the `PixMap` structure for the `GDevice` structure for the video device |
| `keyPixMapPixelType` | `'dppt'` | `typeShortInteger` | The storage format for the pixel image on the device; that is, the value of the `pixelType` field in the `PixMap` structure for the `GDevice` structure for the video device |
| `keyPixMapRect` | `'dpdr'` | `typeQDRectangle` | The boundary rectangle into which QuickDraw can draw; that is, the `bounds` field in the `PixMap` structure for the `GDevice` structure for the video device |
| `keyPixMapReserved` | `'dppr'` | `typeLongInteger` | Reserved for future use |
| `keyPixMapResReserved` | `'dprr'` | `typeLongInteger` | Reserved for future use |
| `keyPixMapVResolution` | `'dpvr'` | `typeFixed` | The vertical resolution of the pixel image in the `PixMap` structure for the `GDevice` structure for the video device |

To handle the Display Notice event as a high-level event like any other Apple event, you need to

- set the `isHighLevelEventAware` bit in your application’s '`SIZE`' resource to indicate that your application supports high-level events (in which case your application must also support the four required Apple events)
- include code to handle high-level events in your main event loop (as illustrated in [Listing 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzrfvjvomq))
- write a function that handles the Display Notice event (as illustrated in [Listing 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzrfvjvomy))
- use the `AEInstallEventHandler` function to install the entry for handling the Display Notice event in your application’s Apple event dispatch table

If you want your application to handle all window positioning itself (that is, if you do not want the Display Manager to automatically move any of your windows), you should also set the `isDisplayManagerAware` bit in the '`SIZE`' resource.

__Listing 2-1__  Handling Apple events in the event loop

```swift
void MyDoEvent(EventRecord *event)
{
    short           part, err;
    WindowPtr       window;
    char            key;
    switch ( event->what ) {
        /* here, handle null, mouse down, key down, update, and
            other necessary events */
        case kHighLevelEvent:
DoHighLevelEvent(event);
break;
    }
}
void DoHighLevelEvent(EventRecord *event)
{
    OSErr   myErr;
        /* handling only Apple-event types of high-level events */
        myErr = AEProcessAppleEvent(event);
}
```

Your application must use the `AEInstallEventHandler` function to add an entry to your application’s Apple event dispatch table. This entry is the function that responds to the Display Notice event. For example, the following code fragment illustrates how to use `AEInstallEventHandler` to install an application-defined function called `DoAEDisplayUpdate`.

```
err = AEInstallEventHandler (kCoreEventClass,
                            kAESystemConfigNotice,
                            (ProcPtr)DoAEDisplayUpdate, 0, false);
```

Listing 2-2 shows an application-defined function called `DoAEDisplayUpdate` that uses Apple Event Manager functions to obtain information about the various video devices reported by the Display Notice event. The function `DoAEDisplayUpdate` uses this information to update its internal data structures for its windows and then calls another application-defined function that ensures that its windows are displayed optimally in the new configuration environment.

__Listing 2-2__  Responding to the Display Notice event

```
pascal OSErr DoAEDisplayUpdate
(AppleEvent theAE,AppleEvent reply,long ref) {
    #pragma unused(theAE,reply,ref)
    AEDescList      DisplayList;
    AEDescList      DisplayID;
    AERecord        OldConfig,NewConfig;
    AEKeyword       tempWord;
    AEDesc          returnType;
    OSErr           myErr;
    long            result;
    long            count;
    Rect            oldRect, newRect;
    Size            actualSizeUnused;
/* get a list of the displays from the Display Notice event */

    myErr =
    AEGetParamDesc(&theAE,kAEDisplayNotice,typeWildCard,&DisplayList);

/* count the elements in the list */
    myErr = AECountItems(&DisplayList,&count);
    while (count >0)        /* decode the Display Notice event */
{
        myErr = AEGetNthDesc(&DisplayList, count, typeWildCard,
            &tempWord, &DisplayID);
        myErr = AEGetNthDesc(&DisplayID, 1, typeWildCard, &tempWord,
            &OldConfig);
        myErr = AEGetKeyPtr(&OldConfig, keyDeviceRect, typeWildCard,
            &returnType, &oldRect, 8, actualSizeUnused);
        myErr = AEGetNthDesc(&DisplayID, 2, typeWildCard, &tempWord,
            &NewConfig);
        myErr = AEGetKeyPtr(&NewConfig, keyDeviceRect, typeWildCard,
            &returnType, &newRect, 8, actualSizeUnused);
/* update internal info about the gdRects for the devices */
        MyUpdateWindowStructures(oldRect, newRect);
        count--;
}
/* move and resize windows as necessary*/
    MyDisplayWindows();
    return (noErr);
}
```


You may want your application to handle the Display Notice event as soon as it is issued instead of waiting for it to appear in the event queue. You can use the `DMRegisterExtendedNotifyProc` function to register a function to which the Display Manager directly sends the Display Notice event. By using `DMRegisterExtendedNotifyProc`, and by not setting the `isHighLevelEventAware` bit in the '`SIZE`' resource, you cause the Display Manager to send a Display Notice event directly to your handling function; your application or utility then receives no high-level Display Notice event.

To remove your Display Notice event-handling function, use the `DMRemoveExtendedNotifyProc` function.

Using the Monitors control panel, the user can switch displays to use a different display mode and to change the display configurations. When your application receives the Display Notice event as described in the previous section, your application must determine whether it needs to reposition and perhaps resize its windows.

Listing 2-3 illustrates how an application can check whether its nonstandard window appears onscreen after Display Manager configuration changes have occurred. In this example, the application has a window with a title bar on its left side, as shown in the tool palette illustrated in [Figure 1-4](About%20the%20Display%20Manager.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzsfvjvomy). After receiving the Display Notice event as shown in [Listing 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydenzrfvjvomy), the application calls its `MyDisplayWindows` function, which in turn calls its `MyMakeToolWindowVisible` function. If `MyMakeToolWindowVisible` determines that the nonstandard title bar does not appear on any displays (in which case the user cannot move the window), `MyMakeToolWindowVisible` moves the entire window to the main screen where the user has access to the window.

__Listing 2-3__  Ensuring that a nonstandard window appears onscreen

```swift
static pascal OSErr MyMakeToolWindowVisible (WindowPeek window) {
    if (window->windowKind == applicationFloatKind) {
        Rect        checkRect;
        Rect        mainRect;
        GDHandle    maxAreaDevice;
        short       theWVariant;
        Rect        windowRect;
        theWVariant = GetWVariant(&window->port);
        MyGetWindowGlobalRect(window, &windowRect);
        /*get rectangle of window, in global coordinates, here */
        if (0 != (kVerBarFW & theWVariant))
        /* check if this is the window with a vertical title bar */
        {
        /* following line gets the rectangle of the title bar */
        SetRect(&checkRect, windowRect.left-kMyVertTitleWidth+kMyMinVisX,
                                     windowRect.top+kkMyMinVisV,
                                     windowRect.left-1-kMyMinVisX,
                                     windowRect.bottom-kMyMinVisV);
        /* following line calls an application-defined function that
        determines which screen contains the largest amount of the title
        bar */
        maxAreaDevice = MyFindMaxCoverageDevice(&checkRect);
        if (nil == maxAreaDevice)
        /* if the title bar doesn't appear on any screen, move window to
        the main screen */
        {   mainRect = (*GetMainDevice()) -> gdRect;
            MoveWindow(&Window->port, mainRect.left+10+kMyVertTitleWidth,
            mainRect.bottom-10-(windowRect.bottom-windowRec.top, FALSE);
        } }
        MyKeepWindowOnscreen(window, nil);
        /* handle other nonstandard window variants here */
        }
        return noErr;
}
```

Your application may find it useful to resize a window after moving it, or to optimize the color for its newly configured video device. You can use Display Manager functions to determine the characteristics of video devices, as explained in the next section.

To determine the characteristics of available video devices, your application can use the `DMGetFirstScreenDevice` function to obtain a handle to the `GDevice` structure for the first video device in the device list. The `DMGetFirstScreenDevice` function is similar to the QuickDraw function `GetDeviceList`, except that when returning `GDevice` structures, `GetDeviceList` does not distinguish between the `GDevice` structures for video devices and the `GDevice` structures associated with no video devices. (For example, if system software uses the function `DMDisableDisplay` to disable the last remaining device in the device list, then `DMDisableDisplay` inserts into the device list a `GDevice` structure that is not associated with any video device. The `DMGetFirstScreenDevice` function will not return this `GDevice` structure, but `GetDeviceList` might.)

After using the `DMGetFirstScreenDevice` function to obtain a handle to the first `GDevice` structure for a display in the device list, your application can use the `DMGetNextScreenDevice` function to loop through all of the video devices in the device list. The `DMGetNextScreenDevice` function is similar to the QuickDraw function `GetNextDevice`, except that when returning `GDevice` structures, `GetNextDevice` does not distinguish between the `GDevice` structures for video devices and the `GDevice` structures associated with no video devices.

Another important difference between these two Display Manager functions (`DMGetFirstScreenDevice` and `DMGetNextScreenDevice`) and their related QuickDraw functions (`GetDeviceList` and `GetNextDevice`) is that with both Display Manager functions, your application can specify that the Display Manager return handles only to active video devices. (An active device is a video device whose display area is included in the user’s desktop; the display area of an inactive device does not appear on the user’s desktop.)

To get a handle to the `GDevice` structure for a video device that mirrors another, your application can use the `DMGetNextMirroredDevice` function.

Your application can pass the `GDevice` handle returned for any of these video devices to a QuickDraw function like `TestDeviceAttribute` or `HasDepth` to determine various characteristics of the video device, or your application can examine the `gdRect` field of the `GDevice` structure to determine the dimensions of the screen it represents.

Macintosh system software uses the `DMCheckDisplayMode` function to determine whether a video device supports a particular display mode and pixel depth. Typically, your application does not need to know whether a display mode is supported, but only whether a specific pixel depth is supported, in which case your application can use the Color QuickDraw function `HasDepth`.

To determine whether QuickDraw supports video mirroring on the user’s computer system, your application can use the `DMQDIsMirroringCapable` function. Your application can use the `DMCanMirrorNow` function to determine whether video mirroring can activate. And to determine whether the user’s computer system currently uses video mirroring, your application can use the `DMIsMirroringOn` function.

Finally, your application can use the `DMGetDisplayIDByGDevice` function to determine the display ID for a video device. A display ID is a long integer used by the Display Manager to uniquely identify a video device. Associating a display by its display ID is helpful when using functions such as `DMRemoveDisplay` that could change the `GDevice` structure associated with a video device. You can first determine the display ID for a device by using the `DMGetDisplayIDByGDevice` function. To later retrieve that device’s `GDevice` structure after calling various Display Manager functions, your application can use the `DMGetGDeviceByDisplayID` function. Display IDs are not guaranteed to be persistent across reboots or sleep.

The Monitors control panel is the user interface for changing the pixel depth, color capabilities, and positions of video devices. Because the user can control the capabilities of the video devices, your application should be flexible. For instance, although your application may have a preferred pixel depth, it should do its best to accommodate less than ideal conditions.

Your application can use Display Manager functions to change the display mode and display configuration of the user’s video devices, but your application should do so only with the consent of the user.

If your application must have a specific pixel depth, for example, it can display a dialog box that offers the user a choice between changing to that depth or canceling display of the image. This dialog box saves the user the trouble of going to the control panel before returning to your application. If it is absolutely necessary for your application to draw on a video device of a specific pixel depth, your application can then use either the `SetDepth` function or the `DMSetDisplayMode` function.

With the possible exception of the `DMSetDisplayMode` function and the `DMMirrorDevices` and `DMUnmirrorDevice` functions, applications should not need to use any of the Display Manager functions that change the user’s display configuration. However, they are described for completeness, in case you find a compelling need for your application to change the user’s display configuration. If your application must use multiple Display Manager calls that configure the user’s displays, your application should first use the `DMBeginConfigureDisplays` function to postpone Display Manager configuration checking, the rebuilding of desktop regions, and Apple event notification of Display Manager changes. When finished configuring the user’s displays, use the `DMEndConfigureDisplays` function. Using `DMBeginConfigureDisplays` and `DMEndConfigureDisplays` allows your application to wait until it has made all display changes before managing its windows in response to a single Display Notice event. It is important to pass the `displayState` variable obtained in `DMBeginConfigureDisplays` to the `DMEndConfigureDisplays` function.

[Next](Document%20Revision%20History.md)[Previous](About%20the%20Display%20Manager.md)

