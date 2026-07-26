---
title: 'CGConfigureDisplayFadeEffect(_:_:_:_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgconfiguredisplayfadeeffect(_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgconfiguredisplayfadeeffect(_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgconfiguredisplayfadeeffect%28_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:b44db25b3292a4bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGConfigureDisplayFadeEffect(_:_:_:_:_:_:)

<sub>Function</sub>

Modifies the settings of the built-in fade effect that occurs during a display configuration.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGConfigureDisplayFadeEffect(_ config: CGDisplayConfigRef?, _ fadeOutSeconds: CGDisplayFadeInterval, _ fadeInSeconds: CGDisplayFadeInterval, _ fadeRed: Float, _ fadeGreen: Float, _ fadeBlue: Float) -> CGError
```

## Parameters

- `config` — A display configuration, acquired by calling [CGBeginDisplayConfiguration](<cgbegindisplayconfiguration(__).md>).

- `fadeOutSeconds` — The time, in seconds, to fade from the normal display to the specified fade color. The fade out is completed before the display configuration is changed. If the interval is 0, Quartz applies the color immediately.

- `fadeInSeconds` — The time, in seconds, to return from the specified fade color to the normal display. The fade-in is run asynchronously after the display configuration is changed.

- `fadeRed` — An intensity value in the interval [0, 1] that represents the red component of the desired blend color.

- `fadeGreen` — An intensity value in the interval [0, 1] that represents the green component of the desired blend color.

- `fadeBlue` — An intensity value in the interval [0, 1] that represents the blue component of the desired blend color.

## Return Value

A result code. See `Core Graphics Data Types and Constants`.

## Discussion

This function provides a way to customize the built-in fade effect that Quartz performs when displays are reconfigured. The default time settings for this fade effect are 0.3 seconds to fade out, and 0.5 seconds to fade back in. The default fade color is French Blue for a normal desktop, and black for a captured display.

Before using this function, you need to call [CGBeginDisplayConfiguration](<cgbegindisplayconfiguration(__).md>) to acquire the display configuration token for the desired display. No fade reservation is needed—when you call [CGCompleteDisplayConfiguration](<cgcompletedisplayconfiguration(____).md>), Quartz reserves the fade hardware (assuming it is available) and performs the fade.

Calling this function modifies the fade behavior for a single display configuration and has no permanent effect.

## See Also

### Functions

- [CGAcquireDisplayFadeReservation](<cgacquiredisplayfadereservation(____).md>) — Reserves the fade hardware for a specified time interval.
- [CGAssociateMouseAndMouseCursorPosition](<cgassociatemouseandmousecursorposition(__).md>) — Connects or disconnects the mouse and cursor while an application is in the foreground.
- [CGBeginDisplayConfiguration](<cgbegindisplayconfiguration(__).md>) — Begins a new set of display configuration changes.
- [CGCancelDisplayConfiguration](<cgcanceldisplayconfiguration(__).md>) — Cancels a set of display configuration changes.
- [CGCaptureAllDisplays](<cgcapturealldisplays().md>) — Obtains exclusive use of all active displays, preventing other applications and system services from using the display or changing its configuration.
- [CGCaptureAllDisplaysWithOptions](<cgcapturealldisplayswithoptions(__).md>) — Captures all attached displays, using the specified options.
- [CGCompleteDisplayConfiguration](<cgcompletedisplayconfiguration(____).md>) — Completes a set of display configuration changes.
- [CGConfigureDisplayMirrorOfDisplay](<cgconfiguredisplaymirrorofdisplay(______).md>) — Changes the configuration of a mirroring set.
- [CGConfigureDisplayMode](<cgconfiguredisplaymode(______).md>) — Configures the display mode of a display. _(deprecated)_
- [CGConfigureDisplayOrigin](<cgconfiguredisplayorigin(________).md>) — Configures the origin of a display relative to the global display coordinate space.
- [CGConfigureDisplayStereoOperation](<cgconfiguredisplaystereooperation(________).md>) — Enables or disables stereo operation for a display, as part of a display configuration.
- [CGConfigureDisplayWithDisplayMode](<cgconfiguredisplaywithdisplaymode(________).md>) — Configures the display mode of a display.
- [CGCursorIsDrawnInFramebuffer](<cgcursorisdrawninframebuffer().md>) — Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory. _(deprecated)_
- [CGCursorIsVisible](<cgcursorisvisible().md>) — Returns a Boolean value indicating whether the mouse cursor is visible. _(deprecated)_
- [CGDirectDisplayCopyCurrentMetalDevice](<cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
