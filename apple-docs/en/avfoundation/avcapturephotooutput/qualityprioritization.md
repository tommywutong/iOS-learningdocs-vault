---
title: AVCapturePhotoOutput.QualityPrioritization
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/qualityprioritization
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/qualityprioritization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/qualityprioritization.json'
content_hash: 'sha256:48665cdace38c3fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# AVCapturePhotoOutput.QualityPrioritization

<sub>Enumeration</sub>

Constants that indicate how to prioritize photo quality relative to capture speed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum QualityPrioritization
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Specifying priority

- [AVCapturePhotoQualityPrioritizationSpeed](qualityprioritization/speed.md) — Speed of photo delivery is most important, even at the expense of quality.
- [AVCapturePhotoQualityPrioritizationQuality](qualityprioritization/quality.md) — Photo quality is most important, even at the expense of shot-to-shot time.
- [AVCapturePhotoQualityPrioritizationBalanced](qualityprioritization/balanced.md) — Priority is balanced between photo quality and speed of delivery.

### Initializers

- [init(rawValue:)](<qualityprioritization/init(rawvalue_).md>)

## See Also

### Setting the capture prioritization

- [maxPhotoQualityPrioritization](maxphotoqualityprioritization.md) — The highest quality the photo output should prepare to deliver on a capture-by-capture basis.
