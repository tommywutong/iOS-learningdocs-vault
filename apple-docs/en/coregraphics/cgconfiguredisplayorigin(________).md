---
title: 'CGConfigureDisplayOrigin(_:_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgconfiguredisplayorigin(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgconfiguredisplayorigin(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgconfiguredisplayorigin%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:859847fd85361ce2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGConfigureDisplayOrigin(_:_:_:_:)

<sub>Function</sub>

Configures the origin of a display relative to the global display coordinate space.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGConfigureDisplayOrigin(_ config: CGDisplayConfigRef?, _ display: CGDirectDisplayID, _ x: Int32, _ y: Int32) -> CGError
```

## Parameters

- `config` — A display configuration that you acquire by calling [CGBeginDisplayConfiguration](<cgbegindisplayconfiguration(__).md>).

- `display` — The identifier of the display to configure.

- `x` — The desired x-coordinate for the upper-left corner of the display.

- `y` — The desired y-coordinate for the upper-left corner of the display.

## Return Value

A result code. If the request to configure the origin of the display is successful, the result is `kCGErrorSuccess`. For other possible values, see [CGError](cgerror.md).

## Discussion

In Quartz, the upper-left corner of a display is the origin. You specify the origin of a display in the global display coordinate space. The origin of the main or primary display is `(0,0)`.

The placement of the new origin is as close as possible to the requested location, without overlapping or leaving a gap between displays.

If you use this function to change the origin of a mirrored display, the mirrored set might not include the display.

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
- [CGConfigureDisplayStereoOperation](<cgconfiguredisplaystereooperation(________).md>) — Enables or disables stereo operation for a display, as part of a display configuration.
- [CGConfigureDisplayWithDisplayMode](<cgconfiguredisplaywithdisplaymode(________).md>) — Configures the display mode of a display.
- [CGCursorIsDrawnInFramebuffer](<cgcursorisdrawninframebuffer().md>) — Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory. _(deprecated)_
- [CGCursorIsVisible](<cgcursorisvisible().md>) — Returns a Boolean value indicating whether the mouse cursor is visible. _(deprecated)_
- [CGDirectDisplayCopyCurrentMetalDevice](<cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
