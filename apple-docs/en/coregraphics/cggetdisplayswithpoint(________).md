---
title: 'CGGetDisplaysWithPoint(_:_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+, macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cggetdisplayswithpoint(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cggetdisplayswithpoint(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cggetdisplayswithpoint%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4da4e618d08d1e12'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGGetDisplaysWithPoint(_:_:_:_:)

<sub>Function</sub>

Provides a list of online displays with bounds that include the specified point.

<sub>Mac Catalyst, macOS</sub>

```swift
func CGGetDisplaysWithPoint(_ point: CGPoint, _ maxDisplays: UInt32, _ displays: UnsafeMutablePointer<CGDirectDisplayID>?, _ matchingDisplayCount: UnsafeMutablePointer<UInt32>?) -> CGError
```

## Parameters

- `point` — The coordinates of a point in the global display coordinate space. The origin is the upper-left corner of the main display.

- `maxDisplays` — The size of the `displays` array. This value determines the maximum number of displays the list includes.

- `displays` — A pointer to storage you provide for an array of display IDs. On return, the array contains a list of displays with bounds that include the point. If you pass `NULL`, on return the display count contains the total number of displays with bounds that include the point.

- `matchingDisplayCount` — A pointer to a display count variable you provide. On return, the display count contains the actual number of displays the list includes in the `dspys` array. This value is at most `maxDisplays`.

## Return Value

A result code. To interpret the result code, see [CGError](cgerror.md).

## Discussion

If the `displays` array is `nil`, this function ignores the `maxDisplays` parameter. If the `maxDisplays` parameter is `0`, this function ignores the `displays` array. In any case, this function fills in the `matchingDisplayCount` pointer with the number of displays that contain the specified point.

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
