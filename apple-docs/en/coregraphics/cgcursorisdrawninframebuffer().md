---
title: CGCursorIsDrawnInFramebuffer()
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/coregraphics/cgcursorisdrawninframebuffer()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcursorisdrawninframebuffer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcursorisdrawninframebuffer%28%29.json'
content_hash: 'sha256:b02419e23a1470dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGCursorIsDrawnInFramebuffer()

<sub>Function</sub>

Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory.

> [!warning] Deprecated
> There is no replacement.

<sub>Mac Catalyst</sub>

```swift
func CGCursorIsDrawnInFramebuffer() -> boolean_t
```

## Return Value

If `true`, the cursor is drawn in framebuffer memory; otherwise, `false`.

## Discussion

This function returns a Boolean value that indicates whether or not the cursor is drawn in the framebuffer. (The cursor could exist in an overlay plane or a similar mechanism that puts pixels on-screen without altering framebuffer content.) If the cursor is drawn in the framebuffer, it is read back along with window data.

The reported Boolean value is based on the union of the state of the cursor on all displays.  If the cursor is drawn in the framebuffer on any display, the function returns `true`.

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
- [CGCursorIsVisible](<cgcursorisvisible().md>) — Returns a Boolean value indicating whether the mouse cursor is visible. _(deprecated)_
- [CGDirectDisplayCopyCurrentMetalDevice](<cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
