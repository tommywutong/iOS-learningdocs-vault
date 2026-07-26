---
title: CGPostMouseEvent
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.6 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/coregraphics/cgpostmouseevent
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpostmouseevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpostmouseevent.json'
content_hash: 'sha256:065e8f989740191d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPostMouseEvent

<sub>Function</sub>

Synthesizes a low-level mouse-button event on the local machine.

<sub>Mac Catalyst, macOS</sub>

```objc
extern CGError CGPostMouseEvent(CGPoint mouseCursorPosition, boolean_t updateMouseCursorPosition, CGButtonCount buttonCount, boolean_t mouseButtonDown, ...);
```

### Parameters

- **mouseCursorPosition** — The new coordinates of the mouse in global display space.
- **updateMouseCursorPosition** — Pass `true` if the on-screen cursor should be moved to the location specified in the `mouseCursorPosition` parameter; otherwise, pass `false`.
- **buttonCount** — The number of mouse buttons, up to a maximum of 32.
- **mouseButtonDown** — Pass `true` to specify that the primary or left mouse button is down; otherwise, pass `false`.
- **…** — Zero or more Boolean values that specify whether the remaining mouse buttons are down (`true`) or up (`false`). The second value, if any, should specify the state of the secondary mouse button (right). A third value would specify the state of the center button, and the remaining buttons would be in USB device order.

### Returns

A result code. See the result codes described in [Quartz Display Services](quartz-display-services.md).

## Discussion

Based on the arguments you pass to this function, the function generates the appropriate mouse-down, mouse-up, mouse-move, or mouse-drag events by comparing the new state with the current state.

This function is not recommended for general use because of undocumented special cases and undesirable side effects. The recommended replacement for this function is [CGEventCreateMouseEvent](<cgevent/init(mouseeventsource_mousetype_mousecursorposition_mousebutton_).md>), which allows you to create a mouse event and customize the event before posting it to the event system.

## See Also

### Functions

- [CGAcquireDisplayFadeReservation](<cgacquiredisplayfadereservation(____).md>) — Reserves the fade hardware for a specified time interval.
- [CGAssociateMouseAndMouseCursorPosition](<cgassociatemouseandmousecursorposition(__).md>) — Connects or disconnects the mouse and cursor while an application is in the foreground.
- [CGBeginDisplayConfiguration](<cgbegindisplayconfiguration(__).md>) — Begins a new set of display configuration changes.
- [CGCancelDisplayConfiguration](<cgcanceldisplayconfiguration(__).md>) — Cancels a set of display configuration changes.
- [CGCaptureAllDisplays](<cgcapturealldisplays().md>) — Obtains exclusive use of all active displays, preventing other applications and system services from using the display or changing its configuration.
- [CGCaptureAllDisplaysWithOptions](<cgcapturealldisplayswithoptions(__).md>) — Captures all attached displays, using the specified options.
- [CGColorConversionInfoCreateFromList](cgcolorconversioninfocreatefromlist.md) — Creates a conversion between an arbitrary number of specified color spaces.
- [CGCompleteDisplayConfiguration](<cgcompletedisplayconfiguration(____).md>) — Completes a set of display configuration changes.
- [CGConfigureDisplayFadeEffect](<cgconfiguredisplayfadeeffect(____________).md>) — Modifies the settings of the built-in fade effect that occurs during a display configuration.
- [CGConfigureDisplayMirrorOfDisplay](<cgconfiguredisplaymirrorofdisplay(______).md>) — Changes the configuration of a mirroring set.
- [CGConfigureDisplayMode](<cgconfiguredisplaymode(______).md>) — Configures the display mode of a display. _(deprecated)_
- [CGConfigureDisplayOrigin](<cgconfiguredisplayorigin(________).md>) — Configures the origin of a display relative to the global display coordinate space.
- [CGConfigureDisplayStereoOperation](<cgconfiguredisplaystereooperation(________).md>) — Enables or disables stereo operation for a display, as part of a display configuration.
- [CGConfigureDisplayWithDisplayMode](<cgconfiguredisplaywithdisplaymode(________).md>) — Configures the display mode of a display.
- [CGContextDrawPDFDocument](cgcontextdrawpdfdocument.md) _(deprecated)_
