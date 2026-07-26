---
title: AVVideoCompositionValidationHandling
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositionvalidationhandling
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositionvalidationhandling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositionvalidationhandling.json'
content_hash: 'sha256:855be9635c9e08b6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoCompositionValidationHandling

<sub>Protocol</sub>

Methods you can implement to indicate whether validation of a video composition should continue after specific errors are found.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol AVVideoCompositionValidationHandling : NSObjectProtocol
```

## Overview

You might chose to stop validation after particular errors have been found so as to avoid unnecessary subsequent processing following an eror from which there is no suitable recovery.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring validation methods

- [- videoComposition:shouldContinueValidatingAfterFindingInvalidValueForKey:](<avvideocompositionvalidationhandling/videocomposition(__shouldcontinuevalidatingafterfindinginvalidvalueforkey_).md>) — Reports that a key that has an invalid value.
- [- videoComposition:shouldContinueValidatingAfterFindingEmptyTimeRange:](<avvideocompositionvalidationhandling/videocomposition(__shouldcontinuevalidatingafterfindingemptytimerange_).md>) — Reports a time range that has no corresponding video composition instruction.
- [- videoComposition:shouldContinueValidatingAfterFindingInvalidTimeRangeInInstruction:](<avvideocompositionvalidationhandling/videocomposition(__shouldcontinuevalidatingafterfindinginvalidtimerangein_).md>) — Reports a video composition instruction with a time range that is invalid.
- [- videoComposition:shouldContinueValidatingAfterFindingInvalidTrackIDInInstruction:layerInstruction:asset:](<avvideocompositionvalidationhandling/videocomposition(__shouldcontinuevalidatingafterfindinginvalidtrackidin_layerinstruction_asset_).md>) — Reports a video composition layer instruction that does not correspond to the track ID used for the composition’s animation or to a track of the asset.

## See Also

### Validating the time range

- [- isValidForTracks:assetDuration:timeRange:validationDelegate:](<avvideocomposition/isvalid(for_assetduration_timerange_validationdelegate_).md>) — Indicates whether the time ranges of the composition’s instructions conform to validation requirements.
- [- determineValidityForAsset:timeRange:validationDelegate:completionHandler:](<avvideocomposition/determinevalidity(for_timerange_validationdelegate_completionhandler_).md>) — Determines whether the time ranges of the composition’s instructions conform to validation requirements. _(deprecated)_
- [- isValidForAsset:timeRange:validationDelegate:](<avvideocomposition/isvalid(for_timerange_validationdelegate_).md>) — Indicates whether the time ranges of the composition’s instructions conform to validation requirements. _(deprecated)_
