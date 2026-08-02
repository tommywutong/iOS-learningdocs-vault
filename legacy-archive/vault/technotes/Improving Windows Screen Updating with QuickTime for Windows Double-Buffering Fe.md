---
title: Improving Windows Screen Updating with QuickTime for Windows Double-Buffering
  Feature
apple_id: DTS10003802
resource_type: Technical Note
platform: macOS
topic: null
technology: QuickTime
published: '2005-10-18'
source_url: https://developer.apple.com/library/archive/technotes/tn2153/_index.html
archived_at: '2026-07-26T19:54:08.682140Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2153

# Improving Windows Screen Updating with QuickTime for Windows Double-Buffering Feature

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

This TechNote describes the new QuickTime double-buffering feature which provides optimal screen updating for Windows applications.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobqgiwugsbrfvke4vcbi4yq)[Feature Is Optional](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobqgiwugsbrfvke4vcbi4za)[Simplest Use](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobqgiwugsbrfvke4vcbi4zq)[Using the New APIs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobqgiwugsbrfvke4vcbi42q)[New flags](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobqgiwugsbrfvke4vcbi43a)[New functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobqgiwugsbrfvke4vcbi43q)[Important Notes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobqgiwugsbrfvke4vcbi44a)[QuickTime](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobqgiwugsbrfvke4vcbi4yte)[QuickDraw](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobqgiwugsbrfvke4vcbi4ytg)[GDI](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobqgiwugsbrfvke4vcbi4yti)[Direct PixMap Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobqgiwugsbrfvke4vcbi4ytk)[Examples](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobqgiwugsbrfvke4vcbi44q)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobqgiwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

QuickTime 6.4 includes a new double-buffering feature to improve screen updating for Windows applications. This feature uses a deferred flushing model, similar to that used on Mac OS X. It provides a complete off-screen (back) buffer for each QuickTime graphics port, flushing the buffer to the screen periodically or upon explicit request. This approach provides numerous benefits, including improved clipping and elimination of occasional flashing of UI elements.

Here's more detail:

Updated pixel data for QuickTime graphics ports are drawn into a back buffer -- they are not immediately drawn to the screen. The "dirty" area (the area that has changed) for each port is accumulated until a flush is performed, at which time the entire dirty region is drawn to the screen.

__Important:__ QuickTime will automatically flush the dirty region to the screen when movies are drawn or when movies are idled.

Your application can also explicitly perform a flush when appropriate (see [New functions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobqgiwugsbrfvke4vcbi43q)).

[Back to Top](#)

## Feature Is Optional

Some applications may choose not to use this feature, so its use is optional (see [Important Notes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobqgiwugsbrfvke4vcbi44a) below).

To use it, your Windows application must activate it by passing the `kInitializeQTMLEnableDoubleBufferedSurface` flag to `InitializeQTML` at startup as shown here:

__Listing 1__  Activating QuickTime double-buffering.

```
// enable QuickTime double-buffering
InitializeQTML(kInitializeQTMLEnableDoubleBufferedSurface);
```

Once the feature is activated, QuickTime will then automatically use double-buffering for screen updates to graphics ports associated with the requesting application.

[Back to Top](#)

## Simplest Use

If your application doesn’t perform any special processing of update regions, it can simply activate the feature as shown in Listing 1 above. QuickTime will use it by default to perform dirty region accumulation and basic flushing for normal screen update operations. In some cases, no further use of the API will be required.

[Back to Top](#)

## Using the New APIs

If your application does perform special processing of update regions, you will need to use the new double-buffering APIs to take advantage of this facility. This section briefly describes these APIs.

### New flags

```
 kInitializeQTMLEnableDoubleBufferedSurface
```

The `kInitializeQTMLEnableDoubleBufferedSurface` flag is passed in the `InitializeQTML` call to activate the double-buffering feature.

```
kQTMLNoDoubleBufferPort
```

The `kQTMLNoDoubleBufferPort` flag is passed in the `CreatePortAssociation` call to disable double buffering on a particular port. This flag will be ignored if the feature hasn’t been activated.

### New functions

The following new APIs can be used to add a region (`MacRegion`, `Rect`, or Windows `HRGN`) to the accumulated dirty region for a port:

```
QTMLAddRgnToDirtyRgn(GrafPtr port, RgnHandle *dirtyRgn)
QTMLAddRectToDirtyRgn(GrafPtr port, Rect *dirtyRect)
QTMLAddNativeRgnToDirtyRgn(GrafPtr port, void *dirtyHRGN)
```

Use these new APIs to:

- indicate an application has drawn directly into the back buffer using `HDC` access to the back buffer (through the `HDC` access APIs)
- add a region dirtied by directly manipulating the bits in a `pixMap` (after locking it)
- add Windows update regions to the dirty region during `WM_PAINT` handling to explictily force them to refresh

__Note:__ The above calls are provided to allow you to add to the dirty region in a format convenient to your code, with a minimum of conversion. Use whichever call is appropriate for the update task at hand.

__QTMLFlushDirtyPorts__

Walks the list of all dirtied ports, flushing their dirtied regions to the screen. This call is intended to be used for periodic total flushes, not for flushes that are being invoked because of an immediate need to sync a particular port’s back buffer to the screen.

```
QTMLFlushDirtyPorts()
```

__QTMLFlushPortDirtyRgn__

Flushes the dirty region of the specified port to the screen. This call is useful during `WM_PAINT` handling to flush the window contents to the screen after adding the Windows update region to the dirty region.

```
QTMLFlushPortDirtyRgn(GrafPtr port)
```

__QTMLGetBackbufferHDC__

Allows GDI access to the back buffer. The caller must release the back buffer `HDC` with `QTMLReleaseBackbufferHDC`. This is reference counted, so a Release call must be made for each Get call.

```
QTMLGetBackbufferHDC(GrafPtr port, HDC *backBufferHDC)
```

__QTMLReleaseBackbufferHDC__

Allows GDI access to the back buffer. The caller will have to call `QTMLAddRegionToDirtyRgn` after releasing the back buffer `HDC` in order to let QuickTime know what area of the back buffer has been dirtied.

```
QTMLReleaseBackbufferHDC(GrafPtr port, HDC *backBufferHDC)
```

[Back to Top](#)

## Important Notes

Applications should avoid combining QTML and Windows drawing on top of each other into a single window. Use of a child `hWnd` for a QTML owned area within a Windows owned window is encouraged.

Another important consideration is your application must not cache the `baseAddress` of the port `pixMap`. When the port is locked, the `pixMap` will be updated to reflect the backbuffer `baseAddress` and metrics, and when it is unlocked it will contain the screen `baseAddress` and metrics. This backbuffer `baseAddress` may change as the window size changes or for a variety of other reasons.

Drawing into a port generally falls into one of four categories which all behave slightly differently:

### QuickTime

QuickTime drawing involves a movie drawing visual elements into the port associated with the movie. This type of drawing will be done into the backbuffer if double buffering is enabled, and the dirty region will automatically be added to the port and flushed to the screen.

### QuickDraw

Drawing done using QuickDraw calls will automatically add the appropriate dirty region to the port, but they will not automatically flush to the screen (this is done to allow you to perform batches of QuickDraw rendering, but only incur the expense of a single blit to the screen). The screen flush must be done either explicitly after the call(s) or through a periodic timer.

### GDI

Drawing can be done into a port using GDI to render into the `HDC` acquired from `QTMLGetBackbufferHDC`. Since QuickTime and QuickDraw have no hint about what pixels have been touched, it is important to call `QTMLAddDirtyRect` or something similar, or the pixels that were touched may not get flushed to the screen. As with QuickDraw rendering, an explicit flush is required.

### Direct PixMap Access

If you are careful to lock the port, you can directly manipulate the pixels in the backbuffer since the `baseAddress` and `rowBytes` will be updated to point there. As with GDI drawing, you must explicitly declare the region that you have dirtied in the backbuffer, and an explicit flush is required.

As with any new feature, if you want to use the double-buffering feature but also wish to retain backwards compatibility with older QuickTime versions, be sure to check the QuickTime version when your application launches and do not attempt to use the new APIs on earlier QuickTime versions. These calls should function back to QuickTime 6.4.

Here's code showing how to get the QuickTime version:

__Listing 2__  Getting the QuickTime version.

```
{
    /* check the version of QuickTime installed */

    long version;
    OSErr result;

    result = Gestalt(gestaltQuickTime,&version);
    if ((result == noErr) && (version >= 0x06408000))
    {
        /* we have version 6.4 or better! */
    }
}
```

[Back to Top](#)

## Examples

Example 1

An application opting into this behavior may wish to handle `WM_PAINT` messages a little differently, since there is already a valid representation of the window in the offscreen buffer. The Windows update region needs to be added to the port's dirty region, and then the port can be flushed to the screen. A simple example of this follows:

__Listing 3__  Adding Windows update region to the port's dirty region, then flushing the port to the screen.

```
case WM_PAINT:
{
    RgnHandle   macUpdateRgn = nil;
    HRGN    winUpdateRgn = CreateRectRgn(0,0,0,0);

    macUpdateRgn = NewRgn();

    BeginUpdate((GrafPtr) moviePort);
    // If your app does any special handling of update regions,
    // grab the Mac update region. Otherwise,
    // you can skip this.
    MacCopyRgn(moviePort->visRgn, macUpdateRgn);
    EndUpdate((GrafPtr) moviePort);

    // If there is any new drawing that your app wants to
    // do (in response to the MacUpdateRgn or for any other
    // reason) it should be done here. This drawing will
    // be done into the backbuffer, and flushed to the screen
    // at the end of this call.

    // Get the Windows update region
    GetUpdateRgn(hWnd, winUpdateRgn, FALSE);
    // Call BeginPaint/EndPaint to clear the update region
    BeginPaint (hWnd, &ps);
    EndPaint(hWnd, &ps);

    // Add to the dirty region of the port any region
    // that Windows says needs updating. This allows the
    // union of the two to be copied from the back buffer
    // to the screen on the next flush.
    QTMLAddNativeRgnToDirtyRgn((GrafPtr) moviePort, winUpdateRgn);
    DeleteObject(winUpdateRgn);

    // Flush the entire dirty region to the screen
    QTMLFlushPortDirtyRgn((GrafPtr) moviePort);
}
```

Example 2

It is often useful to combine a long series of drawing operations and use a single flush at the end to display them all simultaneously. The following example draws a series of inset rectangles, first using QuickDraw, and then using GDI to draw directly into the backbuffer `HDC`. All of these are flushed to the screen at once at the end.

__Listing 4__  Combining a long series of drawing operations and using a single flush to display them all simultaneously.

```
{
    Rect    myRect;
    Pattern currentPattern;

    myRect.top = myRect.left = 0;
    myRect.bottom = myRect.right = 200;

    SetPort(myWindowPort);

    // this drawing is done using QuickDraw.
    // QuickDraw drawing operations
    // will automatically add the area that
    // they have touched to the accumulated
    // dirty region for the port.
    while (myRect.top < 50) {
        // alternate patterns
        currentPattern =
            (currentPattern == pattern1) ? pattern2 : pattern1;
        // fill the current rect with the pattern
        MacFillRect(myRect, currentPattern);
        // inset the rect a tiny bit.
        MacInsetRect(myRect, 10, 10);
    }

    {
        RECT winRect;
        HDC backbufferHDC = NULL;

        // get the HDC of the Backbuffer for the port
        QTMLGetBackbufferHDC(myWindowPort, &backbufferHDC);

        // create a Windows RECT where we left off with our QuickDraw
        // rendering above
        winRect.top = myRect.top;
        winRect.left = myRect.left;
        winRect.bottom = myRect.bottom;
        winRect.right = myRect.right;

        // fill in yet another rect
        FillRect(backbufferHDC, &winRect, hBrush);

        // need to release that backbuffer HDC.
        QTMLReleaseBackbufferHDC(myWindowPort, &backbufferHDC);

        // since this drawing was done directly into the backbuffer,
        // we need to add the dirty region to the port.
        QTMLAddRectToDirtyRgn(myWindowPort, & myRect);
    }

    // now, go ahead and flush all that drawing to the screen
    QTMLFlushPortDirtyRgn(myWindowPort);
}
```

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-10-18 | New document that quickTime 6.4 includes a facility to improve screen updating for Windows applications |

