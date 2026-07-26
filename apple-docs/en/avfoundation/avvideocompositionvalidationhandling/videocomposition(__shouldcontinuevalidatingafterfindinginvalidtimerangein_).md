---
title: 'videoComposition(_:shouldContinueValidatingAfterFindingInvalidTimeRangeIn:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocompositionvalidationhandling/videocomposition(_:shouldcontinuevalidatingafterfindinginvalidtimerangein:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling/videocomposition(_:shouldcontinuevalidatingafterfindinginvalidtimerangein:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionvalidationhandling/videocomposition%28_%3Ashouldcontinuevalidatingafterfindinginvalidtimerangein%3A%29.json'
content_hash: 'sha256:115fceabb2f01010'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionValidationHandling](../avvideocompositionvalidationhandling.md)

# videoComposition(_:shouldContinueValidatingAfterFindingInvalidTimeRangeIn:)

<sub>Instance Method</sub>

Reports a video composition instruction with a time range that is invalid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func videoComposition(_ videoComposition: AVVideoComposition, shouldContinueValidatingAfterFindingInvalidTimeRangeIn videoCompositionInstruction: any AVVideoCompositionInstructionProtocol) -> Bool
```

## Parameters

- `videoComposition` — The video composition being validated.

- `videoCompositionInstruction` — The video composition instruction.

## Return Value

[true](../../swift/true.md) if the video composition should continue validation in order to report additional problems that may exist, otherwise [false](../../swift/false.md).

## Discussion

A time range is considered invalid when it overlaps with the time range of a prior instruction, or that contains times earlier than the time range of a prior instruction

## See Also

### Configuring validation methods

- [- videoComposition:shouldContinueValidatingAfterFindingInvalidValueForKey:](<videocomposition(__shouldcontinuevalidatingafterfindinginvalidvalueforkey_).md>) — Reports that a key that has an invalid value.
- [- videoComposition:shouldContinueValidatingAfterFindingEmptyTimeRange:](<videocomposition(__shouldcontinuevalidatingafterfindingemptytimerange_).md>) — Reports a time range that has no corresponding video composition instruction.
- [- videoComposition:shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction:layerInstruction:asset:](<videocomposition(__shouldcontinuevalidatingafterfindinginvalidtrackidin_layerinstruction_asset_).md>) — Reports a video composition layer instruction that does not correspond to the track ID used for the composition’s animation or to a track of the asset.
