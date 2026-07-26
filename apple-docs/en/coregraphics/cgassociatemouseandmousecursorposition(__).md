---
title: 'CGAssociateMouseAndMouseCursorPosition(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgassociatemouseandmousecursorposition(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgassociatemouseandmousecursorposition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgassociatemouseandmousecursorposition%28_%3A%29.json'
content_hash: 'sha256:3bbbc00e8e5b0f80'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGAssociateMouseAndMouseCursorPosition(_:)

<sub>Function</sub>

Connects or disconnects the mouse and cursor while an application is in the foreground.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGAssociateMouseAndMouseCursorPosition(_ connected: boolean_t) -> CGError
```

## Parameters

- `connected` — Pass [true](../swift/true.md) to connect the mouse and cursor; otherwise, pass [false](../swift/false.md).

## Return Value

A result code. To interpret the result code, see [CGError](cgerror.md).

## Discussion

Call this function to disconnect the mouse from the cursor. When you call this function, the events your application receives from the system have a constant absolute location but contain delta updates to the X and Y coordinates of the mouse. You can hide the cursor or change it into something appropriate for your application. You can reposition the cursor by using the function [CGDisplayMoveCursorToPoint](<cgdisplaymovecursortopoint(____).md>) or the function [CGWarpMouseCursorPosition](<cgwarpmousecursorposition(__).md>).

## See Also

### Functions

- [CGAcquireDisplayFadeReservation](<cgacquiredisplayfadereservation(____).md>) — Reserves the fade hardware for a specified time interval.
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
- [CGDirectDisplayCopyCurrentMetalDevice](<cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
