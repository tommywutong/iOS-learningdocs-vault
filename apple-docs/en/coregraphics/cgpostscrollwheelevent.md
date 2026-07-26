---
title: CGPostScrollWheelEvent
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.6 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/coregraphics/cgpostscrollwheelevent
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpostscrollwheelevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpostscrollwheelevent.json'
content_hash: 'sha256:4fba6c642f39f639'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPostScrollWheelEvent

<sub>Function</sub>

Synthesizes a low-level scrolling event on the local machine.

<sub>Mac Catalyst, macOS</sub>

```objc
extern CGError CGPostScrollWheelEvent(CGWheelCount wheelCount, int32_t wheel1, ...);
```

### Parameters

- **wheelCount** — The number of scrolling devices, up to a maximum of 3.
- **wheel1** — A value that reflects the movement of the primary scrolling device on the mouse.
- **…** — Up to two values that reflect the movements of the other scrolling devices on the mouse (if any).

### Returns

A result code. See the result codes described in [Quartz Display Services](quartz-display-services.md).

## Discussion

Scrolling movement is generally represented by small signed integer values, typically in a range from -10 to +10.  Large values may have unexpected results, depending on the application that processes the event.

This function is not recommended for general use because of undocumented special cases and undesirable side effects. The recommended replacement for this function is [CGEventCreateScrollWheelEvent](cgeventcreatescrollwheelevent.md), which allows you to create a scrolling event and customize the event before posting it to the event system.

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
