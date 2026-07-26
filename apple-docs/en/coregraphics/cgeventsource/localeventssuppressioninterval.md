---
title: localEventsSuppressionInterval
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.1+, macOS 10.4+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventsource/localeventssuppressioninterval
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventsource/localeventssuppressioninterval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventsource/localeventssuppressioninterval.json'
content_hash: 'sha256:2f328ac0b8b216bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGEventSource](../cgeventsource.md)

# localEventsSuppressionInterval

<sub>Instance Property</sub>

Returns the interval that local hardware events may be suppressed following the posting of a Quartz event.

<sub>Mac Catalyst, macOS</sub>

```swift
var localEventsSuppressionInterval: CFTimeInterval { get set }
```

## Discussion

By default, the system does not suppress local hardware events from the keyboard or mouse during a short interval after a Quartz event is posted. You can use the function [CGEventSourceSetLocalEventsFilterDuringSuppressionState](<setlocaleventsfilterduringsuppressionstate(__state_).md>) to modify this behavior.

This function gets the period of time in seconds that local hardware events may be suppressed after posting a Quartz event created with the specified event source. You can use the function [CGEventSourceSetLocalEventsSuppressionInterval](../cgeventsourcesetlocaleventssuppressioninterval.md) to change this time interval.

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
