---
title: AVSpatialCaptureDiscomfortReason
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avspatialcapturediscomfortreason
source_url: 'https://developer.apple.com/documentation/avfoundation/avspatialcapturediscomfortreason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avspatialcapturediscomfortreason.json'
content_hash: 'sha256:951fa002fe1efdca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSpatialCaptureDiscomfortReason

<sub>Structure</sub>

Constants that indicate the suitability of the current scene to create a comfortable viewing experience.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
struct AVSpatialCaptureDiscomfortReason
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Discomfort reasons

- [AVSpatialCaptureDiscomfortReasonNotEnoughLight](avspatialcapturediscomfortreason/notenoughlight.md) — A value that indicates the lighting of the current scene isn’t bright enough.
- [AVSpatialCaptureDiscomfortReasonSubjectTooClose](avspatialcapturediscomfortreason/subjecttooclose.md) — A value that indicates the focus point of the current scene is too close.

### Initializers

- [init(rawValue:)](<avspatialcapturediscomfortreason/init(rawvalue_).md>) — Creates a discomfort reason with a string value.

## See Also

### Supporting spatial capture

- [spatialCaptureDiscomfortReasons](avcapturedevice/spatialcapturediscomfortreasons.md) — Reasons why current environmental conditions aren’t suitable to capturing spatial videos that are comfortable to view.
