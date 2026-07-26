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
doc_path: '/documentation/avfoundation/avplayeritemoutputpushdelegate/outputsequencewasflushed(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpushdelegate/outputsequencewasflushed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemoutputpushdelegate/outputsequencewasflushed%28_%3A%29.json'
content_hash: 'sha256:c2eb53955ea7755e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemOutputPushDelegate](../avplayeritemoutputpushdelegate.md)

# outputSequenceWasFlushed(_:)

<sub>Instance Method</sub>

Tells the delegate that the output is starting a new sequence of media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func outputSequenceWasFlushed(_ output: AVPlayerItemOutput)
```

## Parameters

- `output` — The [AVPlayerItemOutput](../avplayeritemoutput.md) object.

## Discussion

This method is invoked after any seeking and change in playback direction. If you are maintaining any queued future media data, you may want to discard those objects after receiving this message.
