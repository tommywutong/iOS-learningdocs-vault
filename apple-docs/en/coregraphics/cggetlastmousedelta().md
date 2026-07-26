---
title: CGGetLastMouseDelta()
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cggetlastmousedelta()
source_url: 'https://developer.apple.com/documentation/coregraphics/cggetlastmousedelta()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cggetlastmousedelta%28%29.json'
content_hash: 'sha256:2bee7e3c2bbc03c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGGetLastMouseDelta()

<sub>Function</sub>

Reports the change in mouse position since the last mouse movement event received by the application.

<sub>macOS</sub>

```swift
func CGGetLastMouseDelta() -> (x: Int32, y: Int32)
```

## Return Value

A tuple whose `x` and `y` members represent the horizontal and vertical change in the mouse position since the last mouse movement event.

## Discussion

This function is not recommended for general use. Instead, you should use the mouse-tracking functions provided by the [NSEvent](../appkit/nsevent.md) class.

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
