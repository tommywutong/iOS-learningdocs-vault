---
title: 'CGDisplayIsInHWMirrorSet(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgdisplayisinhwmirrorset(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplayisinhwmirrorset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplayisinhwmirrorset%28_%3A%29.json'
content_hash: 'sha256:b2a358f54f3a01af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayIsInHWMirrorSet(_:)

<sub>Function</sub>

Returns a Boolean value indicating whether a display is in a hardware mirroring set.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGDisplayIsInHWMirrorSet(_ display: CGDirectDisplayID) -> boolean_t
```

## Parameters

- `display` — The identifier of the display to be accessed.

## Return Value

If `true`, the specified display is a member of a hardware mirroring set; otherwise, `false`.

## Discussion

When hardware mirroring is enabled, the contents of a single framebuffer are rendered in all displays in the hardware mirroring set. All drawing operations are directed to the primary display in the set—see [CGDisplayPrimaryDisplay](<cgdisplayprimarydisplay(__).md>).

For more information about display mirroring, see [CGConfigureDisplayMirrorOfDisplay](<cgconfiguredisplaymirrorofdisplay(______).md>).

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
