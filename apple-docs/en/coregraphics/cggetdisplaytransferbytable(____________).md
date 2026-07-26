---
title: 'CGGetDisplayTransferByTable(_:_:_:_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cggetdisplaytransferbytable(_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cggetdisplaytransferbytable(_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cggetdisplaytransferbytable%28_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:581fd58f657a5e44'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGGetDisplayTransferByTable(_:_:_:_:_:_:)

<sub>Function</sub>

Gets the values in the RGB gamma tables for a display.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGGetDisplayTransferByTable(_ display: CGDirectDisplayID, _ capacity: UInt32, _ redTable: UnsafeMutablePointer<CGGammaValue>?, _ greenTable: UnsafeMutablePointer<CGGammaValue>?, _ blueTable: UnsafeMutablePointer<CGGammaValue>?, _ sampleCount: UnsafeMutablePointer<UInt32>?) -> CGError
```

## Parameters

- `display` — The identifier of the display to be accessed.

- `capacity` — The number of entries each table can hold.

- `redTable` — A pointer to an array of type `CGGammaValue` with size `capacity`. On return, the array contains the values of the red channel in the display’s gamma table.

- `greenTable` — A pointer to an array of type `CGGammaValue` with size `capacity`. On return, the array contains the values of the green channel in the display’s gamma table.

- `blueTable` — A pointer to an array of type `CGGammaValue` with size `capacity`. On return, the array contains the values of the blue channel in the display’s gamma table.

- `sampleCount` — The number of samples actually copied into each array.

## Return Value

A result code. See `Core Graphics Data Types and Constants`.

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
