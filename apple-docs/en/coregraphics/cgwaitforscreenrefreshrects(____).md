---
title: 'CGWaitForScreenRefreshRects(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coregraphics/cgwaitforscreenrefreshrects(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgwaitforscreenrefreshrects(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgwaitforscreenrefreshrects%28_%3A_%3A%29.json'
content_hash: 'sha256:32e42ea5c1353191'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGWaitForScreenRefreshRects(_:_:)

<sub>Function</sub>

Waits for screen refresh operations.

> [!warning] Deprecated
> Use display streaming instead. See [Quartz Display Services](quartz-display-services.md).

<sub>Mac Catalyst</sub>

```swift
func CGWaitForScreenRefreshRects(_ rects: UnsafeMutablePointer<UnsafeMutablePointer<CGRect>?>?, _ count: UnsafeMutablePointer<UInt32>?) -> CGError
```

## Parameters

- `rects` — A pointer to a `CGRect*` variable. On return, the variable contains an array of rectangles that bound the refreshed areas, specified in the global display coordinate space. When you no longer need the array, you should deallocate it by calling [CGReleaseScreenRefreshRects](<cgreleasescreenrefreshrects(__).md>).

- `count` — A pointer to a `CGRectCount` variable. On return, the variable contains the number of entries in the returned array of rectangles.

## Return Value

A result code. See `Core Graphics Data Types and Constants`.

## Discussion

In some applications it may be preferable to wait for screen-refresh data synchronously, using this function. You should call this function in a thread other than the main event-processing thread.

As an alternative, Quartz also supports asynchronous notification—see [CGRegisterScreenRefreshCallback](<cgregisterscreenrefreshcallback(____).md>). If refresh callback functions are registered, this function should not be used.

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
