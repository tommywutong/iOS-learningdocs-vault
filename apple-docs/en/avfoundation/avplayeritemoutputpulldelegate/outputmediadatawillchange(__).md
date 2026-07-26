---
title: 'outputMediaDataWillChange(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemoutputpulldelegate/outputmediadatawillchange(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpulldelegate/outputmediadatawillchange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemoutputpulldelegate/outputmediadatawillchange%28_%3A%29.json'
content_hash: 'sha256:facdecf127eaf8de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemOutputPullDelegate](../avplayeritemoutputpulldelegate.md)

# outputMediaDataWillChange(_:)

<sub>Instance Method</sub>

Tells the delegate that new samples are about to arrive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func outputMediaDataWillChange(_ sender: AVPlayerItemOutput)
```

## Parameters

- `sender` — The output object that sent the message.

## Discussion

You can use this method to prepare for any new sample data. This method is called at some point after a call to your video output object’s `requestNotificationOfMediaDataChangeWithAdvanceInterval:` method.

## See Also

### Responding to pixel buffer changes

- [- outputSequenceWasFlushed:](<outputsequencewasflushed(__).md>) — Tells the delegate that a new sample sequence is commencing.
