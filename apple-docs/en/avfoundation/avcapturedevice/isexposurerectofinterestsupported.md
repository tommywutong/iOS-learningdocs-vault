---
title: isExposureRectOfInterestSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isexposurerectofinterestsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isexposurerectofinterestsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isexposurerectofinterestsupported.json'
content_hash: 'sha256:20f5ad81d1fee019'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isExposureRectOfInterestSupported

<sub>Instance Property</sub>

Whether the device supports exposure rectangles of interest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isExposureRectOfInterestSupported: Bool { get }
```

## Discussion

You may only set the device’s [exposureRectOfInterest](exposurerectofinterest.md) property if this property returns `true`.

## See Also

### Setting an exposure rectangle of interest

- [exposureRectOfInterest](exposurerectofinterest.md) — The device’s current exposure rectangle of interest, if it has one.
- [minExposureRectOfInterestSize](minexposurerectofinterestsize.md) — The minimum size you may use when specifying a rectangle of interest.
- [- defaultRectForExposurePointOfInterest:](<defaultrectforexposurepoint(ofinterest_).md>) — The default rectangle of interest used for a given exposure point of interest.
