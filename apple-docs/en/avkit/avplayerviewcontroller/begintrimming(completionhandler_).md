---
title: 'beginTrimming(completionHandler:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontroller/begintrimming(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/begintrimming(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/begintrimming%28completionhandler%3A%29.json'
content_hash: 'sha256:ed9da4b936ae5892'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# beginTrimming(completionHandler:)

<sub>Instance Method</sub>

Presents the system trimming interface controls inside the player view.

<sub>visionOS</sub>

```swift
func beginTrimming(completionHandler handler: ((Bool) -> Void)? = nil)
```

<sub>visionOS</sub>

```swift
func beginTrimming() async -> Bool
```

## Parameters

- `handler` — A completion handler that the system calls with a Boolean value that indicates whether the user completed the trim operation, or if they canceled it.

## Discussion

After trimming is complete, you can access the trimmed range by querying the [forwardPlaybackEndTime](../../avfoundation/avplayeritem/forwardplaybackendtime.md) and [reversePlaybackEndTime](../../avfoundation/avplayeritem/reverseplaybackendtime.md) properties on the [AVPlayerItem](../../avfoundation/avplayeritem.md).

For more information on supporting trimming in your app, see [Trimming and exporting media in visionOS](../trimming-and-exporting-media-in-visionos.md).

## See Also

### Presenting the visionOS trimming UI

- [canBeginTrimming](canbegintrimming.md) — A Boolean value that indicates whether the current media supports trimming.
