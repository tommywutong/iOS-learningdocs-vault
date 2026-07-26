---
title: 'CGCompleteDisplayConfiguration(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcompletedisplayconfiguration(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcompletedisplayconfiguration(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcompletedisplayconfiguration%28_%3A_%3A%29.json'
content_hash: 'sha256:8b09c676d816eeef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGCompleteDisplayConfiguration(_:_:)

<sub>Function</sub>

Completes a set of display configuration changes.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGCompleteDisplayConfiguration(_ config: CGDisplayConfigRef?, _ option: CGConfigureOption) -> CGError
```

## Parameters

- `config` — The display configuration that contains the desired changes. On return, this configuration is no longer valid.

- `option` — The scope of the display configuration changes. Pass one of the constants listed in [CGConfigureOption](cgconfigureoption.md).

## Return Value

A result code. If the request to apply changes is successful, the result is `kCGErrorSuccess`. For other possible values, see [CGError](cgerror.md).

## Discussion

This function applies a set of display configuration changes as a single atomic transaction. The duration or scope of the changes depends on the value of the `option` parameter. For more information about possible scopes, see [CGConfigureOption](cgconfigureoption.md).

A configuration change can fail if you request an unsupported display mode or if another application is running in full-screen mode.

## See Also

### Functions

- [CGAcquireDisplayFadeReservation](<cgacquiredisplayfadereservation(____).md>) — Reserves the fade hardware for a specified time interval.
- [CGAssociateMouseAndMouseCursorPosition](<cgassociatemouseandmousecursorposition(__).md>) — Connects or disconnects the mouse and cursor while an application is in the foreground.
- [CGBeginDisplayConfiguration](<cgbegindisplayconfiguration(__).md>) — Begins a new set of display configuration changes.
- [CGCancelDisplayConfiguration](<cgcanceldisplayconfiguration(__).md>) — Cancels a set of display configuration changes.
- [CGCaptureAllDisplays](<cgcapturealldisplays().md>) — Obtains exclusive use of all active displays, preventing other applications and system services from using the display or changing its configuration.
- [CGCaptureAllDisplaysWithOptions](<cgcapturealldisplayswithoptions(__).md>) — Captures all attached displays, using the specified options.
- [CGConfigureDisplayFadeEffect](<cgconfiguredisplayfadeeffect(____________).md>) — Modifies the settings of the built-in fade effect that occurs during a display configuration.
- [CGConfigureDisplayMirrorOfDisplay](<cgconfiguredisplaymirrorofdisplay(______).md>) — Changes the configuration of a mirroring set.
- [CGConfigureDisplayMode](<cgconfiguredisplaymode(______).md>) — Configures the display mode of a display. _(deprecated)_
- [CGConfigureDisplayOrigin](<cgconfiguredisplayorigin(________).md>) — Configures the origin of a display relative to the global display coordinate space.
- [CGConfigureDisplayStereoOperation](<cgconfiguredisplaystereooperation(________).md>) — Enables or disables stereo operation for a display, as part of a display configuration.
- [CGConfigureDisplayWithDisplayMode](<cgconfiguredisplaywithdisplaymode(________).md>) — Configures the display mode of a display.
- [CGCursorIsDrawnInFramebuffer](<cgcursorisdrawninframebuffer().md>) — Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory. _(deprecated)_
- [CGCursorIsVisible](<cgcursorisvisible().md>) — Returns a Boolean value indicating whether the mouse cursor is visible. _(deprecated)_
- [CGDirectDisplayCopyCurrentMetalDevice](<cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
