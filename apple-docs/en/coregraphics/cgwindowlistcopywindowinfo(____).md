---
title: 'CGWindowListCopyWindowInfo(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgwindowlistcopywindowinfo(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwindowlistcopywindowinfo(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwindowlistcopywindowinfo%28_%3A_%3A%29.json'
content_hash: 'sha256:7fbce3bd27eabbc6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGWindowListCopyWindowInfo(_:_:)

<sub>Function</sub>

Generates and returns information about the selected windows in the current user session.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGWindowListCopyWindowInfo(_ option: CGWindowListOption, _ relativeToWindow: CGWindowID) -> CFArray?
```

## Parameters

- `option` — The options describing which window dictionaries to return. Typical options let you return dictionaries for all windows or for windows above or below the window specified in the `relativeToWindow` parameter. For more information, see [Window List Option Constants](window-list-option-constants.md).

- `relativeToWindow` — The ID of the window to use as a reference point when determining which other window dictionaries to return. For options that do not require a reference window, this parameter can be [kCGNullWindowID](kcgnullwindowid.md).

## Return Value

An array of [CFDictionary](../corefoundation/cfdictionary.md) types, each of which contains information about one of the windows in the current user session. If there are no windows matching the desired criteria, the function returns an empty array. If you call this function from outside of a GUI security session or when no window server is running, this function returns `NULL`.

## Discussion

You can use this function to get detailed information about the configuration of one or more windows in the current user session. For example, you can use this function to get the bounds of the window, its window ID, and information about how it is managed by the window server. For the list of keys and values that may be present in the dictionary, see [Required Window List Keys](required-window-list-keys.md) and [Optional Window List Keys](optional-window-list-keys.md).

Generating the dictionaries for system windows is a relatively expensive operation. As always, you should profile your code and adjust your usage of this function appropriately for your needs.

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
