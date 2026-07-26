---
title: 'defaultRectForExposurePoint(ofInterest:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/defaultrectforexposurepoint(ofinterest:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/defaultrectforexposurepoint(ofinterest:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/defaultrectforexposurepoint%28ofinterest%3A%29.json'
content_hash: 'sha256:21217366912c2cba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# defaultRectForExposurePoint(ofInterest:)

<sub>Instance Method</sub>

The default rectangle of interest used for a given exposure point of interest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func defaultRectForExposurePoint(ofInterest pointOfInterest: CGPoint) -> CGRect
```

## Parameters

- `pointOfInterest` — The point of interest for which you want the default rectangle of interest.

## Discussion

For example, pass `(0.5, 0.5)` to get the exposure rectangle of interest used for the default exposure point of interest at `(0.5, 0.5)`.

This method returns `CGRectNull` if [exposureRectOfInterestSupported](isexposurerectofinterestsupported.md) returns `false`.

## See Also

### Setting an exposure rectangle of interest

- [exposureRectOfInterestSupported](isexposurerectofinterestsupported.md) — Whether the device supports exposure rectangles of interest.
- [exposureRectOfInterest](exposurerectofinterest.md) — The device’s current exposure rectangle of interest, if it has one.
- [minExposureRectOfInterestSize](minexposurerectofinterestsize.md) — The minimum size you may use when specifying a rectangle of interest.
