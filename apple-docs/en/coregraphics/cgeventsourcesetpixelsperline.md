---
title: CGEventSourceSetPixelsPerLine
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventsourcesetpixelsperline
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventsourcesetpixelsperline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventsourcesetpixelsperline.json'
content_hash: 'sha256:f7137ebdd66fb2f9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGEventSourceSetPixelsPerLine

<sub>Function</sub>

Sets the scale of pixels per line in a scrolling event source.

<sub>Mac Catalyst, macOS</sub>

```objc
extern void CGEventSourceSetPixelsPerLine(CGEventSourceRef source, double pixelsPerLine);
```

## Parameters

- `source` — The event source to access.

- `pixelsPerLine` — The scale of pixels per line in the specified event source.

## Discussion

This function sets the scale of pixels per line in the specified event source. For example, if you pass the value 12.0 in the `pixelsPerLine` parameter, the scale of pixels per line in the event source would be changed to 12.0. Every scrolling event can be interpreted to be scrolling by pixel or by line. By default, the scale is about ten pixels per line. You can retrieve the scale with the function `CGEventSourceGetPixelsPerLine`.

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
