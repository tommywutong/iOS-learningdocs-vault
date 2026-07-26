---
title: 'requestNotificationOfMediaDataChange(withAdvanceInterval:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemvideooutput/requestnotificationofmediadatachange(withadvanceinterval:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/requestnotificationofmediadatachange(withadvanceinterval:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemvideooutput/requestnotificationofmediadatachange%28withadvanceinterval%3A%29.json'
content_hash: 'sha256:e767f93dff4ac39c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemVideoOutput](../avplayeritemvideooutput.md)

# requestNotificationOfMediaDataChange(withAdvanceInterval:)

<sub>Instance Method</sub>

Tells the receiver that the video out put client is entering a quiescent state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func requestNotificationOfMediaDataChange(withAdvanceInterval interval: TimeInterval)
```

## Parameters

- `interval` — The amount of time to wait before notifying the delegate of the media change.

## Discussion

Call this method before you suspend your use of a [CVDisplayLink](../../corevideo/cvdisplaylink.md) type or a [CADisplayLink](../../quartzcore/cadisplaylink.md) object. After the interval expires, the video output object notifies its delegate that it should resume the display link. If the interval value you specify is large, the delegate is notified as soon as possible rather than waiting.

Do not call this method repeatedly to force the delegate to be notified for each sample.
