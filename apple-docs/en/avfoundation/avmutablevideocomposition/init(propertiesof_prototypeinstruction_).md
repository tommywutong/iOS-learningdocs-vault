---
title: 'init(propertiesOf:prototypeInstruction:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（18.0 起废弃）, iPadOS 13.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.15+（15.0 起废弃）, tvOS 13.0+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avmutablevideocomposition/init(propertiesof:prototypeinstruction:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/init(propertiesof:prototypeinstruction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocomposition/init%28propertiesof%3Aprototypeinstruction%3A%29.json'
content_hash: 'sha256:35c261943bbe6950'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoComposition](../avmutablevideocomposition.md)

# init(propertiesOf:prototypeInstruction:)

<sub>Initializer</sub>

Creates a mutable video composition with the specified asset properties and a prototype video composition instruction.

> [!warning] Deprecated
> Use videoCompositionWithPropertiesOfAsset:prototypeInstruction:completionHandler: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
init(propertiesOf asset: AVAsset, prototypeInstruction: AVVideoCompositionInstruction)
```

## Parameters

- `asset` — The asset for which to create a video composition. Load the asset’s [duration](../avasset/duration.md) and [tracks](../avasset/tracks.md) properties before invoking this method.

- `prototypeInstruction` — A video composition instruction to use as a prototype.

## See Also

### Creating a video composition

- [+ videoCompositionWithPropertiesOfAsset:completionHandler:](<videocomposition(withpropertiesof_completionhandler_).md>) — Returns a new video composition that’s configured to present the video tracks of the specified asset. _(deprecated)_
- [+ videoCompositionWithPropertiesOfAsset:prototypeInstruction:completionHandler:](<videocomposition(withpropertiesof_prototypeinstruction_completionhandler_).md>) — Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:](<videocomposition(with_applyingcifilterswithhandler_completionhandler_).md>) — Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [+ videoCompositionWithPropertiesOfAsset:](<init(propertiesof_).md>) — Creates a mutable video composition with the specified asset properties. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<init(asset_applyingcifilterswithhandler_).md>) — Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
