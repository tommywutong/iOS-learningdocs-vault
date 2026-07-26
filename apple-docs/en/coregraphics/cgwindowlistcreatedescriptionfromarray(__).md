---
title: 'CGWindowListCreateDescriptionFromArray(_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgwindowlistcreatedescriptionfromarray(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowlistcreatedescriptionfromarray(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowlistcreatedescriptionfromarray%28_%3A%29.json'
content_hash: 'sha256:d04fbee13d504bdf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGWindowListCreateDescriptionFromArray(_:)

<sub>Function</sub>

Generates and returns information about windows with the specified window IDs.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGWindowListCreateDescriptionFromArray(_ windowArray: CFArray?) -> CFArray?
```

## Parameters

- `windowArray` — An array of [CGWindowID](cgwindowid.md) types, each of which corresponds to a window whose information you want to retrieve.

## Return Value

An array of [CFDictionary](../corefoundation/cfdictionary.md) types, each of which contains information about one of the windows in the current user session. If there are no windows matching the desired criteria, the function returns an empty array. If you call this function from outside of a GUI security session or when no window server is running, this function returns `NULL`.

## Discussion

This function ignores any window IDs in the `windowArray` parameter that refer to windows that no longer exist. (This can occur if the user closes a window between the time you retrieve its ID and the time you call this function.) You should therefore not assume that the returned array of dictionaries contains the same number of entries as this parameter. To make it easier to associate window IDs with the correct information, however, each dictionary does contain a [kCGWindowNumber](kcgwindownumber.md) key whose value is the corresponding window ID. For the list of keys and values that may be present in the dictionary, see [Required Window List Keys](required-window-list-keys.md) and [Optional Window List Keys](optional-window-list-keys.md).

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
