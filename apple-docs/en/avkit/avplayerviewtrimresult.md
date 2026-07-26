---
title: AVPlayerViewTrimResult
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewtrimresult
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewtrimresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewtrimresult.json'
content_hash: 'sha256:1466676fa739a173'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlayerViewTrimResult

<sub>Enumeration</sub>

Constants that specify an action a user takes when trimming media in a player view.

<sub>macOS</sub>

```swift
enum AVPlayerViewTrimResult
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a trim result

- [init(rawValue:)](<avplayerviewtrimresult/init(rawvalue_).md>)

### Trim Results

- [AVPlayerViewTrimOKButton](avplayerviewtrimresult/okbutton.md) — The user clicked the Trim button.
- [AVPlayerViewTrimCancelButton](avplayerviewtrimresult/cancelbutton.md) — The user clicked the Cancel button.

## See Also

### Trimming media

- [canBeginTrimming](avplayerview/canbegintrimming.md) — A Boolean value that indicates whether the player view can begin trimming.
- [- beginTrimmingWithCompletionHandler:](<avplayerview/begintrimming(completionhandler_).md>) — Puts the player view into trimming mode.
