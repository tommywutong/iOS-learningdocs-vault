---
title: subjectTooClose
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avspatialcapturediscomfortreason/subjecttooclose
source_url: 'https://developer.apple.com/documentation/avfoundation/avspatialcapturediscomfortreason/subjecttooclose'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avspatialcapturediscomfortreason/subjecttooclose.json'
content_hash: 'sha256:893b70b27f34e076'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSpatialCaptureDiscomfortReason](../avspatialcapturediscomfortreason.md)

# subjectTooClose

<sub>Type Property</sub>

A value that indicates the focus point of the current scene is too close.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
static let subjectTooClose: AVSpatialCaptureDiscomfortReason
```

## Discussion

The playback experience would likely be uncomfortable due to the subject being closer than the minimum focus distance of one or both of the lenses.

## See Also

### Discomfort reasons

- [AVSpatialCaptureDiscomfortReasonNotEnoughLight](notenoughlight.md) — A value that indicates the lighting of the current scene isn’t bright enough.
