---
title: AVPlayerLooper.Status.failed
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerlooper/status-swift.enum/failed
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlooper/status-swift.enum/failed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlooper/status-swift.enum/failed.json'
content_hash: 'sha256:8c20de66b444dea8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayerLooper](../../avplayerlooper.md) · [Status](../status-swift.enum.md)

# AVPlayerLooper.Status.failed

<sub>Case</sub>

The looper isn’t able to perform looping playback due to an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case failed
```

## Discussion

Examine the looper’s [error](../error.md) property to determine the cause of the failure.

## See Also

### Status values

- [AVPlayerLooperStatusUnknown](unknown.md) — The status isn’t known.
- [AVPlayerLooperStatusReady](ready.md) — The looper is ready to perform looping playback.
- [AVPlayerLooperStatusCancelled](cancelled.md) — The app canceled looping on the player.
