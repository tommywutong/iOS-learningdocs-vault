---
title: AVPlayerLooper.Status.cancelled
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerlooper/status-swift.enum/cancelled
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlooper/status-swift.enum/cancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlooper/status-swift.enum/cancelled.json'
content_hash: 'sha256:290a53f9a514da4c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayerLooper](../../avplayerlooper.md) · [Status](../status-swift.enum.md)

# AVPlayerLooper.Status.cancelled

<sub>Case</sub>

The app canceled looping on the player.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case cancelled
```

## Discussion

The system sets this status after you call the [- disableLooping](<../disablelooping().md>) method.

## See Also

### Status values

- [AVPlayerLooperStatusUnknown](unknown.md) — The status isn’t known.
- [AVPlayerLooperStatusReady](ready.md) — The looper is ready to perform looping playback.
- [AVPlayerLooperStatusFailed](failed.md) — The looper isn’t able to perform looping playback due to an error.
