---
title: 'outputSequenceWasFlushed(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemoutputpulldelegate/outputsequencewasflushed(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpulldelegate/outputsequencewasflushed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemoutputpulldelegate/outputsequencewasflushed%28_%3A%29.json'
content_hash: 'sha256:9547887c68e948d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemOutputPullDelegate](../avplayeritemoutputpulldelegate.md)

# outputSequenceWasFlushed(_:)

<sub>Instance Method</sub>

Tells the delegate that a new sample sequence is commencing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func outputSequenceWasFlushed(_ output: AVPlayerItemOutput)
```

## Parameters

- `output` — The output object that sent the message.

## Discussion

This method is called after any attempt to seek or change the playback direction of the item’s content. If you are maintaining any queued future samples, you can use your implementation of this method to discard those samples.

## See Also

### Responding to pixel buffer changes

- [- outputMediaDataWillChange:](<outputmediadatawillchange(__).md>) — Tells the delegate that new samples are about to arrive.
