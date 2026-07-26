---
title: 'generateCGImageAsynchronously(for:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetimagegenerator/generatecgimageasynchronously(for:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/generatecgimageasynchronously(for:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/generatecgimageasynchronously%28for%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:067624c160c34d1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetImageGenerator](../avassetimagegenerator.md)

# generateCGImageAsynchronously(for:completionHandler:)

<sub>Instance Method</sub>

Generates an image asynchronously for a requested time, and returns the result in a callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func generateCGImageAsynchronously(for requestedTime: CMTime, completionHandler handler: @escaping @Sendable (CGImage?, CMTime, (any Error)?) -> Void)
```

## Parameters

- `requestedTime` — A time in the video timeline for which to generate an image. The requested time and actual time at which it generates an image may differ depending on the generator’s time tolerance settings.

- `handler` — A callback that the image generator invokes with the result of the request.

## Discussion

Swift clients should use the asynchronous [image(at:)](<image(at_).md>) method instead.

## Topics

### Data types

- [AVAssetImageGeneratorCompletionHandler](../avassetimagegeneratorcompletionhandler.md) — A type alias for a closure that provides the result of an image generation request.
- [Result](result.md) — Constants that indicate the result of an image generation request.

## See Also

### Generating images

- [image(at:)](<image(at_).md>) — Generates an image for a requested time.
- [images(for:)](<images(for_).md>) — Generates images for times within the video timeline.
- [Images](images.md) — An asynchronous sequence of images created by an image generator.
- [- generateCGImagesAsynchronouslyForTimes:completionHandler:](<generatecgimagesasynchronously(fortimes_completionhandler_).md>) — Generates images asynchronously for an array of requested times, and returns the results in a callback.
- [AVAssetImageGeneratorCompletionHandler](../avassetimagegeneratorcompletionhandler.md) — A type alias for a closure that provides the result of an image generation request.
- [- cancelAllCGImageGeneration](<cancelallcgimagegeneration().md>) — Cancels all pending image generation requests.
- [- copyCGImageAtTime:actualTime:error:](<copycgimage(at_actualtime_).md>) — Returns an image for the asset at or near a specified time. _(deprecated)_
