---
title: minExposureRectOfInterestSize
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/minexposurerectofinterestsize
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/minexposurerectofinterestsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/minexposurerectofinterestsize.json'
content_hash: 'sha256:428501f0c5cd1a70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# minExposureRectOfInterestSize

<sub>Instance Property</sub>

The minimum size you may use when specifying a rectangle of interest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var minExposureRectOfInterestSize: CGSize { get }
```

## Discussion

The size returned is in normalized coordinates, and depends on the current [activeFormat](activeformat.md). If [exposureRectOfInterestSupported](isexposurerectofinterestsupported.md) returns `false`, this property returns { 0, 0 }.

## See Also

### Setting an exposure rectangle of interest

- [exposureRectOfInterestSupported](isexposurerectofinterestsupported.md) — Whether the device supports exposure rectangles of interest.
- [exposureRectOfInterest](exposurerectofinterest.md) — The device’s current exposure rectangle of interest, if it has one.
- [- defaultRectForExposurePointOfInterest:](<defaultrectforexposurepoint(ofinterest_).md>) — The default rectangle of interest used for a given exposure point of interest.
