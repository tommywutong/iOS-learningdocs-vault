---
title: 'keyboardGetUnicodeString(maxStringLength:actualStringLength:unicodeString:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+, macOS 10.4+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgevent/keyboardgetunicodestring(maxstringlength:actualstringlength:unicodestring:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgevent/keyboardgetunicodestring(maxstringlength:actualstringlength:unicodestring:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgevent/keyboardgetunicodestring%28maxstringlength%3Aactualstringlength%3Aunicodestring%3A%29.json'
content_hash: 'sha256:a9b1516c1a115353'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGEvent](../cgevent.md)

# keyboardGetUnicodeString(maxStringLength:actualStringLength:unicodeString:)

<sub>Instance Method</sub>

Returns the Unicode string associated with a Quartz keyboard event.

<sub>Mac Catalyst, macOS</sub>

```swift
func keyboardGetUnicodeString(maxStringLength: Int, actualStringLength: UnsafeMutablePointer<Int>?, unicodeString: UnsafeMutablePointer<UniChar>?)
```

## Parameters

- `maxStringLength` — The length of the array you provide in the `unicodeString` parameter.

- `actualStringLength` — A pointer to a `UniCharCount` variable. On return, the variable contains the actual count of Unicode characters in the event data.

- `unicodeString` — A pointer to a `UniChar` array. You are responsible for allocating storage for the array. On return, your array contains the Unicode string associated with the specified event.

## Discussion

When you call this function and specify a `NULL` string or a maximum string length of 0, the function still returns the actual count of Unicode characters in the event data.

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
