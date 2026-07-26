---
title: CGMainDisplayID()
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgmaindisplayid()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgmaindisplayid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgmaindisplayid%28%29.json'
content_hash: 'sha256:155a11d64921b481'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGMainDisplayID()

<sub>Function</sub>

Returns the display ID of the main display.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGMainDisplayID() -> CGDirectDisplayID
```

## Return Value

The display ID assigned to the main display.

## Discussion

The main display is the display with its screen location at (0,0) in the global display coordinate space. In a system without display mirroring, the display with the menu bar is typically the main display.

If mirroring is enabled and the menu bar appears on more than one display, this function provides a reliable way to find the main display.

In case of hardware mirroring, the drawable display becomes the main display. In case of software mirroring, the display with the highest resolution and deepest pixel depth typically becomes the main display.

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
