---
title: CGDisplayModeRetain
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.6+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaymoderetain
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaymoderetain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaymoderetain.json'
content_hash: 'sha256:30965c0b02a48a1d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayModeRetain

<sub>Function</sub>

Retains a Core Graphics display mode.

<sub>Mac Catalyst, macOS</sub>

```objc
extern CGDisplayModeRefCGDisplayModeRetain(CGDisplayModeRef mode);
```

## Parameters

- `mode` — A display mode to be retained.

## Return Value

The input value `mode`.

## Discussion

This function is equivalent to [CFRetain](../corefoundation/cfretain.md), except that it does not cause an error if the `mode` parameter is `NULL`.

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
