---
title: 'tapCreateForPSN(processSerialNumber:place:options:eventsOfInterest:callback:userInfo:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.1+, macOS 10.4+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgevent/tapcreateforpsn(processserialnumber:place:options:eventsofinterest:callback:userinfo:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgevent/tapcreateforpsn(processserialnumber:place:options:eventsofinterest:callback:userinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgevent/tapcreateforpsn%28processserialnumber%3Aplace%3Aoptions%3Aeventsofinterest%3Acallback%3Auserinfo%3A%29.json'
content_hash: 'sha256:c300d5ad9b807ef9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGEvent](../cgevent.md)

# tapCreateForPSN(processSerialNumber:place:options:eventsOfInterest:callback:userInfo:)

<sub>Type Method</sub>

Creates an event tap for a specified process.

<sub>Mac Catalyst, macOS</sub>

```swift
class func tapCreateForPSN(processSerialNumber: UnsafeMutableRawPointer, place: CGEventTapPlacement, options: CGEventTapOptions, eventsOfInterest: CGEventMask, callback: CGEventTapCallBack, userInfo: UnsafeMutableRawPointer?) -> CFMachPort?
```

## Parameters

- `processSerialNumber` — The process to monitor.

- `place` — The placement of the new event tap in the list of active event taps. Pass one of the constants listed in [CGEventTapPlacement](../cgeventtapplacement.md).

- `options` — A constant that specifies whether the new event tap is a passive listener or an active filter.

- `eventsOfInterest` — A bit mask that specifies the set of events to be observed. For a list of possible events, see [CGEventType](../cgeventtype.md). For information on how to specify the mask, see [CGEventMask](../cgeventmask.md). If the event tap is not permitted to monitor one or more of the events specified in the `eventsOfInterest` parameter, then the appropriate bits in the mask are cleared. If that action results in an empty mask, this function returns `NULL`.

- `callback` — An event tap callback function that you provide. Your callback function is invoked from the run loop to which the event tap is added as a source. The thread safety of the callback is defined by the run loop’s environment. To learn more about event tap callbacks, see [CGEventTapCallBack](../cgeventtapcallback.md).

- `userInfo` — A pointer to user-defined data. This pointer is passed into the callback function specified in the `callback` parameter.

## Return Value

A Core Foundation mach port that represents the new event tap, or `NULL` if the event tap could not be created. When you are finished using the event tap, you should release the mach port using the function `CFRelease`. Releasing the mach port also releases the tap.

## Discussion

This function creates an event tap that receives events being routed by the window server to the specified process. For more information about creating event taps, see [CGEventTapCreate](<tapcreate(tap_place_options_eventsofinterest_callback_userinfo_).md>).

## See Also

### Functions

- [CGAcquireDisplayFadeReservation](<../cgacquiredisplayfadereservation(____).md>) — Reserves the fade hardware for a specified time interval.
- [CGAssociateMouseAndMouseCursorPosition](<../cgassociatemouseandmousecursorposition(__).md>) — Connects or disconnects the mouse and cursor while an application is in the foreground.
- [CGBeginDisplayConfiguration](<../cgbegindisplayconfiguration(__).md>) — Begins a new set of display configuration changes.
- [CGCancelDisplayConfiguration](<../cgcanceldisplayconfiguration(__).md>) — Cancels a set of display configuration changes.
- [CGCaptureAllDisplays](<../cgcapturealldisplays().md>) — Obtains exclusive use of all active displays, preventing other applications and system services from using the display or changing its configuration.
- [CGCaptureAllDisplaysWithOptions](<../cgcapturealldisplayswithoptions(__).md>) — Captures all attached displays, using the specified options.
- [CGCompleteDisplayConfiguration](<../cgcompletedisplayconfiguration(____).md>) — Completes a set of display configuration changes.
- [CGConfigureDisplayFadeEffect](<../cgconfiguredisplayfadeeffect(____________).md>) — Modifies the settings of the built-in fade effect that occurs during a display configuration.
- [CGConfigureDisplayMirrorOfDisplay](<../cgconfiguredisplaymirrorofdisplay(______).md>) — Changes the configuration of a mirroring set.
- [CGConfigureDisplayMode](<../cgconfiguredisplaymode(______).md>) — Configures the display mode of a display. _(deprecated)_
- [CGConfigureDisplayOrigin](<../cgconfiguredisplayorigin(________).md>) — Configures the origin of a display relative to the global display coordinate space.
- [CGConfigureDisplayStereoOperation](<../cgconfiguredisplaystereooperation(________).md>) — Enables or disables stereo operation for a display, as part of a display configuration.
- [CGConfigureDisplayWithDisplayMode](<../cgconfiguredisplaywithdisplaymode(________).md>) — Configures the display mode of a display.
- [CGCursorIsDrawnInFramebuffer](<../cgcursorisdrawninframebuffer().md>) — Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory. _(deprecated)_
- [CGCursorIsVisible](<../cgcursorisvisible().md>) — Returns a Boolean value indicating whether the mouse cursor is visible. _(deprecated)_
