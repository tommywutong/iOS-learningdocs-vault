---
title: 'init(asset:applyingCIFiltersWithHandler:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+（18.0 起废弃）, iPadOS 9.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.11+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avmutablevideocomposition/init(asset:applyingcifilterswithhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/init(asset:applyingcifilterswithhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablevideocomposition/init%28asset%3Aapplyingcifilterswithhandler%3A%29.json'
content_hash: 'sha256:3009c074a211c1c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableVideoComposition](../avmutablevideocomposition.md)

# init(asset:applyingCIFiltersWithHandler:)

<sub>Initializer</sub>

Creates a mutable video composition configured to apply Core Image filters to each video frame of the specified asset.

> [!warning] Deprecated
> Use videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
init(asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping @Sendable (AVAsynchronousCIImageFilteringRequest) -> Void)
```

## Parameters

- `asset` — The asset whose configuration matches the intended use of the video composition.

- `applier` — A block that AVFoundation calls when processing each video frame. The block takes a single parameter and has no return value: - **request** — An [AVAsynchronousCIImageFilteringRequest](../avasynchronousciimagefilteringrequest.md) object representing the frame to be processed.

## Return Value

A new video composition object.

## Discussion

To process video frames using Core Image filters—whether for display or export—create a composition with this method. AVFoundation calls your applier block once for each frame to be displayed (or processed for export) from the asset’s first enabled video track. In that block, you access the video frame and return a filtered result using the provided [AVAsynchronousCIImageFilteringRequest](../avasynchronousciimagefilteringrequest.md) object. Use that object’s [sourceImage](../avasynchronousciimagefilteringrequest/sourceimage.md) property to get the video frame in the form of a CIImage object you can apply filters to. Pass the result of your filters to the `request` object’s [- finishWithImage:context:](<../avasynchronousciimagefilteringrequest/finish(with_context_).md>) method. (If your filter rendering fails, call the `request` object’s [- finishWithError:](<../avasynchronousciimagefilteringrequest/finish(with_).md>) method if you cannot apply filters.)

Creating a composition with this method sets values for the following properties:

- The [frameDuration](frameduration.md) property is set to accommodate the [nominalFrameRate](../avassettrack/nominalframerate.md) value for the asset’s first enabled video track. If the nominal frame rate is zero, AVFoundation uses a default framerate of 30 fps.
- The [renderSize](rendersize.md) property is set to a size that encompasses the asset’s first enabled video track, respecting the track’s [preferredTransform](../avassettrack/preferredtransform.md) property.
- The [animationTool](animationtool.md) property is set to `1.0`.

## See Also

### Creating a video composition

- [+ videoCompositionWithPropertiesOfAsset:completionHandler:](<videocomposition(withpropertiesof_completionhandler_).md>) — Returns a new video composition that’s configured to present the video tracks of the specified asset. _(deprecated)_
- [+ videoCompositionWithPropertiesOfAsset:prototypeInstruction:completionHandler:](<videocomposition(withpropertiesof_prototypeinstruction_completionhandler_).md>) — Returns a new mutable video composition with the specified asset properties and a prototype video composition instruction. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:](<videocomposition(with_applyingcifilterswithhandler_completionhandler_).md>) — Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.
- [+ videoCompositionWithPropertiesOfAsset:](<init(propertiesof_).md>) — Creates a mutable video composition with the specified asset properties. _(deprecated)_
- [+ videoCompositionWithPropertiesOfAsset:prototypeInstruction:](<init(propertiesof_prototypeinstruction_).md>) — Creates a mutable video composition with the specified asset properties and a prototype video composition instruction. _(deprecated)_
