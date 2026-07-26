---
title: 'pixelBufferAndDisplayTime(forItemTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemvideooutput/pixelbufferanddisplaytime(foritemtime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/pixelbufferanddisplaytime(foritemtime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemvideooutput/pixelbufferanddisplaytime%28foritemtime%3A%29.json'
content_hash: 'sha256:fd1d38cb0f5d8e90'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemVideoOutput](../avplayeritemvideooutput.md)

# pixelBufferAndDisplayTime(forItemTime:)

<sub>Instance Method</sub>

Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func pixelBufferAndDisplayTime(forItemTime itemTime: CMTime) -> (pixelBuffer: CVReadOnlyPixelBuffer?, itemTimeForDisplay: CMTime)
```

## Return Value

A tuple containing the image to be displayed and a CMTime representing the true display deadline for the pixel buffer

## Discussion

- itemTime: A CMTime that expresses a desired item time

Typically you would call this method in response to a CADisplayLink delegate invocation and if hasNewPixelBuffer(forItemTime:) also returns true.

The buffer retrieved from pixelBufferAndDisplayTime(forItemTime:) may itself be nil. A nil pixel buffer communicates that nothing should be displayed for the supplied item time.

## See Also

### Getting pixel buffer data

- [- hasNewPixelBufferForItemTime:](<hasnewpixelbuffer(foritemtime_).md>) — Returns a Boolean value that indicates whether video output is available for the specified item time.
- [- copyPixelBufferForItemTime:itemTimeForDisplay:](<copypixelbuffer(foritemtime_itemtimefordisplay_).md>) — Retrieves an image that is appropriate for display at the specified item time, and marks the image as acquired. _(deprecated)_
