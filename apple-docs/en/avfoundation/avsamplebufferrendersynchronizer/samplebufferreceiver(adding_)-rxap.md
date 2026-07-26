---
title: 'sampleBufferReceiver(adding:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebufferrendersynchronizer/samplebufferreceiver(adding:)-rxap'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/samplebufferreceiver(adding:)-rxap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/samplebufferreceiver%28adding%3A%29-rxap.json'
content_hash: 'sha256:82d0c3ee6302a629'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# sampleBufferReceiver(adding:)

<sub>Instance Method</sub>

Adds a renderer to the list of renderers under the synchronizer’s control and returns a sample buffer receiver to enqueue samples.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func sampleBufferReceiver(adding renderer: AVSampleBufferVideoRenderer) -> sending AVSampleBufferVideoRenderer.Receiver
```

## Parameters

- `renderer` — The render to be added.

## Return Value

A sample buffer receiver to enqueue samples asynchronously in a detached Task
