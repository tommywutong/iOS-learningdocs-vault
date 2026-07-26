---
title: videoComposition
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmutablevideocomposition/videocomposition
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/videocomposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocomposition/videocomposition.json'
content_hash: 'sha256:3af7bd072263927d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoComposition](../avmutablevideocomposition.md)

# videoComposition

<sub>Type Method</sub>

Creates a new mutable video composition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (AVMutableVideoComposition *) videoComposition;
```

## Return Value

A newly created and initialized instance of `AVMutableVideoComposition`.

## Discussion

The returned `AVMutableVideoComposition` has the following properties:

- A [frameDuration](frameduration.md) of [zero](../../coremedia/cmtime/zero.md).
- A [renderSize](rendersize.md) of `{0.0, 0.0}`.
- A `nil` array of [instructions](instructions.md).
- The [animationTool](animationtool.md) property set to `nil`.

## See Also

### Creating a video composition

- [+ videoCompositionWithPropertiesOfAsset:completionHandler:](<videocomposition(withpropertiesof_completionhandler_).md>) — Returns a new video composition that’s configured to present the video tracks of the specified asset. _(deprecated)_
- [+ videoCompositionWithPropertiesOfAsset:prototypeInstruction:completionHandler:](<videocomposition(withpropertiesof_prototypeinstruction_completionhandler_).md>) — Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:](<videocomposition(with_applyingcifilterswithhandler_completionhandler_).md>) — Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [+ videoCompositionWithPropertiesOfAsset:](<init(propertiesof_).md>) — Creates a mutable video composition with the specified asset properties. _(deprecated)_
- [+ videoCompositionWithPropertiesOfAsset:prototypeInstruction:](<init(propertiesof_prototypeinstruction_).md>) — Creates a mutable video composition with the specified asset properties and a prototype video composition instruction. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<init(asset_applyingcifilterswithhandler_).md>) — Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
