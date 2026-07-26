---
title: 'CGSetLocalEventsSuppressionInterval(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coregraphics/cgsetlocaleventssuppressioninterval(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgsetlocaleventssuppressioninterval(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgsetlocaleventssuppressioninterval%28_%3A%29.json'
content_hash: 'sha256:f3b8661f33b2de16'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGSetLocalEventsSuppressionInterval(_:)

<sub>Function</sub>

Sets the time interval in seconds that local hardware events are suppressed after posting a synthetic event.

> [!warning] Deprecated
> No longer supported

<sub>Mac Catalyst</sub>

```swift
func CGSetLocalEventsSuppressionInterval(_ seconds: CFTimeInterval) -> CGError
```

## Parameters

- `seconds` — The desired time interval in seconds. The value should be a number in the range [0.0, 10.0].

## Return Value

A result code. If the `seconds` parameter is outside the allowed range, returns `kCGErrorRangeCheck`.

## Discussion

This function determines how long local events matching an event filter are to be suppressed following the posting of a synthetic event. The default time interval for event suppression is 0.25 seconds.

This function is not recommended for general use because of undocumented special cases and undesirable side effects. The recommended replacement for this function is [CGEventSourceSetLocalEventsSuppressionInterval](cgeventsourcesetlocaleventssuppressioninterval.md), which allows the suppression interval to be adjusted for a specific event source, affecting only events posted using that event source.

## See Also

### Functions

- [CGAcquireDisplayFadeReservation](<cgacquiredisplayfadereservation(____).md>) — Reserves the fade hardware for a specified time interval.
- [CGAssociateMouseAndMouseCursorPosition](<cgassociatemouseandmousecursorposition(__).md>) — Connects or disconnects the mouse and cursor while an application is in the foreground.
- [CGBeginDisplayConfiguration](<cgbegindisplayconfiguration(__).md>) — Begins a new set of display configuration changes.
- [CGCancelDisplayConfiguration](<cgcanceldisplayconfiguration(__).md>) — Cancels a set of display configuration changes.
- [CGCaptureAllDisplays](<cgcapturealldisplays().md>) — Obtains exclusive use of all active displays, preventing other applications and system services from using the display or changing its configuration.
- [CGCaptureAllDisplaysWithOptions](<cgcapturealldisplayswithoptions(__).md>) — Captures all attached displays, using the specified options.
- [CGCompleteDisplayConfiguration](<cgcompletedisplayconfiguration(____).md>) — Completes a set of display configuration changes.
- [CGConfigureDisplayFadeEffect](<cgconfiguredisplayfadeeffect(____________).md>) — Modifies the settings of the built-in fade effect that occurs during a display configuration.
- [CGConfigureDisplayMirrorOfDisplay](<cgconfiguredisplaymirrorofdisplay(______).md>) — Changes the configuration of a mirroring set.
- [CGConfigureDisplayMode](<cgconfiguredisplaymode(______).md>) — Configures the display mode of a display. _(deprecated)_
- [CGConfigureDisplayOrigin](<cgconfiguredisplayorigin(________).md>) — Configures the origin of a display relative to the global display coordinate space.
- [CGConfigureDisplayStereoOperation](<cgconfiguredisplaystereooperation(________).md>) — Enables or disables stereo operation for a display, as part of a display configuration.
- [CGConfigureDisplayWithDisplayMode](<cgconfiguredisplaywithdisplaymode(________).md>) — Configures the display mode of a display.
- [CGCursorIsDrawnInFramebuffer](<cgcursorisdrawninframebuffer().md>) — Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory. _(deprecated)_
- [CGCursorIsVisible](<cgcursorisvisible().md>) — Returns a Boolean value indicating whether the mouse cursor is visible. _(deprecated)_
