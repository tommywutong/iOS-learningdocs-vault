---
title: 'videoComposition(_:shouldContinueValidatingAfterFindingInvalidValueForKey:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositionvalidationhandling/videocomposition(_:shouldcontinuevalidatingafterfindinginvalidvalueforkey:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/videocomposition(_:shouldcontinuevalidatingafterfindinginvalidvalueforkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionvalidationhandling/videocomposition%28_%3Ashouldcontinuevalidatingafterfindinginvalidvalueforkey%3A%29.json'
content_hash: 'sha256:9d8ed9f7c78390d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionValidationHandling](../avvideocompositionvalidationhandling.md)

# videoComposition(_:shouldContinueValidatingAfterFindingInvalidValueForKey:)

<sub>Instance Method</sub>

Reports that a key that has an invalid value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidValueForKey key: String) -> Bool
```

## Parameters

- `videoComposition` — The video composition being validated.

- `key` — The key being validated.

## Return Value

[true](../../swift/true.md) if the video composition should continue validation in order to report additional problems that may exist, otherwise [false](../../swift/false.md).

## See Also

### Configuring validation methods

- [- videoComposition:shouldContinueValidatingAfterFindingEmptyTimeRange:](<videocomposition(__shouldcontinuevalidatingafterfindingemptytimerange_).md>) — Reports a time range that has no corresponding video composition instruction.
- [- videoComposition:shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction:](<videocomposition(__shouldcontinuevalidatingafterfindinginvalidtimerangein_).md>) — Reports a video composition instruction with a time range that is invalid.
- [- videoComposition:shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction:layerInstruction:asset:](<videocomposition(__shouldcontinuevalidatingafterfindinginvalidtrackidin_layerinstruction_asset_).md>) — Reports a video composition layer instruction that does not correspond to the track ID used for the composition’s animation or to a track of the asset.
