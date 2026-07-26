---
title: CGEventSourceSetUserData
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.4+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventsourcesetuserdata
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventsourcesetuserdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventsourcesetuserdata.json'
content_hash: 'sha256:2ced8284e1df5fc4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGEventSourceSetUserData

<sub>Function</sub>

Sets the 64-bit user-specified data for a Quartz event source.

<sub>Mac Catalyst, macOS</sub>

```objc
extern void CGEventSourceSetUserData(CGEventSourceRef source, int64_t userData);
```

## Parameters

- `source` — The event source to access.

- `userData` — The user-specified data. For example, you could specify a vendor hardware ID.

## Discussion

Each input event includes 64 bits of user-specified data. This function sets the user-specified data for all events created by the specified event source. This data may also be set per event using the [CGEventSetIntegerValueField](<cgevent/setintegervaluefield(__value_).md>) function.

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
