---
title: minFocusRectOfInterestSize
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/minfocusrectofinterestsize
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/minfocusrectofinterestsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/minfocusrectofinterestsize.json'
content_hash: 'sha256:3be4079c724ce350'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# minFocusRectOfInterestSize

<sub>Instance Property</sub>

The minimum size you may use when specifying a rectangle of interest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var minFocusRectOfInterestSize: CGSize { get }
```

## Discussion

The size returned is in normalized coordinates, and depends on the current [activeFormat](activeformat.md). If [focusRectOfInterestSupported](isfocusrectofinterestsupported.md) returns `false`, this property returns { 0, 0 }.

## See Also

### Setting a focus rectangle of interest

- [focusRectOfInterestSupported](isfocusrectofinterestsupported.md) — Whether the receiver supports focus rectangles of interest.
- [focusRectOfInterest](focusrectofinterest.md) — The device’s current focus rectangle of interest, if it has one.
- [- defaultRectForFocusPointOfInterest:](<defaultrectforfocuspoint(ofinterest_).md>) — The default rectangle of interest used for a given focus point of interest.
