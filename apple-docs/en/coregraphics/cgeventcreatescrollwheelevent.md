---
title: CGEventCreateScrollWheelEvent
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventcreatescrollwheelevent
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventcreatescrollwheelevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventcreatescrollwheelevent.json'
content_hash: 'sha256:bbb767610b177a1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGEventCreateScrollWheelEvent

<sub>Function</sub>

Returns a new Quartz scrolling event.

<sub>Mac Catalyst, macOS</sub>

```objc
extern CGEventRefCGEventCreateScrollWheelEvent(CGEventSourceRef source, CGScrollEventUnit units, uint32_t wheelCount, int32_t wheel1, ...);
```

### Parameters

- **source** — An event source taken from another event, or `NULL`.
- **units** — The unit of measurement for the scrolling event. Pass one of the constants listed in [CGScrollEventUnit](cgscrolleventunit.md).
- **wheelCount** — The number of scrolling devices on the mouse, up to a maximum of 3.
- **wheel1** — A value that reflects the movement of the primary scrolling device on the mouse. Scrolling movement is generally represented by small signed integer values, typically in a range from -10 to +10.  Large values may have unexpected results, depending on the application that processes the event.
- **…** — Up to two values that reflect the movements of the other scrolling devices on the mouse, if any.

### Returns

A new scrolling event, or `NULL` if the event could not be created. When you no longer need the event, you should release it using the function `CFRelease`.

## Discussion

This function allows you to create a scrolling event and customize the event before posting it to the event system.

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
