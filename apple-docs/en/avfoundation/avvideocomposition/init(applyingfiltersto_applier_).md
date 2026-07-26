---
title: 'init(applyingFiltersTo:applier:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocomposition/init(applyingfiltersto:applier:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/init(applyingfiltersto:applier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/init%28applyingfiltersto%3Aapplier%3A%29.json'
content_hash: 'sha256:a34ee7f4c5539da1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoComposition](../avvideocomposition.md)

# init(applyingFiltersTo:applier:)

<sub>Initializer</sub>

Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated(nonsending) convenience init(applyingFiltersTo asset: AVAsset, applier: @escaping @Sendable (AVCIImageFilteringParameters) async throws -> AVCIImageFilteringResult) async throws
```

## Parameters

- `asset` — The asset whose configuration matches the intended use of the video composition.

- `applier` — A closure that AVFoundation calls when processing each video frame.

## Return Value

A new AVVideoComposition instance configured for Core Image filtering.

## See Also

### Creating a video composition

- [init(configuration:)](<init(configuration_).md>) — Initialize an AVVideoComposition with a configuration.
- [Configuration](configuration.md) — Configurable properties for initializing a new AVVideoComposition instance.
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:](<videocomposition(with_applyingcifilterswithhandler_completionhandler_).md>) — Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
- [AVAsynchronousCIImageFilteringRequest](../avasynchronousciimagefilteringrequest.md) — An object that supports using Core Image filters to process an individual video frame in a video composition. _(deprecated)_
- [AVCIImageFilteringParameters](../avciimagefilteringparameters.md)
- [AVCIImageFilteringResult](../avciimagefilteringresult.md) — An output video frame processed with Core Image filtering.
- [+ videoCompositionWithPropertiesOfAsset:completionHandler:](<videocomposition(withpropertiesof_completionhandler_).md>) — Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [+ videoCompositionWithPropertiesOfAsset:](<init(propertiesof_).md>) — Creates a video composition object configured to present the video tracks of the specified asset. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<init(asset_applyingcifilterswithhandler_).md>) — Creates a video composition configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
