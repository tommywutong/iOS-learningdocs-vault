---
title: typeID
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.1+, macOS 10.6+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgdisplaymode/typeid
source_url: 'https://developer.apple.com/documentation/coregraphics/cgdisplaymode/typeid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgdisplaymode/typeid.json'
content_hash: 'sha256:e037a8c3cee6c906'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGDisplayMode](../cgdisplaymode.md)

# typeID

<sub>Type Property</sub>

Returns the type identifier of Quartz display modes.

<sub>Mac Catalyst, macOS</sub>

```swift
class var typeID: CFTypeID { get }
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
