---
title: CGEventSourceSetLocalEventsSuppressionInterval
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.4+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventsourcesetlocaleventssuppressioninterval
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventsourcesetlocaleventssuppressioninterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventsourcesetlocaleventssuppressioninterval.json'
content_hash: 'sha256:afba47727e821f5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGEventSourceSetLocalEventsSuppressionInterval

<sub>Function</sub>

Sets the interval that local hardware events may be suppressed following the posting of a Quartz event.

<sub>Mac Catalyst, macOS</sub>

```objc
extern void CGEventSourceSetLocalEventsSuppressionInterval(CGEventSourceRef source, CFTimeInterval seconds);
```

## Parameters

- `source` — The event source to access.

- `seconds` — The period of time in seconds that local hardware events (keyboard or mouse) are suppressed after posting a Quartz event created with the specified event source. The value should be a number in the range [0.0, 10.0].

## Discussion

By default, the system does not suppress local hardware events from the keyboard or mouse during a short interval after a Quartz event is posted. You can use the function [CGEventSourceSetLocalEventsFilterDuringSuppressionState](<cgeventsource/setlocaleventsfilterduringsuppressionstate(__state_).md>) to modify this behavior.

This function sets the period of time in seconds that local hardware events may be suppressed after posting a Quartz event created with the specified event source. The default suppression interval is 0.25 seconds.

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
