---
title: 'CGConfigureDisplayMirrorOfDisplay(_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgconfiguredisplaymirrorofdisplay(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgconfiguredisplaymirrorofdisplay(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgconfiguredisplaymirrorofdisplay%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0e9ef1712ace0b2b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGConfigureDisplayMirrorOfDisplay(_:_:_:)

<sub>Function</sub>

Changes the configuration of a mirroring set.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGConfigureDisplayMirrorOfDisplay(_ config: CGDisplayConfigRef?, _ display: CGDirectDisplayID, _ master: CGDirectDisplayID) -> CGError
```

## Parameters

- `config` — A display configuration, acquired by calling [CGBeginDisplayConfiguration](<cgbegindisplayconfiguration(__).md>).

- `display` — The identifier of the display to add to a mirroring set.

- `master` — A display in a mirroring set, or `kCGNullDirectDisplay` to disable mirroring. To specify the main display, use [CGMainDisplayID](<cgmaindisplayid().md>).

## Return Value

A result code. See `Core Graphics Data Types and Constants`.

## Discussion

Display mirroring and display matte generation are implemented either in hardware (preferred) or software, at the discretion of the device driver.

- Hardware mirroring

With hardware mirroring enabled, all drawing is directed to the primary display—see [CGDisplayPrimaryDisplay](<cgdisplayprimarydisplay(__).md>).

If the device driver selects hardware matte generation, the display bounds and row-bytes values are adjusted to reflect the active drawable area.

- Software mirroring

In this form of mirroring, identical content is drawn into each display in the mirroring set. Applications that use the window system need not be concerned about mirroring, as the window system takes care of all flushing of window content to the appropriate displays.

Applications that draw directly to the display, as with display capture, must make sure to draw the same content to all mirrored displays in a software mirror set. When drawing to software mirrored displays using a full screen OpenGL context (not drawing through a window), you should create shared OpenGL contexts for each display and rerender for each display.

You can use the function [CGGetActiveDisplayList](<cggetactivedisplaylist(______).md>) to determine which displays are active, or drawable. This automatically gives your application the correct view of the current displays.

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
- [CGConfigureDisplayMode](<cgconfiguredisplaymode(______).md>) — Configures the display mode of a display. _(deprecated)_
- [CGConfigureDisplayOrigin](<cgconfiguredisplayorigin(________).md>) — Configures the origin of a display relative to the global display coordinate space.
- [CGConfigureDisplayStereoOperation](<cgconfiguredisplaystereooperation(________).md>) — Enables or disables stereo operation for a display, as part of a display configuration.
- [CGConfigureDisplayWithDisplayMode](<cgconfiguredisplaywithdisplaymode(________).md>) — Configures the display mode of a display.
- [CGCursorIsDrawnInFramebuffer](<cgcursorisdrawninframebuffer().md>) — Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory. _(deprecated)_
- [CGCursorIsVisible](<cgcursorisvisible().md>) — Returns a Boolean value indicating whether the mouse cursor is visible. _(deprecated)_
- [CGDirectDisplayCopyCurrentMetalDevice](<cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
