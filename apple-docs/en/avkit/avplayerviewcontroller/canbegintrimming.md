---
title: canBeginTrimming
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/canbegintrimming
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/canbegintrimming'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/canbegintrimming.json'
content_hash: 'sha256:a67ae457365bda1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# canBeginTrimming

<sub>Instance Property</sub>

A Boolean value that indicates whether the current media supports trimming.

<sub>visionOS</sub>

```swift
var canBeginTrimming: Bool { get }
```

## Discussion

Not all media supports trimming. For example, this property returns `false` for HTTP Live Streaming media or protected content.

Observe this property to determine when to change the enabled state of your app UI that initiates trimming.

## See Also

### Presenting the visionOS trimming UI

- [- beginTrimmingWithCompletionHandler:](<begintrimming(completionhandler_).md>) — Presents the system trimming interface controls inside the player view.
