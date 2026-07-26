---
title: AVCIImageFilteringResult
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avciimagefilteringresult
source_url: 'https://developer.apple.com/documentation/avfoundation/avciimagefilteringresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avciimagefilteringresult.json'
content_hash: 'sha256:ecd93a5d8e0f2797'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCIImageFilteringResult

<sub>Structure</sub>

An output video frame processed with Core Image filtering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct AVCIImageFilteringResult
```

## Topics

### Creating a result

- [init(resultImage:ciContext:)](<avciimagefilteringresult/init(resultimage_cicontext_).md>)

### Inspecting the result

- [ciContext](avciimagefilteringresult/cicontext.md) — The core image context used to render the image
- [resultImage](avciimagefilteringresult/resultimage.md) — Provides the filtered video frame image to AVFoundation for further processing or display.

## See Also

### Creating a video composition

- [init(configuration:)](<avvideocomposition/init(configuration_).md>) — Initialize an AVVideoComposition with a configuration.
- [Configuration](avvideocomposition/configuration.md) — Configurable properties for initializing a new AVVideoComposition instance.
- [init(applyingFiltersTo:applier:)](<avvideocomposition/init(applyingfiltersto_applier_).md>) — Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:](<avvideocomposition/videocomposition(with_applyingcifilterswithhandler_completionhandler_).md>) — Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
- [AVAsynchronousCIImageFilteringRequest](avasynchronousciimagefilteringrequest.md) — An object that supports using Core Image filters to process an individual video frame in a video composition. _(deprecated)_
- [AVCIImageFilteringParameters](avciimagefilteringparameters.md)
- [+ videoCompositionWithPropertiesOfAsset:completionHandler:](<avvideocomposition/videocomposition(withpropertiesof_completionhandler_).md>) — Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [+ videoCompositionWithPropertiesOfAsset:](<avvideocomposition/init(propertiesof_).md>) — Creates a video composition object configured to present the video tracks of the specified asset. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<avvideocomposition/init(asset_applyingcifilterswithhandler_).md>) — Creates a video composition configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
