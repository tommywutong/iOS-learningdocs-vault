---
title: 'CGDisplayBestModeForParameters(_:_:_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coregraphics/cgdisplaybestmodeforparameters(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaybestmodeforparameters(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaybestmodeforparameters%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e8c9777a50613da6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayBestModeForParameters(_:_:_:_:_:)

<sub>Function</sub>

Returns information about the display mode closest to a specified depth and screen size.

> [!warning] Deprecated
> Use the display mode query functions instead; see [Getting Information About a Display Mode](quartz-display-services.md#Getting-Information-About-a-Display-Mode).

<sub>Mac Catalyst</sub>

```swift
func CGDisplayBestModeForParameters(_ display: CGDirectDisplayID, _ bitsPerPixel: Int, _ width: Int, _ height: Int, _ exactMatch: UnsafeMutablePointer<boolean_t>?) -> CFDictionary?
```

## Parameters

- `display` — The identifier of the display to optimize.

- `bitsPerPixel` — Optimal display depth in bits per pixel. Note that this value is not the same as pixel depth, which is the number of bits per channel or component.

- `width` — Optimal display width in pixel units.

- `height` — Optimal display height in pixel units.

- `exactMatch` — A pointer to a Boolean variable. On return, its value is `true` if an exact match in display depth, width, and height is found; otherwise, `false`. If this information is not needed, pass `NULL`.

## Return Value

A display mode dictionary, or `NULL` if the display is invalid. The dictionary is owned by the system and you should not release it. The dictionary contains information about the display mode closest to the specified depth and screen size. For a list of the properties in a display mode dictionary, see [Display Mode Standard Properties](display-mode-standard-properties.md) and [Display Mode Optional Properties](display-mode-optional-properties.md). For general information about using dictionaries, see [CFDictionary](../corefoundation/cfdictionary.md).

## Discussion

This function tries to find an optimal display mode for the specified display. The function first tries to find a mode with the specified pixel depth and dimensions equal to or greater than the specified width and height. If no depth match is found, it tries to find a mode with greater depth and the same or greater dimensions. If a suitable display mode is not found, this function simply returns the current display mode.

### Special Considerations

This deprecated function selects a display mode closest to the specified parameters. Starting in OS X v10.6 new display mode APIs should be used to query display modes so that an application can tailor its definition of “best” to its graphics and memory needs.

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
