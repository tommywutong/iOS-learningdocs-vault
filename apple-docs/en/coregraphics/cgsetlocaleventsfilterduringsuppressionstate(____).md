---
title: 'CGSetLocalEventsFilterDuringSuppressionState(_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coregraphics/cgsetlocaleventsfilterduringsuppressionstate(_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgsetlocaleventsfilterduringsuppressionstate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgsetlocaleventsfilterduringsuppressionstate%28_%3A_%3A%29.json'
content_hash: 'sha256:a092f695c4d4c736'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGSetLocalEventsFilterDuringSuppressionState(_:_:)

<sub>Function</sub>

Filters local hardware events from the keyboard and mouse during the short interval after a synthetic event is posted.

> [!warning] Deprecated
> No longer supported

<sub>Mac Catalyst</sub>

```swift
func CGSetLocalEventsFilterDuringSuppressionState(_ filter: CGEventFilterMask, _ state: CGEventSuppressionState) -> CGError
```

## Parameters

- `filter` — The class of local hardware events to enable after a synthetic event is posted. Pass one of the constants listed in [CGEventFilterMask](cgeventfiltermask.md).

- `state` — The type of interval during which the filter is applied. Pass one of the constants listed in [CGEventSuppressionState](cgeventsuppressionstate.md).

## Return Value

A result code. See the result codes described in [Quartz Display Services](quartz-display-services.md).

## Discussion

By default, the system suppresses local hardware events from the keyboard and mouse during a short interval after a synthetic event is posted and during a synthetic mouse drag (mouse movement with the left or only mouse button down).

Some applications may want to enable events from some of the local hardware. For example, if you post mouse events only, you may wish to permit local keyboard hardware events to pass through.

This function lets you specify a state (event suppression interval or mouse drag), and a mask of event categories to be passed through. The new filter state takes effect with the next synthetic event you post.

This function is not recommended for general use because of undocumented special cases and undesirable side effects. The recommended replacement for this function is [CGEventSourceSetLocalEventsFilterDuringSuppressionState](<cgeventsource/setlocaleventsfilterduringsuppressionstate(__state_).md>), which allows the filter behavior to be associated only with events created from a specific event source.

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
