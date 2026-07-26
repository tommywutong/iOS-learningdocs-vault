---
title: AVPlayerViewControllerSkippingBehavior
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [tvOS 10.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontrollerskippingbehavior
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerskippingbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerskippingbehavior.json'
content_hash: 'sha256:74cac56cdd01ee34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlayerViewControllerSkippingBehavior

<sub>Enumeration</sub>

Constants that represent the player view controller’s skipping behavior.

<sub>tvOS</sub>

```swift
enum AVPlayerViewControllerSkippingBehavior
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a skipping behavior

- [init(rawValue:)](<avplayerviewcontrollerskippingbehavior/init(rawvalue_).md>)

### Skipping Behaviors

- [AVPlayerViewControllerSkippingBehaviorDefault](avplayerviewcontrollerskippingbehavior/default.md) — The default skipping behavior, which is to skip forward or backward in 10-second intervals.
- [AVPlayerViewControllerSkippingBehaviorSkipItem](avplayerviewcontrollerskippingbehavior/skipitem.md) — Skipping behavior that specifies skipping to the next or previous item in the player’s playlist.

## See Also

### Configuring skipping behavior

- [skipForwardEnabled](avplayerviewcontroller/isskipforwardenabled.md) — A Boolean value that indicates whether forward-skipping is available.
- [skipBackwardEnabled](avplayerviewcontroller/isskipbackwardenabled.md) — A Boolean value that indicates whether backward-skipping is available.
- [skippingBehavior](avplayerviewcontroller/skippingbehavior.md) — The behavior that skipping gestures perform.
