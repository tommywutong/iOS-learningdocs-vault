---
title: 'tapEnable(tap:enable:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.1+, macOS 10.4+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgevent/tapenable(tap:enable:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgevent/tapenable(tap:enable:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgevent/tapenable%28tap%3Aenable%3A%29.json'
content_hash: 'sha256:59ee5181610d327b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGEvent](../cgevent.md)

# tapEnable(tap:enable:)

<sub>Type Method</sub>

Enables or disables an event tap.

<sub>Mac Catalyst, macOS</sub>

```swift
class func tapEnable(tap: CFMachPort, enable: Bool)
```

## Parameters

- `tap` — The event tap to enable or disable.

- `enable` — Pass `true` to enable the event tap. To disable it, pass `false`.

## Discussion

Event taps are normally enabled when created. If an event tap becomes unresponsive, or if a user requests that event taps be disabled, then a `kCGEventTapDisabled` event is passed to the event tap callback function. Event taps may be re-enabled by calling this function.

## See Also

### Functions

- [CGAcquireDisplayFadeReservation](<../cgacquiredisplayfadereservation(____).md>) — Reserves the fade hardware for a specified time interval.
- [CGAssociateMouseAndMouseCursorPosition](<../cgassociatemouseandmousecursorposition(__).md>) — Connects or disconnects the mouse and cursor while an application is in the foreground.
- [CGBeginDisplayConfiguration](<../cgbegindisplayconfiguration(__).md>) — Begins a new set of display configuration changes.
- [CGCancelDisplayConfiguration](<../cgcanceldisplayconfiguration(__).md>) — Cancels a set of display configuration changes.
- [CGCaptureAllDisplays](<../cgcapturealldisplays().md>) — Obtains exclusive use of all active displays, preventing other applications and system services from using the display or changing its configuration.
- [CGCaptureAllDisplaysWithOptions](<../cgcapturealldisplayswithoptions(__).md>) — Captures all attached displays, using the specified options.
- [CGCompleteDisplayConfiguration](<../cgcompletedisplayconfiguration(____).md>) — Completes a set of display configuration changes.
- [CGConfigureDisplayFadeEffect](<../cgconfiguredisplayfadeeffect(____________).md>) — Modifies the settings of the built-in fade effect that occurs during a display configuration.
- [CGConfigureDisplayMirrorOfDisplay](<../cgconfiguredisplaymirrorofdisplay(______).md>) — Changes the configuration of a mirroring set.
- [CGConfigureDisplayMode](<../cgconfiguredisplaymode(______).md>) — Configures the display mode of a display. _(deprecated)_
- [CGConfigureDisplayOrigin](<../cgconfiguredisplayorigin(________).md>) — Configures the origin of a display relative to the global display coordinate space.
- [CGConfigureDisplayStereoOperation](<../cgconfiguredisplaystereooperation(________).md>) — Enables or disables stereo operation for a display, as part of a display configuration.
- [CGConfigureDisplayWithDisplayMode](<../cgconfiguredisplaywithdisplaymode(________).md>) — Configures the display mode of a display.
- [CGCursorIsDrawnInFramebuffer](<../cgcursorisdrawninframebuffer().md>) — Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory. _(deprecated)_
- [CGCursorIsVisible](<../cgcursorisvisible().md>) — Returns a Boolean value indicating whether the mouse cursor is visible. _(deprecated)_
