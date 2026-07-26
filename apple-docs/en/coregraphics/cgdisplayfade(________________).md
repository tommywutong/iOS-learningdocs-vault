---
title: 'CGDisplayFade(_:_:_:_:_:_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgdisplayfade(_:_:_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplayfade(_:_:_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplayfade%28_%3A_%3A_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:07574328182a3fd0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayFade(_:_:_:_:_:_:_:_:)

<sub>Function</sub>

Performs a single fade operation.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGDisplayFade(_ token: CGDisplayFadeReservationToken, _ duration: CGDisplayFadeInterval, _ startBlend: CGDisplayBlendFraction, _ endBlend: CGDisplayBlendFraction, _ redBlend: Float, _ greenBlend: Float, _ blueBlend: Float, _ synchronous: boolean_t) -> CGError
```

## Parameters

- `token` — A reservation token for the fade hardware you acquire by calling [CGAcquireDisplayFadeReservation](<cgacquiredisplayfadereservation(____).md>).

- `duration` — The desired number of seconds for the fade operation. You should use a value in the interval `[0, kCGMaxDisplayReservationInterval`]. If the value is `0`, Quartz applies the ending blend color immediately.

- `startBlend` — An intensity value in the interval `[0, 1]` that specifies the alpha component of the desired blend color at the beginning of the fade operation. For more information, see [Display Fade Blend Fractions](display-fade-blend-fractions.md).

- `endBlend` — An intensity value in the interval `[0, 1]` that specifies the alpha component of the desired blend color at the end of the fade operation. For more information, see [Display Fade Blend Fractions](display-fade-blend-fractions.md).

- `redBlend` — An intensity value in the interval `[0, 1]` that specifies the red component of the desired blend color.

- `greenBlend` — An intensity value in the interval `[0, 1]` that specifies the green component of the desired blend color.

- `blueBlend` — An intensity value in the interval `[0, 1]` that specifies the blue component of the desired blend color.

- `synchronous` — Pass `true` if you want the fade operation to be synchronous; otherwise, pass `false`. If a fade operation is synchronous, the function doesn’t return until the operation is complete.

## Return Value

A result code. To interpret the result code, see [CGError](cgerror.md).

## Discussion

Over the fade operation time interval, Quartz interpolates a blending coefficient between the starting and ending values given, applying a nonlinear (sine-based) bias term. Using this coefficient, Quartz blends the video output with the specified color.

The following example shows how to perform a 2-second synchronous fade-out to black:

```objc
CGDisplayFade (
    myToken,
    2.0,                        // 2 seconds
    kCGDisplayBlendNormal,      // starting state
    kCGDisplayBlendSolidColor,  // ending state
    0.0, 0.0, 0.0,              // black
    true                        // wait for completion
);
```

To perform a 2-second asynchronous fade-in from black:

```objc
CGDisplayFade (
    myToken,
    2.0,                        // 2 seconds
    kCGDisplayBlendSolidColor,  // starting state
    kCGDisplayBlendNormal,      // ending state
    0.0, 0.0, 0.0,              // black
    false                       // don't wait for completion
);
```

If you specify an asynchronous fade operation, it’s safe to call [CGReleaseDisplayFadeReservation](<cgreleasedisplayfadereservation(__).md>) immediately after this function returns.

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
