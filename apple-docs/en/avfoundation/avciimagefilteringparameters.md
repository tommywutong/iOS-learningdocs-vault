---
title: AVCIImageFilteringParameters
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avciimagefilteringparameters
source_url: 'https://developer.apple.com/documentation/avfoundation/avciimagefilteringparameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avciimagefilteringparameters.json'
content_hash: 'sha256:e5fc68969c4533fa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCIImageFilteringParameters

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct AVCIImageFilteringParameters
```

## Topics

### Inspecting the parameters

- [compositionTime](avciimagefilteringparameters/compositiontime.md) — The time in the video composition corresponding to the frame being processed.
- [renderSize](avciimagefilteringparameters/rendersize.md) — The width and height, in pixels, of the frame being processed.
- [sourceImage](avciimagefilteringparameters/sourceimage.md) — The current video frame image.

## See Also

### Creating a video composition

- [init(configuration:)](<avvideocomposition/init(configuration_).md>) — Initialize an AVVideoComposition with a configuration.
- [Configuration](avvideocomposition/configuration.md) — Configurable properties for initializing a new AVVideoComposition instance.
- [init(applyingFiltersTo:applier:)](<avvideocomposition/init(applyingfiltersto_applier_).md>) — Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:](<avvideocomposition/videocomposition(with_applyingcifilterswithhandler_completionhandler_).md>) — Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
- [AVAsynchronousCIImageFilteringRequest](avasynchronousciimagefilteringrequest.md) — An object that supports using Core Image filters to process an individual video frame in a video composition. _(deprecated)_
- [AVCIImageFilteringResult](avciimagefilteringresult.md) — An output video frame processed with Core Image filtering.
- [+ videoCompositionWithPropertiesOfAsset:completionHandler:](<avvideocomposition/videocomposition(withpropertiesof_completionhandler_).md>) — Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [+ videoCompositionWithPropertiesOfAsset:](<avvideocomposition/init(propertiesof_).md>) — Creates a video composition object configured to present the video tracks of the specified asset. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<avvideocomposition/init(asset_applyingcifilterswithhandler_).md>) — Creates a video composition configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
