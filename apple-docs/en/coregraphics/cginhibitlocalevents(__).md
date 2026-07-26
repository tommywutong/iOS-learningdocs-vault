---
title: 'CGInhibitLocalEvents(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coregraphics/cginhibitlocalevents(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cginhibitlocalevents(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cginhibitlocalevents%28_%3A%29.json'
content_hash: 'sha256:46bd6037bf1174ed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGInhibitLocalEvents(_:)

<sub>Function</sub>

Turns off local hardware events in the current session.

> [!warning] Deprecated
> No longer supported

<sub>Mac Catalyst</sub>

```swift
func CGInhibitLocalEvents(_ inhibit: boolean_t) -> CGError
```

## Parameters

- `inhibit` — Pass `true` to specify that local hardware events on the remote system should be inhibited; otherwise, pass `false`.

## Return Value

A result code. See the result codes described in [Quartz Display Services](quartz-display-services.md).

## Discussion

This function is typically used during remote operation of a system to disconnect the keyboard and mouse for a short period of time, as in automated system testing or telecommuting applications.

The `CGInhibitLocalEvents` function is not recommended for general use because of undocumented special cases and undesirable side effects. For example, this function can permanently disable the keyboard and mouse, rendering the system unusable. The recommended replacement for this function is [CGEventSourceSetLocalEventsFilterDuringSuppressionState](<cgeventsource/setlocaleventsfilterduringsuppressionstate(__state_).md>).

### Special Considerations

In OS X v10.2 and earlier, this function inhibits local events only after a synthetic keyboard or mouse event is posted by the calling application. In macOS 10.3 and later, event inhibition takes effect immediately. If your application terminates for any reason, event inhibition on the remote system is immediately turned off.

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
