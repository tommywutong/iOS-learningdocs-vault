---
title: AVAssetImageGenerator.Images
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/images
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/images'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/images.json'
content_hash: 'sha256:c91f6b572faf59d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetImageGenerator](../avassetimagegenerator.md)

# AVAssetImageGenerator.Images

<sub>Structure</sub>

An asynchronous sequence of images created by an image generator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct Images
```

## Relationships

- **Conforms To**: [AsyncIteratorProtocol](../../swift/asynciteratorprotocol.md), [AsyncSequence](../../swift/asyncsequence.md)

## Topics

### Creating an iterator

- [makeAsyncIterator()](<images/makeasynciterator().md>) — Creates an asynchronous iterator that produces elements of this type.

### Iterating elements

- [next()](<images/next().md>) — Returns the next element in the sequence.
- [Element](images/element.md) — An element that provides the result of an image generation request.

## See Also

### Generating images

- [image(at:)](<image(at_).md>) — Generates an image for a requested time.
- [images(for:)](<images(for_).md>) — Generates images for times within the video timeline.
- [- generateCGImageAsynchronouslyForTime:completionHandler:](<generatecgimageasynchronously(for_completionhandler_).md>) — Generates an image asynchronously for a requested time, and returns the result in a callback.
- [- generateCGImagesAsynchronouslyForTimes:completionHandler:](<generatecgimagesasynchronously(fortimes_completionhandler_).md>) — Generates images asynchronously for an array of requested times, and returns the results in a callback.
- [AVAssetImageGeneratorCompletionHandler](../avassetimagegeneratorcompletionhandler.md) — A type alias for a closure that provides the result of an image generation request.
- [- cancelAllCGImageGeneration](<cancelallcgimagegeneration().md>) — Cancels all pending image generation requests.
- [- copyCGImageAtTime:actualTime:error:](<copycgimage(at_actualtime_).md>) — Returns an image for the asset at or near a specified time. _(deprecated)_
