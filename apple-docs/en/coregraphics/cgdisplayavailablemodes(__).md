---
title: 'CGDisplayAvailableModes(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coregraphics/cgdisplayavailablemodes(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplayavailablemodes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplayavailablemodes%28_%3A%29.json'
content_hash: 'sha256:5a85b3529cf86573'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayAvailableModes(_:)

<sub>Function</sub>

Returns information about the currently available display modes.

> [!warning] Deprecated
> Use [CGDisplayCopyAllDisplayModes](<cgdisplaycopyalldisplaymodes(____).md>) instead.

<sub>Mac Catalyst</sub>

```swift
func CGDisplayAvailableModes(_ dsp: CGDirectDisplayID) -> CFArray?
```

## Parameters

- `dsp` — The identifier of the display to be accessed.

## Return Value

An array of dictionaries with display mode information, or `NULL` if the display is invalid. The array is owned by the system and you should not release it. Each dictionary in the array contains information about a mode that the display supports. For a list of the properties in a display mode dictionary, see [Display Mode Standard Properties](display-mode-standard-properties.md) and [Display Mode Optional Properties](display-mode-optional-properties.md). For general information about using dictionaries, see [CFDictionary](../corefoundation/cfdictionary.md).

## Discussion

This deprecated function returns an array of display mode dictionary. Starting in OS X v10.6, display mode dictionaries have been replaced by the `CGDisplayMode` opaque type. Whereas display mode dictionaries returned by `CGDisplayAvailableModes` are owned by the system and are not to be released, display mode opaque type references returned by `CGDisplayCopyAllDisplayModes` are owned by the caller and you must release them.

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
