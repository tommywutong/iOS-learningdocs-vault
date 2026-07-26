---
title: 'init(keyboardEventSource:virtualKey:keyDown:)'
framework: Core Graphics
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.1+, macOS 10.4+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgevent/init(keyboardeventsource:virtualkey:keydown:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgevent/init(keyboardeventsource:virtualkey:keydown:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgevent/init%28keyboardeventsource%3Avirtualkey%3Akeydown%3A%29.json'
content_hash: 'sha256:92181fd83c7bfd6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGEvent](../cgevent.md)

# init(keyboardEventSource:virtualKey:keyDown:)

<sub>Initializer</sub>

Returns a new Quartz keyboard event.

<sub>Mac Catalyst, macOS</sub>

```swift
init?(keyboardEventSource source: CGEventSource?, virtualKey: CGKeyCode, keyDown: Bool)
```

## Parameters

- `source` — An event source taken from another event, or `NULL`.

- `virtualKey` — The virtual key code for the event.

- `keyDown` — Pass `true` to specify that the key position is down. To specify that the key position is up, pass `false`. This value is used to determine the type of the keyboard event—see [CGEventType](../cgeventtype.md).

## Return Value

A new keyboard event, or `NULL` if the event could not be created. When you no longer need the event, you should release it using the function `CFRelease`.

## Discussion

All keystrokes needed to generate a character must be entered, including modifier keys.  For example, to produce a ‘Z’, the SHIFT key must be down, the ‘z’ key must go down, and then the SHIFT and ‘z’ key must be released:

```objc
CGEventRef event1, event2, event3, event4;
event1 = CGEventCreateKeyboardEvent (NULL, (CGKeyCode)56, true);
event2 = CGEventCreateKeyboardEvent (NULL, (CGKeyCode)6, true);
event3 = CGEventCreateKeyboardEvent (NULL, (CGKeyCode)6, false);
event4 = CGEventCreateKeyboardEvent (NULL, (CGKeyCode)56, false);
```

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
