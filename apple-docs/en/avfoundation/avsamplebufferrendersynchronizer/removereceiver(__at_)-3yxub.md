---
title: 'removeReceiver(_:at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebufferrendersynchronizer/removereceiver(_:at:)-3yxub'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/removereceiver(_:at:)-3yxub'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/removereceiver%28_%3Aat%3A%29-3yxub.json'
content_hash: 'sha256:268263f7094ebb8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# removeReceiver(_:at:)

<sub>Instance Method</sub>

Removes a receiver and its renderer from the synchronizer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeReceiver(_ receiver: sending AVSampleBufferVideoRenderer.Receiver, at time: CMTime) async -> Bool
```

## Parameters

- `receiver` — The receiver to be removed.

- `time` — The time on the timebase’s timeline at which the renderer should be removed. If the time is in the past, the renderer is immediately removed.
