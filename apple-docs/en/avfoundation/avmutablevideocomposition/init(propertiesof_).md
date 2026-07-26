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
doc_path: '/documentation/avfoundation/avmutablevideocomposition/init(propertiesof:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/init(propertiesof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocomposition/init%28propertiesof%3A%29.json'
content_hash: 'sha256:ebcd7c8701893ed8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoComposition](../avmutablevideocomposition.md)

# init(propertiesOf:)

<sub>Initializer</sub>

Creates a mutable video composition with the specified asset properties.

> [!warning] Deprecated
> Use videoCompositionWithPropertiesOfAsset:completionHandler: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
init(propertiesOf asset: AVAsset)
```

## Parameters

- `asset` — An instance of [AVAsset](../avasset.md). Ensure that the duration and tracks properties of the asset are already loaded before invoking this method.

## Discussion

The returned `AVMutableVideoComposition` has instructions that respect the spatial properties and time ranges of the specified asset’s video tracks.

It also has the following values for its properties:

- A value for [frameDuration](frameduration.md) short enough to accommodate the greatest [nominalFrameRate](../avassettrack/nominalframerate.md) among the asset’s video tracks. If the [nominalFrameRate](../avassettrack/nominalframerate.md) of all of the asset’s video tracks is 0, a default frame rate of 30fps is used.
- If the specified asset is an instance of [AVComposition](../avcomposition.md), the [renderSize](rendersize.md) is set to the [naturalSize](../avcomposition/naturalsize.md) of the [AVComposition](../avcomposition.md); otherwise the [renderSize](rendersize.md) will be set to a value that encompasses all of the asset’s video tracks.
- A [renderScale](renderscale.md) of 1.0.
- The [animationTool](animationtool.md) property set to `nil`.

## See Also

### Creating a video composition

- [+ videoCompositionWithPropertiesOfAsset:completionHandler:](<videocomposition(withpropertiesof_completionhandler_).md>) — Returns a new video composition that’s configured to present the video tracks of the specified asset. _(deprecated)_
- [+ videoCompositionWithPropertiesOfAsset:prototypeInstruction:completionHandler:](<videocomposition(withpropertiesof_prototypeinstruction_completionhandler_).md>) — Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:](<videocomposition(with_applyingcifilterswithhandler_completionhandler_).md>) — Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [+ videoCompositionWithPropertiesOfAsset:prototypeInstruction:](<init(propertiesof_prototypeinstruction_).md>) — Creates a mutable video composition with the specified asset properties and a prototype video composition instruction. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<init(asset_applyingcifilterswithhandler_).md>) — Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
