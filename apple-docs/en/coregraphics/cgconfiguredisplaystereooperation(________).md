---
title: 'CGConfigureDisplayStereoOperation(_:_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgconfiguredisplaystereooperation(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgconfiguredisplaystereooperation(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgconfiguredisplaystereooperation%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:98eea84a356e07ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGConfigureDisplayStereoOperation(_:_:_:_:)

<sub>Function</sub>

Enables or disables stereo operation for a display, as part of a display configuration.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGConfigureDisplayStereoOperation(_ config: CGDisplayConfigRef?, _ display: CGDirectDisplayID, _ stereo: boolean_t, _ forceBlueLine: boolean_t) -> CGError
```

## Parameters

- `config` — A display configuration, acquired by calling [CGBeginDisplayConfiguration](<cgbegindisplayconfiguration(__).md>).

- `display` — The identifier of the display being configured.

- `stereo` — Pass `true` if you want to enable stereo operation. To disable it, pass `false`.

- `forceBlueLine` — When in stereo operation, a display may need to generate a special stereo sync signal as part of the video output.  The sync signal consists of a blue line which occupies the first 25% of the last scan line for the left eye view, and the first 75% of the last scan line for the right eye view. The remainder of the scan line is black. To force the display to generate this sync signal, pass `true`; otherwise, pass `false`.

## Return Value

A result code. See `Core Graphics Data Types and Constants`.

## Discussion

The system normally detects the presence of a stereo window and automatically switches a display containing a stereo window to stereo operation. This function provides a mechanism to force a display to stereo operation, and to set options (blue line sync signal) when in stereo operation.

On success, the display resolution, mirroring mode, and available display modes may change due to hardware-specific capabilities and limitations. You should check these settings to verify that they are appropriate for your application.

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
- [CGConfigureDisplayWithDisplayMode](<cgconfiguredisplaywithdisplaymode(________).md>) — Configures the display mode of a display.
- [CGCursorIsDrawnInFramebuffer](<cgcursorisdrawninframebuffer().md>) — Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory. _(deprecated)_
- [CGCursorIsVisible](<cgcursorisvisible().md>) — Returns a Boolean value indicating whether the mouse cursor is visible. _(deprecated)_
- [CGDirectDisplayCopyCurrentMetalDevice](<cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
