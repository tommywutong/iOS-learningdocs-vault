---
title: 'copyCGImage(at:actualTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+（18.0 起废弃）, iPadOS 4.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetimagegenerator/copycgimage(at:actualtime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/copycgimage(at:actualtime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/copycgimage%28at%3Aactualtime%3A%29.json'
content_hash: 'sha256:9b93329adca01fab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetImageGenerator](../avassetimagegenerator.md)

# copyCGImage(at:actualTime:)

<sub>Instance Method</sub>

Returns an image for the asset at or near a specified time.

> [!warning] Deprecated
> Use [image(at:)](<image(at_).md>) instead or [- generateCGImagesAsynchronouslyForTimes:completionHandler:](<generatecgimagesasynchronously(fortimes_completionhandler_).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func copyCGImage(at requestedTime: CMTime, actualTime: UnsafeMutablePointer<CMTime>?) throws -> CGImage
```

## Parameters

- `requestedTime` — A time within the asset timeline for which to create an image.

- `actualTime` — Upon return, contains the time at which the image was actually generated. If you’re not interested in this information, pass `NULL`.

## Return Value

A [CGImage](../../coregraphics/cgimage.md) for the asset at or near a specified time, or `NULL` if the image could not be created.

## Discussion

This method returns the image synchronously.

## See Also

### Generating images

- [image(at:)](<image(at_).md>) — Generates an image for a requested time.
- [images(for:)](<images(for_).md>) — Generates images for times within the video timeline.
- [Images](images.md) — An asynchronous sequence of images created by an image generator.
- [- generateCGImageAsynchronouslyForTime:completionHandler:](<generatecgimageasynchronously(for_completionhandler_).md>) — Generates an image asynchronously for a requested time, and returns the result in a callback.
- [- generateCGImagesAsynchronouslyForTimes:completionHandler:](<generatecgimagesasynchronously(fortimes_completionhandler_).md>) — Generates images asynchronously for an array of requested times, and returns the results in a callback.
- [AVAssetImageGeneratorCompletionHandler](../avassetimagegeneratorcompletionhandler.md) — A type alias for a closure that provides the result of an image generation request.
- [- cancelAllCGImageGeneration](<cancelallcgimagegeneration().md>) — Cancels all pending image generation requests.
