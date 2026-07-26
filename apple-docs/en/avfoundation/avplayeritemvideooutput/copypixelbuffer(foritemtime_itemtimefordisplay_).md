---
title: 'copyPixelBuffer(forItemTime:itemTimeForDisplay:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（27.0 起废弃）, iPadOS 6.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.8+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avplayeritemvideooutput/copypixelbuffer(foritemtime:itemtimefordisplay:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/copypixelbuffer(foritemtime:itemtimefordisplay:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemvideooutput/copypixelbuffer%28foritemtime%3Aitemtimefordisplay%3A%29.json'
content_hash: 'sha256:3d40e05bbdc0a34f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemVideoOutput](../avplayeritemvideooutput.md)

# copyPixelBuffer(forItemTime:itemTimeForDisplay:)

<sub>Instance Method</sub>

Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired.

> [!warning] Deprecated
> Use pixelBufferAndDisplayTime(forItemTime:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copyPixelBuffer(forItemTime itemTime: CMTime, itemTimeForDisplay outItemTimeForDisplay: UnsafeMutablePointer<CMTime>?) -> CVPixelBuffer?
```

## Parameters

- `itemTime` — The time at which you want to retrieve the image from the item.

- `outItemTimeForDisplay` — The time by which you intend to use the returned pixel buffer. You may specify `nil` for this parameter if you do not have a specific deadline.

## Return Value

A pixel buffer containing the image data to display or `nil` if nothing should be displayed at the specified time. The caller is responsible for calling [CVBufferRelease](../../corevideo/cvbufferrelease.md) on the returned data when it is no longer needed.

## Discussion

Typically, you call this method in response to a CVDisplayLink callback or a [CADisplayLink](../../quartzcore/cadisplaylink.md) delegate method call when the [- hasNewPixelBufferForItemTime:](<hasnewpixelbuffer(foritemtime_).md>) method also returns [true](../../swift/true.md).

After calling this method, the video output object marks the pixel buffer data as having been acquired. This causes the [- hasNewPixelBufferForItemTime:](<hasnewpixelbuffer(foritemtime_).md>) method to return [false](../../swift/false.md) unless newer data becomes available.

## See Also

### Getting pixel buffer data

- [- hasNewPixelBufferForItemTime:](<hasnewpixelbuffer(foritemtime_).md>) — Returns a Boolean value that indicates whether video output is available for the specified item time.
- [pixelBufferAndDisplayTime(forItemTime:)](<pixelbufferanddisplaytime(foritemtime_).md>) — Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired
