---
title: 'CGAcquireDisplayFadeReservation(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgacquiredisplayfadereservation(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgacquiredisplayfadereservation(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgacquiredisplayfadereservation%28_%3A_%3A%29.json'
content_hash: 'sha256:802189b0f271ee69'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGAcquireDisplayFadeReservation(_:_:)

<sub>Function</sub>

Reserves the fade hardware for a specified time interval.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGAcquireDisplayFadeReservation(_ seconds: CGDisplayReservationInterval, _ token: UnsafeMutablePointer<CGDisplayFadeReservationToken>?) -> CGError
```

## Parameters

- `seconds` — The desired number of seconds to reserve the fade hardware. An application can specify any value in the interval `(0, kCGMaxDisplayReservationInterval]`.

- `token` — A pointer to storage (provided by the caller) for a fade reservation token. On return, the storage contains a new token.

## Return Value

Returns [kCGErrorNoneAvailable](cgerror/noneavailable.md) if another fade reservation is in effect. Otherwise, returns [kCGErrorSuccess](cgerror/success.md).

## Discussion

Before performing a fade operation, an application must reserve the fade hardware for a specified period of time. Quartz returns a token that represents a new fade reservation. The application uses this token as an argument in subsequent calls to other display fade functions.

During the fade reservation interval, the application has exclusive rights to use the fade hardware. At the end of the interval, the token becomes invalid and the hardware automatically returns to a normal state. Typically, the application calls [CGReleaseDisplayFadeReservation](<cgreleasedisplayfadereservation(__).md>) to release the fade reservation before it expires.

## See Also

### Functions

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
- [CGDirectDisplayCopyCurrentMetalDevice](<cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
