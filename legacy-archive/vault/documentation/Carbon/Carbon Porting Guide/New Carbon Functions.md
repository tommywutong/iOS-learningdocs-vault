---
title: Carbon Porting Guide
apple_id: TP30000991
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2002-12-01'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/carbon_porting_guide/cpg_apdx_func/cpg_apdx_funcs.html
archived_at: '2026-07-15T05:24:53.396970Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Carbon Porting Guide](Introduction%20to%20Carbon%20Porting%20Guide.md)


[Next](The%20Sample%20Application.md)[Previous](New%20Carbon%20Technologies.md)

# New Carbon Functions

This section provides an overview of some of the new functions introduced in Carbon. Until complete documentation is available, you should refer to the header files and sample code included on the Mac OS X Developer Tools CD for additional information.

Custom defprocs (that is, WDEFs, MDEFs, CDEFs, and LDEFs) must be compiled as PowerPC code and can no longer be stored in resources. Carbon introduces new variants of `CreateWindow` and similar functions (such as `NewControl` and `NewMenu`) that take a universal procedure pointer (UPP) to your custom defproc. Instead of creating a window definition as a WDEF resource, for example, you call the Carbon routine `CreateCustomWindow`:

```
OSStatus CreateCustomWindow(const WindowDefSpec *def,
        WindowClass windowClass, WindowAttributes attributes,
        const Rect *bounds, WindowPtr *outWindow);
```

The `WindowDefSpec` parameter contains a UPP that points to your custom window definition procedure.

You need to be aware of the following changes for custom WDEFs:

- Window defprocs no longer receive the `wCalcRgns` message. Instead they receive the `kWindowMsgGetRegion` message twice, once for the structure region and once for the content region. The structure passed in the message parameter indicates the desired region in each case. Your defproc must handle these messages.
- If you need to get the global bounds of a window’s `portRect` in order to determine the structure or content regions, you should call `GetWindowBounds` and pass the `kWindowGlobalPortRgn` constant. On return, the function will supply a pointer to a `Rect` indicating the bounds in global coordinates. The pixel map (`PixMap`) bounds on Mac OS X will always start at (0,0), so you will obtain incorrect results if you attempt to manually convert the port’s bounds from local to global coordinates by offsetting the bounds by the port’s pixel map’s bounds.

You need to be aware of the following changes to custom MDEFs:

- Menu defprocs no longer receive the `mChooseMsg` message. Instead they receive two new messages: `kMenuFindItemMsg` and `kMenuHiliteItemMsg` .
- Code that sets or reads the low memory global variables `TopMenuItem`, `AtMenuBottom`, `MenuDisable`, and `MBSaveLoc` should use the new `MenuTrackingData` structure instead. You can obtain the contents of the structure at any time by calling the new function `GetMenuTrackingData`.
- When a menu defproc receives a `mDrawMsg` message, it also receives a pointer to a `MenuTrackingData` structure in the `whichItem` parameter. Your defproc should read the structure to obtain the menu virtual top and bottom rather than using the low memory accessor functions `LMTopMenuItem` and `LMAtMenuBottom`.

A major change introduced in Carbon is that some commonly used data structures are now opaque—meaning their internal structure is hidden. Directly referencing fields within these structures is no longer allowed, and will cause a compiler error. QuickDraw global variables, graphics ports, regions, window and dialog records, controls, menus, and TSMTE dialogs are all opaque to Carbon applications. Anywhere you reference fields in these structures directly, you must use new casting and accessor functions described in the following sections.

Many applications assume that window pointer (`WindowPtr`) and dialog pointer (`DialogPtr`) types have a graphics port (`GrafPort`) embedded at the top of their structures. In fact, the standard Universal Interfaces defines dialog pointers and window pointers as graphics pointers so that you don’t have to cast them to a type `GrafPtr` before using them. For example:

```
void DrawIntoWindow(WindowPtr window)
{
    SetPort(window);
    MoveTo(x, y);
    LineTo(x + 50, y + 50);
}
```

If you compile the above code using the Carbon interfaces, you’ll get a number of compilation errors due to the fact that window pointers are no longer defined as graphics pointers. But you can’t simply cast these variables to type `GrafPtr` because doing so will cause your application to crash under Mac OS X.

Instead, Carbon provides a set of casting functions that allow you to obtain a pointer to a window’s `GrafPort` structure or vice versa. Using these new functions, code like the previous example must be updated as follows to be Carbon-compliant and compile without errors:

```
void DrawIntoWindow(WindowPtr window)
{
    SetPort(GetWindowPort(window));
    MoveTo(x, y);
    LineTo(x + 50, y + 50);
}
```

Casting functions are provided for obtaining graphics ports from windows, windows from dialogs, and various other combinations. By convention, functions that cast up (that is, going from a lower-level data structure like a graphics port to a window or going from a window to a dialog pointer) are named `GetHigherLevelTypeFromLowerLevelType`. Functions that cast down are named `GetHigherLevelTypeLowerLevelType`.

Examples of functions that cast up include:

```
pascal DialogPtr GetDialogFromWindow(WindowPtr window);
pascal WindowPtr GetWindowFromPort(CGrafPtr port);
```

Functions that cast down include:

```
pascal WindowPtr GetDialogWindow(DialogPtr dialog);
pascal CGrafPtr GetWindowPort(WindowPtr window);
```


Carbon includes a number of functions to allow applications to access fields within system data structures that are now opaque. [Listing A-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojrfvbuqmrqgywviucykjcummjrgu) shows an example of some typical coding practices that must be modified for Carbon.

__Listing A-1__  Example of unsupported data structure access

```swift
void WalkWindowsAndDoSomething(WindowPtr firstWindow)
{
    WindowPtr currentWindow = firstWindow;

    while (currentWindow != NULL)
    {
        if ((WindowPeek) currentWindow->visible)
            && RectIsFourByFour(&currentWindow->portRect))
        {
            DoSomethingSpecial(currentWindow);
        }
        currentWindow = (WindowPtr) ((WindowPeek) currentWindow->nextWindow);
    }
}
```

There are four problems in [Listing A-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojrfvbuqmrqgywviucykjcummjrgu) that will cause compiler errors when building a Carbon application.

1. Checking the `visible` field directly is not allowed because the `WindowPeek` type is no longer defined (it’s only useful when you can assume that type `WindowPtr` can be cast to a `WindowRecord` pointer, which is not the case in Carbon).
2. The `currentWindow` variable is treated as a graphics port. You need to use the casting functions discussed above to access a window’s `GrafPort` structure.
3. Graphics ports are now opaque data structures, so you must use an accessor to get the port’s bounding rectangle.
4. Accessing the `nextWindow` field directly from the `WindowRecord` structure is not allowed.

To compile and run under Carbon, the code above would have to be changed as shown in Listing A-2.

__Listing A-2__  Example of using Carbon-compatible accessor functions

```
void WalkWindowsAndDoSomething(WindowPtr firstWindow)
{
    WindowPtr currentWindow = firstWindow;

    while (currentWindow != NULL)
    {
        Rect windowBounds;

        if (IsWindowVisible(currentWindow) &&
            RectIsFourByFour(GetPortBounds(GetWindowPort(currentWindow),
                &windowBounds))
        {
            DoSomethingSpecial(currentWindow);
        }
        currentWindow = GetNextWindow(currentWindow);
    }
}
```

One thing to note is that the `GetPortBounds` function returns a pointer to the input rectangle as a syntactic convenience, to allow you to pass the result of `GetPortBounds` directly to another function. Many of the accessor functions return a pointer to the input in the same way, as a convenience to the caller.

With a few exceptions as noted below, all accessor functions return copies to data, not the data itself. You must make sure to allocate storage before you access non-scalar types such as regions and pixel patterns. For example, if you use code like this to test the visible region of a graphics port:

```swift
if (EmptyRgn(somePort->visRgn))
    DoSomething();
```

you’ll have to change it as shown below in order to allow the accessor to copy the port’s visible region into your reference:

```
RgnHandle visibleRegion;

visibleRegion = NewRgn();
if (EmptyRgn(GetPortVisibleRegion(somePort, visibleRegion)))
    DoSomething();
DisposeRgn(visibleRegion);
```

A few accessor functions continue to return actual data rather than copied data. `GetPortPixMap`, for example, is provided specifically to allow calls to `CopyBits`, `CopyMask`, and similar functions, and should only be used for these calls. The interface for the `CopyBits`-type calls will be changing to work around this exception, but for now be aware that this exception exists. The QuickDraw bottleneck routines, which are stored in a `GrafProc` record, continue to operate just like their classic Mac OS equivalents. That is, the actual pointer to the structure is returned rather than creating a copy. Other instances where the actual handle is passed back include cases where user-specified data is carried in a data structure, such as the `UserHandle` field in `ListHandle` records.

Table A-1 lists common accessor functions for Human Interface Toolbox structures.

__Table A-1__  Summary of Carbon Human Interface Toolbox accessors

| Data structure | Element | Accessor |
| Controls |  |  |
| `ControlRecord` | `nextControl` | Use Control Manager embedding hierarchy functions. (See Mac OS 8 Control Manager Reference.) |
|  | `contrlOwner` | `Get/SetControlOwner`. May be replaced in favor of `Embed/DetachControl`. |
|  | `contrlRect` | `Get/SetControlBounds` |
|  | `contrlVis` | `IsControlVisible, SetControlVisibility` |
|  | `contrlHilite` | `GetControlHilite, HiliteControl` |
|  | `contrlValue` | `Get/SetControlValue, Get/SetControl32BitValue` |
|  | `contrlMin` | `Get/SetControlMinimum, Get/SetControl32BitMinimum` |
|  | `contrlMax` | `Get/SetControlMaximum, Get/SetControl32BitMaximum` |
|  | `contrlDefProc` | not supported |
|  | `contrlData` | `Get/SetControlDataHandle` |
|  | `contrlAction` | `Get/SetControlAction` |
|  | `contrlRfCon` | `Get/SetControlReference` |
|  | `contrlTitle` | `Get/SetControlTitle` |
| `AuxCtlRec` | `acNext` | not supported |
|  | `acOwner` | not supported |
|  | `acCTable` | not supported |
|  | `acFlags` | not supported |
|  | `acReserved` | not supported |
|  | `acRefCon` | Use `Get/SetControlProperty` if you need more `refCon`s. |
| `PopupPrivateData` | `mHandle` | Use `Get/SetControlData` with proper tags. |
|  | `mID` | Use `Get/SetControlData` with proper tags. |
| Dialog Boxes |  |  |
| `DialogRecord` | `window` | Use `GetDialogWindow` to obtain the value. There is no equivalent function for setting the value. |
|  | `items` | `AppendDITL, ShortenDITL, AppendDialogItemList, InsertDialogItem, RemoveDialogItems` |
|  | `textH` | `GetDialogTextEditHandle` |
|  | `editField` | `GetDialogKeyboardFocusItem` |
|  | `editOpen` | `Get/SetDialogCancelItem` |
|  | `aDefItem` | `Get/SetDialogDefaultItem` |
| Menus |  |  |
| `MenuInfo` | `menuID` | `Get/SetMenuID` |
|  | `menuWidth` | `Get/SetMenuWidth` |
|  | `menuHeight` | `Get/SetMenuHeight` |
|  | `menuProc` | `SetMenuDefinition` |
|  | `enableFlags` | `Enable/DisableMenuItem, IsMenuItemEnabled` |
|  | `menuData` | `Get/SetMenuTitle` |
| Windows |  |  |
| `WindowRecord CWindowRecord` | `port` | Use `GetWindowPort` to obtain the value. There is no equivalent function for setting the value. |
|  | `windowKind` | `Get/SetWindowKind` |
|  | `visible` | `Hide/ShowWindow, ShowHide, IsWindowVisible` |
|  | `hilited` | `HiliteWindow, IsWindowHilited` |
|  | `goAwayFlag` | `ChangeWindowAttributes` |
|  | `spareFlag` | `ChangeWindowAttributes` |
|  | `strucRgn` | `GetWindowRegion` |
|  | `contRgn` | `GetWindowRegion` |
|  | `updateRgn` | `GetWindowRegion` |
|  | `windowDefProc` | not supported |
|  | `dataHandle` | not supported |
|  | `titleHandle` | `Get/SetWTitle` |
|  | `titleWidth` | `GetWindowRegion` |
|  | `controlList` | `GetRootControl` |
|  | `nextWindow` | `GetNextWindow` |
|  | `windowPic` | `Get/SetWindowPic` |
|  | `refCon` | `Get/SetWRefCon` |
| `AuxWinRec` | `awNext` | not supported |
|  | `awOwner` | not supported |
|  | `awCTable` | `Get/SetWindowContentColor` |
|  | `reserved` | not supported |
|  | `awFlags` | not supported |
|  | `awReserved` | not supported |
|  | `awRefCon` | Use `Get/SetWindowProperty` if you need more reference constants. |
| Lists |  |  |
| `ListRec` | `rView` | `Get/SetListViewBounds` |
|  | `port` | `Get/SetListPort` |
|  | `indent` | `Get/SetListCellIndent` |
|  | `cellSize` | `Get/SetListCellSize` |
|  | `visible` | Use `GetListVisibileCells` to obtain the value. No equivalent function for setting the value. |
|  | `vScroll` | `GetListVerticalScrollBar`, use new API (TBD) to turn off automatic scroll bar drawing. |
|  | `hScroll` | `GetListHorizontalScrollBar`, use new API (TBD) to turn off automatic scroll bar drawing. |
|  | `selFlags` | `Get/SetListSelectionFlags` |
|  | `lActive` | `LActivate, GetListActive` |
|  | `lReserved` | not supported |
|  | `listFlags` | `Get/SetListFlags` |
|  | `clikTime` | `Get/SetListClickTime` |
|  | `clikLoc` | `GetListClickLocation` |
|  | `mouseLoc` | `GetListMouseLocation` |
|  | `lClickLoop` | `Get/SetListClickLoop` |
|  | `lastClick` | `SetListLastClick` |
|  | `refCon` | `Get/SetListRefCon` |
|  | `listDefProc` | not supported |
|  | `userHandle` | `Get/SetListUserHandle` |
|  | `dataBounds` | `GetListDataBounds` |
|  | `cells` | `LGet/SetCell` |
|  | `maxIndex` | `LGet/SetCell` |
|  | `cellArray` | `LGet/SetCell` |

Table A-2 provides a summary of accessor functions you can use to access common QuickDraw data structures.

__Table A-2__  QuickDraw accessor functions

| Data structure | Element | Accessor |
| `GrafPort` | `device` | not supported |
|  | `portBits` | Use `GetPortBitMapsForCopyBits` or `IsPortColor`. |
|  | `portRect` | `Get/SetPortBounds` |
|  | `visRgn` | `Get/SetPortVisibleRegion` |
|  | `clipRgn` | `Get/SetPortClipRgn` |
|  | `bkPat` | not supported |
|  | `fillPat` | not supported |
|  | `pnLoc` | `Get/SetPortPenLocation` |
|  | `pnSize` | `Get/SetPortPenSize` |
|  | `pnMode` | `Get/SetPortPenMode` |
|  | `pnPat` | not supported |
|  | `pnVis` | Use `GetPortPenVisibility` or `Show/HidePen`. |
|  | `txFont` | Use `GetPortTextFont` or `TextFont`. |
|  | `txFace` | Use `GetPortTextFace` or `TextFace`. |
|  | `txMode` | Use `GetPortTextMode` or `TextMode`. |
|  | `txSize` | Use `GetPortTextSize` or `TextSize`. |
|  | `spExtra` | Use `GetPortSpExtra` or `SpaceExtra`. |
|  | `fgColor` | not supported |
|  | `bkColor` | not supported |
|  | `colrBit` | not supported |
|  | `patStretch` | not supported |
|  | `picSave` | `IsPortPictureBeingDefined` |
|  | `rgnSave` | not supported |
|  | `polySave` | not supported |
|  | `grafProcs` | not supported |
| `CGrafPort` | `device` | not supported |
|  | `portPixMap` | `GetPortPixMap` |
|  | `portVersion` | `IsPortColor` |
|  | `grafVars` | not supported |
|  | `chExtra` | `GetPortChExtra` |
|  | `pnLocHFrac` | `Get/SetPortFracHPenLocation` |
|  | `portRect` | `Get/SetPortBounds` |
|  | `visRgn` | `Get/SetPortVisibleRegion` |
|  | `clipRgn` | `Get/SetPortClipRegion` |
|  | `bkPixPat` | Use `GetPortBackPixPat` or `BackPixPat`. |
|  | `rgbFgColor` | Use `GetPortForeColor` or `RGBForeColor`. |
|  | `rgbBkColor` | Use `GetPortBackColor` or `RGBBackColor`. |
|  | `pnLoc` | `Get/SetPortPenLocation` |
|  | `pnSize` | `Get/SetPortPenSize` |
|  | `pnMode` | `Get/SetPortPenMode` |
| `pnPixPat` |  | `Get/SetPortPenPixPat` |
|  | `fillPixPat` | `Get/SetPortFillPixPat` |
|  | `pnVis` | Use `GetPortPenVisibility` or `Show/HidePen`. |
|  | `txFont` | Use `GetPortTextFont` or `TextFont`. |
|  | `txFace` | Use `GetPortTextFace` or `TextFace`. |
|  | `txMode` | Use `GetPortTextMode` or `TextMode`. |
|  | `txSize` | Use `GetPortTextSize` or `TextSize`. |
|  | `spExtra` | Use `GetPortSpExtra` or `SpaceExtra`. |
|  | `fgColor` | not supported |
|  | `bkColor` | not supported |
|  | `colrBit` | not supported |
|  | `patStretch` | not supported |
|  | `picSave` | `IsPortPictureBeingDefined` |
|  | `rgnSave` | not supported |
|  | `polySave` | not supported |
|  | `grafProcs` | `Get/SetPortGrafProcs` |
| `QDGlobals` | `randSeed` | `GetQDGlobalsRandomSeed` |
|  | `screenBits` | `GetQDGlobalsScreenBits` |
|  | `arrow` | `GetQDGlobalsArrow` |
|  | `dkGray` | `GetQDGlobalsDarkGray` |
|  | `ltGray` | `GetQDGlobalsLightGray` |
|  | `gray` | `GetQDGlobalsGray` |
|  | `black` | `GetQDGlobalsBlack` |
|  | `white` | `GetQDGlobalsWhite` |
| `GrafPtr` | `thePort` | `GetQDGlobalsThePort` |

Carbon includes a number of utility functions to make it easier to port your application. Under the classic Mac OS API, new graphics ports were created by allocating non-relocatable memory the size of a `CGrafPort` record and calling `OpenCPort`. Because `GrafPort` records are now opaque, and their size is system-defined, Carbon includes new routines to create and dispose of graphics ports:

```
pascal CGrafPtr CreateNewPort()
pascal void DisposePort(CGrafPtr port)
```

These functions provide access to commonly used bounding rectangles:

```
pascal OSStatus GetWindowBounds(WindowRef window,
                WindowRegionCode regionCode, Rect *bounds);
pascal OSStatus GetWindowRegion(WindowRef window,
                WindowRegionCode regionCode, RgnHandle windowRegion);
```

Often you’ll find the need to set the current port to the one that belongs to a window or dialog box. `SetPortWindowPort` and `SetPortDialogPort` allow you to do this:

```
pascal void SetPortWindowPort(WindowPtr window)
pascal void SetPortDialogPort(DialogPtr dialog)
```

The new function `GetParamText` replaces `LMGetDAStrings` as the method to retrieve the current `ParamText` setting. Pass `NULL` for a parameter if you don’t want a particular string.

```
pascal void GetParamText(StringPtr param0, StringPtr param1,
                         StringPtr param2, StringPtr param3)
```


`CarbonAccessors.o` is a static library that contains implementations of the Carbon functions for accessing opaque toolbox data structures. See [Begin With CarbonAccessors.o](Preparing%20Your%20Code%20for%20Carbon.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojrfvbuqmrqgiwviucykjcummjrge) for information on how you can use this library to assist in porting your code to Carbon.

Table A-3 lists the Carbon functions implemented in `CarbonAccessors.o.` The “•” symbol indicates a function added since the Developer Preview 3 version of this document. “••” indicates a function added since Developer Preview 4.

__Table A-3__  Functions in CarbonAccessors.o

| `AEFlattenDesc`•• | `AEGetDescData` |
| `AEGetDescDataSize` | `AEReplaceDescData`• |
| `AESizeOfFlattenedDesc`•• | `AEUnflattenDesc`•• |
| `c2pstrcpy`• | `CopyCStringToPascal`• |
| `CopyPascalStringToC`• | `CreateNewPort` |
| `DisposePort` | `GetControlBounds` |
| `GetControlDataHandle` | `GetControlHilite` |
| `GetControlOwner` | `GetControlPopupMenuHandle` |
| `GetControlPopupMenuID` | `GetDialogCancelItem` |
| `GetDialogDefaultItem` | `GetDialogFromWindow` |
| `GetDialogKeyboardFocusItem` | `GetDialogPort` |
| `GetDialogTextEditHandle` | `GetDialogWindow` |
| `GetGlobalMouse` | `GetListActive` |
| `GetListCellIndent` | `GetListCellSize` |
| `GetListClickLocation` | `GetListClickLoop` |
| `GetListClickTime` | `GetListDataBounds` |
| `GetListDataHandle` | `GetListDefinition` |
| `GetListFlags` | `GetListHorizontalScrollBar` |
| `GetListMouseLocation` | `GetListPort` |
| `GetListRefCon` | `GetListSelectionFlags` |
| `GetListUserHandle` | `GetListVerticalScrollBar` |
| `GetListViewBounds` | `GetListVisibleCells` |
| `GetMenuHeight` | `GetMenuID` |
| `GetMenuTitle` | `GetMenuWidth` |
| `GetNextWindow`• | `GetParamText` |
| `GetPixBounds` | `GetPixDepth` |
| `GetPortBackColor` | `GetPortBackPixPat` |
| `GetPortBackPixPatDirect` | `GetPortBitMapForCopyBits`• |
| `GetPortBounds` | `GetPortChExtra` |
| `GetPortClipRegion` | `GetPortFillPixPat` |
| `GetPortForeColor` | `GetPortFracHPenLocation` |
| `GetPortGrafProcs` | `GetPortHiliteColor` |
| `GetPortOpColor` | `GetPortPenLocation` |
| `GetPortPenMode` | `GetPortPenPixPat` |
| `GetPortPenPixPatDirect` | `GetPortPenSize` |
| `GetPortPenVisibility` | `GetPortPixMap` |
| `GetPortPrintingReference` | `GetPortSpExtra` |
| `GetPortTextFace` | `GetPortTextFont` |
| `GetPortTextMode` | `GetPortTextSize` |
| `GetPortVisibleRegion` | `GetQDGlobals` |
| `GetQDGlobalsArrow` | `GetQDGlobalsBlack` |
| `GetQDGlobalsDarkGray` | `GetQDGlobalsGray` |
| `GetQDGlobalsLightGray` | `GetQDGlobalsRandomSeed` |
| `GetQDGlobalsScreenBits` | `GetQDGlobalsThePort` |
| `GetQDGlobalsWhite` | `GetRegionBounds` |
| `GetTSMDialogDocumentID` | `GetTSMTEDialogTSMTERecHandle`• |
| `GetWindowFromPort` | `GetWindowKind` |
| `GetWindowList`• | `GetWindowPort` |
| `GetWindowPortBounds` | `GetWindowSpareFlag` |
| `GetWindowStandardState` | `GetWindowUserState` |
| `InvalWindowRect` | `InvalWindowRgn` |
| `IsControlHilited` | `IsPortColor`• |
| `IsPortOffscreen` | `IsPortPictureBeingDefined` |
| `IsPortRegionBeingDefined` | `IsRegionRectangular` |
| `IsTSMTEDialog•` | `IsWindowHilited` |
| `IsWindowUpdatePending` | `IsWindowVisible` |
| `p2cstrcpy`• | `SetControlBounds` |
| `SetControlDataHandle` | `SetControlOwner` |
| `SetControlPopupMenuHandle` | `SetControlPopupMenuID` |
| `SetListCellIndent` | `SetListClickLoop` |
| `SetListClickTime` | `SetListFlags` |
| `SetListLastClick` | `SetListPort` |
| `SetListRefCon` | `SetListSelectionFlags` |
| `SetListUserHandle` | `SetListViewBounds` |
| `SetMenuHeight` | `SetMenuID` |
| `SetMenuTitle` | `SetMenuWidth` |
| `SetPortBackPixPat` | `SetPortBackPixPatDirect` |
| `SetPortBounds` | `SetPortClipRegion` |
| `SetPortDialogPort` | `SetPortFracHPenLocation` |
| `SetPortGrafProcs` | `SetPortOpColor` |
| `SetPortPenMode` | `SetPortPenPixPat` |
| `SetPortPenPixPatDirect` | `SetPortPenSize` |
| `SetPortPrintingReference` | `SetPortVisibleRegion` |
| `SetPortWindowPort` | `SetQDError`• |
| `SetQDGlobalsArrow` | `SetQDGlobalsRandomSeed` |
| `SetTSMDialogDocumentID` | `SetTSMTEDialogTSMTERecHandle`• |
| `SetWindowKind` | `SetWindowStandardState` |
| `SetWindowUserState` | `ValidWindowRect` |
| `ValidWindowRgn` |  |

The following functions were removed from `CarbonAccessors.o`.

__Table A-4__  Functions removed from CarbonAccessors.o

| `DisableMenuItem` | `EnableMenuItem` |
| `GetControlColorTable` | `GetControlDefinition` |
| `GetTSMDialogPtr` | `GetTSMDialogTextEditHandle` |
| `GetWindowGoAwayFlag` | `SetControlColorTable` |

The following functions have been added to `MacMemory.h` to aid in debugging.


```
pascal Boolean CheckAllHeaps(void);
```

Checks all applicable heaps for validity. Returns `false` if there is any corruption.


```
pascal Boolean IsHeapValid(void);
```

Similar to `CheckAllHeaps`, but checks only the application heap for validity.


```
pascal Boolean IsHandleValid(Handle h);
```

Returns `true` if the specified handle is valid. You cannot pass `NULL` or an empty handle to `IsHandleValid.`


```
pascal Boolean IsPointerValid(Ptr p);
```

Returns `true` if the specified pointer is valid. You cannot pass `NULL` or an empty pointer to `IsPointerValid.`

Three functions have been added to `Resources.h` to facilitate resource chain manipulation in Carbon applications.


```
OSErr InsertResourceFile(SInt16 refNum, RsrcChainLocation where);
```

If the file is already in the resource chain, it is removed and re-inserted at the location specified by the `where` parameter. If the file has been detached, it is added to the resource chain at the specified location. Returns `resFNotFound` if the file is not currently open. Valid constants for the `where` parameter are:

```
// RsrcChainLocation constants for InsertResourceFile
enum short
{
    kRsrcChainBelowAll = 0,         /* Below all other app files in
                                            the resource chain */
    kRsrcChainBelowApplicationMap = 1, /* Below the application's
                                            resource map */
    kRsrcChainAboveApplicationMap = 2  /* Above the application's
                                            resource map */
};
```



```
OSErr DetachResourceFile(SInt16 refNum);
```

If the file is not currently in the resource chain, this function returns `resNotFound`. Otherwise, the resource file is removed from the resource chain.


```
Boolean FSpResourceFileAlreadyOpen (
                        const FSSpec *resourceFile,
                        Boolean *inChain,
                        SInt16 *refNum);
```

This function returns `true` if the resource file is already open and known by the Resource Manager (that is, if the file is either in the current resource chain or if it’s a detached resource file). If the file is in the resource chain, the `inChain` parameter is set to `true` on exit and the function returns `true`. If the file is open but currently detached, `inChain` is set to `false` and the function returns `true`. If the file is open, the `refNum` to the file is returned.

[Next](The%20Sample%20Application.md)[Previous](New%20Carbon%20Technologies.md)

