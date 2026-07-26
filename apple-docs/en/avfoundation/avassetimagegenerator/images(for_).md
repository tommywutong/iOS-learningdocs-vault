---
title: 'images(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetimagegenerator/images(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/images%28for%3A%29.json'
content_hash: 'sha256:f640b6d26a487c77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetImageGenerator](../avassetimagegenerator.md)

# images(for:)

<sub>Instance Method</sub>

Generates images for times within the video timeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func images(for times: [CMTime]) -> sending AVAssetImageGenerator.Images
```

## Parameters

- `times` — An array of times within the asset timeline to create images.

## Return Value

An asynchronous sequence of images.

## Topics

### Generated image sequence

- [Images](images.md) — An asynchronous sequence of images created by an image generator.

## See Also

### Generating images

- [image(at:)](<image(at_).md>) — Generates an image for a requested time.
- [Images](images.md) — An asynchronous sequence of images created by an image generator.
- [- generateCGImageAsynchronouslyForTime:completionHandler:](<generatecgimageasynchronously(for_completionhandler_).md>) — Generates an image asynchronously for a requested time, and returns the result in a callback.
- [- generateCGImagesAsynchronouslyForTimes:completionHandler:](<generatecgimagesasynchronously(fortimes_completionhandler_).md>) — Generates images asynchronously for an array of requested times, and returns the results in a callback.
- [AVAssetImageGeneratorCompletionHandler](../avassetimagegeneratorcompletionhandler.md) — A type alias for a closure that provides the result of an image generation request.
- [- cancelAllCGImageGeneration](<cancelallcgimagegeneration().md>) — Cancels all pending image generation requests.
- [- copyCGImageAtTime:actualTime:error:](<copycgimage(at_actualtime_).md>) — Returns an image for the asset at or near a specified time. _(deprecated)_
