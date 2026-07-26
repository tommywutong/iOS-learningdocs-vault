---
title: 'videoCompositionWithVideoComposition:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocomposition/videocompositionwithvideocomposition:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/videocompositionwithvideocomposition:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/videocompositionwithvideocomposition%3A.json'
content_hash: 'sha256:3e9b7adb6eb64884'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoComposition](../avvideocomposition.md)

# videoCompositionWithVideoComposition:

<sub>Type Method</sub>

Pass-through initializer, for internal use in AVFoundation only

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (AVVideoComposition *) videoCompositionWithVideoComposition:(AVVideoComposition *) videoComposition;
```

## See Also

### Creating a video composition

- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:](<videocomposition(with_applyingcifilterswithhandler_completionhandler_).md>) — Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
- [AVAsynchronousCIImageFilteringRequest](../avasynchronousciimagefilteringrequest.md) — An object that supports using Core Image filters to process an individual video frame in a video composition. _(deprecated)_
- [+ videoCompositionWithPropertiesOfAsset:completionHandler:](<videocomposition(withpropertiesof_completionhandler_).md>) — Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [+ videoCompositionWithPropertiesOfAsset:](<init(propertiesof_).md>) — Creates a video composition object configured to present the video tracks of the specified asset. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<init(asset_applyingcifilterswithhandler_).md>) — Creates a video composition configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
