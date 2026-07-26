---
title: 'image(at:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetimagegenerator/image(at:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/image(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/image%28at%3A%29.json'
content_hash: 'sha256:2637b5e5e7ed4814'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetImageGenerator](../avassetimagegenerator.md)

# image(at:)

<sub>Instance Method</sub>

Generates an image for a requested time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func image(at time: CMTime) async throws -> (image: CGImage, actualTime: CMTime)
```

## Parameters

- `time` — A time in the asset timeline at which to create an image.

## Return Value

A tuple that contains the image and the time the asset was created.

## See Also

### Generating images

- [images(for:)](<images(for_).md>) — Generates images for times within the video timeline.
- [Images](images.md) — An asynchronous sequence of images created by an image generator.
- [- generateCGImageAsynchronouslyForTime:completionHandler:](<generatecgimageasynchronously(for_completionhandler_).md>) — Generates an image asynchronously for a requested time, and returns the result in a callback.
- [- generateCGImagesAsynchronouslyForTimes:completionHandler:](<generatecgimagesasynchronously(fortimes_completionhandler_).md>) — Generates images asynchronously for an array of requested times, and returns the results in a callback.
- [AVAssetImageGeneratorCompletionHandler](../avassetimagegeneratorcompletionhandler.md) — A type alias for a closure that provides the result of an image generation request.
- [- cancelAllCGImageGeneration](<cancelallcgimagegeneration().md>) — Cancels all pending image generation requests.
- [- copyCGImageAtTime:actualTime:error:](<copycgimage(at_actualtime_).md>) — Returns an image for the asset at or near a specified time. _(deprecated)_
