---
title: 'videoComposition(withPropertiesOf:prototypeInstruction:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+（26.0 起废弃）, iPadOS 16.0+（26.0 起废弃）, Mac Catalyst 16.0+（26.0 起废弃）, macOS 13.0+（26.0 起废弃）, tvOS 16.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avmutablevideocomposition/videocomposition(withpropertiesof:prototypeinstruction:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/videocomposition(withpropertiesof:prototypeinstruction:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocomposition/videocomposition%28withpropertiesof%3Aprototypeinstruction%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:3869bcc2d2880f9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoComposition](../avmutablevideocomposition.md)

# videoComposition(withPropertiesOf:prototypeInstruction:completionHandler:)

<sub>Type Method</sub>

Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func videoComposition(withPropertiesOf asset: AVAsset, prototypeInstruction: AVVideoCompositionInstruction, completionHandler: @escaping @Sendable (AVMutableVideoComposition?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func videoComposition(withPropertiesOf asset: AVAsset, prototypeInstruction: AVVideoCompositionInstruction) async throws -> AVMutableVideoComposition
```

## Parameters

- `asset` — The asset for which to create a video composition. Load the asset’s [duration](../avasset/duration.md) and [tracks](../avasset/tracks.md) properties before invoking this method.

- `prototypeInstruction` — A video composition instruction to use as a prototype.

- `completionHandler` — A block the system calls when it finishes creating the new video composition.

## See Also

### Creating a video composition

- [+ videoCompositionWithPropertiesOfAsset:completionHandler:](<videocomposition(withpropertiesof_completionhandler_).md>) — Returns a new video composition that’s configured to present the video tracks of the specified asset. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:](<videocomposition(with_applyingcifilterswithhandler_completionhandler_).md>) — Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [+ videoCompositionWithPropertiesOfAsset:](<init(propertiesof_).md>) — Creates a mutable video composition with the specified asset properties. _(deprecated)_
- [+ videoCompositionWithPropertiesOfAsset:prototypeInstruction:](<init(propertiesof_prototypeinstruction_).md>) — Creates a mutable video composition with the specified asset properties and a prototype video composition instruction. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<init(asset_applyingcifilterswithhandler_).md>) — Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
