---
title: 'CGRegisterScreenRefreshCallback(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coregraphics/cgregisterscreenrefreshcallback(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgregisterscreenrefreshcallback(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgregisterscreenrefreshcallback%28_%3A_%3A%29.json'
content_hash: 'sha256:c6403925d0528333'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGRegisterScreenRefreshCallback(_:_:)

<sub>Function</sub>

Registers a callback function to be invoked when local displays are refreshed or modified.

> [!warning] Deprecated
> Use display streaming instead. See [Quartz Display Services](quartz-display-services.md).

<sub>Mac Catalyst</sub>

```swift
func CGRegisterScreenRefreshCallback(_ callback: CGScreenRefreshCallback, _ userInfo: UnsafeMutableRawPointer?) -> CGError
```

## Parameters

- `callback` — A pointer to the callback function to be registered.

- `userInfo` — A pointer to user-defined data, or `NULL`. The `userParameter` argument is passed back to the callback function each time it’s invoked.

## Return Value

A result code. See `Core Graphics Data Types and Constants`.

## Discussion

A callback function may be registered multiple times with different user-defined data pointers, resulting in multiple registration entries.  For each registration, when notification is no longer needed, you should call the function [CGUnregisterScreenRefreshCallback](<cgunregisterscreenrefreshcallback(____).md>) to remove the registration.

The callback function you register is invoked only if your application has an active event loop. The callback is invoked in the same thread of execution that is processing events within your application.

### Special Considerations

In OS X v10.4 and earlier, the result code returned by this function is a random value and should be ignored. In macOS 10.5 and later, the result code is valid.

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
