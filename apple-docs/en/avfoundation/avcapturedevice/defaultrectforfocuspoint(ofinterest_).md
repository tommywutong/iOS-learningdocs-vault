---
title: 'defaultRectForFocusPoint(ofInterest:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/defaultrectforfocuspoint(ofinterest:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/defaultrectforfocuspoint(ofinterest:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/defaultrectforfocuspoint%28ofinterest%3A%29.json'
content_hash: 'sha256:5f468d82f4367ca0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# defaultRectForFocusPoint(ofInterest:)

<sub>Instance Method</sub>

The default rectangle of interest used for a given focus point of interest.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func defaultRectForFocusPoint(ofInterest pointOfInterest: CGPoint) -> CGRect
```

## Parameters

- `pointOfInterest` — The point of interest for which you want the default rectangle of interest.

## Discussion

For example, pass `(0.5, 0.5)` to get the focus rectangle of interest used for the default focus point of interest at `(0.5, 0.5)`.

> [!note] Note
> The particular default rectangle returned depends on the current focus mode.

This method returns `CGRectNull` if [focusRectOfInterestSupported](isfocusrectofinterestsupported.md) returns `false`.

## See Also

### Setting a focus rectangle of interest

- [focusRectOfInterestSupported](isfocusrectofinterestsupported.md) — Whether the receiver supports focus rectangles of interest.
- [focusRectOfInterest](focusrectofinterest.md) — The device’s current focus rectangle of interest, if it has one.
- [minFocusRectOfInterestSize](minfocusrectofinterestsize.md) — The minimum size you may use when specifying a rectangle of interest.
