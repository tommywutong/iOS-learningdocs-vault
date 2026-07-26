---
title: AVAssetImageGeneratorCompletionHandler
framework: AVFoundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegeneratorcompletionhandler
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegeneratorcompletionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegeneratorcompletionhandler.json'
content_hash: 'sha256:1a615892e518ff8c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetImageGeneratorCompletionHandler

<sub>Type Alias</sub>

A type alias for a closure that provides the result of an image generation request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias AVAssetImageGeneratorCompletionHandler = @Sendable (CMTime, CGImage?, CMTime, AVAssetImageGenerator.Result, (any Error)?) -> Void
```

## Parameters

- `requestedTime` — A time in the video timeline for which to generate an image.

- `image` — A generated image for the requested time.

- `actualTime` — The actual time in the video timeline at which it generated an image. The requested and actual times may differ depending on your image generator configuration including its time tolerance values.

- `result` — A value that indicates the result of the image generation request.

- `error` — An optional error. If an error occurs the system provides an error object that provides the details of the failure.

## See Also

### Generating images

- [image(at:)](<avassetimagegenerator/image(at_).md>) — Generates an image for a requested time.
- [images(for:)](<avassetimagegenerator/images(for_).md>) — Generates images for times within the video timeline.
- [Images](avassetimagegenerator/images.md) — An asynchronous sequence of images created by an image generator.
- [- generateCGImageAsynchronouslyForTime:completionHandler:](<avassetimagegenerator/generatecgimageasynchronously(for_completionhandler_).md>) — Generates an image asynchronously for a requested time, and returns the result in a callback.
- [- generateCGImagesAsynchronouslyForTimes:completionHandler:](<avassetimagegenerator/generatecgimagesasynchronously(fortimes_completionhandler_).md>) — Generates images asynchronously for an array of requested times, and returns the results in a callback.
- [- cancelAllCGImageGeneration](<avassetimagegenerator/cancelallcgimagegeneration().md>) — Cancels all pending image generation requests.
- [- copyCGImageAtTime:actualTime:error:](<avassetimagegenerator/copycgimage(at_actualtime_).md>) — Returns an image for the asset at or near a specified time. _(deprecated)_
