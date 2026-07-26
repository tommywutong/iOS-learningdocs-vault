---
title: 'videoComposition(withPropertiesOf:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+（26.0 起废弃）, iPadOS 16.0+（26.0 起废弃）, Mac Catalyst 16.0+（26.0 起废弃）, macOS 13.0+（26.0 起废弃）, tvOS 16.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avmutablevideocomposition/videocomposition(withpropertiesof:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/videocomposition(withpropertiesof:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocomposition/videocomposition%28withpropertiesof%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:2ba392b7022d386b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoComposition](../avmutablevideocomposition.md)

# videoComposition(withPropertiesOf:completionHandler:)

<sub>Type Method</sub>

Returns a new video composition that’s configured to present the video tracks of the specified asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func videoComposition(withPropertiesOf asset: AVAsset, completionHandler: @escaping @Sendable (AVMutableVideoComposition?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func videoComposition(withPropertiesOf asset: AVAsset) async throws -> AVMutableVideoComposition
```

## Parameters

- `asset` — An asset to create a video composition for.

- `completionHandler` — A callback the system invokes with the created video composition, or an error if a failure occurs.

## Discussion

This method creates the video composition object and configures it with the values and instructions suitable for presenting the video tracks of the specified asset. The returned object contains instructions that respect the spatial properties and time ranges of the specified asset’s video tracks. It also configures the object properties in the following way:

- The value of the [frameDuration](../avvideocomposition/frameduration.md) property is short enough to accommodate the greatest nominal frame rate value among the asset’s video tracks, as indicated by the [nominalFrameRate](../avpartialasyncproperty/nominalframerate.md) property of each track. If all its tracks have a nominal frame rate of `0`, it uses a frame rate of 30 frames per second, with the frame duration set accordingly.
- The value of the [renderSize](../avvideocomposition/rendersize.md) property depends on whether the asset is an [AVComposition](../avcomposition.md) object. For an [AVComposition](../avcomposition.md), the render size is the composition’s [naturalSize](../avcomposition/naturalsize.md) value, and for other assets, its a size large enough to encompass all of its video tracks.
- The value of the [renderScale](../avvideocomposition/renderscale.md) property is `1.0`.
- The value of the [animationTool](../avvideocomposition/animationtool.md) property is `nil`.

> [!note] Note
> If you specify an asset that doesn’t contain video tracks, this method returns a video composition with no instructions.

## See Also

### Creating a video composition

- [+ videoCompositionWithPropertiesOfAsset:prototypeInstruction:completionHandler:](<videocomposition(withpropertiesof_prototypeinstruction_completionhandler_).md>) — Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:](<videocomposition(with_applyingcifilterswithhandler_completionhandler_).md>) — Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [+ videoCompositionWithPropertiesOfAsset:](<init(propertiesof_).md>) — Creates a mutable video composition with the specified asset properties. _(deprecated)_
- [+ videoCompositionWithPropertiesOfAsset:prototypeInstruction:](<init(propertiesof_prototypeinstruction_).md>) — Creates a mutable video composition with the specified asset properties and a prototype video composition instruction. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<init(asset_applyingcifilterswithhandler_).md>) — Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
