---
title: 'CGSetDisplayTransferByFormula(_:_:_:_:_:_:_:_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgsetdisplaytransferbyformula(_:_:_:_:_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgsetdisplaytransferbyformula(_:_:_:_:_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgsetdisplaytransferbyformula%28_%3A_%3A_%3A_%3A_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c709f3bfd5a95a02'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGSetDisplayTransferByFormula(_:_:_:_:_:_:_:_:_:_:)

<sub>Function</sub>

Sets the gamma function for a display by specifying the coefficients of the gamma transfer formula.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGSetDisplayTransferByFormula(_ display: CGDirectDisplayID, _ redMin: CGGammaValue, _ redMax: CGGammaValue, _ redGamma: CGGammaValue, _ greenMin: CGGammaValue, _ greenMax: CGGammaValue, _ greenGamma: CGGammaValue, _ blueMin: CGGammaValue, _ blueMax: CGGammaValue, _ blueGamma: CGGammaValue) -> CGError
```

## Parameters

- `display` — The identifier of the display to be accessed.

- `redMin` — The minimum value of the red channel in the gamma table. The value should be a number in the interval [0, redMax).

- `redMax` — The maximum value of the red channel in the gamma table. The value should be a number in the interval (redMin, 1].

- `redGamma` — A positive value used to compute the red channel in the gamma table.

- `greenMin` — The minimum value of the green channel in the gamma table. The value should be a number in the interval [0, greenMax).

- `greenMax` — The maximum value of the green channel in the gamma table. The value should be a number in the interval (greenMin, 1].

- `greenGamma` — A positive value used to compute the green channel in the gamma table.

- `blueMin` — The minimum value of the blue channel in the gamma table. The value should be a number in the interval [0, blueMax).

- `blueMax` — The maximum value of the blue channel in the gamma table. The value should be a number in the interval (blueMin, 1].

- `blueGamma` — A positive value used to compute the blue channel in the gamma table.

## Return Value

A result code. See `Core Graphics Data Types and Constants`.

## Discussion

This function uses the specified parameter values to compute a gamma correction table for the specified display. The values in the table are computed by sampling the following gamma transfer formula for a range of indices from 0 to 1:

```objc
value = Min + ((Max - Min) * pow(index, Gamma))
```

The resulting values are converted to a machine-specific format and loaded into display hardware.

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
