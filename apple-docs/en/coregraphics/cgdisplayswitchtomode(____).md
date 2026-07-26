---
title: 'CGDisplaySwitchToMode(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coregraphics/cgdisplayswitchtomode(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplayswitchtomode(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplayswitchtomode%28_%3A_%3A%29.json'
content_hash: 'sha256:df56c51db4efda6e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplaySwitchToMode(_:_:)

<sub>Function</sub>

Switches a display to a different mode.

> [!warning] Deprecated
> Use [CGDisplaySetDisplayMode](<cgdisplaysetdisplaymode(______).md>) instead.

<sub>Mac Catalyst</sub>

```swift
func CGDisplaySwitchToMode(_ display: CGDirectDisplayID, _ mode: CFDictionary?) -> CGError
```

## Parameters

- `display` — The identifier of the display to be accessed.

- `mode` — A display mode dictionary that contains information about the display mode to set. The dictionary passed in must be a dictionary returned by another Quartz display function such as [CGDisplayAvailableModes](<cgdisplayavailablemodes(__).md>) or [CGDisplayBestModeForParameters](<cgdisplaybestmodeforparameters(__________).md>). For a list of the properties in a display mode dictionary, see [Display Mode Standard Properties](display-mode-standard-properties.md) and [Display Mode Optional Properties](display-mode-optional-properties.md). For general information about using dictionaries, see [CFDictionary](../corefoundation/cfdictionary.md).

## Return Value

A result code. See `Core Graphics Data Types and Constants`.

## Discussion

This function switches the display mode of the specified display. The operation is always synchronous; the function does not return until the mode switch is complete. Note that after switching, display parameters and addresses may change.

The selected display mode persists for the life of the calling program. When the program terminates, the display mode automatically reverts to the permanent setting in the Displays panel of System Preferences.

When changing the display mode of a display in a mirroring set, other displays in the mirroring set will be assigned a mode that’s capable of mirroring the bounds of the display being adjusted. To avoid this automatic behavior, you can use the following procedure: call[CGBeginDisplayConfiguration](<cgbegindisplayconfiguration(__).md>), call [CGConfigureDisplayMode](<cgconfiguredisplaymode(______).md>) for each display to explicitly set the mode, and finally call [CGCompleteDisplayConfiguration](<cgcompletedisplayconfiguration(____).md>)

### Special Considerations

This deprecated function takes as a parameter a display mode dictionary. Starting in OS X v10.6, display mode dictionaries have been replaced by the `CGDisplayMode` opaque type.

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
