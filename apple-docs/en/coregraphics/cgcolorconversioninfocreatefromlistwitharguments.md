---
title: CGColorConversionInfoCreateFromListWithArguments
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorconversioninfocreatefromlistwitharguments
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfocreatefromlistwitharguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorconversioninfocreatefromlistwitharguments.json'
content_hash: 'sha256:a84b52195236665b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGColorConversionInfoCreateFromListWithArguments

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGColorConversionInfoRefCGColorConversionInfoCreateFromListWithArguments(CFDictionaryRef options, CGColorSpaceRef , CGColorConversionInfoTransformType , CGColorRenderingIntent , va_list );
```

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
