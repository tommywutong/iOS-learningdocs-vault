---
title: CGGetLastMouseDelta
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cggetlastmousedelta
source_url: 'https://developer.apple.com/documentation/coregraphics/cggetlastmousedelta'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cggetlastmousedelta.json'
content_hash: 'sha256:61559791ba8c7093'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGGetLastMouseDelta

<sub>Function</sub>

Reports the change in mouse position since the last mouse movement event received by the application.

<sub>Mac Catalyst, macOS</sub>

```objc
extern void CGGetLastMouseDelta(int32_t *deltaX, int32_t *deltaY);
```

## Parameters

- `deltaX` — A pointer to a `int32_t` variable. On return, this variable contains the horizontal change in the mouse position since the last mouse movement event.

- `deltaY` — A pointer to a `int32_t` variable. On return, this variable contains the vertical change in the mouse position since the last mouse movement event.

## Discussion

This function is not recommended for general use. Instead, you should use the mouse-tracking functions provided by the `NSEvent` class.

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
