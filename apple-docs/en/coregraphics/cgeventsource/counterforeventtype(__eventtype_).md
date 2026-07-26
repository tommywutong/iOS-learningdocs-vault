---
title: 'counterForEventType(_:eventType:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.1+, macOS 10.4+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgeventsource/counterforeventtype(_:eventtype:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventsource/counterforeventtype(_:eventtype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventsource/counterforeventtype%28_%3Aeventtype%3A%29.json'
content_hash: 'sha256:553244fb22e0ac50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGEventSource](../cgeventsource.md)

# counterForEventType(_:eventType:)

<sub>Type Method</sub>

Returns a count of events of a given type seen since the window server started.

<sub>Mac Catalyst, macOS</sub>

```swift
class func counterForEventType(_ stateID: CGEventSourceStateID, eventType: CGEventType) -> UInt32
```

## Parameters

- `stateID` — The source state to access. Pass one of the constants listed in [CGEventSourceStateID](../cgeventsourcestateid.md).

- `eventType` — The event type to access. To get the count of input events—keyboard, mouse, or tablet—specify `kCGAnyInputEventType`.

## Return Value

The count of events of the specified type seen since the window server started.

## Discussion

Quartz provides these counters for applications that monitor user activity. For example, an application could prompt a typist to take a break to reduce repetitive stress injuries.

Modifier keys produce `kCGEventFlagsChanged` events, not `kCGEventKeyDown` events, and do so both on press and release. The volume, brightness, and CD eject keys on some keyboards (both desktop and laptop) do not generate key up or key down events.

For various reasons, the number of key up and key down events may not be the same when all keyboard keys are up. As a result, a mismatch does not necessarily indicate that some keys are down.

Key autorepeat events are not counted.

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
