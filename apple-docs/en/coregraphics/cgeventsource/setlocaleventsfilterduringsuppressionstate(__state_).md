---
title: 'setLocalEventsFilterDuringSuppressionState(_:state:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+, macOS 10.4+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgeventsource/setlocaleventsfilterduringsuppressionstate(_:state:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventsource/setlocaleventsfilterduringsuppressionstate(_:state:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventsource/setlocaleventsfilterduringsuppressionstate%28_%3Astate%3A%29.json'
content_hash: 'sha256:e7fdee45c2510f3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGEventSource](../cgeventsource.md)

# setLocalEventsFilterDuringSuppressionState(_:state:)

<sub>Instance Method</sub>

Sets the mask that indicates which classes of local hardware events are enabled during event suppression.

<sub>Mac Catalyst, macOS</sub>

```swift
func setLocalEventsFilterDuringSuppressionState(_ filter: CGEventFilterMask, state: CGEventSuppressionState)
```

## Parameters

- `filter` — A mask that specifies the categories of local hardware events to enable during the event suppression interval. See [CGEventFilterMask](../cgeventfiltermask.md).

- `state` — The type of event suppression interval during which the filter is applied. Pass one of the constants listed in [CGEventSuppressionState](../cgeventsuppressionstate.md).

## Discussion

By default, the system does not suppress local hardware events from the keyboard or mouse during a short interval after a Quartz event is posted—see [CGEventSourceSetLocalEventsSuppressionInterval](../cgeventsourcesetlocaleventssuppressioninterval.md)—and during a synthetic mouse drag (mouse movement with the left or only mouse button down).

Some applications may want to disable events from some of the local hardware during this interval. For example, if you post mouse events only, you may wish to suppress local mouse events and permit local keyboard events to pass through. This function lets you specify an event source, a suppression state (event suppression interval or mouse drag), and a filter mask of event classes to be passed through. The new local events filter takes effect with the next Quartz event you post using this event source.

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
