---
title: isFocusRectOfInterestSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isfocusrectofinterestsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isfocusrectofinterestsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isfocusrectofinterestsupported.json'
content_hash: 'sha256:0622622fcf8717e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isFocusRectOfInterestSupported

<sub>Instance Property</sub>

Whether the receiver supports focus rectangles of interest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isFocusRectOfInterestSupported: Bool { get }
```

## Discussion

You may only set the device’s [focusRectOfInterest](focusrectofinterest.md) property if this property returns `true`.

## See Also

### Setting a focus rectangle of interest

- [focusRectOfInterest](focusrectofinterest.md) — The device’s current focus rectangle of interest, if it has one.
- [minFocusRectOfInterestSize](minfocusrectofinterestsize.md) — The minimum size you may use when specifying a rectangle of interest.
- [- defaultRectForFocusPointOfInterest:](<defaultrectforfocuspoint(ofinterest_).md>) — The default rectangle of interest used for a given focus point of interest.
