---
title: CGCursorIsVisible()
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/coregraphics/cgcursorisvisible()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcursorisvisible()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcursorisvisible%28%29.json'
content_hash: 'sha256:747945fa9d1d1759'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGCursorIsVisible()

<sub>Function</sub>

Returns a Boolean value indicating whether the mouse cursor is visible.

> [!warning] Deprecated
> There is no replacement.

<sub>Mac Catalyst</sub>

```swift
func CGCursorIsVisible() -> boolean_t
```

## Return Value

If `true`, the cursor is visible on any display; otherwise, `false`.

## Discussion

To hide or show the cursor, you can use the functions [CGDisplayHideCursor](<cgdisplayhidecursor(__).md>) and [CGDisplayShowCursor](<cgdisplayshowcursor(__).md>).

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
- [CGDirectDisplayCopyCurrentMetalDevice](<cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
