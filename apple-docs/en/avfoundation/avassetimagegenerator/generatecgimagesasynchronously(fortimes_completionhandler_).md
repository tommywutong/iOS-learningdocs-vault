---
title: 'generateCGImagesAsynchronously(forTimes:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetimagegenerator/generatecgimagesasynchronously(fortimes:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/generatecgimagesasynchronously(fortimes:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/generatecgimagesasynchronously%28fortimes%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:8d45c76cb8c7fecc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetImageGenerator](../avassetimagegenerator.md)

# generateCGImagesAsynchronously(forTimes:completionHandler:)

<sub>Instance Method</sub>

Generates images asynchronously for an array of requested times, and returns the results in a callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func generateCGImagesAsynchronously(forTimes requestedTimes: [NSValue], completionHandler handler: @escaping AVAssetImageGeneratorCompletionHandler)
```

## Parameters

- `requestedTimes` — An array of times, contained in NSValue objects, in the video timeline for which to generate images.

- `handler` — A callback that the image generator invokes for each requested image time.

## Discussion

Swift clients should prefer the asynchronous `images(for:)` method instead.

## Topics

### Data types

- [AVAssetImageGeneratorCompletionHandler](../avassetimagegeneratorcompletionhandler.md) — A type alias for a closure that provides the result of an image generation request.
- [Result](result.md) — Constants that indicate the result of an image generation request.

## See Also

### Generating images

- [image(at:)](<image(at_).md>) — Generates an image for a requested time.
- [images(for:)](<images(for_).md>) — Generates images for times within the video timeline.
- [Images](images.md) — An asynchronous sequence of images created by an image generator.
- [- generateCGImageAsynchronouslyForTime:completionHandler:](<generatecgimageasynchronously(for_completionhandler_).md>) — Generates an image asynchronously for a requested time, and returns the result in a callback.
- [AVAssetImageGeneratorCompletionHandler](../avassetimagegeneratorcompletionhandler.md) — A type alias for a closure that provides the result of an image generation request.
- [- cancelAllCGImageGeneration](<cancelallcgimagegeneration().md>) — Cancels all pending image generation requests.
- [- copyCGImageAtTime:actualTime:error:](<copycgimage(at_actualtime_).md>) — Returns an image for the asset at or near a specified time. _(deprecated)_
