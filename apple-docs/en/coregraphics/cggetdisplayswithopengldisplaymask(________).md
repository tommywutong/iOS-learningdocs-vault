---
title: 'CGGetDisplaysWithOpenGLDisplayMask(_:_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cggetdisplayswithopengldisplaymask(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cggetdisplayswithopengldisplaymask(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cggetdisplayswithopengldisplaymask%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:170c5a4989c4fde8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGGetDisplaysWithOpenGLDisplayMask(_:_:_:_:)

<sub>Function</sub>

Provides a list of displays that corresponds to the bits set in an OpenGL display mask.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGGetDisplaysWithOpenGLDisplayMask(_ mask: CGOpenGLDisplayMask, _ maxDisplays: UInt32, _ displays: UnsafeMutablePointer<CGDirectDisplayID>?, _ matchingDisplayCount: UnsafeMutablePointer<UInt32>?) -> CGError
```

## Parameters

- `mask` — An OpenGL display mask that identifies one or more displays.

- `maxDisplays` — The size of the `displays` array. This value determines the maximum number of displays the list includes.

- `displays` — A pointer to storage you provide for an array of display IDs. On return, the array contains a list of displays that corresponds to the bits set in the mask. If you pass `NULL`, on return the display count contains the total number of displays specified in the mask.

- `matchingDisplayCount` — A pointer to a display count variable you provide. On return, the display count contains the actual number of displays the function added to the `displays` array. This value is at most `maxDisplays`.

## Return Value

A result code. To interpret the result code, see [CGError](cgerror.md).

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
