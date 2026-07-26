---
title: 'hasNewPixelBuffer(forItemTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemvideooutput/hasnewpixelbuffer(foritemtime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/hasnewpixelbuffer(foritemtime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemvideooutput/hasnewpixelbuffer%28foritemtime%3A%29.json'
content_hash: 'sha256:800ec618f1d96fcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemVideoOutput](../avplayeritemvideooutput.md)

# hasNewPixelBuffer(forItemTime:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether video output is available for the specified item time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func hasNewPixelBuffer(forItemTime itemTime: CMTime) -> Bool
```

## Parameters

- `itemTime` — The item time to query. The time value is relative to the [AVPlayerItem](../avplayeritem.md) object with which the receiver is associated.

## Return Value

[true](../../swift/true.md) if there is available video output that has not been previously acquired or [false](../../swift/false.md) if there is not.

## Discussion

This method returns [true](../../swift/true.md) if the video data at the specified time has not yet been acquired or is different from the video that was acquired previously. If you require multiple objects to acquire video output from the same [AVPlayerItem](../avplayeritem.md) object, you should create separate `AVPlayerItemVideoOutput` objects for each.

## See Also

### Getting pixel buffer data

- [- copyPixelBufferForItemTime:itemTimeForDisplay:](<copypixelbuffer(foritemtime_itemtimefordisplay_).md>) — Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired. _(deprecated)_
- [pixelBufferAndDisplayTime(forItemTime:)](<pixelbufferanddisplaytime(foritemtime_).md>) — Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired
