---
title: AVCaptureEventPhase
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.2+, iPadOS 17.2+, Mac Catalyst 17.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcaptureeventphase
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureeventphase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureeventphase.json'
content_hash: 'sha256:1fc4feb2bc74b7f7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVCaptureEventPhase

<sub>Enumeration</sub>

Constants that indicate the phase of a system capture event.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum AVCaptureEventPhase
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a phase

- [init(rawValue:)](<avcaptureeventphase/init(rawvalue_).md>)

### Event phases

- [AVCaptureEventPhaseBegan](avcaptureeventphase/began.md) — A phase that indicates the beginning of a capture event.
- [AVCaptureEventPhaseEnded](avcaptureeventphase/ended.md) — A phase that indicates the end of a capture event.
- [AVCaptureEventPhaseCancelled](avcaptureeventphase/cancelled.md) — A phase that indicates the cancellation of a capture event.

## See Also

### Inspecting the event

- [phase](avcaptureevent/phase.md) — The current phase of a capture event.
