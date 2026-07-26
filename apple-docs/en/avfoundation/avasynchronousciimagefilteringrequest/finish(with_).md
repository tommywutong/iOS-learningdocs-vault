---
title: 'finish(with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.11+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avasynchronousciimagefilteringrequest/finish(with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/finish(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronousciimagefilteringrequest/finish%28with%3A%29.json'
content_hash: 'sha256:0b22d1f6ea9f7517'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousCIImageFilteringRequest](../avasynchronousciimagefilteringrequest.md)

# finish(with:)

<sub>Instance Method</sub>

Notifies AVFoundation that you cannot fulfill the image filtering request.

> [!warning] Deprecated
> Use AVCIImageFilteringParameters instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func finish(with error: any Error)
```

## Parameters

- `error` — An error object describing the reason to

## Discussion

Call this method if you cannot process the input image and wish to abort playback as a result—for example, if the [outputImage](../../coreimage/cifilter-swift.class/outputimage.md) object from your filter chain is nil. (If instead you want to fall back to rendering an unfiltered image, call the [- finishWithImage:context:](<finish(with_context_).md>) and pass the [sourceImage](sourceimage.md) object to the `filteredImage` parameter.)

Calling this method causes AVFoundation to post a notification named [AVPlayerItemFailedToPlayToEndTimeNotification](../avplayeritem/failedtoplaytoendtimenotification.md). Observers of this notification can use the [AVPlayerItemFailedToPlayToEndTimeErrorKey](../avplayeritemfailedtoplaytoendtimeerrorkey.md) key to examine the error you provide.

## See Also

### Returning the filtered image

- [- finishWithImage:context:](<finish(with_context_).md>) — Provides the filtered video frame image to AVFoundation for further processing or display. _(deprecated)_
