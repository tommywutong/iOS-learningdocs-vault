---
title: 'init(propertiesOf:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+（18.0 起废弃）, iPadOS 6.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.9+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avvideocomposition/init(propertiesof:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/init(propertiesof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/init%28propertiesof%3A%29.json'
content_hash: 'sha256:5ce3b7f698379a07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoComposition](../avvideocomposition.md)

# init(propertiesOf:)

<sub>Initializer</sub>

Creates a video composition object configured to present the video tracks of the specified asset.

> [!warning] Deprecated
> Use videoCompositionWithPropertiesOfAsset:completionHandler: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
init(propertiesOf asset: AVAsset)
```

## Parameters

- `asset` — The asset whose configuration matches the intended use of the video composition.

## Return Value

A new video composition object.

## Discussion

Apple discourages using this method in iOS 16, tvOS 16, and macOS 13 or later. Create a video composition asynchronously using [+ videoCompositionWithPropertiesOfAsset:completionHandler:](<videocomposition(withpropertiesof_completionhandler_).md>) instead.

This method creates the video composition object and configures it with the values and instructions suitable for presenting the video tracks of the specified asset. The returned object contains instructions that respect the spatial properties and time ranges of the specified asset’s video tracks. It also configures the object properties in the following way:

- The value of the [frameDuration](frameduration.md) property is short enough to accommodate the greatest nominal frame rate value among the asset’s video tracks, as indicated by the [nominalFrameRate](../avpartialasyncproperty/nominalframerate.md) property of each track. If all its tracks have a nominal frame rate of `0`, it uses a frame rate of 30 frames per second, with the frame duration set accordingly.
- The value of the [renderSize](rendersize.md) property depends on whether the asset is an [AVComposition](../avcomposition.md) object. For an [AVComposition](../avcomposition.md), the render size is the composition’s [naturalSize](../avcomposition/naturalsize.md) value, and for other assets, its a size large enough to encompass all of its video tracks.
- The value of the [renderScale](renderscale.md) property is `1.0`.
- The value of the [animationTool](animationtool.md) property is `nil`.

> [!note] Note
> If you specify an asset that doesn’t contain video tracks, this method returns a video composition with no instructions.

## See Also

### Creating a video composition

- [init(configuration:)](<init(configuration_).md>) — Initialize an AVVideoComposition with a configuration.
- [Configuration](configuration.md) — Configurable properties for initializing a new AVVideoComposition instance.
- [init(applyingFiltersTo:applier:)](<init(applyingfiltersto_applier_).md>) — Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:](<videocomposition(with_applyingcifilterswithhandler_completionhandler_).md>) — Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
- [AVAsynchronousCIImageFilteringRequest](../avasynchronousciimagefilteringrequest.md) — An object that supports using Core Image filters to process an individual video frame in a video composition. _(deprecated)_
- [AVCIImageFilteringParameters](../avciimagefilteringparameters.md)
- [AVCIImageFilteringResult](../avciimagefilteringresult.md) — An output video frame processed with Core Image filtering.
- [+ videoCompositionWithPropertiesOfAsset:completionHandler:](<videocomposition(withpropertiesof_completionhandler_).md>) — Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<init(asset_applyingcifilterswithhandler_).md>) — Creates a video composition configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
