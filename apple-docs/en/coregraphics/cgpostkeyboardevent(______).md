---
title: 'CGPostKeyboardEvent(_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coregraphics/cgpostkeyboardevent(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpostkeyboardevent(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpostkeyboardevent%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0df25129526960d7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPostKeyboardEvent(_:_:_:)

<sub>Function</sub>

Synthesizes a low-level keyboard event on the local machine.

> [!warning] Deprecated
> No longer supported

<sub>Mac Catalyst</sub>

```swift
func CGPostKeyboardEvent(_ keyChar: CGCharCode, _ virtualKey: CGKeyCode, _ keyDown: boolean_t) -> CGError
```

## Parameters

- `keyChar` — The value of the character to generate, or 0 to specify that the system should guess an appropriate value based on the default key mapping.

- `virtualKey` — The virtual key code for the event. See [CGKeyCode](cgkeycode.md).

- `keyDown` — Pass `true` to specify that the key position is down; otherwise, pass `false`.

## Return Value

A result code. See the result codes described in [Quartz Display Services](quartz-display-services.md).

## Discussion

This function is not recommended for general use because of undocumented special cases and undesirable side effects. The recommended replacement for this function is [CGEventCreateKeyboardEvent](<cgevent/init(keyboardeventsource_virtualkey_keydown_).md>), which allows you to create a keyboard event and customize the event before posting it to the event system.

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
