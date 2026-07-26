---
title: AVAssetImageGenerator.Result
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetimagegenerator/result
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/result'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetimagegenerator/result.json'
content_hash: 'sha256:2c27733369ce6dbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetImageGenerator](../avassetimagegenerator.md)

# AVAssetImageGenerator.Result

<sub>Enumeration</sub>

Constants that indicate the result of an image generation request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Result
```

## Overview

The constants used in the block completion handler for [- generateCGImagesAsynchronouslyForTimes:completionHandler:](<generatecgimagesasynchronously(fortimes_completionhandler_).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Results

- [AVAssetImageGeneratorSucceeded](result/succeeded.md) — A result that indicates that image generation succeeded.
- [AVAssetImageGeneratorFailed](result/failed.md) — A result that indicates that image generation failed.
- [AVAssetImageGeneratorCancelled](result/cancelled.md) — A result that indicates you canceled image generation.

### Initializers

- [init(rawValue:)](<result/init(rawvalue_).md>)

## See Also

### Data types

- [AVAssetImageGeneratorCompletionHandler](../avassetimagegeneratorcompletionhandler.md) — A type alias for a closure that provides the result of an image generation request.
