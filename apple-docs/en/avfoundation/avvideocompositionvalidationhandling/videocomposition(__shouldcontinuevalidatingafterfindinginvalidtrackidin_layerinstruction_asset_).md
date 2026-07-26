---
title: 'videoComposition(_:shouldContinueValidatingAfterFindingInvalidTrackIDIn:layerInstruction:asset:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositionvalidationhandling/videocomposition(_:shouldcontinuevalidatingafterfindinginvalidtrackidin:layerinstruction:asset:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/videocomposition(_:shouldcontinuevalidatingafterfindinginvalidtrackidin:layerinstruction:asset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionvalidationhandling/videocomposition%28_%3Ashouldcontinuevalidatingafterfindinginvalidtrackidin%3Alayerinstruction%3Aasset%3A%29.json'
content_hash: 'sha256:3981bd0dba3e6fed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionValidationHandling](../avvideocompositionvalidationhandling.md)

# videoComposition(_:shouldContinueValidatingAfterFindingInvalidTrackIDIn:layerInstruction:asset:)

<sub>Instance Method</sub>

Reports a video composition layer instruction that does not correspond to the track ID used for the composition’s animation or to a track of the asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTrackIDIn videoCompositionInstruction: any AVVideoCompositionInstructionProtocol, layerInstruction: AVVideoCompositionLayerInstruction, asset: AVAsset) -> Bool
```

## Parameters

- `videoComposition` — The video composition being validated.

- `videoCompositionInstruction` — The video composition instruction.

- `layerInstruction` — The layer instruction.

- `asset` — The underlying asset.

## Return Value

[true](../../swift/true.md) if the video composition should continue validation in order to report additional problems that may exist, otherwise [false](../../swift/false.md).

## Discussion

The asset track is specified in the [- isValidForAsset:timeRange:validationDelegate:](<../avvideocomposition/isvalid(for_timerange_validationdelegate_).md>) method.

## See Also

### Configuring validation methods

- [- videoComposition:shouldContinueValidatingAfterFindingInvalidValueForKey:](<videocomposition(__shouldcontinuevalidatingafterfindinginvalidvalueforkey_).md>) — Reports that a key that has an invalid value.
- [- videoComposition:shouldContinueValidatingAfterFindingEmptyTimeRange:](<videocomposition(__shouldcontinuevalidatingafterfindingemptytimerange_).md>) — Reports a time range that has no corresponding video composition instruction.
- [- videoComposition:shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction:](<videocomposition(__shouldcontinuevalidatingafterfindinginvalidtimerangein_).md>) — Reports a video composition instruction with a time range that is invalid.
