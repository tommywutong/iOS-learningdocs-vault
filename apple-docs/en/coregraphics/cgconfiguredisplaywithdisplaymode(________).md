---
title: 'CGConfigureDisplayWithDisplayMode(_:_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.6+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgconfiguredisplaywithdisplaymode(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgconfiguredisplaywithdisplaymode(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgconfiguredisplaywithdisplaymode%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:96723bcf0628eef7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGConfigureDisplayWithDisplayMode(_:_:_:_:)

<sub>Function</sub>

Configures the display mode of a display.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGConfigureDisplayWithDisplayMode(_ config: CGDisplayConfigRef?, _ display: CGDirectDisplayID, _ mode: CGDisplayMode?, _ options: CFDictionary?) -> CGError
```

## Parameters

- `config` — A display configuration you aquire by calling [CGBeginDisplayConfiguration](<cgbegindisplayconfiguration(__).md>).

- `display` — The identifier of the display to configure.

- `mode` — A display mode to configure.

- `options` — Reserved for future expansion. Pass `NULL` for now.

## Return Value

A result code. If the request to change modes is successful, the result is `kCGErrorSuccess`. For other possible values, see [CGError](cgerror.md).

## Discussion

This function allows you to specify a display mode with which to configure the display using a transaction. Before using this function, call [CGBeginDisplayConfiguration](<cgbegindisplayconfiguration(__).md>) to acquire the display configuration token for the desired display. Call [CGCompleteDisplayConfiguration](<cgcompletedisplayconfiguration(____).md>) to execute the transaction.

Using this function to change the mode of a display in a mirroring set might cause Quartz to adjust settings of the other displays in the set. When necessary, Quartz adjusts the bounds, resolutions, and depth of the displays to a safe mode with matching depth and the smallest enclosing size.

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
- [CGCursorIsDrawnInFramebuffer](<cgcursorisdrawninframebuffer().md>) — Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory. _(deprecated)_
- [CGCursorIsVisible](<cgcursorisvisible().md>) — Returns a Boolean value indicating whether the mouse cursor is visible. _(deprecated)_
- [CGDirectDisplayCopyCurrentMetalDevice](<cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
