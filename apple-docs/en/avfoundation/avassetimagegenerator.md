---
title: AVAssetImageGenerator
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator.json'
content_hash: 'sha256:586f9f2aa96be2f2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAssetImageGenerator

<sub>Class</sub>

An object that generates images from a video asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAssetImageGenerator
```

## Overview

Use an image generator to extract images from a video asset at particular times within its timeline.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an image generator

- [- initWithAsset:](<avassetimagegenerator/init(asset_).md>) — Creates an object that generates images for times within a video asset.

### Configuring image generation

- [maximumSize](avassetimagegenerator/maximumsize.md) — The maximum size of images to generate.
- [requestedTimeToleranceBefore](avassetimagegenerator/requestedtimetolerancebefore.md) — A maximum length of time before the requested time to allow image generation to occur.
- [requestedTimeToleranceAfter](avassetimagegenerator/requestedtimetoleranceafter.md) — A maximum length of time after the requested time to allow image generation to occur.
- [dynamicRangePolicy](avassetimagegenerator/dynamicrangepolicy-swift.property.md) — The dynamic range policy to use when generating images.
- [DynamicRangePolicy](avassetimagegenerator/dynamicrangepolicy-swift.struct.md) — A type that specifies the dynamic range policy to apply when generating images.
- [appliesPreferredTrackTransform](avassetimagegenerator/appliespreferredtracktransform.md) — A Boolean value that specifies whether to apply the track matrix or matrices when generating an image from the asset.
- [apertureMode](avassetimagegenerator/aperturemode-swift.property.md) — Specifies the aperture mode for the generated image.
- [ApertureMode](avassetimagegenerator/aperturemode-swift.struct.md) — Constants that define aperture modes to use when generating images.

### Configuring compositing

- [videoComposition](avassetimagegenerator/videocomposition.md) — A video composition to use when extracting images from assets with multiple video tracks.
- [customVideoCompositor](avassetimagegenerator/customvideocompositor.md) — A custom video compositor to use when extracting images from assets with multiple video tracks.

### Generating images

- [image(at:)](<avassetimagegenerator/image(at_).md>) — Generates an image for a requested time.
- [images(for:)](<avassetimagegenerator/images(for_).md>) — Generates images for times within the video timeline.
- [Images](avassetimagegenerator/images.md) — An asynchronous sequence of images created by an image generator.
- [- generateCGImageAsynchronouslyForTime:completionHandler:](<avassetimagegenerator/generatecgimageasynchronously(for_completionhandler_).md>) — Generates an image asynchronously for a requested time, and returns the result in a callback.
- [- generateCGImagesAsynchronouslyForTimes:completionHandler:](<avassetimagegenerator/generatecgimagesasynchronously(fortimes_completionhandler_).md>) — Generates images asynchronously for an array of requested times, and returns the results in a callback.
- [AVAssetImageGeneratorCompletionHandler](avassetimagegeneratorcompletionhandler.md) — A type alias for a closure that provides the result of an image generation request.
- [- cancelAllCGImageGeneration](<avassetimagegenerator/cancelallcgimagegeneration().md>) — Cancels all pending image generation requests.
- [- copyCGImageAtTime:actualTime:error:](<avassetimagegenerator/copycgimage(at_actualtime_).md>) — Returns an image for the asset at or near a specified time. _(deprecated)_

### Accessing the asset

- [asset](avassetimagegenerator/asset.md) — The asset that initialized the image generator.

## See Also

### Image generation

- [Creating images from a video asset](creating-images-from-a-video-asset.md) — Display images for specific times within the media timeline by generating images from a video’s frames.
