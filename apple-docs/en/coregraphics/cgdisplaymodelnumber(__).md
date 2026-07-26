---
title: 'CGDisplayModelNumber(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgdisplaymodelnumber(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaymodelnumber(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaymodelnumber%28_%3A%29.json'
content_hash: 'sha256:c461da9da4fe085d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayModelNumber(_:)

<sub>Function</sub>

Returns the model number of a display monitor.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGDisplayModelNumber(_ display: CGDirectDisplayID) -> UInt32
```

## Parameters

- `display` — The identifier of the display to be accessed.

## Return Value

A model number for the monitor associated with the specified display, or a constant to indicate an exception—see the discussion below.

## Discussion

This function uses I/O Kit to identify the monitor associated with the specified display. The return value depends on the following:

- If I/O Kit can identify the monitor, the product ID code for the monitor is returned.
- If I/O Kit can’t identify the monitor, `kDisplayProductIDGeneric` is returned.
- If no monitor is connected, a value of `0xFFFFFFFF` is returned.

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
