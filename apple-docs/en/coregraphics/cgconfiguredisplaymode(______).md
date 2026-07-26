---
title: 'CGConfigureDisplayMode(_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coregraphics/cgconfiguredisplaymode(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgconfiguredisplaymode(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgconfiguredisplaymode%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f49bf90013a346eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGConfigureDisplayMode(_:_:_:)

<sub>Function</sub>

Configures the display mode of a display.

> [!warning] Deprecated
> Use [CGConfigureDisplayWithDisplayMode](<cgconfiguredisplaywithdisplaymode(________).md>) instead.

<sub>Mac Catalyst</sub>

```swift
func CGConfigureDisplayMode(_ config: CGDisplayConfigRef?, _ display: CGDirectDisplayID, _ mode: CFDictionary?) -> CGError
```

## Parameters

- `config` — A display configuration, acquired by calling [CGBeginDisplayConfiguration](<cgbegindisplayconfiguration(__).md>).

- `display` — The identifier of the display being configured.

- `mode` — A display mode dictionary (see the discussion below).

## Return Value

A result code. See `Core Graphics Data Types and Constants`.

## Discussion

A display mode is a set of properties such as width, height, pixel depth, and refresh rate, and options such as stretched LCD panel filling.

The display mode you provide must be one of the following:

- A dictionary returned by one of the `CGDisplayBestMode` functions, such as [CGDisplayBestModeForParameters](<cgdisplaybestmodeforparameters(__________).md>).
- A dictionary in the array returned by [CGDisplayAvailableModes](<cgdisplayavailablemodes(__).md>).

If you use this function to change the mode of a display in a mirroring set, Quartz may adjust the bounds, resolutions, and depth of the other displays in the set to a safe mode, with matching depth and the smallest enclosing size.

### Special Considerations

This deprecated function takes as a parameter a display mode dictionary. Starting in OS X v10.6, display mode dictionaries have been replaced by the `CGDisplayMode` opaque type. For information on the `CGDisplayMode` opaque type, see [Getting Information About a Display Mode](quartz-display-services.md#Getting-Information-About-a-Display-Mode).

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
- [CGConfigureDisplayOrigin](<cgconfiguredisplayorigin(________).md>) — Configures the origin of a display relative to the global display coordinate space.
- [CGConfigureDisplayStereoOperation](<cgconfiguredisplaystereooperation(________).md>) — Enables or disables stereo operation for a display, as part of a display configuration.
- [CGConfigureDisplayWithDisplayMode](<cgconfiguredisplaywithdisplaymode(________).md>) — Configures the display mode of a display.
- [CGCursorIsDrawnInFramebuffer](<cgcursorisdrawninframebuffer().md>) — Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory. _(deprecated)_
- [CGCursorIsVisible](<cgcursorisvisible().md>) — Returns a Boolean value indicating whether the mouse cursor is visible. _(deprecated)_
- [CGDirectDisplayCopyCurrentMetalDevice](<cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
