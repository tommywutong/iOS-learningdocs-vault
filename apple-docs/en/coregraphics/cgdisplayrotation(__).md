---
title: 'CGDisplayRotation(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgdisplayrotation(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplayrotation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplayrotation%28_%3A%29.json'
content_hash: 'sha256:bfa53793c5fd1661'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayRotation(_:)

<sub>Function</sub>

Returns the rotation angle of a display in degrees.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGDisplayRotation(_ display: CGDirectDisplayID) -> Double
```

## Parameters

- `display` — The identifier of the display to be accessed.

## Return Value

The rotation angle of the display in degrees, or 0 if the display is not valid.

## Discussion

This function returns the rotation angle of a display in a clockwise direction. For example, if the specified display is rotated clockwise 90 degrees, then this function returns 90.0. After a 90-degree clockwise rotation, the physical bottom of the display is on the left side and the physical top is on the right side.

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
