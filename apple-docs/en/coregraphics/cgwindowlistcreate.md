---
title: CGWindowListCreate
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgwindowlistcreate
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowlistcreate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowlistcreate.json'
content_hash: 'sha256:0a532762b964304b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGWindowListCreate

<sub>Function</sub>

Returns the list of window IDs associated with the specified windows in the current user session.

<sub>Mac Catalyst, macOS</sub>

```objc
extern CFArrayRefCGWindowListCreate(CGWindowListOption option, CGWindowID relativeToWindow);
```

## Parameters

- `option` — The options describing which window IDs to return. Typical options let you obtain IDs for all windows or for windows above or below the window specified in the `relativeToWindow` parameter. For more information, see [Window List Option Constants](window-list-option-constants.md).

- `relativeToWindow` — The ID of the window to use as a reference point when determining which other windows to return. For options that do not require a reference window, this parameter can be [kCGNullWindowID](kcgnullwindowid.md).

## Return Value

An array of [CGWindowID](cgwindowid.md) values corresponding to the desired windows. If there are no windows matching the desired criteria, the function returns an empty array. If you call this function from outside of a GUI security session or when no window server is running, this function returns `NULL`.

## See Also

### Functions

- [CGAcquireDisplayFadeReservation](<cgacquiredisplayfadereservation(____).md>) — Reserves the fade hardware for a specified time interval.
- [CGAssociateMouseAndMouseCursorPosition](<cgassociatemouseandmousecursorposition(__).md>) — Connects or disconnects the mouse and cursor while an application is in the foreground.
- [CGBeginDisplayConfiguration](<cgbegindisplayconfiguration(__).md>) — Begins a new set of display configuration changes.
- [CGCancelDisplayConfiguration](<cgcanceldisplayconfiguration(__).md>) — Cancels a set of display configuration changes.
- [CGCaptureAllDisplays](<cgcapturealldisplays().md>) — Obtains exclusive use of all active displays, preventing other applications and system services from using the display or changing its configuration.
- [CGCaptureAllDisplaysWithOptions](<cgcapturealldisplayswithoptions(__).md>) — Captures all attached displays, using the specified options.
- [CGColorConversionInfoCreateFromList](cgcolorconversioninfocreatefromlist.md) — Creates a conversion between an arbitrary number of specified color spaces.
- [CGCompleteDisplayConfiguration](<cgcompletedisplayconfiguration(____).md>) — Completes a set of display configuration changes.
- [CGConfigureDisplayFadeEffect](<cgconfiguredisplayfadeeffect(____________).md>) — Modifies the settings of the built-in fade effect that occurs during a display configuration.
- [CGConfigureDisplayMirrorOfDisplay](<cgconfiguredisplaymirrorofdisplay(______).md>) — Changes the configuration of a mirroring set.
- [CGConfigureDisplayMode](<cgconfiguredisplaymode(______).md>) — Configures the display mode of a display. _(deprecated)_
- [CGConfigureDisplayOrigin](<cgconfiguredisplayorigin(________).md>) — Configures the origin of a display relative to the global display coordinate space.
- [CGConfigureDisplayStereoOperation](<cgconfiguredisplaystereooperation(________).md>) — Enables or disables stereo operation for a display, as part of a display configuration.
- [CGConfigureDisplayWithDisplayMode](<cgconfiguredisplaywithdisplaymode(________).md>) — Configures the display mode of a display.
- [CGContextDrawPDFDocument](cgcontextdrawpdfdocument.md) _(deprecated)_
