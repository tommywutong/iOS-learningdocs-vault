---
title: 'CGDisplayRegisterReconfigurationCallback(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.3+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgdisplayregisterreconfigurationcallback(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplayregisterreconfigurationcallback(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplayregisterreconfigurationcallback%28_%3A_%3A%29.json'
content_hash: 'sha256:1888e482ec3f601f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGDisplayRegisterReconfigurationCallback(_:_:)

<sub>Function</sub>

Registers a callback function to be invoked whenever a local display is reconfigured.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGDisplayRegisterReconfigurationCallback(_ callback: CGDisplayReconfigurationCallBack?, _ userInfo: UnsafeMutableRawPointer?) -> CGError
```

## Parameters

- `callback` — A pointer to the callback function to be registered.

- `userInfo` — A pointer to user-defined data, or `NULL`. The `userInfo` argument is passed back to the callback function each time it’s invoked.

## Discussion

Whenever local displays are reconfigured, the callback function you register is invoked twice for each display that’s added, removed, or currently online—once before the reconfiguration, and once after the reconfiguration. For more information, see the callback type [CGDisplayReconfigurationCallBack](cgdisplayreconfigurationcallback.md).

A callback function may be registered multiple times with different user-defined data pointers, resulting in multiple registration entries.  For each registration, when notification is no longer needed you should remove the registration by calling the function [CGDisplayRemoveReconfigurationCallback](<cgdisplayremovereconfigurationcallback(____).md>).

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
