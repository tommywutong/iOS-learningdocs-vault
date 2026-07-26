---
title: cancelAllCGImageGeneration()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/cancelallcgimagegeneration()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/cancelallcgimagegeneration()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/cancelallcgimagegeneration%28%29.json'
content_hash: 'sha256:4c6f689f24f04e30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetImageGenerator](../avassetimagegenerator.md)

# cancelAllCGImageGeneration()

<sub>Instance Method</sub>

Cancels all pending image generation requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func cancelAllCGImageGeneration()
```

## Discussion

Calling this method invokes the handler block with a result of [AVAssetImageGeneratorCancelled](result/cancelled.md) for all requested times for which the generator hasn’t yet produced an image.

## See Also

### Generating images

- [image(at:)](<image(at_).md>) — Generates an image for a requested time.
- [images(for:)](<images(for_).md>) — Generates images for times within the video timeline.
- [Images](images.md) — An asynchronous sequence of images created by an image generator.
- [- generateCGImageAsynchronouslyForTime:completionHandler:](<generatecgimageasynchronously(for_completionhandler_).md>) — Generates an image asynchronously for a requested time, and returns the result in a callback.
- [- generateCGImagesAsynchronouslyForTimes:completionHandler:](<generatecgimagesasynchronously(fortimes_completionhandler_).md>) — Generates images asynchronously for an array of requested times, and returns the results in a callback.
- [AVAssetImageGeneratorCompletionHandler](../avassetimagegeneratorcompletionhandler.md) — A type alias for a closure that provides the result of an image generation request.
- [- copyCGImageAtTime:actualTime:error:](<copycgimage(at_actualtime_).md>) — Returns an image for the asset at or near a specified time. _(deprecated)_
